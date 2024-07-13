from dataclasses import dataclass
from enum import StrEnum

import requests


@dataclass
class MethodCall:
    method: str
    kwargs: dict
    # Note: the final "id" argument will be automatically inserted for you.


class ContentType(StrEnum):
    TEXT = "text/plain"
    HTML = "text/html"
    JSON = "application/json"


class MailboxRoles(StrEnum):
    INBOX = "inbox"
    DRAFTS = "drafts"
    SENT = "sent"


class Capabilities(StrEnum):
    CORE = "urn:ietf:params:jmap:core"
    MAIL = "urn:ietf:params:jmap:mail"
    SUBMISSION = "urn:ietf:params:jmap:submission"


class JmapClient:
    def __init__(self, email_address, provider_domain, auth_token):
        self.email_address = email_address
        self.provider_domain = provider_domain
        self.auth_token = auth_token
        self.headers = {
            # not sure why we need to do this for a StrEnum
            "Content-Type": str(ContentType.JSON),
            "Authorization": f"Bearer {auth_token}",
        }
        resp = requests.get(
            f"https://{provider_domain}/.well-known/jmap", headers=self.headers
        )
        resp.raise_for_status()
        self.session = resp.json()
        self.api_url = self.session["apiUrl"]
        self.account_id = self.session["primaryAccounts"][Capabilities.MAIL]
        self.mailboxen_mapping = self.get_mailboxen_mapping()
        self.draft_mailbox_id = self.mailboxen_mapping[MailboxRoles.DRAFTS]
        self.sent_mailbox_id = self.mailboxen_mapping[MailboxRoles.SENT]

    def try_get_identity_id(self, email):
        query_args = {
            "accountId": self.account_id,
            "filter": {"email": email},
        }
        query_identity = MethodCall("Identity/query", query_args)
        resp = self._make_request([query_identity])
        return str(resp["methodResponses"][0][1]["ids"][0])

    def get_mailboxen_mapping(self):
        """Returns the "Drafts" and "Sent" mailboxen."""
        query_args = {
            "accountId": self.account_id,
            "filter": {
                "operator": "OR",
                "conditions": [
                    {"role": str(MailboxRoles.DRAFTS)},
                    {"role": str(MailboxRoles.SENT)},
                ],
            },
        }
        query_mailboxen = MethodCall("Mailbox/query", query_args)
        get_args = {
            "accountId": self.account_id,
            "#ids": {
                "resultOf": "0",
                "name": "Mailbox/query",
                "path": "/ids",
            },
        }
        get_mailboxen = MethodCall("Mailbox/get", get_args)
        resp = self._make_request([query_mailboxen, get_mailboxen])
        mailboxen = resp["methodResponses"][1][1]["list"]
        return {x["role"]: x["id"] for x in mailboxen}

    def send_text_email(
        self, from_email, to_email, subject, text_content, draft_only=True
    ):
        return self._send_email(
            from_email, to_email, subject, text_content, ContentType.TEXT, draft_only
        )

    def send_html_email(
        self, from_email, to_email, subject, html_content, draft_only=True
    ):
        return self._send_email(
            from_email, to_email, subject, html_content, ContentType.HTML, draft_only
        )

    def _send_email(
        self, from_email, to_email, subject, content, content_type, draft_only
    ):
        identity_id = self.try_get_identity_id(from_email)
        match content_type:
            case ContentType.TEXT:
                body_dict = {
                    "textBody": [{"partId": "body", "type": str(ContentType.TEXT)}]
                }
            case ContentType.HTML:
                body_dict = {
                    "htmlBody": [{"partId": "body", "type": str(ContentType.HTML)}]
                }
            case _:
                raise ValueError(f"Unknown content type for email: {content_type}")

        draft = {
            "from": [{"email": from_email}],
            "to": [{"email": to_email}],
            "subject": subject,
            "mailboxIds": {self.draft_mailbox_id: True},
            "bodyValues": {"body": {"value": content, "charset": "utf-8"}},
            **body_dict,
        }
        set_email = MethodCall(
            "Email/set", {"accountId": self.account_id, "create": {"draft": draft}}
        )
        set_emailsubmission_args = {
            "accountId": self.account_id,
            "create": {
                "delivery": {
                    "emailId": "#draft",
                    "identityId": identity_id,
                }
            },
            "onSuccessUpdateEmail": {
                "#delivery": {
                    f"mailboxIds/{self.draft_mailbox_id}": None,
                    f"mailboxIds/{self.sent_mailbox_id}": True,
                }
            },
        }
        set_emailsubmission = MethodCall(
            "EmailSubmission/set", set_emailsubmission_args
        )

        if draft_only:
            method_calls = [set_email]
        else:
            method_calls = [set_email, set_emailsubmission]

        resp = self._make_request(method_calls)
        return resp

    def _build_request(self, method_calls):
        return {
            # TODO: don't just blindly use everything...
            "using": [str(x) for x in Capabilities],
            "methodCalls": [
                (x.method, x.kwargs, f"{idx}") for idx, x in enumerate(method_calls)
            ],
        }

    def _make_request(self, method_calls):
        resp = requests.post(
            self.api_url, headers=self.headers, json=self._build_request(method_calls)
        )
        resp.raise_for_status()
        return resp.json()

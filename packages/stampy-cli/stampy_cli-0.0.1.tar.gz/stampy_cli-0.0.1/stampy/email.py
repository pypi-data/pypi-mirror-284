import subprocess
import tempfile
from pathlib import Path

from stampy.types import EmailAction

EMAIL_INSTRUCTIONS = """
# You're writing the body of an email for {context}.
# All lines starting with '#' will be ignored; everything else will become the
# body of your email. A header and closing will be added automatically.
"""


def prompt_bool(prompt, default=True):
    suffix = "[y]/n" if default else "y/[n]"
    result = input(f"{prompt} {suffix}: ")
    if result.startswith("y"):
        return True
    elif result.startswith("n"):
        return False
    elif result == "":
        return default
    else:
        raise ValueError("huh?")


def handle_email(editor, template, context, sender, email_client):
    email_body = "\n".join(
        x.decode("utf-8") for x in get_email_body(editor, f"{context.name}'s birthday")
    )
    email_html = template.render(
        recipient_name=context.display_name, message=email_body, sender_name=sender.name
    )
    with tempfile.NamedTemporaryFile(suffix=".html") as tf:
        tf.write(email_html.encode("utf-8"))
        tf.flush()
        print(f"Preview your email here: file://{Path(tf.name).absolute()}")
        from_email = sender.email_address
        to_email = context.email_address
        subject = "Happy birthday!!"
        match EmailAction.prompt("What would you like to do with it?"):
            case EmailAction.SEND:
                email_client.send_html_email(
                    from_email, to_email, subject, email_html, draft_only=False
                )
            case EmailAction.DRAFT:
                email_client.send_html_email(
                    from_email, to_email, subject, email_html, draft_only=True
                )
            case EmailAction.DISCARD:
                print("Aborting; email was not sent.")


# TODO rename context here (it's a more limited context)
def get_email_body(editor, context):
    with tempfile.NamedTemporaryFile() as tf:
        tf.write(EMAIL_INSTRUCTIONS.format(context=context).encode("utf-8"))
        tf.flush()
        subprocess.run([editor, tf.name])
        tf.seek(0)
        for line in tf.readlines():
            if line.startswith(b"#"):
                continue
            else:
                yield line

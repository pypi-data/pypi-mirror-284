import concurrent.futures
import os
import sqlite3

from stampy.config import Config, JmapConfig
from stampy.contextvars import db_conn, jinja_env, jmap_client
from stampy.email import handle_email
from stampy.jmap import JmapClient
from stampy.sql import (
    CREATE_STATEMENT,
    INSERT_BIRTHDAY,
    INSERT_EMAIL,
    INSERT_FRIEND,
    SELECT_USER_INFO,
    UPCOMING_BIRTHDAYS,
    initialize_db,
)
from stampy.types import Action, BirthdayContext, SenderContext


def _create_jmap_client(jmap_config: JmapConfig):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    return executor.submit(JmapClient, **jmap_config.model_dump())


def act(config):
    upcoming_birthdays = db_conn.get().execute(UPCOMING_BIRTHDAYS).fetchall()
    user = SenderContext(name=config.signature, email_address=config.jmap.email_address)
    # Creating the JMAP client requires making an HTTP request--we kick that
    # off in the background while the user makes their selections.
    future_email_client = _create_jmap_client(config.jmap)
    for row in upcoming_birthdays:
        ctx = BirthdayContext(*row)
        print(f"It's {ctx.name}'s birthday on {ctx.birthday}.")
        match Action.prompt():
            case Action.SKIP:
                continue
            case Action.CARD:
                print(f"{ctx.name}'s mailing address is:\n{ctx.mailing_address}")
            case Action.EMAIL:
                print(f"{ctx.name}'s email address is: {ctx.email_address}")
                template = jinja_env.get().get_template("happy_birthday.html")
                email_client = future_email_client.result()
                email_html = handle_email(
                    config.editor, template, ctx, user, email_client
                )


def add(config):
    try:
        name = input("What's your friend's full name?  ").strip()
        display_name = input("What should we call your friend? ").strip()
        birth_year = int(input("What's their birth year? ").strip())
        birth_month = int(input("What's their birth month? ").strip())
        birth_day = int(input("What's their birth day? ").strip())
        email_address = input("What's their email address? ").strip()
    except EOFError:
        print()
        print("Aborting; friend was not added.")
        return

    with db_conn.get() as conn:
        friend_id = conn.execute(
            INSERT_FRIEND, {"name": name, "display_name": display_name}
        ).fetchone()[0]
        conn.execute(
            INSERT_BIRTHDAY,
            {
                "friend_id": friend_id,
                "year": birth_year,
                "month": birth_month,
                "day": birth_day,
            },
        )
        conn.execute(
            INSERT_EMAIL, {"friend_id": friend_id, "email_address": email_address}
        )


def check(config: Config):
    upcoming_birthdays = db_conn.get().execute(UPCOMING_BIRTHDAYS).fetchall()
    if not upcoming_birthdays:
        return

    print("Here are your upcoming events:")
    for x in upcoming_birthdays:
        print(f"- {x[0]}'s birthday on {x[2]}.")

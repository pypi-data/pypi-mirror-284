import sqlite3

CREATE_STATEMENT = """
BEGIN;
CREATE TABLE IF NOT EXISTS "birthday" (
	"id" INTEGER UNIQUE,
	"friend_id" INTEGER,
	"year" INTEGER NOT NULL,
	"month" INTEGER,
	"day" INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY ("friend_id") REFERENCES "friend"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "friend" (
	"id" INTEGER UNIQUE,
	"name" TEXT,
	"display_name" TEXT,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "mailing_address" (
	"id" INTEGER UNIQUE,
	"friend_id" INTEGER,
	"effective_date" TEXT,
	"address" TEXT,
	PRIMARY KEY("id"),
	FOREIGN KEY ("friend_id") REFERENCES "friend"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "email_address" (
	"id" INTEGER UNIQUE,
	"friend_id" INTEGER,
	"email_address" TEXT,
	"effective_date" TEXT,
	PRIMARY KEY("id"),
	FOREIGN KEY ("friend_id") REFERENCES "friend"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);
COMMIT;
"""


UPCOMING_BIRTHDAYS = """
SELECT
    name,
    display_name,
    date('now', 'localtime', 'start of year', (month-1) || ' months', (day-1) || ' days') AS current_yr_bday,
    email_address.email_address,
    mailing_address.address
FROM birthday
JOIN friend ON friend.id = birthday.friend_id
LEFT JOIN email_address ON friend.id = email_address.friend_id
LEFT JOIN mailing_address ON friend.id = mailing_address.friend_id
WHERE
    date('now', 'localtime') <= current_yr_bday AND
    current_yr_bday < date('now', 'localtime', '+7 days')
"""


SELECT_USER_INFO = """
SELECT name, email_address, email_api_url FROM user
"""


INSERT_FRIEND = """
INSERT INTO friend (name, display_name) VALUES (:name, :display_name) RETURNING id
"""

INSERT_BIRTHDAY = """
INSERT INTO birthday (friend_id, year, month, day) VALUES (:friend_id, :year, :month, :day)
"""

INSERT_EMAIL = """
INSERT INTO email_address (friend_id, email_address) VALUES (:friend_id, :email_address)
"""


def initialize_db(db_path):
    if not db_path.exists():
        db_path.parent.mkdir(parents=True, exist_ok=True)
        db_path.touch()
    con = sqlite3.connect(db_path)
    con.executescript(CREATE_STATEMENT)
    return con

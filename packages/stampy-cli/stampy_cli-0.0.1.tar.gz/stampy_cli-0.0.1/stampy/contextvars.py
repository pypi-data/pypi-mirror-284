from contextvars import ContextVar

db_conn = ContextVar("db_conn")
jmap_client = ContextVar("jmap_client")
jinja_env = ContextVar("jinja_env")

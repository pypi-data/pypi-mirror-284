import os
from typing import Union

from sqlalchemy import create_engine

PGUSER = os.environ.get("PGUSER", "pgadmin")
PGPASSWORD = os.environ.get("PGPASSWORD", "")
PGHOST = os.environ.get("PGHOST", "localhost")
PGDATABASE = os.environ.get("PGDATABASE", "aq")
ENGINE = None


def get_engine(
    pg_user: str = PGUSER,
    pg_password: str = PGPASSWORD,
    pg_host: str = PGHOST,
    pg_database: str = PGDATABASE,
    sslmode: Union[str, None] = None,
):
    global ENGINE
    if ENGINE is None:
        ENGINE = create_engine(
            f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_database}",
            echo=False,
            execution_options={"isolation_level": "AUTOCOMMIT"},
            connect_args={"sslmode": sslmode if sslmode else "require"},
            pool_size=10,
            max_overflow=10,
            pool_timeout=30,
            
        )
    return ENGINE

def reset_engine():
    global ENGINE
    ENGINE = None
    return ENGINE

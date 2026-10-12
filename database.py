# Manage database connections
import sqlite3
from pathlib import Path
from contextlib import contextmanager

DATABASE = Path(__file__).with_name("guildmembers.db")

# Get a database connection
@contextmanager
def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row # This allows us to access columns by name

    try:
        yield connection
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()

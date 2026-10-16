from database import get_db_connection
from guild_member import GuildMember

class GuildMemberDAO:
    @staticmethod
    def init_db():
        with get_db_connection() as connection:
                connection.execute('''
                    CREATE TABLE IF NOT EXISTS guild_members (
                        name TEXT PRIMARY KEY,
                        class_name TEXT NOT NULL
                    )
                ''')

    @staticmethod
    def get_all_guild_members(order_by='name'):
        if order_by not in ('name', 'class_name'):
            order_by = 'name'

        with get_db_connection() as connection:
            members = connection.execute(
                f'SELECT name, class_name FROM guild_members ORDER BY {order_by}'
            ).fetchall()

        return [
            GuildMember(member['name'], member['class_name'])
            for member in members
        ]

    @staticmethod
    def add_guild_member(name, class_name):
        with get_db_connection() as connection:
            cursor = connection.execute(
                'INSERT INTO guild_members (name, class_name) VALUES (?, ?)',
                (name, class_name)
            )

            return cursor.rowcount == 1  # Return True if one row was inserted, False otherwise

    @staticmethod
    def delete_guild_member(name):
        with get_db_connection() as connection:
            cursor = connection.execute(
                "DELETE FROM guild_members WHERE name = ?",
                (name, )
            )

            return cursor.rowcount > 0
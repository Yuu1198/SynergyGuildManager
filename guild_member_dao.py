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
        
                # Add sample data to the database if it is empty
                count = connection.execute('' \
                'SELECT COUNT(*) FROM guild_members'
                ).fetchone()[0]
        
                if count == 0:
                    sample_members = [
                        ("Calcain", "Warrior"),
                        ("Nortag", "Rogue"),
                        ("Biha", "Druid"),
                        ("Neptune", "Mage"),
                        ("Jocap", "Hunter")
                    ]
                    connection.executemany('''
                        INSERT INTO guild_members (name, class_name)
                        VALUES (?, ?)
                    ''', sample_members)

    @staticmethod
    def get_all_guild_members():
        with get_db_connection() as connection:
            members = connection.execute(
                'SELECT name, class_name FROM guild_members ORDER BY name'
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
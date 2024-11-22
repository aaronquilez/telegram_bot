from Models.DBConnection import db, connection
from datetime import datetime

class User:
    
    def create_table():
        db.execute("""--sql
            CREATE TABLE IF NOT EXISTS "User" (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                identifier TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                created_at TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES User(telegram_id) ON DELETE CASCADE
            );
        """)
    
    def create_user(name: str, indentifier: str, telegram_id: int):
        db.execute("""--sql
                   INSERT INTO "User" (name, identifier, user_id)
                   VALUES (?, ?, ?);
                   """,
                   (name, indentifier, telegram_id))
        connection.commit()

    def exists(id: int):
        result = User.findByPk(id)
        return True if result else False
    
    def findByPk(id: int):
        result = db.execute("SELECT * FROM 'User' WHERE id = ?",(id,)).fetchone()
        return result[0]


    def get_user_by_telegram_id(telegram_id: int):
        result = db.execute("""SELECT id, name, identifier FROM 'User' WHERE user_id = ?;""", (telegram_id,)).fetchone()
        return result


    def get_all_users_by_telegram_id(telegram_id: int) -> list[tuple[str]]:
        result: list = db.execute("""SELECT id, name, identifier FROM 'User' WHERE user_id = ?;""", (telegram_id,)).fetchall()
        return result

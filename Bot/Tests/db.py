import sqlite3

connection = sqlite3.connect('scamEX\Bot\Tests\mydata.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS scams(
    server_id INTEGER
    server_invite TEXT
    server_reason TEXT
)
""")

cursor.execute("""
INSERT INTO scams VALUES
(('888428503261909042', 'https://discord.gg/td4FhYgK5V', 'This is a test be aware!'))
""")


connection.commit()
connection.close()
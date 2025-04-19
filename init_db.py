import sqlite3, csv

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS channels")
cursor.execute("""
CREATE TABLE channels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    link TEXT NOT NULL,
    description TEXT
)
""")

with open("sample_data.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO channels (name, link, description) VALUES (?, ?, ?)",
                       (row['name'], row['link'], row['description']))

conn.commit()
conn.close()

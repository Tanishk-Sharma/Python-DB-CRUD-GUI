import sqlite3


def connect():
    conn = sqlite3.connect("subscribers.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS subscribers (id INTEGER PRIMARY KEY, first_name text, last_name text, email text, age integer)")
    conn.commit()
    conn.close()


def insert(first_name, last_name, email, age):
    conn = sqlite3.connect("subscribers.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO subscribers VALUES (NULL,?,?,?,?)",
                (first_name, last_name, email, age))
    conn.commit()
    conn.close()
    view()


def view():
    conn = sqlite3.connect("subscribers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM subscribers")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(first_name="", last_name="", email="", age=""):
    conn = sqlite3.connect("subscribers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM subscribers WHERE first_name=? OR last_name=? OR email=? OR age=?",
                (first_name, last_name, email, age))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("subscribers.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM subscribers WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, first_name, last_name, email, age):
    conn = sqlite3.connect("subscribers.db")
    cur = conn.cursor()
    cur.execute("UPDATE subscribers SET first_name=?, last_name=?, email=?, age=? WHERE id=?",
                (first_name, last_name, email, age, id))
    conn.commit()
    conn.close()


connect()

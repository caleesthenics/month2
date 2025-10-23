import sqlite3

conn = sqlite3.connect('database.db')

def create_table():
    conn.execute("""CREATE TABLE IF NOT EXISTS genres(
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT)""")


    conn.execute("""CREATE TABLE IF NOT EXISTS books(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    author TEXT,
    price INTEGER,
    genre_id INTEGER,
    FOREIGN KEY(genre_id) REFERENCES genres(genre_id))""")

def add_book(name, author, price, genre_id):
    conn.execute("INSERT INTO books (name, author, price, genre_id) VALUES (?,?,?,?)", (name, author, price, genre_id,))
    conn.commit()

def add_genre(name)g
    conn.execute("INSERT INTO genres (name) VALUES (?)", (name,))
    conn.commit()

def get_books():
    result = conn.execute("SELECT books.book_id, books.name, genres.name FROM books JOIN genres ON books.genre_id = genres.genre_id")
    return result.fetchall()

def get_books_genre():
    result = conn.execute("SELECT books.book_id, books.name, genres.name FROM books JOIN genres ON books.genre_id = genres.genre_id WHERE books.genre_id = 1")
    return result.fetchall()

def get_books_price(low, high):
    result = conn.execute("SELECT books.name, genres.name, books.price FROM books JOIN genres ON books.genre_id = genres.genre_id WHERE books.price BETWEEN ? AND ?", (low, high))
    return result.fetchall()

def pro4itai_pervii_bukvi_reelsov():
    pass

create_table()

# add_genre('Language')
# add_genre('Soft')
# add_genre('Boolean')
# add_book('Python', 'Unknown', 100,1)
# add_book('JS', 'Unknown2', 200,1)
# add_book('True', 'Unknown3', 150,3)
# add_book('Pycharm', 'Unknown4', 1000,2)
# add_book('VScode', 'Unknown5', 800,2)


print(get_books())
print(get_books_genre())
print(get_books_price(100,799))
import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('books.db')
    conn_archive = sqlite3.connect('archive_books.db')

    def create_archive_table():
        conn_archive.execute("""CREATE TABLE IF NOT EXISTS archive_books 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                author TEXT,
                                publication_year INTEGER,
                                genre TEXT,
                                number_of_pages INTEGER,
                                number_of_copies INTEGER) """)

    create_archive_table()

    def create_table():
        conn.execute("""CREATE TABLE IF NOT EXISTS books
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        deleted INTEGER DEFAULT 0,
                        name TEXT,
                        author TEXT,
                        publication_year INTEGER,
                        genre TEXT,
                        number_of_pages INTEGER,
                        number_of_copies INTEGER)""")

    def add_book(name, author, publication_year, genre, number_of_pages, number_of_copies):
        conn.execute("INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES (?, ?, ?, ?, ?, ?)",
                     (name, author, publication_year, genre, number_of_pages, number_of_copies))
        conn.commit()

    def soft_delete_book(zna4enie, book_id):
        conn.execute("UPDATE books SET deleted = ? WHERE id = ?", (zna4enie, book_id))
        cursor = conn.execute("SELECT name, author, publication_year, genre, number_of_pages, number_of_copies FROM books WHERE id = ?", (book_id,))
        row = cursor.fetchone()
        conn_archive.execute("""INSERT INTO archive_books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES (?, ?, ?, ?, ?, ?)""", row)
        conn.commit()
        conn_archive.commit()

    def hard_delete_book(book_id):
        cursor = conn.execute("SELECT deleted FROM books WHERE id = ?", (book_id,))
        result = cursor.fetchone()
        deleted = result[0]
        if deleted == 1:
            conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
        else:
            print('sna4ala vipolnite soft_delete_book')
        conn.commit()


    create_table()

    # counter = 0
    # while counter < 10:
    #     counter += 1
    #     add_book('hz', 'kto-to', '1818', 'detective', '8','10')

    soft_delete_book('1','3')
    hard_delete_book(3)


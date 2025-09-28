import sqlite3


def create_tables():
    """Функция для создания таблиц"""

    # удаление таблицы
    conn.execute("DROP TABLE IF EXISTS students")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS department (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)

    # создание таблицы students с колонками
    conn.execute("""
         CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            city TEXT,
            department_id INTEGER,
            FOREIGN KEY(department_id) REFERENCES department(id)
        )
    """)



def add_student(name: str, age: int, city: str, department_id: int):
    """Функция для добавления студента в базу данных"""

    # внесение новых данных в таблицу students
    conn.execute(
        "INSERT INTO students (name, age, city, department_id) VALUES (?, ?, ?, ?)", (name, age, city, department_id)
    )
    conn.commit()


def delete_student(student_id: int):
    """Функция для удаления студента из базы данных по id"""

    conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()


def get_some_students():
    result = conn.execute("SELECT name, age FROM students ORDER BY age LIMIT 4")
    return result.fetchall()

def get_student(name: str):
    result = conn.execute("SELECT * FROM students WHERE name = ?", (name,))
    return result.fetchall()

def update_student_name(student_id: int, new_name: str):
    conn.execute("UPDATE students SET name = ? WHERE id = ?", (new_name, student_id))
    conn.commit()

def add_department(name: str):
    conn.execute("INSERT INTO department (name) VALUES (?)", (name, ))
    conn.commit()


def get_all_students():
    result = conn.execute("SELECT s.name, d.name FROM students AS s JOIN department AS d ON s.department_id = d.id WHERE s.department_id = 1")
    return result.fetchall()


if __name__ == "__main__":
    conn = sqlite3.connect("database.db")

    create_tables()

    add_department("Backend")
    add_department("Frontend")

    add_student("Aibek", 23, "Bishkek", 1)
    add_student("Aisulu", 19, "Karakol", 2)
    add_student("Nursultan", 21, "Osh", 1)
    add_student("Maksat", 22, "Bishkek", 2)
    add_student("Aidana", 20, "Karakol", 1)
    add_student("Bakyt", 24, "Osh", 1)
    add_student("Gulnara", 18, "Bishkek", 1)
    add_student("Tilek", 23, "Karakol", 1)


    delete_student(1)
    update_student_name(4, "Maksim")

    print(get_all_students())
    print(get_student("Maksat"))
    print(get_student("Maksim"))

    conn.close()
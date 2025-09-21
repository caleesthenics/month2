class User:
    # переменные класса
    total_users = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.total_users += 1

    @classmethod
    def get_total_users(cls):
        return cls.total_users

    @classmethod
    def create_user(cls, name, email):
        if not cls.validate_email(email):
            raise ValueError("Invalid email")
        user = cls(name, email)
        return user

    @staticmethod
    def validate_email(email):
        return "@" in email

user_3 = User.create_user("John", "<w>")
print(user_3)
print(User.get_total_users())

print(User.total_users)

user_1 = User("Albert", "albert@gmail.com")
user_2 = User("Igor", "igor@gmail.com")

user_1.total_users = 4

print(User.total_users)
print(user_1.total_users)

def printer(func):
    print(func.__name__)
    def wrapper(*args, **kwargs):
        print(f"До вызова ф-ии {func.__name__}")
        result = func(*args, **kwargs)
        print(f"После вызова ф-ии {func.__name__}")
        return result

    return wrapper

@printer
def hello_world():
    print("Hello World!")

@printer
def add_numbers(number1, number2):
    return number1 + number2

hello_world()
print(add_numbers(1, 2))


def blahblah():
    print("blah blah blah")

blahblah = printer(blahblah)
blahblah()
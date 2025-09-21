class BaseView:
    def render(self):
        print('Template rendering')

class Logging:
    def render(self):
        print('Log start')
        super().render()
        print('log end')

class AuthRequired:
    def __init__(self, authorization):
        self.authorization = authorization

    def render(self):
        if self.authorization:
            print('auth ok')
            super().render()
        else:
            print('access denied')

class AdminPage(Logging, AuthRequired, BaseView):
    def render(self):
        print('admin page render start')
        super().render()
        print('admin page render end')

a = AdminPage(int(input('Пользователь авторизован ? (0 - да, 1 - нет)')))
a.render()
import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QFileDialog, QHBoxLayout
from PyQt6.QtGui import QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

# Словарь для хранения зарегистрированных пользователей
registered_users = {}


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Авторизация')

        # Устанавливаем розовый фон
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('pink'))
        self.setPalette(palette)

        # Создаем виджеты
        self.username_label = QLabel('Логин:')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Пароль:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton('Войти')
        self.login_button.clicked.connect(self.check_credentials)

        self.register_button = QPushButton('Регистрация')
        self.register_button.clicked.connect(self.open_register_window)

        # Располагаем виджеты в вертикальный макет
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Проверка на наличие пользователя в словаре зарегистрированных
        if username in registered_users and registered_users[username]['password'] == password:
            self.profile_window = ProfileWindow(username)
            self.profile_window.show()
            self.close()
        else:
            self.username_input.clear()
            self.password_input.clear()

    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Регистрация')

        # Устанавливаем розовый фон
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('pink'))
        self.setPalette(palette)

        # Создаем виджеты для регистрации
        self.username_label = QLabel('Придумайте логин:')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Придумайте пароль:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.photo_label = QLabel('Выберите фотографию:')
        self.photo_path_label = QLabel('Файл не выбран')
        self.photo_button = QPushButton('Выбрать файл')
        self.photo_button.clicked.connect(self.select_photo)

        self.register_button = QPushButton('Зарегистрироваться')
        self.register_button.clicked.connect(self.register_user)

        self.back_button = QPushButton('Назад')
        self.back_button.clicked.connect(self.back_to_login)

        # Макет
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.photo_label)
        layout.addWidget(self.photo_path_label)
        layout.addWidget(self.photo_button)
        layout.addWidget(self.register_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

        # Переменная для хранения пути к фотографии
        self.photo_path = ''

    def select_photo(self):
        # Открытие диалога для выбора файла
        photo_path, _ = QFileDialog.getOpenFileName(self, "Выберите фотографию", "", "Images (*.png *.xpm *.jpg)")
        if photo_path:
            self.photo_path = photo_path
            self.photo_path_label.setText(os.path.basename(photo_path))  # Отображаем имя файла

    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username and password and self.photo_path:
            if username not in registered_users:  # Проверяем, есть ли уже такой пользователь
                # Сохраняем пользователя в словарь
                registered_users[username] = {'password': password, 'photo': self.photo_path}
                print(f"Пользователь {username} успешно зарегистрирован.")
                self.back_to_login()
            else:
                print("Пользователь с таким логином уже существует.")
        else:
            print("Логин, пароль и фотография не могут быть пустыми.")

    def back_to_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


class ProfileWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle('Личный Профиль')

        # Устанавливаем розовый фон
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('pink'))
        self.setPalette(palette)

        # Лейбл с фотографией
        self.photo_label = QLabel()
        self.username = username
        user_data = registered_users.get(username, {})
        self.photo_pixmap = QPixmap(
            user_data.get('photo', 'default.png'))  # Замените на путь к вашему изображению по умолчанию
        self.photo_label.setPixmap(self.photo_pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio,
                                                            Qt.TransformationMode.SmoothTransformation))

        # Личная информация
        self.name_label = QLabel(f'Имя пользователя: {username}')
        self.email_label = QLabel(f'Email: {username}@mail.com')  # Для примера используем логин в качестве email

        # Кнопка для замены фотографии
        self.change_photo_button = QPushButton('Изменить фотографию')
        self.change_photo_button.clicked.connect(self.change_photo)

        # Макет
        layout = QVBoxLayout()
        layout.addWidget(self.photo_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.email_label)
        layout.addWidget(self.change_photo_button)

        self.setLayout(layout)

    def change_photo(self):
        # Открытие диалога для выбора файла
        photo_path, _ = QFileDialog.getOpenFileName(self, "Выберите новую фотографию", "", "Images (*.png *.xpm *.jpg)")
        if photo_path:
            # Обновляем фотографию в словаре и в профиле
            registered_users[self.username]['photo'] = photo_path
            self.photo_pixmap = QPixmap(photo_path)
            self.photo_label.setPixmap(self.photo_pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
            print(f"Фотография для {self.username} успешно изменена.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())

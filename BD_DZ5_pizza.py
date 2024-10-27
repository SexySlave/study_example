import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QRadioButton, QCheckBox, QPushButton, QTabWidget, QListWidget, QFrame, QMessageBox,
    QGridLayout  # Added QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


class FoodOrderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("6.1 - GUI заказа еды")
        self.setGeometry(300, 300, 800, 600)

        # Основное окно с вкладками и заказом
        self.main_layout = QHBoxLayout()

        # Создаем вкладки
        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_pizza_tab(), "Пицца")
        self.tabs.addTab(self.create_wings_tab(), "Крылышки")

        # Добавляем заказы в правой колонке
        self.order_widget = QListWidget()
        self.order_widget.setStyleSheet("background-color: #ffcc99; border: none; padding: 10px;")
        self.order_widget.setWordWrap(True)  # Включаем перенос слов

        # Добавляем правую колонку с заказами
        order_layout = QVBoxLayout()
        order_label = QLabel("ВАШ ЗАКАЗ")
        order_label.setStyleSheet("font-weight: bold; font-size: 16px; padding-bottom: 5px;")
        order_layout.addWidget(order_label)
        order_layout.addWidget(self.order_widget)

        # Кнопка для удаления позиции из заказа
        remove_button = QPushButton("Удалить из заказа")
        remove_button.setStyleSheet("background-color: #FF6347; color: white; padding: 10px; font-size: 14px;")
        remove_button.clicked.connect(self.remove_order_item)
        order_layout.addWidget(remove_button)

        # Контейнер для заказа с рамкой
        order_frame = QFrame()
        order_frame.setLayout(order_layout)
        order_frame.setFixedWidth(200)  # Ограничиваем ширину контейнера
        order_frame.setStyleSheet(
            "background-color: #f3e2c7; border: 2px solid #b88a65; border-radius: 8px; padding: 10px;")  # Полная рамка

        # Добавляем вкладки и правую колонку в главный макет
        self.main_layout.addWidget(self.tabs)
        self.main_layout.addWidget(order_frame)

        # Центральный виджет
        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def create_pizza_tab(self):
        pizza_tab = QWidget()
        pizza_layout = QVBoxLayout()

        # Заголовок "Пробуйте нашу удивительную пиццу"
        special_title = QLabel("Пробуйте нашу удивительную пиццу")
        special_title.setStyleSheet( "font-weight: bold; font-size: 16px; color: brown; padding: 5px;")
        pizza_layout.addWidget(special_title)

        # Заголовок и описание
        header_frame = QFrame()
        header_layout = QHBoxLayout()

        # Иконка пиццы
        pizza_icon_label = QLabel()
        pizza_icon = QPixmap('pizza_icon.png')  # замените на путь к изображению иконки пиццы
        pizza_icon_label.setPixmap(pizza_icon.scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio))

        # Текстовое описание
        pizza_description_label = QLabel(
            "Создаем для вас пиццу на заказ. Начните с вашего любимого коржа и добавьте любые начинки, а также идеальное количество сыра и соуса.")
        pizza_description_label.setWordWrap(True)
        pizza_description_label.setStyleSheet("font-size: 14px; padding: 10px;")

        header_layout.addWidget(pizza_icon_label)
        header_layout.addWidget(pizza_description_label)
        header_frame.setLayout(header_layout)
        header_frame.setStyleSheet("background-color: #f5d1a4; border-radius: 8px; padding: 10px;")

        # Блок "Выбор коржа"
        crust_frame = QFrame()
        crust_layout = QVBoxLayout()
        crust_label = QLabel("ВЫБОР ВАШЕГО КОРЖА")
        crust_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.crust_manual = QRadioButton("Тонкое тесто")
        self.crust_flat = QRadioButton("Толстое тесто")
        self.crust_stuffed = QRadioButton("Бортики с сыром")

        crust_layout.addWidget(crust_label)
        crust_layout.addWidget(self.crust_manual)
        crust_layout.addWidget(self.crust_flat)
        crust_layout.addWidget(self.crust_stuffed)
        crust_frame.setLayout(crust_layout)
        crust_frame.setStyleSheet("background-color: #ff9999; padding: 10px; border-radius: 8px;")  # Changed to red

        # Блок "Выбор начинки"
        toppings_frame = QFrame()
        toppings_layout = QGridLayout()  # Changed to QGridLayout

        # Заголовок для выбора начинки
        topping_label = QLabel("Выберите начинку")
        topping_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        toppings_layout.addWidget(topping_label, 0, 0, 1, 2)  # Add the label spanning both columns

        toppings = [
            "Пепперони", "Колбаса", "Бекон", "Говядина",
            "Ананас", "Оливки", "Томат", "Зеленый перец", "Грибы", "Лук", "Сыр"
        ]

        self.topping_checkboxes = []
        for i, topping in enumerate(toppings):
            checkbox = QCheckBox(topping)
            self.topping_checkboxes.append(checkbox)
            row = (i // 2) + 1  # Calculate the row (first row for label)
            column = i % 2  # Alternate between two columns
            toppings_layout.addWidget(checkbox, row, column)  # Add checkboxes to grid layout

        toppings_frame.setLayout(toppings_layout)
        toppings_frame.setStyleSheet("background-color: #ff9999; padding: 10px; border-radius: 8px;")  # Changed to red

        # Кнопка добавления пиццы к заказу
        add_button = QPushButton("Добавить к заказу")
        add_button.setStyleSheet("background-color: #FF6347; color: white; padding: 10px; font-size: 14px;")
        add_button.clicked.connect(self.add_pizza_to_order)

        # Добавляем элементы на вкладку пиццы
        pizza_layout.addWidget(header_frame)
        pizza_layout.addWidget(crust_frame)
        pizza_layout.addWidget(toppings_frame)
        pizza_layout.addWidget(add_button)

        pizza_tab.setLayout(pizza_layout)
        return pizza_tab

    def create_wings_tab(self):
        wings_tab = QWidget()
        wings_layout = QVBoxLayout()

        # Заголовок "Пробуйте наши удивительные крылышки"
        special_title = QLabel("Пробуйте наши удивительные крылышки")
        special_title.setStyleSheet("font-weight: bold; font-size: 16px; color: brown; padding: 5px;")
        wings_layout.addWidget(special_title)

        # Заголовок и описание
        header_frame = QFrame()
        header_layout = QHBoxLayout()

        # Иконка крылышек
        wings_icon_label = QLabel()
        wings_icon = QPixmap('wings_icon.png')  # замените на путь к изображению иконки крылышек
        wings_icon_label.setPixmap(wings_icon.scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio))

        # Текстовое описание
        wings_description_label = QLabel(
            "6 кусочков белого мяса с насыщенным вкусом курицы, которые заставят вас вернуться за добавкой.")
        wings_description_label.setWordWrap(True)
        wings_description_label.setStyleSheet("font-size: 14px; padding: 10px;")

        header_layout.addWidget(wings_icon_label)
        header_layout.addWidget(wings_description_label)
        header_frame.setLayout(header_layout)
        header_frame.setStyleSheet("background-color: #f5d1a4; border-radius: 8px; padding: 10px;")

        # Блок выбора вкуса
        flavor_frame = QFrame()
        flavor_layout = QVBoxLayout()
        flavor_label = QLabel("ВЫБЕРИТЕ СВОЙ ВКУС")
        flavor_label.setStyleSheet("font-weight: bold; font-size: 16px;")

        self.buffalo_radio = QRadioButton("Баффало")
        self.sour_sweet_radio = QRadioButton("Кисло-сладкий")
        self.teriyaki_radio = QRadioButton("Терияки")

        flavor_layout.addWidget(flavor_label)
        flavor_layout.addWidget(self.buffalo_radio)
        flavor_layout.addWidget(self.sour_sweet_radio)
        flavor_layout.addWidget(self.teriyaki_radio)
        flavor_frame.setLayout(flavor_layout)
        flavor_frame.setStyleSheet("background-color: #ff9999; padding: 10px; border-radius: 8px;")  # Changed to red

        # Кнопка добавления крылышек к заказу
        add_wings_button = QPushButton("Добавить крылышки к заказу")
        add_wings_button.setStyleSheet("background-color: #FF6347; color: white; padding: 10px; font-size: 14px;")
        add_wings_button.clicked.connect(self.add_wings_to_order)

        # Добавляем элементы на вкладку крылышек
        wings_layout.addWidget(header_frame)
        wings_layout.addWidget(flavor_frame)
        wings_layout.addWidget(add_wings_button)

        wings_tab.setLayout(wings_layout)
        return wings_tab

    def add_pizza_to_order(self):
        crust = ""
        if self.crust_manual.isChecked():
            crust = "Тонкое тесто"
        elif self.crust_flat.isChecked():
            crust = "Толстое тесто"
        elif self.crust_stuffed.isChecked():
            crust = "Бортики с сыром"

        toppings = [cb.text() for cb in self.topping_checkboxes if cb.isChecked()]
        order_item = f"Пицца с {crust} и {' + '.join(toppings) if toppings else 'без начинки'}"
        self.order_widget.addItem(order_item)

    def add_wings_to_order(self):
        flavor = ""
        if self.buffalo_radio.isChecked():
            flavor = "Баффало"
        elif self.sour_sweet_radio.isChecked():
            flavor = "Кисло-сладкий"
        elif self.teriyaki_radio.isChecked():
            flavor = "Терияки"

        order_item = f"Крылышки со вкусом {flavor}"
        self.order_widget.addItem(order_item)

    def remove_order_item(self):
        selected_items = self.order_widget.selectedItems()
        if selected_items:
            for item in selected_items:
                self.order_widget.takeItem(self.order_widget.row(item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FoodOrderApp()
    window.show()
    sys.exit(app.exec())

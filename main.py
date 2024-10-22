import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout,
                             QPushButton, QFileDialog, QListWidget, QTextEdit, QFormLayout, QLineEdit,
                             QComboBox, QSpinBox, QCheckBox, QLabel)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создаем центральный виджет с вкладками
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Добавляем каждое окно как отдельную вкладку
        self.tabs.addTab(self.createTab1(), "Сканирование папки")
        self.tabs.addTab(self.createTab2(), "Редактирование файла")
        self.tabs.addTab(self.createTab3(), "Сохранение текста")
        self.tabs.addTab(self.createTab4(), "Форма")
        self.tabs.addTab(self.createTab5(), "Чтение списка")

        self.setWindowTitle("PyQt6 Приложение с вкладками")
        self.setGeometry(300, 300, 600, 400)

    def createTab1(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.fileList = QListWidget()
        btnScan = QPushButton("Сканировать папку")
        btnScan.clicked.connect(self.scanFolder)
        layout.addWidget(self.fileList)
        layout.addWidget(btnScan)
        tab.setLayout(layout)
        return tab

    def scanFolder(self):
        folder = QFileDialog.getExistingDirectory(self, "Выбрать папку")
        if folder:
            self.fileList.clear()
            for file_name in os.listdir(folder):
                self.fileList.addItem(file_name)

    def createTab2(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.textEdit = QTextEdit()
        btnOpen = QPushButton("Открыть файл")
        btnSave = QPushButton("Сохранить файл")
        btnOpen.clicked.connect(self.openFile)
        btnSave.clicked.connect(self.saveFile)
        layout.addWidget(self.textEdit)
        layout.addWidget(btnOpen)
        layout.addWidget(btnSave)
        tab.setLayout(layout)
        return tab

    def openFile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'r') as file:
                self.textEdit.setText(file.read())

    def saveFile(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.textEdit.toPlainText())

    def createTab3(self):
        tab = QWidget()
        layout = QVBoxLayout()
        btnSave = QPushButton("Сохранить текст в другую папку")
        btnSave.clicked.connect(self.saveTextInFolder)
        layout.addWidget(self.textEdit)
        layout.addWidget(btnSave)
        tab.setLayout(layout)
        return tab

    def saveTextInFolder(self):
        folder = QFileDialog.getExistingDirectory(self, "Выбрать папку")
        if folder:
            file_path = os.path.join(folder, "output.txt")
            with open(file_path, 'w') as file:
                file.write(self.textEdit.toPlainText())

    def createTab4(self):
        tab = QWidget()
        layout = QFormLayout()
        self.line_edit = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Option 1", "Option 2", "Option 3"])
        self.spin_box = QSpinBox()
        self.check_box = QCheckBox("Опция")
        self.line_edit2 = QLineEdit()

        layout.addRow("Поле 1", self.line_edit)
        layout.addRow("Поле 2", self.combo_box)
        layout.addRow("Поле 3", self.spin_box)
        layout.addRow("Поле 4", self.check_box)
        layout.addRow("Поле 5", self.line_edit2)

        btnSave = QPushButton("Сохранить данные формы")
        btnSave.clicked.connect(self.saveFormData)
        layout.addWidget(btnSave)
        tab.setLayout(layout)
        return tab

    def saveFormData(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'a') as file:
                file.write(f"1. Поле 1: {self.line_edit.text()}\n")
                file.write(f"2. Поле 2: {self.combo_box.currentText()}\n")
                file.write(f"3. Поле 3: {self.spin_box.value()}\n")
                file.write(f"4. Поле 4: {self.check_box.isChecked()}\n")
                file.write(f"5. Поле 5: {self.line_edit2.text()}\n\n")

    def createTab5(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.label = QLabel("Результаты")
        btnRead = QPushButton("Прочитать список из файла")
        btnRead.clicked.connect(self.readList)
        layout.addWidget(self.label)
        layout.addWidget(btnRead)
        tab.setLayout(layout)
        return tab

    def readList(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'r') as file:
                data = file.readlines()
                self.label.setText(f"Прочитано {len(data)} элементов, Поле 2: {data[1]}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())

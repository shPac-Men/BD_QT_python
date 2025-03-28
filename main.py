from PyQt6.QtWidgets import QApplication, QLabel, QWidget  # Для PyQt6
# from PySide6.QtWidgets import QApplication, QLabel, QWidget  # Для PySide6

app = QApplication([])  # Создаём приложение

window = QWidget()      # Создаём окно
window.setWindowTitle("Qt в Python")
window.setGeometry(100, 100, 300, 200)  # (x, y, width, height)

label = QLabel("Привет, Qt!", parent=window)
label.move(100, 80)     # Позиция текста

window.show()           # Показываем окно
app.exec()              # Запускаем цикл событий
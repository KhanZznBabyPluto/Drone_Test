import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtGui import QColor, QBrush, QPen
from PyQt6.QtCore import Qt, QTimer

class CellAutomaton(QMainWindow):
    def __init__(self, grid_size):
        super().__init__()
        self.setWindowTitle("Клеточный автомат")
        self.setGeometry(100, 100, 800, 600)
        self.grid_size = grid_size
        self.cell_size = 30
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setCentralWidget(self.view)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_cells)
        self.timer.start(1000)  # Обновление каждую секунду

        self.create_grid()

    def create_grid(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x = col * self.cell_size
                y = row * self.cell_size
                color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                cell = QGraphicsRectItem(x, y, self.cell_size, self.cell_size)
                cell.setPen(QPen(Qt.GlobalColor.black))
                cell.setBrush(QBrush(color))
                self.scene.addItem(cell)

    def update_cells(self):
        for item in self.scene.items():
            if isinstance(item, QGraphicsRectItem):
                new_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                item.setBrush(QBrush(new_color))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    automaton = CellAutomaton(10)  # Замените 10 на желаемый размер сетки
    automaton.show()
    sys.exit(app.exec())

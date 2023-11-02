import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor, QPen
import random
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.colors as matcolors


class CitySimulation(QMainWindow):
    def __init__(self, grid_size=20):
        super().__init__()
        self.setWindowTitle("Моделирование города")
        self.setGeometry(100, 100, 800, 800)

        self.view = QGraphicsView(self)
        self.view.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)

        self.grid_size = grid_size
        self.num_districts = self.grid_size * self.grid_size

        self.city_grid = [[random.randint(0, 10) for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        self.cell_size = 30
        self.update_visualization()

    def update_visualization(self):
        self.scene.clear()

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                rating = self.city_grid[row][col]
                fill_color = self.color_by_rating(rating)

                rect = self.scene.addRect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                brush = QBrush(QColor(fill_color))
                rect.setBrush(brush)

        self.view.viewport().update()

    def color_by_rating(self, rating):
        colors = [(0, 'green'), (0.25, 'lime'),(0.5, 'yellow'), (0.75, 'orange'), (1, 'red')]
        custom_cmap = LinearSegmentedColormap.from_list('custom', colors)   
        normalized_rating = rating / 10.0
        color = custom_cmap(normalized_rating)
        return matcolors.to_hex(color)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CitySimulation()
    window.show()
    sys.exit(app.exec())

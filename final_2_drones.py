import sys
from PyQt6.QtGui import QBrush, QColor, QTransform
import random
from cell_class import District
from drone_class import Drone
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QTimer


class CityGrid(QMainWindow):
    def __init__(self, grid_size, show_drone=True):
        super().__init__()
        self.setWindowTitle("Клеточный автомат")
        self.setGeometry(100, 100, 800, 600)
        self.grid_size = grid_size
        self.cell_size = 30
        self.show_drone = show_drone

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        layout.addWidget(self.view)

        if self.show_drone:
            self.drone = Drone(3, 2)
            self.drone.make_active()

        self.create_grid()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_cells)
        self.timer.start(1300)

    def create_grid(self):
        self.city_grid = [[District(1) for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for _ in range(15):
            row, col = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            self.city_grid[row][col].rating = 100

        for _ in range(30):
            row, col = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            self.city_grid[row][col].rating = 0

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                district = self.city_grid[row][col]
                if district.rating == 0 or district.rating == 100:
                    continue
                district.rating = random.randint(0, 100)
                district.color = district.color_by_rating()

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                current_district = self.city_grid[row][col]
                neighbors_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for offset_row, offset_col in neighbors_offsets:
                    neighbor_row, neighbor_col = row + offset_row, col + offset_col
                    if 0 <= neighbor_row < self.grid_size and 0 <= neighbor_col < self.grid_size:
                        neighbor_district = self.city_grid[neighbor_row][neighbor_col]
                        current_district.add_neighbours(neighbor_district)

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                district = self.city_grid[row][col]
                color = QColor(district.color)
                rect = QGraphicsRectItem(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                rect.setBrush(QBrush(color))
                self.scene.addItem(rect)



    def update_cells(self):
        print("update_cells() вызван")
        if self.show_drone:
            for _ in range(6):
                self.drone.set_direction()
                self.drone.move(self.grid_size)
                x, y = self.drone.x, self.drone.y
                self.city_grid[x][y].flag = 3

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                district = self.city_grid[row][col]
                district.rating_change()
                district.color = district.color_by_rating()
                district.clear_neighbours()
                neighbors_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for offset_row, offset_col in neighbors_offsets:
                    neighbor_row, neighbor_col = row + offset_row, col + offset_col
                    if 0 <= neighbor_row < self.grid_size and 0 <= neighbor_col < self.grid_size:
                        neighbor_district = self.city_grid[neighbor_row][neighbor_col]
                        district.add_neighbours(neighbor_district)
                

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                district = self.city_grid[row][col]
                item = self.scene.itemAt(col * self.cell_size, row * self.cell_size, QTransform())
                if isinstance(item, QGraphicsRectItem):
                    item.setBrush(QBrush(QColor(district.color)))
        
        self.view.viewport().update()

if __name__ == "__main__":
    app = QApplication([])

    window_with_drone = CityGrid(10, show_drone=True)

    window_without_drone = CityGrid(10, show_drone=False)

    main_window = QMainWindow()
    main_window.setWindowTitle("Главное окно")
    main_window.setGeometry(100, 100, 800, 600)

    layout = QHBoxLayout()
    layout.addWidget(window_with_drone)
    layout.addWidget(window_without_drone)

    central_widget = QWidget()
    central_widget.setLayout(layout)
    main_window.setCentralWidget(central_widget)

    main_window.show()
    app.exec()

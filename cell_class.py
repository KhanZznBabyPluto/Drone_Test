import matplotlib.colors as matcolors
from matplotlib.colors import LinearSegmentedColormap
from integrating_formula import integrating
from scipy.stats import norm

class District():

    def __init__(self, rating):
        self.rating = rating
        self.color = self.color_by_rating()
        self.neighbours = []
        self.flag = 0

    def color_by_rating(self):
        colors = [(0, 'green'), (0.25, 'lime'), (0.5, 'yellow'), (0.75, 'orange'), (1, 'red')]
        custom_cmap = LinearSegmentedColormap.from_list('custom', colors)
        normalized_rating = self.rating / 10.0
        color = custom_cmap(normalized_rating)
        hex_color = matcolors.to_hex(color)
        return hex_color
    
    def add_neighbours(self, neighbour_district):
        self.neighbours.append(neighbour_district)

    def rating_change(self):
        if self.flag != 0:
            self.flag -= 1
            self.rating -= 25
        else:
            integrating(self)

    def clear_neighbours(self):
        self.neighbours.clear()
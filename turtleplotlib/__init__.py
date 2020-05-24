import math

from matplotlib import pyplot as plt
from matplotlib.lines import Line2D as Line


class Turtle:
    """Class to emulate Python's turtle inside a matplotlib Figure
    """
    def __init__(self, figure=None, figsize=(5, 5), steps=500):
        if figure is None:
            figure = plt.figure(figsize=figsize)
        self.figure = figure
        self.steps = 500
        self.reset()

    def _to_canvas(self, point):
        return (
            ((point[0] + self.center_x) / self.steps),
            ((point[1] + self.center_y) / self.steps),
        )

    def line(self, origin, dest):
        if not self.drawing:
            return
        origin = self._to_canvas(origin)
        dest = self._to_canvas(dest)
        line = Line(
            [origin[0], dest[0]],
            [origin[1], dest[1]],
            transform=self.figure.transFigure,
            **self.attributes,
        )

        self.figure.lines.append(line)
        self.figure.canvas.draw()

    def clear(self):
        self.figure.clear()

    def reset(self):
        self.center_x = self.steps // 2
        self.center_y = self.steps // 2

        self.x = 0
        self.y = 0

        self.direction = 0
        self.drawing = True

        self.attributes = {}

    def up(self):
        self.drawing = False

    def down(self):
        self.drawing = True

    def forward(self, amount):
        original_x = self.x
        original_y = self.y
        alpha = math.radians(self.direction)
        self.x += amount * math.cos(alpha)
        self.y += amount * math.sin(alpha)
        self.line((original_x, original_y), (self.x, self.y))

    def left(self, amount):
        self.direction += amount
        self.direction = self.direction % 360

    def right(self, amount):
        self.direction -= amount
        self.direction = self.direction % 360

    def __repr__(self):
        return f"[Turtle (self.x, self.y), drawing: {self.drawing}]"

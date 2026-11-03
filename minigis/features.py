class Feature:
    def __init__(self):
        self.name = "GIS Feature"

    def vis(self, canvas):
        raise NotImplementedError(
            "Subclasses must implement vis()"
        )

class Point(Feature):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

    def vis(self, canvas):
        canvas.create_oval(
            self.x - 4,
            self.y - 4,
            self.x + 4,
            self.y + 4,
            fill="red"
        )

import math


class Polyline(Feature):
    def __init__(self, points):
        super().__init__()

        self.points = points

    def length(self):
        total_length = 0

        for i in range(len(self.points) - 1):

            x1, y1 = self.points[i]
            x2, y2 = self.points[i + 1]

            distance = math.sqrt(
                (x2 - x1) ** 2 +
                (y2 - y1) ** 2
            )

            total_length += distance

        return total_length

    def vis(self, canvas):

        coordinates = []

        for x, y in self.points:
            coordinates.extend([x, y])

        if len(coordinates) >= 4:

            canvas.create_line(
                coordinates,
                fill="blue",
                width=2
            )

class Polygon(Polyline):

    def __init__(self, points):
        super().__init__(points)

    def vis(self, canvas):

        coordinates = []

        for x, y in self.points:
            coordinates.extend([x, y])

        if len(coordinates) >= 6:

            canvas.create_polygon(
                coordinates,
                fill="lightblue",
                outline="black"
            )


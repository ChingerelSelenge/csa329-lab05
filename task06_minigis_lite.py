import tkinter as tk

from minigis import Point, Polyline, Polygon


def main():

    root = tk.Tk()

    root.title("Mini-GIS Lite")
    root.geometry("900x650")

    canvas = tk.Canvas(
        root,
        width=900,
        height=650,
        bg="white"
    )

    canvas.pack()

    # Point object
    point = Point(150, 150)

    # Polyline object
    line = Polyline([
        (100, 300),
        (200, 250),
        (300, 350),
        (400, 200)
    ])

    # Polygon object
    polygon = Polygon([
        (500, 200),
        (700, 200),
        (750, 400),
        (600, 500),
        (500, 200)
    ])

    # Visualize features
    point.vis(canvas)

    line.vis(canvas)

    polygon.vis(canvas)

    # Calculate polyline length
    print("Polyline length:", line.length())

    root.mainloop()


if __name__ == "__main__":
    main()


# GIS Laboratory 05
## Python Programming Environment, Exceptions, Modules and Mini-GIS Package

**Course:** GIS Programming  
**Laboratory:** 05  
**Topic:** Python IDE, Exception Handling, Modules and Mini-GIS-lite

---

## 1. Objectives

The objectives of this laboratory are:

- Understand Python IDLE and its different windows.
- Identify and fix SyntaxError and runtime exceptions.
- Use try-except-finally for exception handling.
- Create and import custom Python modules.
- Understand sys.path and Python package organization.
- Use built-in modules such as os, sys, math, glob, shutil and zipfile.
- Create a simplified GIS package using object-oriented programming.
- Understand inheritance between Feature, Point, Polyline and Polygon.
- Run and explore the Mini-GIS application.

## 2. Technologies Used

- Python 3.12
- Visual Studio Code
- Python IDLE
- Tkinter
- struct
- Git and GitHub
- QGIS

## 3. Project Structure

```text
csa329-lab05/
│
├── data/
│   ├── Test_Points/
│   ├── Test_Lines/
│   └── Test_Polygons/
│
├── minigis/
│   ├── __init__.py
│   ├── features.py
│   ├── commons.py
│   └── readshp.py
│
├── output/
│   ├── gis_data.txt
│
├── task01_ide.py
├── task02_syntax_error.py
├── task03_exception.py
├── task04_try_except.py
├── task05_modules.py
├── task06_minigis_lite.py
├── task07_run_minigis.py
├── gis_utils.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 4. Laboratory Tasks

### Task 1: Python IDE

- Opened Python IDLE.
- Explored Interactive Shell and Editor.
- Tested Python commands.
- Configured fonts, tabs and syntax highlighting.

### Task 2: SyntaxError

- Created intentional syntax errors.
- Identified missing parentheses and indentation errors.
- Corrected the errors and executed the program successfully.

### Task 3: Runtime Exceptions

Practiced the following exceptions:

- NameError
- TypeError
- ValueError
- ZeroDivisionError
- FileNotFoundError

Identified the causes of runtime errors and corrected them.

### Task 4: Exception Handling

- Implemented try-except-finally.
- Handled file-related errors.
- Created and wrote data to a text file.
- Closed files safely using finally.

### Task 5: Python Modules

- Created a custom module named `gis_utils.py`.
- Imported custom functions into another Python file.
- Explored sys.path and the current working directory.
- Practiced built-in modules: os, sys, math, glob, shutil and zipfile.

### Task 6: Mini-GIS-lite Package

Created a simplified GIS package using Python classes and inheritance.

Class hierarchy:

```text
Feature
├── Point
└── Polyline
    └── Polygon
```

Implemented:

- Feature superclass with `__init__()` and `vis()`.
- Point class for point visualization.
- Polyline class with `length()` and `vis()`.
- Polygon class inheriting from Polyline.
- Method overriding for polygon visualization.
- Package initialization using `__init__.py`.

Used Tkinter Canvas to visualize geometric objects.

### Task 7: Shapefile and Mini-GIS

- Read Shapefile header information using Python's struct module.
- Examined file code, file length, version and shape type.
- Explored the Mini-GIS application.
- Practiced loading spatial datasets and visualizing GIS layers.

## 5. Shapefile Data

The laboratory uses three types of spatial data:

| Geometry | Description |
|---|---|
| Point | Represents individual locations |
| Polyline | Represents linear features such as rivers |
| Polygon | Represents areas and boundaries |

The Shapefile components include:

- `.shp` — Geometry data
- `.shx` — Shape index
- `.dbf` — Attribute data
- `.prj` — Coordinate reference system

## 6. How to Run

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run individual tasks:

```powershell
python task02_syntax_error.py
python task03_exception.py
python task04_try_except.py
python task05_modules.py
python task06_minigis_lite.py
python task07_run_minigis.py
```

## 7. Conclusion

In this laboratory, I learned how to configure the Python programming environment, identify and handle different types of errors, and organize code using Python modules and packages.

I also practiced object-oriented programming by creating Feature, Point, Polyline and Polygon classes with inheritance and method overriding.

Finally, I developed a simplified Mini-GIS package and explored how Python can be used to process and visualize spatial data.

## 8. Repository

GitHub: https://github.com/ChingerelSelenge/csa329-lab05

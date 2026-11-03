import os
import sys
import math
import glob
import shutil
import zipfile

# OS module
print("Current directory:", os.getcwd())

# SYS module
print("Python version:", sys.version)

# MATH module
print("Square root:", math.sqrt(25))

# GLOB module
print("Python files:", glob.glob("*.py"))

# SHUTIL module
print("Copy module available:", callable(shutil.copyfile))

# ZIPFILE module
print("Zip module available:", zipfile.is_zipfile("data.zip"))
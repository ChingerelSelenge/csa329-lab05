file = None

try:
    file = open("output/gis_data.txt", "w")

    file.write("GIS Laboratory 05\n")
    file.write("Python Exception Handling\n")

    print("File written successfully")

except OSError as error:
    print("Error:", error)

finally:
    if file is not None:
        file.close()
        print("File closed")

    print("Program finished")
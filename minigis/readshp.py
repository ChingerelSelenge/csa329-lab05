import struct


def read_shapefile_header(filename):

    with open(filename, "rb") as file:

        header = file.read(100)

        if len(header) != 100:
            raise ValueError("Invalid shapefile header")

        file_code = struct.unpack(">i", header[0:4])[0]

        file_length = struct.unpack(">i", header[24:28])[0]

        version = struct.unpack("<i", header[28:32])[0]

        shape_type = struct.unpack("<i", header[32:36])[0]

        return {
            "file_code": file_code,
            "file_length": file_length * 2,
            "version": version,
            "shape_type": shape_type
        }
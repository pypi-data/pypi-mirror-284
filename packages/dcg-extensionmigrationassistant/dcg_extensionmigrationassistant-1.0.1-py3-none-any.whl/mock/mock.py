import importlib_metadata
import csv

# def read_csv_file():
#     # Get the distribution object for the current package
#     distribution = importlib_metadata.distribution(__package__)

#     # Locate the path to sct_input.csv relative to the distribution
#     csv_file_path = distribution.locate_file('assessment/sct_input.csv')

#     # Read the CSV file
#     with open(csv_file_path, 'r', newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             print(row)  # Example: Print each row

# read_csv_file()

# from importlib_metadata import version, metadata
# dist = metadata("mock")  
# print(dist)

# import importlib.resources as pkg_resources
# import mock

# # Reading a non-Python file
# with pkg_resources.open_text(mock, 'mock.txt') as file:
#     data = file.read()
#     print(data)
import os
import pandas as pd

package_dir = os.path.dirname(__file__)
file_path = os.path.join(package_dir, "mock.txt")
# print(file_path)

data = pd.read_csv(file_path)
print(data)


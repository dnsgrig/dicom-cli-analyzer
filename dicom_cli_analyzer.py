# imports
import sys
import os
from pydicom import dcmread
from pathlib import Path
from collections import defaultdict


# function extracts the unique study indentifier(s) of all files found in the input directory
def extract_study_identifiers_from_directory(path_to_directory):
    directory_path = Path(path_to_directory)
    dicom_files = directory_path.rglob("*.dcm") # perform dfs and return iterator
    uids = set() # use uniqueness of sets to our advantage

    # populate uids set with StudyInstanceUIDs
    for file in dicom_files:
        try:
            dicom_file = dcmread(file, force = True)
            uids.add(dicom_file.StudyInstanceUID)

        except AttributeError:
            print(f"Problem reading StudyInstanceUID from {file.name}")

    # output result into stderr
    for uid in uids:
        print(uid, file=sys.stderr)


# function lists the input file paths sorted by series
def list_file_paths_by_series(path_to_directory):
    # create variables
    series_dict = defaultdict(list)
    directory_path = Path(path_to_directory)

    # perform dfs and return iterator of paths
    dicom_files = directory_path.rglob("*.dcm")

    # populate series_dict with file paths
    for file in dicom_files:
        try:
            dicom_file = dcmread(file, force = True)
            series_description = dicom_file.SeriesDescription
            series_dict[series_description].append(str(file))

        except AttributeError:
            print(f"Problem reading SeriesDescription from {file.name}")

    # output result into stderr
    for series_description, files in sorted(series_dict.items()):
        print(f"\nSeries: {series_description}", file=sys.stderr)
        for file in sorted(files):
            print(f"  {file}", file=sys.stderr)


# main function
def main():
    # initialise variables
    command_to_perform = ""
    path_to_directory = ""

    # check user input is correct
    if len(sys.argv) != 3:
        print("Please provide two arguments: 1) action to perform and 2) full path to a DICOM folder", file=sys.stderr)
        sys.exit(1)

    # assign user input to variables
    command_to_perform = sys.argv[1]
    path_to_directory = sys.argv[2]

    # perform a command based on user's request
    if command_to_perform == "extract_study_identifiers_from_directory":
        extract_study_identifiers_from_directory(path_to_directory)

    elif command_to_perform == "list_file_paths_by_series":
        list_file_paths_by_series(path_to_directory)
    
    else:
        print("Invalid command", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

# dicom-cli-analyzer
Python CLI tool for analysing DICOM files

The tool takes as input two parameters: 1) action to perform and 2) full path to a folder containing DICOM files both provided as strings.
In this implementation there are two functions to choose from: 1) extract_study_identifiers_from_directory and 2) list_file_paths_by_series

Provide one of these command names when running the code. The output of the tool will be written into stderr.

Note: Error handling was implemented to deal with corrupt or empty DICOM files. Names of these files will be written into standard output.
It is thus advised to direct your normal output to a separate file like output.txt.

An example run of the code could look like:
python3 dicom_cli_analyzer.py extract_study_identifiers_from_directory /Users/admin/Desktop/.../ProstateX-0001_0002 > output.txt

Enjoy!

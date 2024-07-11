from pathlib import Path
from autogradercpp.exceptions import TestBenchValidationException

def search_cpp_files(root_folder:str, filename_to_match:str) -> dict:
    """The given function expects that there is a directory of following order -

        root_folder/\n
            |-- roll1/\n
            | |---- file1.cpp\n
            | |---- file2.cpp\n
            | |---- some_filename_to_match.cpp\n
            |--roll2/\n
            | |---- file1.cpp\n
            ...
    
    roll is the unique identification string of the submitter 
    
    The function looks for every folder/roll in the root folder and checks for the first file with filename containing the keyword filename_to_match. If found, the path to it is returned along with the roll of the person. If for a given roll no such file found, the function returns absent corresponding to the path for the roll.
    Args:
        root_folder (str): path to the directory containing folders and files under test
        filename_to_match (str): the unique keyword/pattern in file names

    Returns:
        dict: key: name of folder/roll: path to file
    """
    root = Path(root_folder)
    cpp_file_path_dict={}
    for roll_number_path in root.iterdir():
        if roll_number_path.is_dir():
            found = False
            for file_path in roll_number_path.rglob('*.cpp'):
                if filename_to_match in file_path.name:
                    cpp_file_path_dict[roll_number_path.name]=file_path
                    found = True
                    break
            if not found:
                cpp_file_path_dict[roll_number_path.name]="absent"
    return cpp_file_path_dict

def read_test_cases(file_path:str) -> list[str]:
    file = open(file_path, "r") 
    lines = file.readlines()
    test_cases = []
    file_category = None
    for line in lines:
        if line.startswith("#testcase_input"):
            if file_category == "output":
                raise TestBenchValidationException("Input values found in output test case file, please check the test files")
            test_cases.append("")
            if file_category == None:
                file_category = "input"
            
        elif line.startswith("#testcase_output"):
            if file_category == "input":
                raise TestBenchValidationException("Output values found in input test case file, please check the test files")
            test_cases.append("")
            if file_category == None:
                file_category = "output"
        else:
            test_cases[-1] += line
    file.close()
    return test_cases

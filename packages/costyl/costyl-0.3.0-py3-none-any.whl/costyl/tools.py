
import glob
import os

def get_authors_files_paths(path: str):
    
    if os.name == "posix":
        files_paths = glob.glob(path.replace("'", "") + "/*/*.cpp")
        return files_paths

    elif os.name == "nt":
        files_paths = glob.glob(path.replace("'", "") + "\*\*.cpp")
        return files_paths

def get_target_files_paths(path: str):
    
    if os.name == "posix":
        files_paths = glob.glob(path.replace("'", "") + "/*.cpp")
        return files_paths

    elif os.name == "nt":
        files_paths = glob.glob(path.replace("'", "") + "\*.cpp")
        return files_paths


def printTestsPredicts(y_test, predictedAuthor):
    print('\n\n' + "\u0332".join("Tests:") + '\n')
    print("Author        || Predicted    : Check status")
    print("--------------------------------------------")
    erros = 0
    for a, b in zip(y_test, predictedAuthor):

        if a == b:
            print(f'{a}{" " * (13 - len(a))} == {b}{" " * (13 - len(b))}: V')
        if a != b:
            print(f'{a}{" " * (13 - len(a))} != {b}{" " * (13 - len(b))}: F')
            erros += 1

    print(f'\nTotal: {len(y_test)}')
    print(f'Erros: {erros}')

def determine_algorithm():
    #TODO implement this function
    pass
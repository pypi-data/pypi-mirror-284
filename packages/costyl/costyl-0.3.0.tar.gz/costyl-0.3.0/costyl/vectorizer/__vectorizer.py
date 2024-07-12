
import io
from sklearn.feature_extraction.text import CountVectorizer


def vectorize_file_whole(filePath: str, silenceWarnings: bool) -> str:
    
    try:
        with open(filePath, "rb") as f:
            file = f.read().decode("utf-8")
            
            return file
        
    except UnicodeDecodeError:
        if not silenceWarnings:
            print()
            print("WARNING: Skipping file")
            print(f'Failed reading file "{filePath}": file encoding different from utf-8')
            print("It's recommended you encode the file in utf-8 and run the script again or accuracy may be affected!")
            print("To silence these warnings set the silenceWarnings param on generate_model() to True")
            print()
        else:
            pass
    

def vectorize_file_in_lines(filePath: str, silenceWarnings: bool) -> list[str]:

    try:
    
        with open(filePath, "rb") as f:
            file = f.readlines()
            file = [line.decode("utf-8") for line in file]

            return file
    
    except UnicodeDecodeError:
        if not silenceWarnings:
            print()
            print("WARNING: Skipping file")
            print(f'Failed reading file "{filePath}": file encoding different from utf-8')
            print("It's recommended you encode the file in utf-8 and run the script again or accuracy may be affected!")
            print("To silence these warnings set the silenceWarnings param on generate_model() to True")
            print()
        else:
            pass
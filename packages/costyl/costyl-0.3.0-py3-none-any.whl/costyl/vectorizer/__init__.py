
from . import __vectorizer as vec
import os

def vectorize_train_files(source_files_paths: list[str], silenceWarnings: bool):
    
    vectorized_files_whole = []
    vectorized_files_lines = []
    files_labels = []
    
    for i, path in enumerate(source_files_paths):
        
        vecFileWhole = vec.vectorize_file_whole(path, silenceWarnings)
        vecFileLines = vec.vectorize_file_in_lines(path, silenceWarnings)
        
        if vecFileWhole == None:
            continue
        
        vectorized_files_whole.append(vecFileWhole)
        vectorized_files_lines.append(vecFileLines)
        
        if os.name == "posix":
            files_labels.append(path.split("/")[-2])

        elif os.name == "nt":
            files_labels.append(path.split("\\")[-2])
        
            
    return vectorized_files_whole, vectorized_files_lines, files_labels



def vectorize_target_files(source_files_paths: list[str], silenceWarnings: bool):
    
    vectorized_files_whole = []
    vectorized_files_lines = []
    files_labels = []
    
    for i, path in enumerate(source_files_paths):
        
        vecFileWhole = vec.vectorize_file_whole(path, silenceWarnings)
        vecFileLines = vec.vectorize_file_in_lines(path, silenceWarnings)
        
        if vecFileWhole == None:
            continue
        
        vectorized_files_whole.append(vecFileWhole)
        vectorized_files_lines.append(vecFileLines)
        
        if os.name == "posix":
            files_labels.append(path.split("/")[-1].removesuffix(".cpp"))

        elif os.name == "nt":
            files_labels.append(path.split("\\")[-1].removesuffix(".cpp"))
        
            
    return vectorized_files_whole, vectorized_files_lines, files_labels
    
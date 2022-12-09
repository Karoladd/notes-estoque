import shutil
import os

def downloadN():
    source_dir = 'C:/Users/Karol/Desktop/excel-python/note/'
    target_dir = 'C:/Users/Karol/Downloads/estoque/'
        
    file_names = os.listdir(source_dir)
        
    for file_name in file_names:
        top = shutil.move(os.path.join(source_dir, file_name), target_dir)

    return top
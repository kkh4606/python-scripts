import os
import shutil


def fileOrganizer():
    file_types = {
    
        "images" : ".png",
        "programs" : ".exe",
        "documents" : ".pdf",
        "archives" : ".rar"
        }



    root = 'E:\\'


    for file in os.listdir(root):
        if not os.path.isfile(os.path.join(root, file)):
            continue
        
        else:
            name, ext = os.path.splitext(os.path.join(root, file))
            
            for file_type, extension in file_types.items():
                
                if ext == extension:
                    os.makedirs(os.path.join(root, file_type), exist_ok=True )
                    
                    try:
                        shutil.move(os.path.join(root, file), os.path.join(root, file_type))
                        
                    except Exception as e:
                        print(f'Error {e} occoured')
                    else:
                        print(f'Successfully moved {name}.{ext} to {root}\\{file_type}')
                    
                    

fileOrganizer()
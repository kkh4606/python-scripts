from pathlib import Path
import re

def check_file_names(fileName : str)->bool:
    if re.fullmatch(r'FIFA 12.part\d+\.rar$', fileName, flags=re.IGNORECASE):
        return True
    return False 

def rename_invalid_files(fileName:str)->str | None:
    if not check_file_names(fileName):
        return re.sub(r'(\s\(\d\))', '', fileName)
        


base_dir = Path(r'E:/')

rar_files = list(base_dir.glob("*.rar"))


def main()->None:
    for file in rar_files:
    
        try:
             if not check_file_names(file.name):
                valid_name = rename_invalid_files(file.name)
                file.rename(base_dir / valid_name)
                print(f'{file.name} successfully renamed to {valid_name}')
            
        except  Exception as e:
            print('Error {e} occoured')



if __name__ == '__main__':
    main()
    








from pathlib import Path
import re

def check_file_names(file_name : str)->bool:
    if re.fullmatch(r'FIFA 12.part\d+\.rar$', file_name, flags=re.IGNORECASE):
        return True
    return False 

def rename_invalid_files(file_name:str)-> str | None:
    if not check_file_names(file_name):
        return re.sub(r'(\s\(\d\))', '', file_name)
    return None


base_dir = Path(r'E:/')

rar_files = list(base_dir.glob("*.rar"))


def main()->None:

    found_invalid = False
    for file in rar_files:
    
        try:
             if not check_file_names(file.name):
                found_invalid = True
                valid_name = rename_invalid_files(file.name)
                file.rename(base_dir / valid_name)
                print(f'{file.name} successfully renamed to {valid_name}')
            
        except  Exception as e:
            print('Error {e} occurred')
    if rar_files and not found_invalid:
        print('All files have valid file names')



if __name__ == '__main__':
    main()
    








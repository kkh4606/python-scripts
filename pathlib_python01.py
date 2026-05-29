from pathlib import Path



current_dir = Path().cwd()

# print(text_file.root)
# 
# print(text_file.suffix)
# 
# print(text_file.stem)

# print(text_file.parts)
# 
# print(list(text_file.parents))

for file in current_dir.iterdir():
    
    if file.is_dir():
        print(file)
    if file.is_file():
        print(file)
        

 


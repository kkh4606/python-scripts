from pathlib import Path



base_dir = Path().home()/"Desktop"

txt_dir = Path().home()/"Desktop"/"Text Files"
txt_dir.mkdir(parents=True , exist_ok=True)

faces_dir = Path().home()/"Desktop"/"Faces"
faces_dir.mkdir(parents=True , exist_ok=True)

try:
    
    for file in base_dir.iterdir():
        if file.is_file() and file.suffix == ".txt":
            file.rename(txt_dir/file.name)
        
        if file.is_dir() and file.name.isdigit():
            file.rename(faces_dir/file.name)            
                
except  Exception as e:
    print(f"Error : {e} occoured")
else:
    print('Successfully moved')


        

            
            
            
   
            
    
        
        
        
        
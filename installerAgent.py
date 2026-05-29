from pathlib import Path 
import psutil




def get_drives(): 
    drives = [Path(drive.device) for drive in psutil.disk_partitions() if drive.fstype] 
    return drives 

def find_rar_file(): 
    drives = get_drives()
    target_files = []
    for drive in drives: 
        print(f'Scanning drive : {drive}...') 
        for file in drive.rglob("*.rar"):
            if "Windows" in file.parts or "$Recycle.Bin" in file.parts or "Program Files (x86)" in file.parts or "FIFA 12.part" not in file.name:
                continue
            target_files.append(file.name)
            print(file)
            
            if len(target_files) == 3:
                break
            

find_rar_file()

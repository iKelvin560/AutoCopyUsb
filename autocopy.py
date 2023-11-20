import os
import shutil

def findExternalDrives(hardDrives):
    drivePaths = os.listdrives()
    for i in hardDrives:
        drivePaths.remove(i)
    return(drivePaths)


def extract_files_from_usb(drivePaths, destination_folder):
    if drivePaths == []:
        print("USB drive not found.")
        return
    else:
        for usb_drive_path in drivePaths:
            # List all files in the USB drive
            files_in_usb = os.listdir(usb_drive_path)
            print("copying...")
            #shutil.copytree(usb_drive_path, destination_folder, dirs_exist_ok=True, copy_function=copy2)
            


if __name__ == "__main__":
    # Specify the destination folder for extracted files (change accordingly)
    destination_folder = "C:\\Users\\User\\Desktop\\test\\extractfiles"
    hardDrives = ["C:\\"]
    
    while True:
        drivePaths = findExternalDrives(hardDrives)

        # Call the function to extract files
        extract_files_from_usb(drivePaths, destination_folder)

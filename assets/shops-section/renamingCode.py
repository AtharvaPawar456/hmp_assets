import os

def renameAllFiles(folderPath):
    """
    Renames all files inside a folder sequentially.

    Input:
        folderPath (str): Target directory path

    Working:
        - Iterates through all files
        - Renames each file to file_<number> with original extension
    """
    try:
        files = sorted(os.listdir(folderPath))
        fileCounter = 1
        # fileCounter = 112

        for fileName in files:
            oldPath = os.path.join(folderPath, fileName)

            if not os.path.isfile(oldPath):
                continue

            _, extension = os.path.splitext(fileName)
            newFileName = f"file_{fileCounter}{extension}"
            # newFileName = f"temp_{fileCounter}{extension}"
            newPath = os.path.join(folderPath, newFileName)

            os.rename(oldPath, newPath)
            fileCounter += 1

        print(f"Renamed {fileCounter - 1} files in '{folderPath}' successfully.")

    except Exception as error:
        print(f"Error: {error}")


folderList = [
    


'shop-1-mauli'
    
    
]

basefolder = "software"
for folder in folderList:
    # folder = f"{basefolder}/{folder}"
    print(folder)
    renameAllFiles(folder)




# basePath = "https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/project_data/"
# folderPath = "hardware/_43_Smart_Waste_Segregation_Bin"
# files = os.listdir(folderPath)

# for fileName in files:
#     # print(f"'{tempPath}{fileName}',")
#     print(f"{basePath}{folderPath}/{fileName};")



"""
https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/project_data/hardware/_10_SALTO_The_Jumping_Robot/file_1.png

https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/project_data/hardware/_11_MIT_Transform_Smart_Desk/file_2.jpg




\
    
    
file_1.mp4
file_2.png
file_3.mp4
file_4.png
file_5.png
file_6.png
file_7.jpeg
file_8.mp4


"""
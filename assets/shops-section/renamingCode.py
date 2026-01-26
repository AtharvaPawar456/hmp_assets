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
    


# 'shop-1-mauli'
'shop-1-mauli/videos'
    
    
]

# basefolder = "software"
# for folder in folderList:
#     # folder = f"{basefolder}/{folder}"
#     print(folder)
#     renameAllFiles(folder)




basePath = "https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/videos"
folderPath = "shop-1-mauli/videos"
files = os.listdir(folderPath)

for fileName in files:
    print(f"{basePath}{fileName};")
    # print(f"{basePath}{folderPath}/{fileName};")



"""



https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/file_5.jpeg;
https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/file_11.jpeg;
https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/file_4.jpeg;
https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/file_1.jpeg;
https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/file_10.png;
https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/file_12.png;
https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/file_3.jpeg;
https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/file_6.png;
https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/file_7.png;
https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/file_8.jpeg;
https://raw.githubusercontent.com/AtharvaPawar456/hmp_assets/refs/heads/main/assets/shops-section/shop-1-mauli/file_9.jpeg;



"""
import os
import re

def smartNormalizeFolderNames(baseFolderPath):
    """
    Smartly normalizes all folder names inside the given base folder.
    - Converts CamelCase / PascalCase to underscore_separated
    - Replaces hyphens and spaces with underscores
    - Cleans up multiple underscores
    """
    try:
        if not os.path.isdir(baseFolderPath):
            raise FileNotFoundError(f"Folder not found: {baseFolderPath}")

        for folderName in os.listdir(baseFolderPath):
            oldPath = os.path.join(baseFolderPath, folderName)
            if os.path.isdir(oldPath):
                # Step 1: Replace hyphens and spaces with underscores
                newFolderName = folderName.replace("-", "_").replace(" ", "_")

                # Step 2: Insert underscores before uppercase letters following lowercase letters (CamelCase -> underscore)
                newFolderName = re.sub(r'(?<=[a-z])([A-Z])', r'_\1', newFolderName)
                
                # Step 3: Remove multiple underscores
                newFolderName = re.sub(r'__+', '_', newFolderName)
                
                # Step 4: Remove leading/trailing underscores
                newFolderName = newFolderName.strip("_")

                newPath = os.path.join(baseFolderPath, newFolderName)
                if oldPath != newPath:
                    os.rename(oldPath, newPath)
                    print(f'Renamed: "{folderName}" → "{newFolderName}"')

    except Exception as error:
        print(f"Error while normalizing folder names: {error}")


# Example usage
# smartNormalizeFolderNames("hardware")
# smartNormalizeFolderNames("software")

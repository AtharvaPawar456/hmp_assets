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
            newPath = os.path.join(folderPath, newFileName)

            os.rename(oldPath, newPath)
            fileCounter += 1

        print(f"Renamed {fileCounter - 1} files in '{folderPath}' successfully.")

    except Exception as error:
        print(f"Error: {error}")


folderList = [
    
    
# hardware

# "Anti_theft_Flooring_Sys",
# "Automatic_Rain_Sensing_Cloth_Shade_System",
# "Autonomous_Mini_Carfor_Ultrasonic_Collision_Avoidance",
# "EBike_Speed_Controller_System",
# "EMO_Robot",
# "general_parts",
# "Guardian_Briefcase_An_Intelligent_Human_Following_Security_System",
# "Human_Following_Robot",
# "Ibin_Iot_Based_Smart_Waste_Sorting_And_Monitoring_System",
# "Iot_Enabled_Smart_Object_Sorting_Machine_With_Real_Time_Monitoring",
# "Iot_Interactive_Aquarium",
# "MIT_Transform_Smart_Desk",
# "Organ_Stiching_Machine",
# "Radar_System",
# "Robotic_ARM_Material_Segregator",
# "SALTO_The_Jumping_Robot",
# "Smart_Attendence_System",
# "Smart_Auto_Door_System_Using_Motion_Detection",
# "Smart_Biometric_Door_Access_System_With_Iot_Integration",
# "Smart_Firefighting_Robot_With_Dual_Mode_Operation",
# "Smart_Home_Controlling_System",
# "Smart_Iot_Based_Automated_Pet_Feeder_With_Real_Time_Monitoring",
# "Smart_Iot_Based_Door_Access_And_Monitoring_System",
# "Smart_Iot_Enabled_Bluetooth_Car_With_Remote_Monitoring",
# "Smart_Irrigation_System",
# "Smart_Locker_System",
# "Smart_Parking_System",
# "Smart_Pill_Reminder",
# "Smart_Vending_Machine",
# "Smart_Waste_Segregation_Bin",
# "Transmission_Line_Fault_Detection",
# "Weather_Station",
   



# software
# "agromark",
# "aiquize",
# "AIResume_Parser",
# "Ai_Based_Content_Planner",
# "AI_Based_Fake_News_Detection_System",
# "AI_Driven_Cybersecurity_Threat_Hunting_Tool",
# "AI_Powered_Recommendation_System",
# "Automated_Malware_Detection_System",
# "Behavioral_Biometrics_for_Continuous_Authentication",
# "Cybersecurity_Risk_Assessment_Tool_Using_Fuzzy_Logic",
# "Cyber_Deception_System_Using_Honeytokens",
# "Facial_Recognition_Based_Authentication_System",
# "Image_Search",
# "Intrusion_Detection_System",
# "Keyword_Research_Using_Genai",
# "Network_Traffic_Analysis_and_Anomaly_Detection",
# "Password_Manager_with_Two_Factor_Authentication",
# "Phishing_Attack_Detection_Tool",
# "playtube",
# "QA_RAG",
# "Remote_Work_Security_Toolkit",
# "Secure_Email_Communication_Platform",
# "Secure_File_Storage_System_Using_Cryptography",

    
    
]

basefolder = "software"
for folder in folderList:
    folder = f"{basefolder}/{folder}"
    print(folder)
    renameAllFiles(folder)




# files = os.listdir("dxn-soap/shorts")
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-soap/shorts/"

# for fileName in files:
#     print(f"'{tempPath}{fileName}',")



"""


"""
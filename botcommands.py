# Importing necessary modules
from info import *
import os

twrp_building_script = "build_twrp.sh"
pbrp_building_script = "build_pbrp.sh"
ofox_building_script = "build_ofox.sh"


# Setting up variables for group ID and group URL
request_id = -4177520948
group_url = "https://t.me/+LcVNpdqBaMlmNjg0"

# Function to handle commands received by the bot
def command(m): 
    # Check if the received command is "/start"
    if m.text == "/start":
        # Reply with a message containing the group join link
        bot.reply_to(m, f"Hi, if you want to use me please join this group: {group_url}")
        bot.send_message(m.chat.id, f"This bot is created by: {bot_creator}")
    # Check if the received command starts with "/twrp"
    if m.text.split()[0] =="/twrp":
        # Check if the user is in the correct group to make requests
        if m.chat.id == request_id:
            # Call the request function to process the request
            request_twrp_build(m)
        else:
            # Reply with a message asking the user to join the correct group
            bot.reply_to(m, f"Please join this group and use me there: {group_url}")
    # Check if the received command starts with "/pbrp"
    if m.text.split()[0] =="/pbrp":
        # Check if the user is in the correct group to make requests
        if m.chat.id == request_id:
            # Call the request function to process the request
            request_pbrp_build(m)
        else:
            # Reply with a message asking the user to join the correct group
            bot.reply_to(m, f"Please join this group and use me there: {group_url}")

def request_twrp_build(m):
    try:
        # Extract the arguments from the message
        Manifest_URL = "https://github.com/minimal-manifest-twrp/platform_manifest_twrp_aosp"
        Manifest_Branch = m.text.split()[1]
        Device_Tree_URL = m.text.split()[2]
        Device_Tree_Branch = m.text.split()[3]
        Device_Path = m.text.split()[4]
        Device_Name = m.text.split()[5]
        Makefile_Name = f"twrp_{Device_Name}"
        Build_Target = m.text.split()[6]
        # Execute one of the dumping scripts with the URL as an argument
        result = os.system(f'bash {twrp_building_script} {Manifest_URL} {Manifest_Branch} {Device_Tree_URL} {Device_Tree_Branch} {Device_Path} {Device_Name} {Makefile_Name} {Build_Target}')
        # Check the result of the script execution
        if result == 0:
            # Reply with a success message if the script executed successfully
            bot.reply_to(m, "Successfully requested the build!")
            bot.reply_to(m, "Check progress here: https://github.com/IMYdev/TG-X-GH-actions_TWRP-Builder/actions")
        else:
            # Reply with an error message if something went wrong during script execution
            bot.reply_to(m, "Something went wrong")
    except:
        # Reply with a message indicating that a URL is needed for the request
        bot.reply_to(m, "You need to give me the required arguments in the correct order")
        bot.reply_to(m, "Usage is as follows: /twrp (Manifest_Branch) (Device_Tree_URL) (Device_Tree_Branch) (Device_Path) (Device_Name) (Build_Target)")
        bot.reply_to(m, "Example: /twrp twrp-12.1 https://github.com/TeamWin/android_device_asus_I003D android-12.1 device/asus/I003D I003D recovery")


def request_pbrp_build(m):
    try:
        # Extract the arguments from the message
        Manifest_URL = "https://github.com/PitchBlackRecoveryProject/manifest_pb"
        Manifest_Branch = m.text.split()[1]
        Device_Tree_URL = m.text.split()[2]
        Device_Tree_Branch = m.text.split()[3]
        Device_Path = m.text.split()[4]
        Device_Name = m.text.split()[5]
        Makefile_Name = f"pb_{Device_Name}"
        Build_Target = m.text.split()[6]
        # Execute one of the dumping scripts with the URL as an argument
        result = os.system(f'bash {pbrp_building_script} {Manifest_URL} {Manifest_Branch} {Device_Tree_URL} {Device_Tree_Branch} {Device_Path} {Device_Name} {Makefile_Name} {Build_Target}')
        # Check the result of the script execution
        if result == 0:
            # Reply with a success message if the script executed successfully
            bot.reply_to(m, "Successfully requested the build!")
            bot.reply_to(m, "Check progress here: https://github.com/IMYdev/TG-X-GH-actions_TWRP-Builder/actions")
        else:
            # Reply with an error message if something went wrong during script execution
            bot.reply_to(m, "Something went wrong")
    except:
        # Reply with a message indicating that a URL is needed for the request
        bot.reply_to(m, "You need to give me the required arguments in the correct order")
        bot.reply_to(m, "Usage is as follows: /twrp (Manifest_Branch) (Device_Tree_URL) (Device_Tree_Branch) (Device_Path) (Device_Name) (Build_Target)")
        bot.reply_to(m, "Example: /pbrp android-12.1 https://github.com/TeamWin/android_device_asus_I003D android-12.1 device/asus/I003D I003D recovery")

def request_ofox_build(m):
    try:
        # Extract the arguments from the message
        Sync_URL = "https://gitlab.com/OrangeFox/sync.git"
        Manifest_Branch = m.text.split()[1]
        Device_Tree_URL = m.text.split()[2]
        Device_Tree_Branch = m.text.split()[3]
        Device_Path = m.text.split()[4]
        Device_Name = m.text.split()[5]
        Makefile_Name = f"twrp_{Device_Name}"
        Build_Target = m.text.split()[6]
        # Execute one of the dumping scripts with the URL as an argument
        result = os.system(f'bash {ofox_building_script} {Sync_URL} {Manifest_Branch} {Device_Tree_URL} {Device_Tree_Branch} {Device_Path} {Device_Name} {Makefile_Name} {Build_Target}')
        # Check the result of the script execution
        if result == 0:
            # Reply with a success message if the script executed successfully
            bot.reply_to(m, "Successfully requested the build!")
            bot.reply_to(m, "Check progress here: https://github.com/IMYdev/TG-X-GH-actions_OFOX-Builder/actions")
        else:
            # Reply with an error message if something went wrong during script execution
            bot.reply_to(m, "Something went wrong")
    except:
        # Reply with a message indicating that a URL is needed for the request
        bot.reply_to(m, "You need to give me the required arguments in the correct order")
        bot.reply_to(m, "Usage is as follows: /twrp (Manifest_Branch) (Device_Tree_URL) (Device_Tree_Branch) (Device_Path) (Device_Name) (Build_Target)")
        bot.reply_to(m, "Example: /ofox 12.1 https://github.com/TeamWin/android_device_asus_I003D android-12.1 device/asus/I003D I003D recovery")

import subprocess
import time
x_coordinate = 100;
y_coordinate = 500;
message1 = "Hi!"
adb_open_telegram = "adb shell am start -n org.telegram.messenger/org.telegram.ui.LaunchActivity"
adb_open_first_chat = f"adb shell input tap {x_coordinate} {y_coordinate}"
adb_set_text1 = f"adb shell input text {message1}"
adb_send_message = "adb shell input tap 1000 1600"
adb_close_telegram = "adb shell am force-stop org.telegram.messenger"
adb_open_cam = "adb shell am start -a android.media.action.IMAGE_CAPTURE" 
adb_take_a_pic = "adb shell input keyevent KEYCODE_CAMERA"

subprocess.run(adb_open_telegram, shell=True)
time.sleep(1)
subprocess.run(adb_open_first_chat, shell=True)
time.sleep(1)
subprocess.run(adb_set_text1, shell=True)
time.sleep(0.5)
subprocess.run(adb_send_message, shell=True)
time.sleep(1)
subprocess.run(adb_close_telegram, shell=True)
time.sleep(0.5)
subprocess.run(adb_open_cam , shell=True)
time.sleep(1)
subprocess.run(adb_take_a_pic , shell=True)

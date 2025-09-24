import os
import keyboard
import time

os.system("title UEFI")
os.system("clear")

f1_pressed = False  # global flag

def on_f1():
    global f1_pressed
    f1_pressed = True

keyboard.on_press_key("f1", lambda e: on_f1())

def boot_options():
    print("Boot with UEFI firmware [Y]")
    print("Boot with BIOS firmware [N]")

    a = input(">> ")
    if a == "BIOS: Y":
        os.system("echo Booting with BIOS...")
        os.system("bios.exe")
    elif a.upper() == "E":
        os.system("build398.exe")
    else:
        print("Invalid option, defaulting to BIOS...")
        os.system("build398.exe")

def boot():
    global f1_pressed
    print("Console AndroidOS UEFI")
    print("Booting......")
    print("Press F1 to enter boot options")

    # 3-second POST check
    for _ in range(30):  # 30 * 0.1s = 3 sec
        if f1_pressed:
            boot_options()
            return
        time.sleep(0.1)

    # Default boot
    os.system("build398.exe")

boot()

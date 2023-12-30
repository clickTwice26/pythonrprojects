import os


if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.1. Created by Giyan")
    while True:
        x = input("Enter what you want me to pronounce: ")
        if x == "q":
            os.system(f"spd-say 'Bye bye my friend'")
            break
        command = f"spd-say '{x}'"
        os.system(command)
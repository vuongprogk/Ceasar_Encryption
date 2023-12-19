import os
import ceasar


def main():
    isRun = True
    while isRun:
        os.system("cls")
        message = input("Input your plaintext: ")
        message = message.upper()
        keyvalue = int(input("Input your key: "))
        option = input("You want \n1.Decrypt \n2.Encrypt \nOption: ")
        if option == "1":
            print(ceasar.decrypt(keyvalue, message))
        elif option == "2":
            print(ceasar.encrypt(keyvalue, message))
        else:
            print("No option your choose")
        choose = input("Do you want continue (y/n): ")
        if choose.lower() == 'y':
            pass
        else:
            isRun = False


if __name__ == '__main__':
    main()

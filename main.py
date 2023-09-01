#!/usr/bin/env python3
# encoding: utf-8
"""_summary_
Main
June 2023, tipio, SOC Analyst Intern
"""
import time
from utils import *
from parser_func import *
                                                               

class Menu:
    @staticmethod
    def banner():
        print("                                                                                                  ") 
        print(Color.BLUE + " ██████╗  █████╗ ██████╗ ███████╗███████╗██████╗  "      + Color.END)
        print(Color.BLUE + " ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗  "     + Color.END)
        print(Color.BLUE + " ██████╔╝███████║██████╔╝███████╗█████╗  ██████╔╝  "     + Color.END)
        print(Color.BLUE + " ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝  ██╔══██╗  "     + Color.END)
        print(Color.BLUE + " ██║     ██║  ██║██║  ██║███████║███████╗██║  ██║  "     + Color.END)
        print(Color.BLUE + " ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝  "     + Color.END)
        print("                                                                                                   ")
        print(Color.BLUE + "                                                                parser " + Color.END)
        Menu.clear(1)   

    @staticmethod
    def help():
        try:
            print("--------------------------------------------------------------------------------------------------------")
            print(Color.BLUE + "[+] Help: " + Color.END)
            print("--------------------------------------------------------------------------------------------------------")
            print("[+] Your work is stored in: " + os.getcwd())
            print("--------------------------------------------------------------------------------------------------------")
            print(
            "\n"
            "[+] coming\n"
            "[+] soon\n"
            )
            print("--------------------------------------------------------------------------------------------------------")
            print("[+] Return to Home?")
            print(Color.BLUE + "1 -> Back Home" + Color.END)
            print(Color.RED + "2 -> Exit" + Color.END)
            option = int(input("[+] What do you want to do? "))
            if option == 1:
                Menu.banner()
                print("--------------------------------------------------------------------------------------------------------")
                Menu.home()
            elif option == 2:
                os.system("exit")
                print(Color.ORANGE + "\nyour 'parser' program has worked. see you soon" + Color.END)
            else:
                print(Color.RED + "Bad value, type: 1 or 2" + Color.END)
                Menu.help()
        except Exception as err:
            print(Color.RED + "[!] error: " + str(err) + Color.END)
            sys.exit(1)

    @staticmethod
    def home():
        try:
            start_prog = time.time()
            print(Color.BLUE + "[+] Home: " + Color.END)
            Menu.clear(1)
            print(Color.BLUE + "1 -> Help" + Color.END)
            print(Color.BLUE + "2 -> Functions" + Color.END)
            print(Color.RED + "3 -> Exit" + Color.END)
            choice = int(input("[+] Indicate your choice: " ))
            if choice == 1:
                Menu.help()
            elif choice == 2:
                Menu.functions()
            elif choice == 3:
                Menu.exit()
            else:
                return Menu.home()
        except KeyboardInterrupt:
            print(Color.ORANGE + "\nyour 'parser' program has worked. see you soon" + Color.END)
            print(Color.ORANGE + "[+] work carried out in: " + str(time.time() - start_prog) + " seconds" + Color.END)
        sys.exit(0)
    
    @staticmethod
    def functions():
        try:
            start_prog = time.time()
            print("--------------------------------------------------------------------------------------------------------")
            print(Color.BLUE + "[+] Functions: " + Color.END)
            Menu.clear(1)
            print(Color.BLUE + "1 -> Download and store the AWS CSV file" + Color.END)
            print(Color.BLUE + "2 -> Extract critical vulnerabilities from the 'AWS_<date>.csv' file and return a list of IP addresses" + Color.END)
            print(Color.BLUE + "3 -> Extract AWS information and return a json file" + Color.END)
            print(Color.BLUE + "4 -> Parse the json file, extract useful information and return a text file to send" + Color.END)
            print(Color.BLUE + "5 -> Download and store other CSV files" + Color.END)
            print(Color.BLUE + "6 -> Parse and rename CSV files to 'outfile_'" + Color.END)
            print(Color.BLUE + "7 -> Send report to kibana" + Color.END)
            print(Color.ORANGE + "8 -> Back Home" + Color.END)
            choice = int(input("Indicate your choice: " ))
            if choice == 1:
                Menu.clear(1)
                print("fill in your arguments: ")
                pname = input("your Windows user name known to company and your computer: ")
                Store.mvCsvFile(pname)
                Menu.clear(1)
                return Menu.functions() 
            elif choice == 2:
                Menu.clear(1)
                print("fill in your arguments: ")
                csvToParse = input("CSV file to parse [AWS_<date>.csv]: ")
                Vulnerability.extractVul(csvToParse)
                Menu.clear(1)
                return Menu.functions()
            elif choice == 3:
                Menu.clear(1)
                print("[+] Fill in your arguments: ")
                csvToParse = input("CSV file to parse [AWS_<date>.csv]: ")
                JsonFile.returnJsonFile(csvToParse)
                Menu.clear(1)
                return Menu.functions()
            elif choice == 4:
                Menu.clear(1)
                print("fill in your arguments: ")
                jsonFileToParse = input("Your file name [return_<date>_aws.json]: ")
                JsonParser.extractAwsInfo(jsonFileToParse)
                Menu.clear(1)
                return Menu.functions()
            elif choice == 5:
                Menu.clear(1)
                print("fill in your arguments: ")
                pname = input("your Windows user name known to company and your computer: ")
                Store.mvCsvFiles(pname)
                return Menu.functions()
            elif choice == 6:
                Menu.clear(1)
                print("fill in your arguments: ")
                print(Color.GREEN + "[+] your csv files name are: " + str(glob.glob("*.csv")) + Color.END)
                csvFileToParse = input("CSV file to parse [<area>_<ID>.csv]: ")
                CsvParser.csvParsing(csvFileToParse)
                Menu.clear(1)
                return Menu.functions()
            elif choice == 7:
                Menu.clear(1)
                Send.sendKibanaReport()
                print(Color.ORANGE + "[!] Coming soon" + Color.END) # soon
                Menu.clear(1)
                return Menu.functions()
            elif choice == 8:
                Menu.clear(1)
                Menu.banner()
                print("--------------------------------------------------------------------------------------------------------")
                return Menu.home()
            else:
                return Menu.home()
        except KeyboardInterrupt:
            print(Color.ORANGE + "\nyour 'parser' program has worked. see you soon" + Color.END)
            print(Color.ORANGE + "[+] work carried out in: " + str(time.time() - start_prog) + " seconds" + Color.END)
        sys.exit(0)

    @staticmethod
    def clear(num):
        print("\n"*num)
    
    @staticmethod
    def exit():
        print("--------------------------------------------------------------------------------------------------------")
        print(Color.RED + "[!] Exit: " + Color.END) 
        choice = input(("do you want to leave the programm [Y/n] ? ") or default)
        default = "Y"
        choiceYes = ["Y","y", "yes", "YES"]
        choiceNo = ["N", "n", "no", "NO"]
        if default:
            print(Color.ORANGE + "\nyour 'parser' program has worked. see you soon" + Color.END)
            os.system("exit")
        for choice in choice:
            if choice in choiceNo:
                print(Color.BLUE + "glad you are staying here!" + Color.END)
                Menu.banner()
                return Menu.home()
            if choice in choiceYes:
                os.system("exit")
                print(Color.ORANGE + "\nyour 'parser' program has worked. see you soon" + Color.END) 
            else:
                print(Color.RED + "bal value, type: 'y' or 'n' (default: y)" + Color.END)
                Menu.exit()


if __name__ == '__main__':
    """_summary_
    program execution
    """
    try:
        Menu.banner()
        print(Color.BLUE + "[+] 'parser' will create a directory to store your work." + Color.END)
        print("--------------------------------------------------------------------------------------------------------")
        print(Color.ORANGE + "[!] You must be root or have the rights to create a directory in the choice of your absolute path!" + Color.END)
        path = input("[+] Please enter your absolute path: ")
        Directory.createDirectory(path)
        print("--------------------------------------------------------------------------------------------------------")
        os.chdir(path)
        print("[+] all your work will be stored in: " + os.getcwd())
        print("--------------------------------------------------------------------------------------------------------")
        Menu.home()
    except KeyboardInterrupt:
            print(Color.ORANGE + "\nyour 'parser' program has worked. see you soon" + Color.END)
            sys.exit(0)

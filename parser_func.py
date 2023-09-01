#!/usr/bin/env python3
# encoding: utf-8
"""_summary_
Work functions
June 2023, tipio, SOC Analyst Intern
"""
from datetime import datetime
import csv
import json
import sys
import os
import sys
import glob
import zipfile
from utils import *


class Store:
    @staticmethod
    def mvCsvFile(pname):
        """_summary_
        Download and store the AWS CSV file
        Args:
            pname (username): your Windows user name known to company and your computer
        """

        # res = ""
        # now = datetime.now()
        # currenttime = now.strftime("%Y-%m-%dT%H:%M:%S")

        # # Contains csv files to parse
        # tab_files = []


        # # Parsing arguments
        # if len(sys.argv) < 2:
        #     print("Usage : ./format.py [-a|-f file1.csv file2.csv]")
        #     print("**********")
        #     print("-a : select every csv files in the current dir")
        #     print("-f : choose the files you want to clean")
        #     exit(-1)
        # elif sys.argv[1] == "-a":
        #     for filename in os.listdir("./"):
        #         if filename.endswith(".csv"):
        #             tab_files.append(filename)
        # elif sys.argv[1] == "-f":
        #     i = 2
        #     while i < len(sys.argv):
        #         if sys.argv[i].endswith(".csv"):
        #             tab_files.append(sys.argv[i])
        #         i+=1
        # else:
        #     print("Usage : ./format.py [-a|-f file1.csv file2.csv]")
        #     print("**********")
        #     print("-a : select every csv files in the current dir")
        #     print("-f : choose the files you want to clean")
        #     print("-h : prints this help dialog")
        #     exit(-1)

        try:
            workDir = os.getcwd()
            awsFileCsv = os.system("mv /mnt/c/Users/"+pname+"/Downloads/AWS* "+ workDir + "/AWS_"+str(datetime.now().strftime("%y%m%d"))+".csv")
            awsFileCsv
            os.system("chmod 777 *.csv")
            print(Color.GREEN + "[+] all your work will be stored in: " + workDir + Color.END)
            print(Color.GREEN + "[+] your csv file name is: " + str(glob.glob("AWS*")) + Color.END)
        except Exception as err:
            print(Color.RED + "[!] error: " + str(err) + Color.END)
            sys.exit(1)

    @staticmethod
    def mvCsvFiles(pname):
        """_summary_
        Download and store other CSV files
        Args:
            pname (username): your Windows user name known to company and your computer
        """
        try:
            workDir = os.getcwd()
            csv = os.system("mv /mnt/c/Users/"+pname+"/Downloads/*.csv " + workDir)
            csv
            os.system("chmod 777 *.csv")
            print(Color.GREEN + "[+] all your work will be stored in: " + workDir + Color.END)
            print(Color.GREEN + "[+] your csv files name are: " + str(glob.glob("*.csv")) + Color.END)
        except Exception as err:
            print(Color.RED + "[!] error: " + str(err) + Color.END)
            sys.exit(1)


class Vulnerability:
    @staticmethod
    def extractVul(csvToParse):
        """_summary_
        Extract critical vulnerabilities from the 'AWS_<date>.csv' file and return a list of IP addresses
        Args:
            csvToParse (csv file): the AWS csv file downloaded from Nessus and stored in your working path
        Returns:
            list: IP addresses used to match aws hostnames
        """
        try:
            ipList = []
            with open(csvToParse, 'r') as fileText:
                file = csv.DictReader(fileText)
                for row in file:
                    if 'Critical' in row['Risk']:
                        ipList.append(row['Host'])
                print(Color.GREEN + "critical vulnerability found in these IP addresses: " + str(ipList) + Color.END)
                characters = "[']"
                ipList = ','.join(x for x in ipList if x not in characters)
                return ipList
        except Exception as err:
            print(Color.RED + "[!] error: " + str(err) + Color.END)
            sys.exit(1)


class JsonFile:
    @staticmethod
    def returnJsonFile(csvToParse):
        """_summary_
        Extract AWS information and return a json file
        Use the "sudo password" set for the debian wsl user
        Args:
            csvToParse (csv file): the AWS csv file downloaded from Nessus and stored in your working path
        """
        try:
            os.system("sudo aws ec2 describe-network-interfaces --filters Name=addresses.private-ip-address,Values=" + 
                  Vulnerability.extractVul(csvToParse) + " --no-verify-ssl > return_aws.json")  # add date to retuned file name
            workDir = os.getcwd()
            print(Color.GREEN + "[+] all your work will be stored in: " + workDir + Color.END)
            print(Color.GREEN + "[+] your json file name is : " + str(glob.glob("*.json")) + Color.END)
        except Exception as err:
            print(Color.RED + "[!] error: " + str(err) + Color.END)
            sys.exit(1)


class JsonParser:
    @staticmethod
    def extractAwsInfo(jsonFileToParse):
        """_summary_
        Parse the json file, extract useful information and return a text file to send
        Args:
            jsonFile (json file): json file returned in "option 3"
        """
        try:
            with open("ip_matching_"+str(datetime.now().strftime("%y%m%d"))+".txt", "a") as txtFile:
                count = 0
                file = open(jsonFileToParse, 'r')
                data = json.load(file)
                for info in data["NetworkInterfaces"]:
                    txtFile.write(
                        ("IP Address: " + info["PrivateIpAddress"]) +
                        ("\nMAC Address: " + info["MacAddress"]) +
                        ("\nDescription: " + info["Description"]) +
                        ("\nPrivate DNS Name: " + info["PrivateDnsName"]) +
                        ("\n---------------------------------------------------------------\n")
                    )
                    count = count + 1
                txtFile.write(
                    ("[+] number of IP found in the file: " + str(count)) +
                    ("\n---------------------------------------------------------------\n")
                )
                print(Color.GREEN + "[+] number of IP found in the file: " + str(count) + Color.END)
            txtZipList = []
            txtFileName = "ip_matching_"+str(datetime.now().strftime("%y%m%d"))+".txt"
            txtZipList.append(txtFileName)
            with zipfile.ZipFile("ip_"+str(datetime.now().strftime("%y%m%d"))+".zip", mode="w") as archive:
                for file in txtZipList:
                    archive.write(file)
            workDir = os.getcwd()
            print(Color.GREEN + "[+] all your work will be stored in: " + workDir + Color.END)
            print(Color.GREEN + "[+] your files name are : " + str(glob.glob("*.txt")) + " and " + str(glob.glob("*.zip")) + Color.END)
        except Exception as err:
            print(Color.RED + "[!] error: " + str(err) + Color.END)
            sys.exit(1)


class CsvParser:
    @staticmethod
    def csvParsing(csvFileToParse):
        """_summary_
        This function was written by another intern in early 2023 and updated here to work with this program
        Parse and rename CSV files to 'outfile_'
        Args:
            csvFileToParse (csv files)
        """
        try:
            res = ""
            now = datetime.now()
            currenttime = now.strftime("%Y-%m-%dT%H:%M:%S")
            tab_files = []
            tab_files.append(csvFileToParse)

            for file in tab_files:
                with open(file, encoding="latin-1") as f:
                    r = csv.reader(f, delimiter=',', quotechar='"')

                    # Pop headers to regenerate them with Site column
                    headers = next(r)
                    headers_cells = [c.replace(',', ';').replace('\r', '').replace('\n', ' ').replace('"', "'") for c in headers]
                    res += ", ".join(headers_cells) + ", site, time\n"

                    # Get the site value from the filename
                    site = file.split('_')[0]
                    if site.startswith("./"):
                        site = site.split("./")[1]

                    # Regenerate the csv
                    for row in r:
                        cells = [c.replace(',', ';').replace('\r', '').replace('\n', ' ').replace('"', "'") for c in row]
                        res += f'{", ".join(cells)}, {site}, {currenttime}\n'

                # Generate the new filename with current date
                outfile = f'outfile_{file.replace(".csv", "").split("/")[-1]}_{datetime.now().strftime("%y%m%d")}.csv'
                # Write to disk
                with open(outfile, 'w') as f:
                    f.write(res)
            workDir = os.getcwd()
            print(Color.GREEN + "[+] all your work will be stored in: " + workDir + Color.END)
            print(Color.GREEN + "[+] your csv outfiles name are : " + str(glob.glob("outfile_*")) + Color.END)
        except Exception as err:
            print(Color.RED + "[!] error: " + str(err) + Color.END)
            sys.exit(1)


class Send:
    @staticmethod
    def sendKibanaReport():
        """_summary_
        Send report to kibana
        """
        try:
            print(os.getcwd())
            os.system("pscp -P 22 "+ os.getcwd() + "/outfile_*.csv user@kibana_ip:/opt/nessus-scan")  # Set the correct kibana user/ip instance
        except Exception as err:
            print(Color.RED + "[!] error: " + str(err) + Color.END)
            sys.exit(1)

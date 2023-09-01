# Readme
# Script for inject Nessus reports in Kibana

> ## **"Clean" the reports for use with Kibana, inject the reports into the Kibana instance. For AWS, also extract the desired information from the report into a text file.**
> ### **V1, Started in June 23, tipio, SOC Analyst Intern**


## Setup
### Requirements:
- Nessus and Kibana instances
- Needs:
	- A kibana index for Nessus scans
	- A kibana dashboard to view data
- [WLS](https://lecrabeinfo.net/installer-wsl-windows-subsystem-for-linux-sur-windows-10.html) installed and operational 
    - Linux packages :
```bash
sudo apt install -y wget ca-certificates python3 pscp scp putty-tools curl unzip python3-pip banner
```
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) operational on WSL
```bash
sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" -k
sudo unzip awscliv2.zip
sudo ./aws/install
sudo aws --version
sudo aws help
```
- AWS config (after AWS CLI installation):
```bash
sudo apt install -y groff glibc less
pip install csv
# Configure AWS
sudo aws configure
	KEY : XXXX  # add your key
	SECRET : XXXX  # add your secret
	region : eu-south/north/east/west-X  # select a single region
# operation test
sudo aws ec2 describe-network-interfaces --no-verify-ssl
```
- DL AWS and other Nessus reports in Downloads folder


### Create an alias:
- edit your `.bashrc` or `.zshrc`
```bash
alias parser='path of main.py directory'
source .zshrc
```

### Run parser:
```bash
cd
parser
```


## In run:
> **Works under Windows with WSL installed and AWS tools operational on WSL.**

- MV the file in the correct directory
- Clean csv files
- Extract IP addresses of critical vulnerabilities (AWS report)
- Run the AWS cmd to extract the json file
- Parse json files
- Return the ip number with their info (AWS)


## Coming soon:
- Adjust for work with other tools

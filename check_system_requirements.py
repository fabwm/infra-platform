#!/usr/bin/python3
import subprocess
import os
import time

system_requirements = ["terraform", "aws", "vagrant", "ansible", "docker"]
repositories = ["yum", "apt"]

def validate_system_requirements():

    print("Checking system requirements...\n")
    for software in system_requirements:
        try:
            subprocess.check_output([software, '--version'])
        except:
            user_decision_to_install = input(f"Would you like to install {software}? (y/n): \n")
            print(f"\n\nIf for some reason the installation does not succeed, please check for the {software} requirements and if your repositorie is configured")
            time.sleep(3)
            if user_decision_to_install == 'y':
                install_system_requirements(software, repositories)
            else:
                print(f"Please install {software} to proceed to use the platform")
        else:
            print(f"{software} installed\n")

def install_system_requirements(software_not_instaled, repo):
    
    repo_name = ""
    
    for rp in repo:
        repo_name = os.popen(f"command -v {rp}").read()
        try:
            repo_name.split('/')[1]
        except:
            pass
        else:
            repo_name = rp
            break

    subprocess.check_call(["sudo", repo_name, "install", software_not_instaled])    
   
if __name__ == "__main__":

    validate_system_requirements()
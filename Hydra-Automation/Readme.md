# Hydra Automation Scripts

This repository contains two Python scripts for automating login attempts using the Hydra tool. These scripts are designed to work with SSH and HTTP POST form services.

## Files

- `sshLogin.py`: Automates SSH login attempts using Hydra.
- `httpLogin.py`: Automates HTTP POST form login attempts using Hydra.

## Requirements

- Python 3.x
- Hydra
- Kali Linux

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install Hydra from [GitHub](https://github.com/vanhauser-thc/thc-hydra).
3. Install kali Linux [Kali.org](https://www.kali.org/get-kali/#kali-platforms).

## Usage

### SSH Login Automation (`sshLogin.py`)

This script automates SSH login attempts using Hydra.

#### Command Line Usage

```sh
python sshLogin.py
```
Example Command : 
```
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://target_ip
```
# Script Description
 - Prompts the user for a username, password, and target IP address.
 - Constructs and runs the Hydra command to perform SSH login attempts.
 - Highlights successful login attempts in green.

### HTTP POST Form Login Automation (```httpLogin.py```)
  This script automates HTTP POST form login attempts using Hydra.

 #### Command Line Usage
 ```
 python httpLogin.py
 ```
 ### Example Command 
 ```
 hydra -l molly -P /usr/share/wordlists/rockyou.txt http-post-form://target_ip "/login:username=^USER^&password=^PASS^:Your username or password is incorrect." -I -V
 ```
 ## Script Description
 - Prompts the user for a username, password, target IP address, and HTTP POST form details.
 - Constructs and runs the Hydra command to perform HTTP POST form login attempts.
 - Highlights successful login attempts in green.

# Functions
## ```sshLogin.py```

 - ```GetUser()```: Prompts the user for a username or uses a default username list.
 - ```GetPassword()```: Prompts the user for a password or uses a default password list.
 - ```GetIp()```: Prompts the user for the target IP address.
 - ``` GetUserflag(input)```: Determines the user flag (-l or -L) based on the input length.
 - ```Getpassflag(input)```: Determines the password flag (-p or -P) based on the input length.
 - ```main()```: Orchestrates the user input and Hydra command execution.
## ```httpLogin.py```
 - ```GetUser()```: Prompts the user for a username or uses a default username list.
 - ```GetPassword()```: Prompts the user for a password or uses a default password list.
 - ```GetIp()```: Prompts the user for the target IP address.
 - ```GetUserflag(input)```: Determines the user flag (-l or -L) based on the input length.
 - ```Getpassflag(input)```: Determines the password flag (-p or -P) based on the input length.
- ```main()```: Orchestrates the user input and Hydra command execution.
# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Disclaimer
These scripts are intended for educational purposes only. Do not use them for illegal activities. The authors are not responsible for any misuse of these scripts.

                    
                               ____  _______    ______  __ _    ____________ 
                              / __ \/ ____/ |  / / __ \/ /| |  / /____/ ___\\
                             / /_/ / __/  | | / / / / / / | | / / __/ / /_/ /
                            / _, _/ /___  | |/ / /_/ / /__| |/ / /___/ _, _/  
                           /_/ |_/_____/  |___/\____/_____/___/_____/_/ |_|   
                                   Hydra automation By ROOT~REVOLVER
import subprocess

def mimikatZ():
  try:
    subprocess.run(['mimikatz.exe'], shell=True)
  except Exception as e:
    print("MimiKatz Not found")


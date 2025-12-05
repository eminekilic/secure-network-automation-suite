import os
from netmiko import ConnectHandler
from dotenv import load_dotenv

#load the secret from .env file
load_dotenv()

#get variables using os.getenv

target_host = os.getenv("ROUTER_IP")
username = os.getenv("ROUTER_USER")
password = os.getenv("ROUTER_PASS")
port = os.getenv("ROUTER_PORT")

if not target_host or not username or not password:
  print("ERROR: Credentials not found in .env file!")
  exit()

r1_info = {
    'device_type': 'cisco_ios',
    'host': target_host,
    'username': username,
    'password': password,
    'port': port
}
print("Connecting to the {target_host}...")

try:
   connection = ConnectHandler(**r1_info)
   print("Connected Succesfuly")
   full_config = connection.send_command("show running-config")
   file_name = "R1_Backup.txt"
   with open(file_name, "w") as file:
     file.write(full_config)
   print(f"SUCCESS! Backup saved to '{file_name}'.")
   connection.disconnect()

except Exception as e:
 print(f"AN ERROR OCCURRED: {e}")



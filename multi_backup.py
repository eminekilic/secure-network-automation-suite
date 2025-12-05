import csv
from netmiko import ConnectHandler

with open('inventory.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
   
    for row in csv_reader:
        print(f"Connecting: {row['hostname']}...")


        device_info = {
            'device_type' : row['device_type'],
            'host' : row['ip_address'],
            'username' : row['username'],
            'password' : row['password'],
            'port': 22
        }
        device_name = row['hostname']
        try:
            connection = ConnectHandler(**device_info)
            output = connection.send_command("show running-config")
            file_name = f"{device_name}_backup.txt"

            with open(file_name, 'w') as f:
                f.write(output)
            print(f"{file_name} saved!")
            connection.disconnect()
        
        except Exception as error:
            print(f"{device_name} ERROR: {error}")





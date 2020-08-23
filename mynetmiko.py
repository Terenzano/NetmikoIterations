from netmiko import ConnectHandler
from getpass import getpass

username = raw_input('Enter your SSH username: ')
password = getpass()


with open('commands_file_switch') as f:
    commands_list = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print('Connecting to device ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type' : 'cisco_ios',
        'ip' : ip_address_of_device,
        'username' : username,
        'password' : password
    }   

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(commands_list)
    print(output)


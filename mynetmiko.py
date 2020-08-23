from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter your SSH username: ')
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

    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print ('Authentication failure: ' + ip_address_of_device)
        continue
    except (NetMikoTimeoutException):
        print ('Timeout to device: ' + ip_address_of_device)
        continue
    except (EOFError):
        print ('End of file while attempting device: ' + ip_address_of_device)
        continue
    except (SSHException):
        print ('SSH issue. Are you sure SSH is enabled on device: ' + ip_address_of_device)
        continue
    except Exception as unknow_error:
        print ('Some other error ' + unknow_error)
        continue
    
    
    output = net_connect.send_config_set(commands_list)
    print(output)


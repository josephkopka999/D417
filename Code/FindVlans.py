import paramiko

# Function to connect to the switch and run a command
def check_vlans(switch_ip, username, password):
    try:
        # Establish an SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(switch_ip, username=username, password=password)

        # Execute the 'show vlan' command
        stdin, stdout, stderr = ssh.exec_command("show vlan")
        output = stdout.read().decode()
        error = stderr.read().decode()

        # Print the VLAN information
        if output:
            print(f"\nVLAN information for {switch_ip}:\n")
            print(output)
        if error:
            print(f"Error on {switch_ip}: {error}")

        # Close the SSH connection
        ssh.close()

    except Exception as e:
        print(f"Error connecting to {switch_ip}: {e}")


# List of switches and credentials
switches = [
    {"ip": "10.10.1.5", "username": "admin", "password": "password"},
    {"ip": "10.10.1.6", "username": "admin", "password": "password"},
    {"ip": "10.10.1.7", "username": "admin", "password": "password"},
    {"ip": "10.10.1.8", "username": "admin", "password": "password"},
    {"ip": "10.10.1.24", "username": "admin", "password": "password"}
]

# Loop through each switch and check VLANs
for switch in switches:
    check_vlans(switch["ip"], switch["username"], switch["password"])

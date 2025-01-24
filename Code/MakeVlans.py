import paramiko

# Function to connect to the switch and create a VLAN
def create_vlan(switch_ip, username, password, vlan_name, vlan_id):
    try:
        # Establish an SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(switch_ip, username=username, password=password)

        # Construct the command to create the VLAN
        command = f"create vlan {vlan_name} tag {vlan_id}"

        # Execute the command
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        # Print the results
        if output:
            print(f"\nOutput from {switch_ip}:\n{output}")
        if error:
            print(f"Error on {switch_ip}:\n{error}")
        else:
            print(f"VLAN {vlan_name} with ID {vlan_id} created on {switch_ip}.")

        # Close the SSH connection
        ssh.close()

    except Exception as e:
        print(f"Error connecting to {switch_ip}: {e}")

# List of switches and VLANs to create
switches = [
{"ip": "10.10.1.30", "username": "admin", "password": "password", "vlan_name": "IT_Network", "vlan_id": 100},
{"ip": "10.10.1.31", "username": "admin", "password": "password", "vlan_name": "MGMT_Network", "vlan_id": 200},
{"ip": "10.10.1.32", "username": "admin", "password": "password", "vlan_name": "ACCT_Network", "vlan_id": 300},
{"ip": "10.10.1.22", "username": "admin", "password": "password", "vlan_name": "User_networ", "vlan_id": 400}
]

# Loop through each switch and create the VLAN
for switch in switches:
    create_vlan(
        switch_ip=switch["ip"],
        username=switch["username"],
        password=switch["password"],
        vlan_name=switch["vlan_name"],
        vlan_id=switch["vlan_id"]
    )

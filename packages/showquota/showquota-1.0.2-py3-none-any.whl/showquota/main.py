# showquota/main.py

import os
import subprocess
import paramiko
import grp
import pwd
import argparse
from showquota.config import __version__, __author__, __license__

CONFIG_PATH = '/opt/showquota/config.cfg'
CONFIG_CONTENT = """#showquota configfile
#by Giulio Librando
#
#can be remote or localhost. if you set remote make sure the ssh public key is on the remote server
home_server_ip: 'x.x.x.x'
home_server_command: 'xfs_quota -x -c 'report -h' /home'
beegfs_server_ip: 'x.x.x.x'
beegfs_server_command: 'beegfs-ctl --getquota --gid %GID%'
"""

# ...resto del codice...

def ensure_config_exists():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, 'w') as config_file:
            config_file.write(CONFIG_CONTENT)
        print(f"Configuration file created at {CONFIG_PATH}. Please update the necessary variables.")
        return False
    return True

def read_config():
    config = {}
    with open(CONFIG_PATH, 'r') as config_file:
        for line in config_file:
            if not line.startswith("#") and ':' in line:
                key, value = line.split(':', 1)
                config[key.strip()] = value.strip().strip("'")
    return config

def get_user_info():
    user_info = {}

    # Get current user info
    user_info['username'] = pwd.getpwuid(os.getuid()).pw_name
    user_info['uid'] = os.getuid()

    # Get the primary group of the current user
    user_primary_gid = pwd.getpwuid(os.getuid()).pw_gid
    user_info['primary_group'] = grp.getgrgid(user_primary_gid).gr_name

    # Get the secondary groups of the current user
    groups_command = f"groups {user_info['username']}"
    groups_output = subprocess.run(groups_command, shell=True, capture_output=True, text=True)
    groups_list = groups_output.stdout.split()[2:]  # Ignore the first two elements ("username :" and "groups")
    user_info['secondary_groups'] = [group for group in groups_list if group != user_info['primary_group']]

    return user_info

def get_gid_for_group(group_name):
    try:
        group_info = grp.getgrnam(group_name)
        return group_info.gr_gid
    except KeyError:
        return None

def execute_ssh_command(host, command, verbose=False):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect using the SSH agent
    ssh.connect(host)

    if verbose:
        print(f"Executing remote command on {host}: {command}")

    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode()

    if verbose:
        print(f"Output of the remote command on {host}:")
        print(output)

    ssh.close()
    return output

def execute_local_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def main():
    parser = argparse.ArgumentParser(description='Show user and projects storage quotas.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {__version__}', help='Show the program version')
    args = parser.parse_args()

    # Check if the configuration file exists
    if not ensure_config_exists():
        return

    # Read the configuration file
    config = read_config()

    # Get local user info
    user_info = get_user_info()

    # Format local user info if verbose is enabled
    if args.verbose:
        user_info_str = (
            f"Username: {user_info['username']}  UID: {user_info['uid']}  "
            f"Primary Group: {user_info['primary_group']}  "
            f"Secondary Groups: {', '.join(user_info['secondary_groups'])}\n"
        )
        print(user_info_str)

    # Server details for /home folder and command to execute
    home_server_ip = config['home_server_ip']
    home_server_command = config['home_server_command']

    # Execute the remote command for /home
    home_server_output = execute_ssh_command(home_server_ip, home_server_command, verbose=args.verbose)

    # Server details for beegfs storage and command to execute
    beegfs_server_ip = config['beegfs_server_ip']
    beegfs_server_command_base = config['beegfs_server_command']

    # Execute the remote command for beegfs storage for each secondary group
    beegfs_server_outputs = []
    for group in user_info['secondary_groups']:
        gid = get_gid_for_group(group)
        if gid is not None:
            command_with_group = beegfs_server_command_base.replace('%GID%', str(gid))
            output = execute_ssh_command(beegfs_server_ip, command_with_group, verbose=args.verbose)
            beegfs_server_outputs.append((group, output))
        else:
            print(f"Group '{group}' not found or does not have a valid GID.")

    # Format the output of the Home folder
    home_folder_output = (
        f"Home folder:\n"
        f"{'-' * 50}\n"
        f"{home_server_output.strip()}\n"
        f"{'-' * 50}\n"
    )

    # Format the output of BeegFS
    beegfs_output = ""
    if beegfs_server_outputs:
        beegfs_output += (
            f"Project(s) folder:\n"
            f"{'-' * 72}\n"
        )
        for group, output in beegfs_server_outputs:
            beegfs_output += (
                f"Group: {group}\n"
                f"{output.strip()}\n"
                f"{'-' * 72}\n"
            )

    # Display the outputs on the screen
    print(home_folder_output)
    if beegfs_output:
        print(beegfs_output)

if __name__ == '__main__':
    main()

import os
import subprocess
import paramiko
import grp
import pwd
import argparse

# Import version
from __version__ import __version__

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

def ensure_config_exists():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, 'w') as config_file:
            config_file.write(CONFIG_CONTENT)
        print(f"Configuration file created at {CONFIG_PATH}. Please modify necessary variables.")
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

    # Get current user information
    user_info['username'] = pwd.getpwuid(os.getuid()).pw_name
    user_info['uid'] = os.getuid()

    # Get current user's primary group
    user_primary_gid = pwd.getpwuid(os.getuid()).pw_gid
    user_info['primary_group'] = grp.getgrgid(user_primary_gid).gr_name

    # Get current user's secondary groups
    groups_command = f"groups {user_info['username']}"
    groups_output = subprocess.run(groups_command, shell=True, capture_output=True, text=True)
    groups_list = groups_output.stdout.split()[2:]  # Ignore first two elements ("username :" and "groups")
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

    # Connect using SSH agent
    ssh.connect(host)

    if verbose:
        print(f"Executing remote command on {host}: {command}")

    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode()

    if verbose:
        print(f"Output of remote command on {host}:")
        print(output)

    ssh.close()
    return output

def execute_local_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def main():
    parser = argparse.ArgumentParser(description='Show user and projects storage quotas.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {__version__}', help='Show program version')
    args = parser.parse_args()

    # Check if configuration file exists
    if not ensure_config_exists():
        return

    # Read configuration file
    config = read_config()

    # Get local user information
    user_info = get_user_info()

    # Format local user information if verbose mode is active
    if args.verbose:
        user_info_str = (
            f"Username: {user_info['username']}  UID: {user_info['uid']}  "
            f"Primary Group: {user_info['primary_group']}  "
            f"Secondary Groups: {', '.join(user_info['secondary_groups'])}\n"
        )
        print(user_info_str)

    # Details for home server with /home folder and command to execute
    home_server_ip = config['home_server_ip']
    home_server_command = config['home_server_command']

    # Execute remote command for /home
    home_server_output = execute_ssh_command(home_server_ip, home_server_command, verbose=args.verbose)

    # Details for BeegFS server with storage and command to execute
    beegfs_server_ip = config['beegfs_server_ip']
    beegfs_server_command_base = config['beegfs_server_command']

    # Execute remote command for BeegFS storage for each secondary group
    beegfs_server_outputs = []
    for group in user_info['secondary_groups']:
        gid = get_gid_for_group(group)
        if gid is not None:
            command_with_group = beegfs_server_command_base.replace('%GID%', str(gid))
            output = execute_ssh_command(beegfs_server_ip, command_with_group, verbose=args.verbose)
            beegfs_server_outputs.append((group, output))
        else:
            print(f"Group '{group}' not found or does not have a valid GID.")

    # Format output for Home folder
    home_folder_output = (
        f"Home folder:\n"
        f"{'-' * 50}\n"
        f"{home_server_output.strip()}\n"
        f"{'-' * 50}\n"
    )

    # Format output for BeegFS
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

    # Print outputs to screen
    print(home_folder_output)
    if beegfs_output:
        print(beegfs_output)

if __name__ == '__main__':
    main()

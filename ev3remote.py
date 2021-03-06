from paramiko import SSHClient
import config # store username/password in local file
# https://www.kite.com/python/answers/how-to-ssh-using-paramiko-in-python

PATH_EV3COMMAND = '/home/robot/python-ev3/ev3command.py'
PATH_PYTHON_EV3 = '/home/robot/python-ev3'

class ev3remote:
    
    def __init__(self, machine, username, password):
        self.client = SSHClient()
        self.client.load_system_host_keys()
        self.client.connect(machine, username=username, password=password)

    def close(self):
        self.client.close()

    def run_command(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        lines = stdout.readlines()
        return lines

    def run_ev3_command(self, cmd, command_path=PATH_EV3COMMAND):
        cmd = 'python3 ' + command_path + ' ' + cmd
        stdin, stdout, stderr = self.client.exec_command(cmd)
        lines = stdout.readlines()
        return lines

if __name__ == '__main__':
    ev3 = ev3remote(config.MACHINE, config.USERNAME, config.PASSWORD)
    lines = ev3.run_command('(cd ' + PATH_PYTHON_EV3 + '; pwd)')
    print(lines)
    ev3.close()


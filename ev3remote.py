from paramiko import SSHClient
import config # store username/password in local file
# https://www.kite.com/python/answers/how-to-ssh-using-paramiko-in-python

class ev3remote:
    
    def __init__(self, machine, username, password):
        self.client = SSHClient()
        self.client.load_system_host_keys()
        # self.client.load_host_keys('~/.ssh/known_hosts')
        # self.client.set_missing_host_key_policy(AutoAddPolicy())
        print(machine + ' ' + username + ' ' + password)
        self.client.connect(machine, username=username, password=password)

    def close(self):
        self.client.close()

    def run_command(self,cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        lines = stdout.readlines()
        return lines

if __name__ == '__main__':
    ev3 = ev3remote(config.MACHINE, config.USERNAME, config.PASSWORD)
    lines = ev3.run_command('(cd /home/robot/python-ev3; pwd)')
    print(lines)
    lines = ev3.run_command("python3 /home/robot/python-ev3/ev3command.py -c 'on_for_rotations' -d 'neg' -s 5. -o 'D' -r 0.2")
    print(lines)
    ev3.close()


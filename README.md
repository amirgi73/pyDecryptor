# pyDecryptor

![](https://img.shields.io/github/stars/amirgi73/pyDecryptor.svg) ![](https://img.shields.io/github/forks/amirgi73/pyDecryptor.svg) ![](https://img.shields.io/github/tag/amirgi73/pyDecryptor.svg) ![](https://img.shields.io/github/release/amirgi73/pyDecryptor.svg) ![](https://img.shields.io/github/issues/amirgi73/pyDecryptor.svg)

A simple pyhton script to decrypt hashed passwords.

Features
=============
- Decrypts hashed passwords using a rainbow table created from a list of common passwords.
- Ability to save the generated rainbow table to use it later and save time and resources.
- Corrently supports following algorithms:
	- md5
	- sha1
	- sha256
	- sha512

Requirements
=============
- python3
- a txt file containing common passwords (an example file is provided in the repo)
- a csv file containing ("user,hash" or "email,hash")es (an example input.csv is provided in the repo)

Installation
=============
Clone repository using `git` and `cd` to newly created directory

    $git clone "https://github.com/amirgi73/pyDecryptor"
    $cd pyDecryptor/
    
Run the script using `python3`

    $python3 menu.py
    #or in arch or arch based distros:
    $python menu.py

How to use it
=============
- After runing the script, use 1 , 2 or 3, ... to make appropriate selection...
- For addressing input files simply place the file in the 'input' folder and enter name of the file when prompted.

Notes
=============
- The input file should be in .csv format. otherwise you get an error.
- The input file should contain two elements seperated by a comma in each line:

        user1,hashedPassword1
        user2,hashedpassword2
        .
        .
        .
	
    or
    
        email1,hashedPassword1
        email2,hashedPassword2
        .
        .
        .

- An example input.csv file is provided.

References
=============
- The 'password.txt' is from danielmiessler's repo: https://github.com/danielmiessler/SecLists

To do
=============
- [x] ability to save generated rainbow table for later use
- [x] add support for other hashing algorithms
- [x] use OOP for easier development...
- [x] Add error handling capability
- [x] Add code 'docstrings' so you can understand the code easier.
- [ ] Add Help.txt


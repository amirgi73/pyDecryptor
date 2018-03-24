# pyDecryptor

![](https://img.shields.io/github/stars/amirgi73/pyDecryptor.svg) ![](https://img.shields.io/github/forks/amirgi73/pyDecryptor.svg) ![](https://img.shields.io/github/tag/amirgi73/pyDecryptor.svg) ![](https://img.shields.io/github/release/amirgi73/pyDecryptor.svg) ![](https://img.shields.io/github/issues/amirgi73/pyDecryptor.svg)

A simple pyhton script to decrypt hashed passwords.

Features
=============
- decrypts sha256 hashed passwords using a rainbow table created from a list of common passwords.
- ability to save the generated rainbow table to use it later and save time and resources.
- corrently supports sha256 algorithm.

Requirements
=============
- python3
- a txt file containing common passwords (an example file is provided in the repo)
- a csv file containing ("user,hash" or "email,hash")es (an example input.csv is provided in the repo)

Installation
=============
clone repository using `git` and `cd` to newly created directory

    $git clone "https://github.com/amirgi73/pyDecryptor"
    $cd pyDecryptor/
    
run the script using `python3`

    $python3 pyDecryptor.py
    #or in arch or arch based distros:
    $python pyDecryptor.py

How to use it
=============
- after runing the script, use 1 , 2 or 3 to make appropriate selection...
- for addressing files you can use absolute path(es) or simply place the file in the projects folder and enter name of file when prompted.

Notes
=============
- the input file should be in .csv format. otherwise you get an error.
- the input file should contain two elements speretaed by a comma in each line:

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

- an example input.csv file is provided.

References
=============
- the 'password.txt' is from danielmiessler's repo: https://github.com/danielmiessler/SecLists

To do
=============
- [x] ability to save generated rainbow table for later use
- [ ] add support for other hashing algorithms

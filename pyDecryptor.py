import hashlib
import csv

hash_pass_dic = dict()
imported_hash_list = list()
pass_list = list()
pre_hashed_dic = dict()


def pre_hashed_dict():
    with open(input("Enter your prehashed .txt file conataining hash:password:(i.e gen_hashed.txt):\n")) as pre_hashed:
        for h in pre_hashed:
            h = h[:-1]
            h = h.split(":")
            pre_hashed_dic[h[0]] = h[1]


def get_input():
    input_file = open(input("Enter the csv file name containing user,hashed combinations:\n"))
    for row in csv.reader(input_file):
        imported_hash_list.append(row)
    input_file.close()
    print("Done!")


def get_pass_list():
    pass_file = open(input("Enter the txt file containing common passwords:\n"))
    for line in pass_file:
        pass_list.append(line[:-1])
    #  print(pass_list)
    pass_file.close()
    print("Done!")
    for i in pass_list:
        hash_ = hashlib.sha256(str(i).encode("utf_8")).hexdigest()
        hash_pass_dic[hash_] = str(i)


def save_gen_hash():
    if input("Do you want to save the hashed dictionary for later use?(y/N)\n").lower() == "y":
        save_gen_hash = input("Enter the file name to save as:(i.e gen_hash.txt)")
        with open(save_gen_hash, "w") as gen_file:
            for a, b in hash_pass_dic.items():
                gen_file.write("{0}:{1}\n".format(a, b))
            gen_file.close()


def write_results(hash_dic):
    with open("results.txt", "w") as res_file:
        for j in imported_hash_list:
            result = hash_dic.get(j[1].lower(), "")
            res_file.write("{0}:{1}\n".format(j[0],result))
        res_file.close()


while True:
    print("\n\n\n\n\n\nPlease select an option:")
    print("[1]: Unhash me using a list of common passwords")
    print("[2]: Unhash me using a pre calculated hash:password txt file")
    print("[3]: Exit")
    try:
        answ = int(input())
    except:
        continue
    if answ == 1:
        get_input()
        get_pass_list()
        save_gen_hash()
        write_results(hash_pass_dic)
        print("Done! Check the results.txt file...\n")
        break
    elif answ == 2:
        get_input()
        pre_hashed_dict()
        write_results(pre_hashed_dic)
        print("Done! Check the results.txt file...\n")
        break
    elif answ == 3:
        print("Exiting...\n")
        break
    else:
        continue
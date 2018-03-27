import modules.hash_calc
import modules.file_handle
import hashlib
from sys import exit
from os import path

scr_path = path.dirname(__file__)


class Menu:
    def __init__(self):
        self.hash_ = modules.hash_calc.Hashes()
        self.in_file = modules.file_handle.InputFile()
        self.e_file = modules.file_handle.Export()
        self.choices = {
            "1": self.unhash_passlist,
            "2": self.unhash_prehashed,
            "3": self.settings_,
            "4": self.help_me,
            "5": self.credits,
            "6": self.donate_,
            "7": self.license_,
            "8": self.quit
        }
        self.hash_choice = {
            "1": hashlib.md5,
            "2": hashlib.sha1,
            "3": hashlib.sha256,
            "4": hashlib.sha512
        }

    def display_menu(self):
        print("""

\t\t\tpyDecryptor Menu:\t\t\t


[1]. Unhash me using a password list file
[2]. Unhash me using a pre calculated hash list file
[3]. Settings
[4]. Help
[5]. Credits
[6]. Donate!
[7]. License
[8]. Exit
""")

    def hashtype_menu(self):
        print("""

Available Hash Algorithms:


[1]. md5
[2]. sha1
[3]. sha256
[4]. sha512
""")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter an Option:\t")
            action = self.choices.get(choice)
            if action:
                action()
                break
            else:
                print("\n{0} is not a valid Option!\n".format(choice))

    def get_hashtype(self):
        hashchoice = input("\nSelect a Hash Algorithm to Use:\t")
        self.hashtype = self.hash_choice.get(hashchoice)
        if self.hashtype:
            return self.hashtype
        else:
            print("\n{0} is not a valid Algorithm!\n".format(hashchoice))

    def save_gen(self):
        print("\nShould I save calculated hashes for later use?(default: Yes)"
              + "\nY or N?:\t")
        answ = input().lower()
        if answ == "n":
            return False
        else:
            return True

    def get_in_file(self):
        in_name = input(("\nEnter the user,hash CSV file name"
                        + " to load. (i.e input.csv)\ncsv file:\t"))
        self.in_file.read_input(in_name)

    def get_in_pass_file(self):
        in_pass_name = input(("\nEnter the passwords list file name"
                              + " to load. (i.e passwords.txt)\ntxt file:\t"))
        self.in_file.read_passlist(in_pass_name)

    def get_in_prehashed(self):
        in_prehash_name = input(("\nEnter the pre hashed file name"
                                 + " to load. (i.e gen_hashed.txt)" +
                                 "\ntxt file:\t"))
        self.in_file.read_prehashed(in_prehash_name)

    def ex_gen_file(self):
                if self.save_gen():
                    e_gen_name = input("\nEnter a file name to save calculated"
                                       + " hashes in it. " +
                                       "(i.e gen_hashes.txt)\nSave as:\t")
                    self.e_file.export_gen_hashes(e_gen_name, self.hashtype)

    def cal_hash(self):
        self.hash_.calculate_hash(self.get_hashtype(), self.in_file.
                                  imp_pass_list)

    def ex_res_file(self, dic_):
        e_res_name = input("\nEnter a file name to save results"
                           + " in it. (i.e gen_hashes.txt)\nSave as:\t")
        self.e_file.export_results(e_res_name, dic_)

    def unhash_passlist(self):
        self.get_in_file()
        self.get_in_pass_file()
        self.hashtype_menu()
        self.cal_hash()
        self.ex_gen_file()
        self.ex_res_file(self.hash_.hash_pass_dic)
        print("\n\t\t\tJob Done! Check export folder for saved files...")

    def unhash_prehashed(self):
        self.get_in_file()
        self.get_in_prehashed()
        self.ex_res_file(modules.file_handle.InputFile.pre_hashed_dic)
        print("\n\t\t\tJob Done! Check export folder for saved files...")

    def settings_(self):
        print("Maybe we have some things to set in the coming days!"
              + " Who Knows...\nReturning to Main Menu...")
        self.run()

    def help_me(self):
        print("Help Docs will be available Soon...\nReturning to Main Menu...")
        self.run()
        # help_file = open(path.join(scr_path, "Documents/Help.txt"))
        # print("\n\n"+help_file)
        # help_file.colse()

    def credits(self):
        cr_file = open(path.join(scr_path, "Documents/Credits.txt"))
        print("\n\n"+cr_file.read())
        cr_file.close()

    def license_(self):
        lic_file = open(path.join(scr_path, "Documents/LICENSE"))
        print("\n\n"+lic_file.read())
        lic_file.close()

    def donate_(self):
        don_file = open(path.join(scr_path, "Documents/Donate.txt"))
        print("\n\n"+don_file.read())
        don_file.close()

    def quit(self):
        print("\n\t\t\tExiting...")
        exit()


if __name__ == "__main__":
    Menu().run()

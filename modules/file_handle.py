from csv import reader
from .hash_calc import Hashes
from os import path
from sys import exit


script_dir = path.dirname(__file__)  # Determine absolute Script path


class InputFile(object):
    """Handles Input Files. Reads them from the given path and imports them\
    in list or dictionary variables"""
    imp_hash_list = []  # a list to hold imported user,hash strings
    imp_pass_list = []  # a list to hold imported password strings
    pre_hashed_dic = {}  # a dictionary to hold imported hash:password strings

    def read_input(self, inf_name):
        """reads input csv file and saves it in imp_hash_list variable
        Note: the input file should be in 'import' folder or you get an\
        error
        gets 1 aurgument: name of the input file which is in 'import' folder"""
        in_f_path = path.join(script_dir, "../import/"+inf_name)
        try:
            in_file = open(in_f_path)
        except FileNotFoundError:
            self.f_not_found([in_f_path], inf_name)
        for row in reader(in_file):
            InputFile.imp_hash_list.append(row)
        print("\n\t\t\t{0} loaded successfully...".format(inf_name))
        in_file.close()

    def read_passlist(self, pass_name):
        """reads common passwords from a txt file in 'import' folder\
        and saves it to imp_pass_list variable
        gets 1 aurgument: name of the file.txt containing common passwords"""
        pass_f_path = path.join(script_dir, "../import/"+pass_name)
        try:
            pass_file = open(pass_f_path)
        except FileNotFoundError:
            self.f_not_found([pass_f_path], pass_name)
        for line in pass_file:
            InputFile.imp_pass_list.append(line[:-1])
        print("\n\t\t\t{0} loaded successfully...".format(pass_name))
        pass_file.close()

    def f_not_found(self, path_, f_name="File"):
        """Handles FileNotFoundError\n
        gets two attributes(the 2nd one is optional):
        path_: a list of pathes that the program looked them for \
        the file without success\n
        f_name:(optional): name of the file that user enters\n
        Note: path_ attribute should be a list."""
        print("\nWe looked for {0} at these addresses".format(f_name) +
              " but we couldn't find it:")
        for q in path_:
            print(q)
        print("\n\t\t\tExiting...")
        exit()

    def read_prehashed(self, prehashed_name):
        """Reads pre_hashed file containing hash:password per line.
        it gets 1 aurgument: 'name of the file to read' and looks in to\
         directories for that file: 'import' and 'export' folders
         """
        path_import = path.join(script_dir, "../import/" + prehashed_name)
        path_export = path.join(script_dir, "../export/" + prehashed_name)
        try:
            preh_file = open(path_import)
        except FileNotFoundError:
            try:
                preh_file = open(path_export)
            except FileNotFoundError:
                self.f_not_found([path_import, path_export], prehashed_name)

        for line in preh_file:
            line = line[:-1]
            line = line.split(":")
            InputFile.pre_hashed_dic[line[0]] = line[1]
        print("\n\t\t\t{0} loaded successfully...".format(prehashed_name))
        preh_file.close()

    def ret_prehashed_dic(self):
        """returns pre_hashed_dic"""
        return InputFile.pre_hashed_dic


class Export(InputFile):
    """Handles file exports. saves information in in 'export' folder"""
    def export_gen_hashes(self, e_hashed_name, hash_t):
        """Saves generated hashes to a file for later use
        gets 2 aurgument: name of file to save as, hash type"""
        with open(path.join(script_dir, "../export/"
                            + "{0}_{1}".format(hash_t, e_hashed_name)),
                  "w") as e_hashed_file:
            for a, b in Hashes.hash_pass_dic.items():
                e_hashed_file.write("{0}:{1}\n".format(a, b))
            e_hashed_file.close()
            print("\n\t\t\t{0} saved successfully...".format(e_hashed_name))
            e_hashed_file.close()

    def export_results(self, e_results_name, hashed_dic):
        with open(path.join(script_dir, "../export/" + e_results_name),
                  "w") as e_res_file:
            for j in InputFile.imp_hash_list:
                result = hashed_dic.get(j[1].lower(), "")
                e_res_file.write("{0}:{1}\n".format(j[0], result))
            print("\n\t\t\t{0} saved successfully...".format(e_results_name))
            e_res_file.close()

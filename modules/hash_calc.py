import hashlib


class Hashes:
    """Calculates Hashes from given list of strings."""
    hash_pass_dic = {}

    def calculate_hash(self, hashtype, passwords):
        """Calculates Hash.
        gets two aurguments: hashtype which specifies the algorithm for hashing
        passwords which is a list of strings to be hashed.
        Saves the results in a dictionary variable {hash:string, ...}
        as hash_pass_dic. It is a class variable so it can be imported in /
        other files easily """
        for i in passwords:
            try:
                hash = hashtype(str(i).encode("utf_8")).hexdigest()
                self.hash_pass_dic[hash] = str(i)
            except AttributeError:
                print("\t\tUnknown Algorithm!\t\t")
        print("\n\t\t\tPass list Hashed successfully...")

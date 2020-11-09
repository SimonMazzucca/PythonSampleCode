class StringManipulation:

    def concatAndReplace(self):
        prefix = "Easy come, easy go,"
        suffix = "will you let me go?"

        # Concatenate and replace
        full_str = prefix + suffix
        full_str = full_str.replace(",will", ". Will")
        print(full_str)

        # Concatenate and replace
        s = "0 0 0 0 0 0 "
        s = s.replace("0", "1", 3)
        print(s)

        # Count substrings
        s = "Simone Coglione"
        print(s.count("on"))


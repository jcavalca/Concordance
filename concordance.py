from hash_quad import *
import string


class Concordance:

    def __init__(self):
        self.stop_table = None  # hash table for stop words
        self.concordance_table = None  # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word
        as a key into the stop words hash table. Starting size of hash table
        should be 191: self.stop_table = HashTable(191) If file does not
        exist, raise FileNotFoundError """
        self.stop_table = HashTable(191)
        try:
            stop_file = open(filename)
        except FileNotFoundError:
            raise FileNotFoundError
        lines_word = stop_file.readlines()
        for i in lines_word:
            word = ""
            for j in range(len(i) - 1):
                word += i[j]
            self.stop_table.insert(word, 0)
        stop_file.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into
        the concordance hash table, after processing for punctuation, numbers
        and filtering out words that are in the stop words hash table. Do not
        include duplicate line numbers (word appearing on same line more than
        once, just one entry for that line) Starting size of hash table
        should be 191: self.concordance_table = HashTable(191) If file does
        not exist, raise FileNotFoundError """
        self.concordance_table = HashTable(191)
        try:
            text_file = open(filename)
        except FileNotFoundError:
            raise FileNotFoundError
        lines = text_file.readlines()
        for i in range(len(lines)):
            current_line = lines[i]
            current_line = current_line.replace("'", "")
            current_line = current_line.replace("-", " ")
            current_line = current_line.split()
            for j in current_line:
                j = j.strip(string.punctuation)
                try:
                    a = float(j)
                except ValueError:
                    j = j.lower()
                    if self.stop_table.in_table(j) is False:
                        if self.concordance_table.in_table(j) is False and j != "":
                            self.concordance_table.insert(j, i + 1)
                        elif j != "":
                            index = self.concordance_table.get_index(j)
                            if self.concordance_table.hash_table[index][1][
                            -1] != i + 1:
                                self.concordance_table.insert(j, i + 1)
        text_file.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        output_file = open(filename, "w", newline="")
        alist = []
        for j in self.concordance_table.hash_table:
            if j is not None:
                alist.append(j[0])
        alist.sort()
        for i in range(len(alist)):
            lines_numbers = self.concordance_table.get_value(alist[i])
            lines_string = ""
            for j in lines_numbers:
                lines_string += " " + str(j)
            word = alist[i].strip(string.punctuation)
            output_file.write(f"{word}:{lines_string}")
            if i != len(alist) - 1:
                output_file.write("\n")
        output_file.close()

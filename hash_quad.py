class HashTable:

    def __init__(self, table_size):  # can add additional attributes
        self.table_size = table_size  # initial table size
        self.hash_table = [None] * table_size  # hash table
        self.num_items = 0  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function
        to determine index, and quadratic probing to resolve collisions). The
        key is a string (a word) to be entered, and value is the line number
        that the word appears on. If the key is not already in the table,
        then the key is inserted, and the value is used as the first line
        number in the list of line numbers. If the key is in the table,
        then the value is appended to that key’s list of line numbers. If
        value is not used for a particular hash table (e.g. the stop words
        hash table), can use the default of 0 for value and just call the
        insert function with the key. If load factor is greater than 0.5
        after an insertion, hash table size should be increased (doubled +
        1). """
        if self.in_table(key) is False:
            self.num_items += 1
        if self.get_load_factor() > 0.5:
            alist = []
            for i in self.hash_table:
                if i is not None:
                    alist.append(i)
            self.table_size = 2 * self.table_size + 1
            self.hash_table = [None] * self.table_size
            self.num_items = 0
            for j in alist:
                self.insert(j[0], j[1])
            self.insert(key, value)
            return
        keep_going = True
        index = self.horner_hash(key)
        new_index = index
        count = 0
        while keep_going:
            if self.hash_table[new_index] is None:
                if isinstance(value, str) or isinstance(value, int):
                    self.hash_table[new_index] = (key, [value])
                else:
                    self.hash_table[new_index] = (key, value)
                return
            elif self.hash_table[new_index][0] == key:
                self.hash_table[new_index][1].append(value)
                return
            else:
                count += 1
                new_index = (index + count ** 2) % self.table_size

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash
        table) - 1 Compute the hash value by using Horner’s rule,
        as described in project specification. """
        h = 0
        n = min(len(key), 8)
        for i in range(n):
            add = ord(key[i]) * (31 ** (n - 1 - i))
            h += add
        return h % self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False
        otherwise. """
        count = 0
        index = self.horner_hash(key)
        new_index = index
        while 1 > 0:
            if self.hash_table[new_index] is None:
                return False
            if self.hash_table[new_index][0] == key:
                return True
            new_index = (index + count ** 2) % self.table_size
            count += 1

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided
        key. If there is not an entry with the provided key, returns None. """
        count = 0
        index = self.horner_hash(key)
        new_index = index
        while 1 > 0:
            new_index = (index + count ** 2) % self.table_size
            if self.hash_table[new_index] is None:
                return
            if self.hash_table[new_index][0] == key:
                return new_index
            count += 1

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        alist = []
        for i in self.hash_table:
            if i is not None:
                alist.append(i[0])
        return alist

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        count = 0
        index = self.horner_hash(key)
        new_index = index
        while 1 > 0:
            new_index = (index + count ** 2) % self.table_size
            if self.hash_table[new_index] is None:
                return
            if self.hash_table[new_index][0] == key:
                return self.hash_table[new_index][1]
            count += 1

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size

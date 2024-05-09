class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]
    
    # hash key to index  
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    
    # insert item
    def insert(self, key, value):
        self.arr[self.get_hash(key)] = value
        
    # get item
    def get(self, key):
        return self.arr[self.get_hash(key)]
    
    def print(self):
        hash_arr = list(filter(lambda x: x != None, self.arr))
        print(hash_arr)
        
    # change insert to __setitem__ and get to __getitem__
    def __setitem__(self, key, value):
        self.arr[self.get_hash(key)] = value
        
    def __getitem__(self, key):
        return self.arr[self.get_hash(key)] 
    
    # delete item
    def __delitem__(self, key):
        self.arr[self.get_hash(key)] = None
        
    
hash_table = HashTable()
hash_table.insert("Monday", 1500)
hash_table.insert("Tuesday", 1600)
hash_table.insert("Wednesday", 1700)
hash_table["Thursday"] = 1800
hash_table["Friday"] = 1900
del hash_table["Monday"]
print(hash_table["Friday"])
hash_table.print()

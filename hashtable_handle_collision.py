class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]
     
    # hash function
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
       
    # insert item
    def __setitem__(self, key, val):
        index = self.get_hash(key)
        
        for idx, item in enumerate(self.arr[index]):
            if len(item) == 2 and item[0] == key:
                self.arr[index][idx] = (key, val)
                return
        self.arr[index].append((key, val))
      
        
    # get item
    def __getitem__(self, key):
        index = self.get_hash(key)
        if len(self.arr[index]) == 0:
            return "Key not found"
        
        for element in self.arr[index]:
            if element[0] == key:
                return element[1]
        return "Key not found"
         
            
    # delete item
    def __delitem__(self, key):
        index = self.get_hash(key)
        if len(self.arr[index]) == 0:
            return "Key not found"
        
        for idx, element in enumerate(self.arr[index]):
            if element[0] == key:
                del self.arr[index][idx]
                return
        return "Key not found"
    
    # print item
    def print(self):
        print(list(filter(lambda x: len(x) != 0, self.arr)))
            

hash_table = HashTable()
hash_table["Monday"] =  1500
hash_table["Tuesday"] = 1600
hash_table["Wednesday"] =  1700
hash_table["Thursday"] = 1800
hash_table["Friday"] = 2000
hash_table["Wednesday"] =  1700
# hash_table["Frida"] = 2100
hash_table["Frid"] = 2200
hash_table["Fri"] = 2300
# hash_table["Fr"] = 2400
print(hash_table["Fri"])
print(hash_table["Frid"])
hash_table.print()    
        
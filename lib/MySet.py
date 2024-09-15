class MySet:

    def __init__(self,enumerable=[]):
       self.dictionary = {}
       for value in enumerable:
        self.dictionary[value] = True


    def has(self, value):
        return value in self.dictionary
    
    
    def add(self, value):
        self.dictionary[value] = True # Add a value as a key on the Dictionary
        return self                   # Return the updated set

    def delete(self, value):
       self.dictionary.pop(value, None)
       return self
    
    def clear(self):
        self.dictionary.clear()
        return self
    
    # def __str__(self):
    #     return f"MySet:{set(self.dictionary.keys())}"

    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'



my_set =MySet([1,2,3,3])
print(my_set)
print(my_set.has(1))
print(my_set.has(7))
print(my_set.add(4))
print(my_set.delete(4))
my_set.clear()
print(my_set)
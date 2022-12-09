class MapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self):
        self.my_arr = []
        self.bucket_size = 10
        self.my_arr = [None for i in range(self.bucket_size)]
        self.my_length = 0


    def load_factor(self):
        if self.my_length / self.bucket_size > 0.7:
            return True
        return False
    def hash_and_compress(self,key):
        hashing = hash(key)
        my_index = abs(hashing) % self.bucket_size
        return my_index

    def add(self, key,value):
        rehashing_needed = self.load_factor()
        if rehashing_needed:
            self.rehashing()
        idx = self.hash_and_compress(key)

        is_key_present = False
        temp = self.my_arr[idx]
        while temp is not None:
            if temp.key == key:
                is_key_present = True
                temp.value = value
                break
            temp = temp.next
        if is_key_present:
            return

        key_value_node = MapNode(key,value)
        key_value_node.next = self.my_arr[idx]
        self.my_arr[idx] = key_value_node
        self.my_length += 1

    def remove_helper(self,key,node):
        if node is None:
            return False, None
        if node.key == key:
            return True, node.next
        found,small_ll = self.remove_helper(key,node.next)
        node.next = small_ll
        return found, node

    def remove(self,key):
        idx = self.hash_and_compress(key)
        node = self.my_arr[idx]
        found, final_node = self.remove_helper(key, node)
        self.my_arr[idx] = final_node
        if found:
            self.my_length -= 1
        return found

    def print(self):
        for i in range(self.bucket_size):
            print(i,end=" ")
            temp = self.my_arr[i]
            while temp is not None:
                print(f"{temp.key}-{temp.value}",end=" ")
                temp = temp.next
            print()


    def rehashing(self):
        new_bucket_size = 2 * self.bucket_size
        old_arr = self.my_arr
        self.my_arr = [None for i in range(new_bucket_size)]
        self.bucket_size = new_bucket_size
        for i in old_arr:
            current_node = i
            while current_node is not None:
                legacy_key, legacy_value = current_node.key, current_node.value
                self.add(legacy_key,legacy_value)
                self.my_length -= 1
                current_node = current_node.next

h1 = HashMap()
# print(h1.my_arr)

for i in range(26):
    key_value = ord('a') + i
    h1.add(chr(key_value),i)
    print(h1.my_length, h1.bucket_size)
    print("--------")


# h1.print()
# print(h1.my_length)
# h1.remove('3')
# h1.print()
# print(h1.my_length)
# # h1.remove()
# h1.length()
# h1.is_present()

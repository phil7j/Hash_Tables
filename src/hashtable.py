# '''
# Linked List hash table key/value pair
# '''

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return f"(Key:{self.key}, Value:{self.value})"
class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0
        self.load = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):

        # if self.load >= 2:
        #     self.resize()
        new_key = self._hash_mod(key)

        # Check if key already exists
        # Add linkedPair to bucket
        if self.storage[new_key] is not None:
            current = self.storage[new_key]
            prev_pair = self.storage[new_key]
            # Iterate to the last linkedList item
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                prev_pair = current
                current = current.next
            prev_pair.next = LinkedPair(key,value)
            print(f"Added to {new_key}, as LinkedList")
            self.count += 1
            self.load = (self.count / self.capacity)

        else:
        # Add new Linked Pair at index
            self.storage[new_key] = LinkedPair(key, value)
            print(f"Added to {new_key}")
        # Adjust count and change load
            self.count += 1
            self.load = (self.count / self.capacity)






    def remove(self, key):

        # Get index
        new_key = self._hash_mod(key)
        # Check if it exists
        if self.storage[new_key] == None:
            print("ERROR: This Key is not found")
            return
        elif self.storage[new_key].key == key:
            if self.storage[new_key].next == None:
                self.storage[new_key] = None
                return
            elif self.storage[new_key].next is not None:

            # Iterate to the last linkedList item
                self.storage[new_key] = self.storage[new_key].next
        else:
            current = self.storage[new_key]
            prev = self.storage[new_key]
            while current is not None:
                if current.key == key:
                    prev.next = current.next
                    break
                else:
                    prev = current
                    current = current.next
            if current == None:
                print("ERROR: This Key is not found")
                return
        # Delete Key and lower count by 1
        # self.storage[new_key] = None
        # Adjust count and change load
        self.count -= 1
        self.load = (self.count / self.capacity)



    def retrieve(self, key):

        # Find Index
        new_key = self._hash_mod(key)

        if self.storage[new_key] == None:
            return None
        elif self.storage[new_key].key == key:
            return self.storage[new_key].value
        elif self.storage[new_key].next is not None:
            current = self.storage[new_key]
            # Iterate to the last linkedList item
            while current.next is not None:
                if current.next.key == key:
                    # print("THIS IS IT", current.next.value)
                    return current.next.value
                current = current.next



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        temp = []
        temp = self.storage

        self.storage = new_storage
        for item in temp:
            current = item
            while current is not None:
                self.insert(current.key, current.value)
                current = current.next
        self.load = (self.count / self.capacity)

    def showit(self):
        for i in range(len(self.storage)):
            if self.storage[i] is not None and self.storage[i].next is not None:
                current = self.storage[i]
                print("IM in it")
                # print(f"Index={i}, current={current}, current.next ={current.next}")
                while current.next is not None:
                    print(f"At indexx {i}, {current}")
                    current = self.storage[i].next
                continue

            else:
                print(f"At index {i}, {self.storage[i]}")


# ht = HashTable(4)

# ht.insert("line_1", "Tiny hash table")
# ht.insert("line_2", "Not Tiny hash table")
# ht.insert("line_3", "Filled beyond capacity")

# ht.retrieve("line_3")
# ht.showit()
# print("Capacity ",ht.capacity)
# print("Count ", ht.count)
# print("Load ",ht.load)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

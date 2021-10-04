
class HashTable:
    def __init__( self, cap ):
        self.cap = cap
        self.length = 0
        nums = []
        for i in range(0, cap, 1):
            nums.append( None )
        self.storage = nums
    
    def printHashTable( self ):
        print( "Capacity: ", self.cap )
        print( "Length: ", self.length )
        print( "Storage: ", self.storage )

    def add( self, val ):
        index = (int((((val / 13) * 32) + 14) * 7)) % self.cap
        print( index )
        # Check if the length has not surpassed the capacity of the hash table 
        if self.storage[ index ] == None:
            self.storage[ index ] = val
            self.length += 1
        else:
            # We should change the current value to a linked list and add the new value at the end of that list
            print( "That spot is already in use." )
    
    def find( self, val ):
        index = (int((((val / 13) * 32) + 14) * 7)) % self.cap

        if self.storage[ index ] == None:
            print( f"The value {val} is not yet in our HashTable!" )
            return None
        else:
            if self.storage[ index ] != val:
                print( f"The value {val} is not yet in our HashTable!" )
                return None
            else:
                print( f"The value {val} is stored at position {index} of the HashTable" )
                return index
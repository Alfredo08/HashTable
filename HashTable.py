from LinkedList import LinkedList
from Node import Node

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
            if type( self.storage[ index ] ) == int:
                list = LinkedList()
                list.insertLast( self.storage[ index ] )
                self.storage[ index ] = list
            self.storage[ index ].insertLast( val )
    
    def find( self, val ):
        index = (int((((val / 13) * 32) + 14) * 7)) % self.cap

        if self.storage[ index ] == None:
            print( f"The value {val} is not yet in our HashTable!" )
            return None
        else:
            print( f"The value {val} is stored at position {index} of the HashTable" )
            if type(self.storage[ index ]) != int:
                list = self.storage[ index ]
                node = list.findNode( val )
                print( "Printing the value from a node in the linked list", node.val)
            return self.storage[ index ], index
    
    def remove( self, val ):
        pass
        # First find if the value is in the hashtable
        # If it is in the hastable remove it (subtracting the length)
        # If it is a linked list, make sure to remove the appropriate Node inside that link list
import hashlib
import os

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    BYTE_LENGTH = 4
    compare_bit = 2 ** k - 1
    #Collision finding code goes here
    while True:
        x = os.urandom(BYTE_LENGTH)
        y = os.urandom(BYTE_LENGTH)
        hash_x = hashlib.sha256(x)
        hash_y = hashlib.sha256(y)
        if (int(hash_x.hexdigest(), 16) & compare_bit) == (int(hash_y.hexdigest(), 16) & compare_bit):
            return (x, y)



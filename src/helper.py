
#Multiplication Rijandel's galois field
#Thank's to https://www.samiam.org/galois.html
#Take tewo eight-bit numbers a, b
def gmul(a, b):
    #eigth-bit product
    p = 0
    counter = 0
    while counter < 8:
        counter += 1
        #if the low bit of b is set
        if (b & 1) == 1:
            #xor the product with a
            p = p ^ a
        hi_bit_set = a & 0x80
        a = a << 1
        if hi_bit_set == 0x80:
            a = a ^ 0x1b
        b = b >> 1
    return p

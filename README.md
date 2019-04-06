# kry_AES - Melvin Johner
Python AES Key Schedule Implementation
##Expand Key
The expandKey in the key_schedule.py takes an int key with the Size of 128, 192 or 256 bit, the Number of key blocks, the the block size and the number of rounds as input.

Then it returns an array of words with the size of block size multiplied by the number of rounds plus 1. (Nb*(Nr+1))

This word array is called the expanded key and will used by the AES Encryption algroithm.

The implementation follows the this standatisation: [FIPS 197, Advanced Encryption Standard (AES) - NIST](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf)

##Tests
The unittests.py 
# kry_AES - Melvin Johner
Python AES Key Schedule Implementation
##Expand Key
The expandKey in the key_schedule.py takes an int key with the Size of 128, 192 or 256 bit, the Number of key blocks, the the block size and the number of rounds as input.

Then it returns an array of words with the size of block size multiplied by the number of rounds plus 1. (Nb*(Nr+1))

This word array is called the expanded key and will used by the AES Encryption algorithm.

The implementation follows the this standardisation: [FIPS 197, Advanced Encryption Standard (AES) - NIST](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf)

##Tests
The unittests.py tests the two edge cases for a 128 bit key: All bits are set to 1 and all bits are set to 0


##Known issues
1. The expandKey can only work for 128 bit keys. Because there was not enough time to apply the whole key splitting and word masking on bigger keys.
2. Some how the algorithm gets an overflow in the 36. Iteration. As example the word gets: 0x1ac7766f3 instead of 0xac7766f3. More debbuging will be required to find the failure.

from src.key_schedule import keyExpand

def main(key):
    '''
    Not working functionality for diffrent key sizes
    switcher = {
        128: keyExpand(key, 4, 4, 10),
        192: keyExpand(key, 6, 4, 12),
        265: keyExpand(key, 8, 4, 12),
    }

    expandFun = switcher.get(key.bit_length(), lambda: "Invalid key")
    expandedWords = expandFun()
'''
    expandedKey = keyExpand(key, 4, 4, 10)
    i = 0
    while i < len(expandedKey):
        print("Nr:" + str(i+1) + " " + hex(expandedKey[i]))
        i = i + 1

if __name__ == '__main__':
    main(0x2b_7e_15_16_28_ae_d2_a6_ab_f7_15_88_09_cf_4f_3c)

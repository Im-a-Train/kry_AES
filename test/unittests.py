import unittest
from src.key_schedule import keyExpand

class TestStringMethods(unittest.TestCase):

    def test_keyExpand_1(self):
        key = 0xff_ff_ff_ff_ff_ff_ff_ff_ff_ff_ff_ff_ff_ff_ff_ff
        result = [
            0xff_ff_ff_ff, 0xff_ff_ff_ff, 0xff_ff_ff_ff, 0xff_ff_ff_ff,
            0xe8_e9_e9_e9, 0x17_16_16_16, 0xe8_e9_e9_e9, 0x17_16_16_16,
            0xad_ae_ae_19, 0xba_b8_b8_0f, 0x52_51_51_e6, 0x45_47_47_f0,
            0x09_0e_22_77, 0xb3_b6_9a_78, 0xe1_e7_cb_9e, 0xa4_a0_8c_6e,
            0xe1_6a_bd_3e, 0x52_dc_27_46, 0xb3_3b_ec_d8, 0x17_9b_60_b6,
            0xe5_ba_f3_ce, 0xb7_66_d4_88, 0x04_5d_38_50, 0x13_c6_58_e6,
            0x71_d0_7d_b3, 0xc6_b6_a9_3b, 0xc2_eb_91_6b, 0xd1_2d_c9_8d,
            0xe9_0d_20_8d, 0x2f_bb_89_b6, 0xed_50_18_dd, 0x3c_7d_d1_50,
            0x96_33_73_66, 0xb9_88_fa_d0, 0x54_d8_e2_0d, 0x68_a5_33_5d,
            0x8b_f0_3f_23, 0x32_78_c5_f3, 0x66_a0_27_fe, 0x0e_05_14_a3,
            0xd6_0a_35_88, 0xe4_72_f0_7b, 0x82_d2_d7_85, 0x8c_d7_c3_26,
        ]
        self.assertEqual(keyExpand(key, 4, 4, 10), result)

    def test_keyExpand_2(self):
        key = 0x00_00_00_00_00_00_00_00_00_00_00_00_00_00_00_00
        result = [
            0x00_00_00_00, 0x00_00_00_00, 0x00_00_00_00, 0x00_00_00_00,
            0x62_63_63_63, 0x62_63_63_63, 0x62_63_63_63, 0x62_63_63_63,
            0x9b_98_98_c9, 0xf9_fb_fb_aa, 0x9b_98_98_c9, 0xf9_fb_fb_aa,
            0x90_97_34_50, 0x69_6c_cf_fa, 0xf2_f4_57_33, 0x0b_0f_ac_99,
            0xee_06_da_7b, 0x87_6a_15_81, 0x75_9e_42_b2, 0x7e_91_ee_2b,
            0x7f_2e_2b_88, 0xf8_44_3e_09, 0x8d_da_7c_bb, 0xf3_4b_92_90,
            0xec_61_4b_85, 0x14_25_75_8c, 0x99_ff_09_37, 0x6a_b4_9b_a7,
            0x21_75_17_87, 0x35_50_62_0b, 0xac_af_6b_3c, 0xc6_1b_f0_9b,
            0x0e_f9_03_33, 0x3b_a9_61_38, 0x97_06_0a_04, 0x51_1d_fa_9f,
            0xb1_d4_d8_e2, 0x8a_7d_b9_da, 0x1d_7b_b3_de, 0x4c_66_49_41,
            0xb4_ef_5b_cb, 0x3e_92_e2_11, 0x23_e9_51_cf, 0x6f_8f_18_8e
        ]
        self.assertEqual(keyExpand(key, 4, 4, 10), result)


if __name__ == '__main__':
    unittest.main()
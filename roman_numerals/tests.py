import unittest
from roman_numerals_converter import get_arabic_numeral

class TestTransformRomanNumerals(unittest.TestCase):

    def test_transfrom_from_roman_numerals(self):
        # Integer provided in Roman numeral gets transformed into Arabic numeral

        roman_per_arabic = {1000: 'M',
                           500: 'D',
                           100: 'C',
                           50: 'L',
                           10: 'X',
                           5: 'V',
                           1: 'I',
                           2: 'II',
                           100: 'LL',
                           900: 'CM',
                           1801: 'MDCCCI',
                           1988: 'MCMLXXXVIII',
                           1999: 'MCMXCIX',
                           2000: 'MM',
                           2013: 'MMXIII'
                           }


        for arabic in roman_per_arabic:
            output = get_arabic_numeral(roman_per_arabic[arabic])
            self.assertEqual(output, arabic)

        
    def test_transform_to_roman_numerals(self):
        output = ''
        self.assertEqual(output, 'I')

if __name__ == '__main__':
    unittest.main()
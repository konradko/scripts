import unittest
from roman_numerals_converter import RomanNumeralsConverter

class TestConvertRomanNumerals(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestConvertRomanNumerals, self).__init__(*args, **kwargs)
        
        self.arabic_to_roman = {1000: 'M',
                                500: 'D',
                                100: 'C',
                                50: 'L',
                                10: 'X',
                                5: 'V',
                                1: 'I',
                                2: 'II',
                                900: 'CM',
                                1801: 'MDCCCI',
                                1988: 'MCMLXXXVIII',
                                1999: 'MCMXCIX',
                                2000: 'MM',
                                2013: 'MMXIII',
                                3999: 'MMMCMXCIX'
                                }
    
    def setUp(self):
        self.converter = RomanNumeralsConverter()

    def test_transfrom_from_roman_numerals(self):
        # Integer provided in Roman numeral gets converted into Arabic numeral
        for arabic in self.arabic_to_roman:
            output = self.converter.get_arabic_numeral(self.arabic_to_roman[arabic])
            self.assertEqual(output, arabic)
        
    def test_transform_to_roman_numerals(self):
        # Integer provided in Arabic numeral gets converted into Roman numeral
        for arabic, roman in self.arabic_to_roman.iteritems():
            output = self.converter.get_roman_numeral(arabic)
            self.assertEqual(output, roman)

if __name__ == '__main__':
    unittest.main()
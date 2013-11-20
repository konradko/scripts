# Write a converter to and from Roman numerals.
# The script should read from files specified on the command-line and writing to STDOUT.
# Each line of input will contain one integer (between 1 and 3999) expressed as an Arabic or Roman 
# numeral.
# There should be one line of output for each line of input, containing the original number in the 
# opposite format.
class RomanNumeralsConverter:

    def __init__(self):
        self.roman_to_arabic = {'M': 1000,
                               'D': 500,
                               'C': 100,
                               'L': 50,
                               'X': 10,
                               'V': 5,
                               'I': 1}

    def arabic_to_roman(self, arabic):
        for roman in self.roman_to_arabic:
            if self.roman_to_arabic[roman] == arabic:
                return roman

    def get_next_symbol(self, roman_symbol):
        sorted_values = sorted(self.roman_to_arabic.values(), reverse=True)
        next_arabic = sorted_values[sorted_values.index(self.roman_to_arabic[roman_symbol]) - 1]
        return self.arabic_to_roman(next_arabic)


    def get_arabic_numeral(self, input_number):
        arabic_numeral = 0
        previous = 0
        for char in input_number:
            # if the symbol appears before a larger symbol it is substracted
            current = self.roman_to_arabic[char]
            if previous >= current:
                arabic_numeral += current
            # When a symbol appears after a larger symbol it is added
            else:
                arabic_numeral += current - previous * 2
            previous = current
        return arabic_numeral

    def substract_roman(self, roman_string):
        for roman in self.roman_to_arabic:
            four_in_row = 4 * roman
            if four_in_row in roman_string:
                symbol_to_the_left = roman_string[roman_string.find(four_in_row) - 1]
                next_symbol = self.get_next_symbol(roman)
                if self.roman_to_arabic[symbol_to_the_left] > self.roman_to_arabic[next_symbol]:
                    substracted = roman + next_symbol
                    roman_string = roman_string.replace(four_in_row, substracted)
                else:
                    substracted = roman + self.get_next_symbol(next_symbol)
                    roman_string = roman_string.replace(next_symbol + four_in_row, substracted)
        return roman_string

    def get_roman_numeral(self, arabic_number):
        roman_string = ''
        for arabic in sorted(self.roman_to_arabic.values(), reverse=True):
            while arabic_number >= arabic:
                arabic_number -= arabic
                roman_string += self.arabic_to_roman(arabic)
        return self.substract_roman(roman_string)

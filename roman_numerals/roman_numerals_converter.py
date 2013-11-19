# Write a converter to and from Roman numerals.
# The script should read from files specified on the command-line and writing to STDOUT.
# Each line of input will contain one integer (between 1 and 3999) expressed as an Arabic or Roman 
# numeral.
# There should be one line of output for each line of input, containing the original number in the 
# opposite format.


def get_broken_int(number):
    b1 = number % 10
    b2 = (number % 100) / 10 * 10
    b3 = (number % 1000) / 100 * 100
    b4 = (number % 10000) / 1000 * 1000
    return [b4, b3, b2, b1]

def get_arabic_numeral(input_number):
    arabic_numeral = 0
    if not isinstance(input_number, int):
        previous = 0
        for char in input_number:
            # if the symbol appears before a larger symbol it is subtracted
            current = mapping[char]

            if previous >= current:
                arabic_numeral += current
            else:
                arabic_numeral += current - previous * 2

            previous = current

        return arabic_numeral

mapping = {'M': 1000,
           'D': 500,
           'C': 100,
           'L': 50,
           'X': 10,
           'V': 5,
           'I': 1}
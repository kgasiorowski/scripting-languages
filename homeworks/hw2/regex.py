import re


def part1():

    print('PART 1\n')
    pattern = r'[^O]*o+'
    tests = [r'balloons', r'FOODY', r'bookstore', r'"Look"', r'PoolRoOM']

    results = [(string, re.match(pattern, string)) for string in tests]

    for string, result in results:
        print(string + ' : ' + str(result))

    return results


def part2():

    print('\nPART 2\n')
    yearpattern = r'((19|20)[0-9]{2})'  # This will match a four digit number between 1900-2099
    month_case_1 = r'(0[13578]|10|12)/(([0][1-9])|([12][0-9])|(3[01]))'  # Provides support for months with 31 days
    month_case_2 = r'(0[469]|11)/((0[1-9])|([12][0-9])|30)'  # Provides support for months with 30 days
    month_case_3 = r'(02/(([0][1-9])|(1[0-9])|(2[0-8])))'  # FEBRUARY

    finalpattern = '(' + month_case_1 + '|' + month_case_2 + '|' + month_case_3 + ')/' + yearpattern

    print(finalpattern)
    return finalpattern


def part3():

    print('\nPART 3\n')
    pattern = r'\d*[02468]-\d{3}-\d*[13579]'
    print(pattern)
    return pattern


def part4():

    print('\nPART 4\n')
    range_pattern = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    pattern = range_pattern + '(\.' + range_pattern + r'){3}(\b|$)'
    print(pattern)
    return pattern


def part5():

    print('\nPART 5\n')
    print("""
    
a) Simply matches any string between two double quotes.
The following strings will match:

""
"a"
"This is a sample string"
"This is also" a sample string" 
(^- This one will also match, but not the whole string, only from index 0 to 13)


b) From left to right:
First, match an optional +/- sign.
Then, match any number of digits greater than 0.
Then, match an option decimal sign, with any number of digits after it.
Then, match a capital F.
Then, match a word boundary.

This basically matches a custom number format (maybe fahrenheit or something)

Example patterns that match:
-34F
+34.F
34.34F
34F
-34F

c) First, match a sequence of AT LEAST two non-digit characters. This is out first capturing group.
Then, match any number of any characters.
Then, match a [.
Then, match the same sequence as the first capturing group.
Then, match a ].

Example patterns that match:

this is a sample string[this]
this is a sample string[this is]
this[this]

These, however, won't match:

this is a sample string[thisA]
t[t]
th[t]

d) First, match a sequence of any characters with any length (0-infinity) (Second capture group)
Then match exactly one digit. (First capture group)
Then match exactly one whitespace character.
Then match the same sequence as the second capture group.

Strings that will match:

asdf1 asdf
a1 a
1 (just a single digit and a whitespace after it

e) First, match the beginning of the entire string.
Then, match any number of digits greater than 0.
Then, match a /.
Then, match another sequence of digits with length >= 1.
Now we have two alternatives:
    Match one of the arithmetic symbols [+-/*] and an equals sign right after.
    Match one of the following: ++ or --
Finally, match a semicolon and then the end of the entire string.

Strings that'll match ([] denote the starts and ends of strings):

[1/1++;]
[1234/1234--;]
[1234/1234*=;]
[12/12+=;]
    """)


if __name__ == "__main__":

    part1()
    part2()
    part3()
    part4()
    part5()

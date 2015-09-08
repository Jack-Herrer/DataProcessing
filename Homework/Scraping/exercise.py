# Name : Michiel van der List   
# Student number : 10363521
'''
This module contains an implementation of split_string.
'''

# You are not allowed to use the standard string.split() function, use of the
# regular expression module, however, is allowed.
# To test your implementation use the test-exercise.py script.

# A note about the proper programming style in Python:
#
# Python uses indentation to define blocks and thus is sensitive to the
# whitespace you use. It is convention to use 4 spaces to indent your
# code. Never, ever mix tabs and spaces - that is a source of bugs and
# failures in Python programs.


def split_string(source, separators):
    '''
    Split a string <source> on any of the characters in <separators>.

    The ouput of this function should be a list of strings split at the
    positions of each of the separator characters.
    '''
    # PROVIDE YOUR IMPLEMENTATION HERE

    output = []
    string = ''
    previous = ''
    if source == '':
        return output

    # Iterate individual elements of source
    for letter in source:

        # append letters to string if previous is not in separators
        if letter not in separators:
            if previous not in separators:
                string += letter

            # Make new element in list before appending if previous is separator
            else:
                if string != '':
                    output.append(string)
                string = letter

        # Keep track of previous                        
        previous = letter

    # Append last letter and return    
    output.append(string)    
    return output

if __name__ == '__main__':
    # You can try to run your implementation here, that will not affect the
    # automated tests.
    print split_string('abaccaddddabra', 'ba')  # should print: ['cc', 'dddd', 'r']

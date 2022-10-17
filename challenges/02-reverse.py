# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

should_run = True

while should_run:
    print('provide a word to have the magic happen:')
    string = input()

    if string == 'q':
            should_run = False
            
    new_string = ''

    for char in string:
        new_string = char + new_string
    print(new_string)
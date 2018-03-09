"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think this will add values in to list
some_words = ['what', 'does', 'this', 'line', 'do', '?']
# I think it would give syntax error.
for word in some_words:
    print(word) # It printed 'what' which is the first word of the list, repeated the steps with following words from the list. Seems like word is representing the strings in general.
# I think it would give syntax error?
for x in some_words:
    print(x)    # Well it did the same thing with obove line. Seems like x represents the variables?
# It will print like this, ['what', 'dose', 'this', 'line', 'do', '?']
print(some_words)   #It printed that way.
# In the list of some_words, there are 6 of components. The number is greater than 3 so it will print 'some_words contains more than 3 words'.
if len(some_words) > 3:
    print('some_words contains more than 3 words')  #It did!

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()

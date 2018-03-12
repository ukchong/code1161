

"""Make 10 stars.
    Using a for loop
    return a list of 10 items, each one a string with exacly one star in it.
    E.g.: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    """

def loops_1a():
    list=[]
    i=0
    for i in range(0, 10):
        i+=1
        list.append("'*'" + " ")

    return list

def fix_it(moves=True, should_move=True):
    """Decide what to do.

    Using the engineering flowchart (in week2 folder engineeringFlowchart.png)
    for the rules, return the apropriate response to the input parameters.
    Use conditional statements: if, else, elif etc.
    This function should return either:
    "WD-40"
    "Duct Tape"
    "No Problem"
    """

    if moves:
        if should_move:
            return "No Problem"
        else:
            return "Duct Tape"
    else:
        if should_move:
            return "WD-40"
        else:
            return "No Problem"

def loops_1c(number_of_items=5, symbol="#"):
    list=[]
    i=0
    for i in range(0, int(number_of_items+1)):
        i +=1
        list.append(symbol+" ")
    
    return list


"""Respond to variables.

    using any method
    return a list of number_of_items items, each one
    a string with exacly one symbol in it.
    E.g.: ['#', '#', '#', '#', '#']
    """

    
    #pass

def loops_2():
    """Make a big square starfield.

    return a list of 10 items, each one a list of 10 items,
    each one of those, a string with exacly one star in it.
    E.g.: [
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
          ]
    """
    list1=[]
    i=0
    for i in range(0, 10):
        i+=1
        list1.append("'*'" + " ")
    list2 = []
    x=0
    for x in range(0, 10):
        x+=1
        list2.append(list1)
    return list2
    
    #pass


def lp(some_kind_of_list, exercise_name):
    """Help to see what's going on.

    This is a helper function that prints your
    results to check that they are tidy.
    Note: You don't have to do anything with it.
    """
    if some_kind_of_list is not None:
        print("\n" + exercise_name)
        if type(some_kind_of_list[0]) is list:
            for row in some_kind_of_list:
                for column in row:
                    print(column, end="")
                print()
        else:
            for column in some_kind_of_list:
                print(column, end="")
            print()
    else:
        print(exercise_name, "maybe you haven't got to this one yet?")


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    #print(is_odd(1), "is_odd odd")
    #print(is_odd(4), "is_odd even")
    print(fix_it(True, True))
    print(fix_it(True, False))
    print(fix_it(False, True))
    print(fix_it(False, False))
    lp(loops_1a(), "loops_1a")
    lp(loops_1c(4, "×°×"), "loops_1c")
    lp(loops_2(), "loops_2")
    #lp(loops_3(), "loops_3")
    #lp(loops_4(), "loops_4")
    #lp(loops_5(), "loops_5")
    #lp(loops_6(), "loops_6")
    #lp(loops_7(), "loops_7")

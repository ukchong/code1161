# -*- coding: UTF-8 -*-
"""Modify each function until the tests pass."""


def is_odd(a_number):
    """Return True if a_number is odd, and False if a_number is even.

    Look into modulo division using the '%' operator as one way of doing this.
    """
    """integer = 100"""

    if a_number % 2 != 0:
        #divide a_number by two and results to be pended by two factors. integer or rest.
        #Need to define integer. I can define the integer and set its neumerical identitiy by stating "integer = 100". 
        # I would state "float = 1000.0" if I need to define float 
        # but it is not necessary in this case as I only need to consider "one or the rest" scenario.
        return "True"
    else:
        return "False"

def fix_it(moves=True, should_move=True):
    # if moves:
    #     if should_move:
    #         return "No Problem"
    #     else:
    #         return "Duct Tape"
    # elif should_move:
    #         return "WD-40"
    #     else:
    #         return "No Problem"
    
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
    elif should_move:
            return "WD-40"
    else:
            return "No Problem"


def loops_1a():
    list1a = []
    for i in range (10):
        list1a.append('*')
    return list1a
    
    
    

    """ 
    ls()
    x = 0
    for x in range (0, 10):
        ls() = list.append(x)
        x += 1
    return ls(x)
    print ls(x)
    """


"""Make 10 stars.
    Using a for loop
    return a list of 10 items, each one a string with exacly one star in it.
    E.g.: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    """


    # pass



def loops_1c(number_of_items=5, symbol="#"):
    list1c=[]
    
    for i in range(int(number_of_items)):
        list1c.append(symbol)
    return list1c
    

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
    list2 = []
    for a in range(10):
        temp_list2 = []
        for b in range(10):
            temp_list2.append('*')
        list2.append(temp_list2)
    return list2
    # list1=[]
    # for i in range(10):
    #     list1.append("*")
    # list2 = []
    # for x in range(10):
    #     list2.append(list1)
    # return list2
    #pass


def loops_3():
    """Make a rising block of numbers.

    Return this:
    [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
        ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3'],
        ['4', '4', '4', '4', '4', '4', '4', '4', '4', '4'],
        ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
        ['6', '6', '6', '6', '6', '6', '6', '6', '6', '6'],
        ['7', '7', '7', '7', '7', '7', '7', '7', '7', '7'],
        ['8', '8', '8', '8', '8', '8', '8', '8', '8', '8'],
        ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9']
    ]
    remember that range(10) produces a list of numbers from 0...9
    So for every step produced by `for i in range(10):` i is a different number
    TIP: notice that this needs to to return strings of numbers,
         so call str(number) to cast.
    """

    list3 = []
    for c in range(10):
        temp_list3 =[]
        for d in range(10):
            temp_list3.append(str(c))
        list3.append(temp_list3)
    return list3



#     myReturnList = []
#     for counter in range(10):
#         tempList=[]
#         for i in range(10):
#             tempList.append(str(counter))
#         myReturnList.append(tempList)
#     return myReturnList
#     #pass


def loops_4():
    """Make a block of numbers that rises left to right.

    Return this:
    [
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    """
    list4 = []
    for k in range(10):
        temp_list4 = []
        for q in range(10):
            temp_list4.append(str(q))
        list4.append(temp_list4)
    return list4

#     list1=[]
#     i=0
#     for i in range(0, 10):
#         list1.append(str(i))
#     list2 = []
#     for x in range(0, 10):
#         list2.append(list1)
#     return list2
#     #pass


def loops_5():
    """Make the coordinates of the block.
    
#     Return this:
#     [
#       ['(i0, j0)', '(i0, j1)', '(i0, j2)', '(i0, j3)', '(i0, j4)'],
#       ['(i1, j0)', '(i1, j1)', '(i1, j2)', '(i1, j3)', '(i1, j4)'],
#       ['(i2, j0)', '(i2, j1)', '(i2, j2)', '(i2, j3)', '(i2, j4)'],
#       ['(i3, j0)', '(i3, j1)', '(i3, j2)', '(i3, j3)', '(i3, j4)'],
#       ['(i4, j0)', '(i4, j1)', '(i4, j2)', '(i4, j3)', '(i4, j4)'],
#       ['(i5, j0)', '(i5, j1)', '(i5, j2)', '(i5, j3)', '(i5, j4)'],
#       ['(i6, j0)', '(i6, j1)', '(i6, j2)', '(i6, j3)', '(i6, j4)'],
#       ['(i7, j0)', '(i7, j1)', '(i7, j2)', '(i7, j3)', '(i7, j4)'],
#       ['(i8, j0)', '(i8, j1)', '(i8, j2)', '(i8, j3)', '(i8, j4)'],
#       ['(i9, j0)', '(i9, j1)', '(i9, j2)', '(i9, j3)', '(i9, j4)']
#     ]
#     you can construct strings either by concatinating them:
#         "There are " + str(8) + " green bottles"
#     or by using format:
#         "There are {} green bottles".format(8)
#     you'll come to see the pros and cons of each over time.
#     """

    list5 = []
    for i in range(10):
        temp_list5 = []
        for j in range(5):
            coord_i = 'i' + str(i)
            coord_j = 'j' + str(j)
            coord = '(' + coord_i + ', ' + coord_j + ')'
            temp_list5.append(coord)
        list5.append(temp_list5)
    # for a in range (10):
    #     smallList5=[]
    #     for b in range (5):
    #         coord = '(' + 'i' + str(a) + ', ' + 'j'+ str(b) + ')'
    #         smallList5.append(coord)
    #     list5.append(smallList5)
    return list5

    # square = []
    # for i in range(10):
    #     stars = []
    #     for j in range(5):
    #         coord_i = 'i' + str(i)
    #         coord_j = 'j' + str(j)
    #         coord = '(' + coord_i + ', ' + coord_j + ')'
    #         stars.append(coord)
    #     square.append(stars)
    # return square

    # bigList =[]
    # for x in range(10):
    #     smallList=[]
    #     for y in range(5):
    #         appendTo = (i + str(x) + ", j" + str(y)
    #         smallList.append(appendTo)
    #     bigList.append(smallList)
    # return bigList

#     my_return_list=[]
#     for counter in range(10):
#         my_temp_list=[]
#         for counter2 in range(5):
#             to_append = ((i = "str(counter) + ", j" + str(counter2) + "))
#             my_temp_list.append(to_append)
#         print(to_append)
#         return my_return_list.append(my_temp_list)    
#     #pass



def loops_6():
    """Make a wedge of numbers.

    Return this:
    [
      ['0'],
      ['0', '1'],
      ['0', '1', '2'],
      ['0', '1', '2', '3'],
      ['0', '1', '2', '3', '4'],
      ['0', '1', '2', '3', '4', '5'],
      ['0', '1', '2', '3', '4', '5', '6'],
      ['0', '1', '2', '3', '4', '5', '6', '7'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    you don't have to use a literal number in the range function.
    You can use a variable.
    TIP: look out for the starting condition.
    """
    list6 = []
    # for row in range(10):
    #     temp_list6 = []
    #     for column in range(row + 1):
    #         temp_list6.append(str(column))
    #     list6.append(temp_list6)
    for a in range (10):
        smallList6 = []
        for b in range (a+1):
            smallList6.append((str(b)))
        list6.append(smallList6)
    return list6







    # list6 = []
    # for row in range(10):
    #     temp_list6 = []
    #     for height in range(row + 1):
    #         temp_list6.append(str(height))
    #     list6.append(temp_list6)
    # return list6

    # list6 = []
    # for s in range(-1,9):
    #     temp_list6 = []
    #     temp_list6.append(micro_temp_list6)
    #     for t += 1:
    #         micro_temp_list6 = []
    #         micro_temp_list6.append(str(t))
    #     list6.append(temp_list6)
    # return list6

    #pass


def loops_7():
    """Make a pyramid.

    Return this:
    [
        [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', ' ', ' '],
        [' ', '*', '*', '*', '*', '*', '*', '*', ' '],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    ]
    or in more simple terms:
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    (this is what will print when you test from inside this file)
    This is a hard problem. Use lots of experimentation and draw
    lots of diagrams!
    """

    list7 = []
    height=5
    width=9
    for a in range (height):
        smallList7 = []
        for b in range (width):
            smallList7.append('*')
        left = int((width/2) - a)
        right = int((width+1)/2 + a)
        for c in range (left):
            smallList7[c] = " "
        for c in range (right, width):
            smallList7[c] = " "
        list7.append(smallList7)

    # width =9
    # height =5
    # for i in range(height):
    #     row = []
    #     for k in range(width):
    #         row.append("*")
    #     leftSpace = int((width-1)/2-i)
    #     rightSpace = int((width+1)/2+i)
    #     for p in range(leftSpace):
    #         row[p] = " "
    #     for p in range(rightSpace, width):
    #         row[p] = " "
    #     list7.append(row)
    return list7
#     pass


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
    # print(is_odd(1), "is_odd odd")
    # print(is_odd(4), "is_odd even")
    # print(fix_it(True, True))
    # print(fix_it(True, False))
    # print(fix_it(False, True))
    # print(fix_it(False, False))
    # lp(loops_1a(), "loops_1a")
    # lp(loops_1c(4, "×°×"), "loops_1c")
    # lp(loops_2(), "loops_2")
    lp(loops_3(), "loops_3")
    lp(loops_4(), "loops_4")
    lp(loops_5(), "loops_5")
    lp(loops_6(), "loops_6")
    lp(loops_7(), "loops_7")

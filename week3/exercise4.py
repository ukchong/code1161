# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    Each guess, print what the guess is Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    This will be quite hard, especially hard if you don't have a good diagram!

    Debugging helpers:
      * GUARD is there to make it only run a few times so that you can see
        what's happening.
      * time.sleep(0.5) makes it pause for half a second.
      You don't need to use both together, and should remove them both before
      you submit. The tests will be checking that they aren't in there.
      (You should remove them from the file, not comment them out, the
      tests aren't that smart yet.)
    """

    d = {"guess": [], "tries": 0}   #d는 딕셔너리고 안에 게스와 트라이스 리스트가 있다.
    current = int(high/2)           #current는 주어진 height을 2로 나눈 값
    current_high = high             #current height는 height
    current_low = low               #Current low는 low
    while current != actual_number:     #current가 actual_number가 아닐때
        if actual_number < current:     #만약 actual이 current보다 작아?
            current_high = current      #current height에 current값을 준다
            current = int((current_high + current_low)/2)   #current는 current height과 current low를 더해서 2로 나눈 값이 된다.
        elif actual_number > current:   #만약 actual이 current보다 커?
            current_low = current       #current low에 current값을 준다
            current = int((current_high + current_low)/2)   #current는 current height과 current low를 더해서 2로 나눈 값이 된다.
        d["guess"].append(current)      #d의 게스 리스트값에 current를 append한다
        d["tries"] += 1                 #d의 tries 리스트값이 1씩 오른다
    return d                            #d 를 보여줘.


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))

def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    myList = []
    for i in range (start, stop, step):
        myList.append(str(i))
    return myList


if __name__ == "__main__":
    print(loop_ranger(2, 10, 2))
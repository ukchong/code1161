TODO: Reflect on what you learned this week and what is still unclear.
Exercise 1
    So I have passed exercise1.py today, but I do not think I got clear understand of codes that I wrote.
        For example: stubborn asker function runs the loop without "try:" argument and "continue, break" statements
        However, Not number rejector function and super_asker function could not run into loop without those argument and statements.
        The only assumption that I can make between these functions is -
        You must use "try:" argument in conjunction with "except" "continue" "break" condition.

        From my investigation:
        
        If you use #1
        while True:
            if
            elif
            else
            return
        "YOU DO NOT NEED TO USE CONTINUE/BREAK, THEY WILL GO INTO LOOP BUT YOU CANNOT CONSTRAIN TYPE OF INPUT"

        If you use #2
        while True:
            try:
            except:
                continue
            else:
                if:
                    continue
                elif:
                    continue
                else:
                    return
                break
        "YOU HAVE TO USE TRY: ARGUEMENT TO USE EXCEPT: AND CONTINUE/BREAK STATEMENTS"
Exercise 2
    This function gives me an error when I have assigned -5 or x into upperbound.
    We need to restrain users to input valid value and type
    Having negative value or bigger value which exceed the upperbound are accepted but strings cannot be tolerated by Valueerror
    Function needs to restrain users to input valid type
    ? What is the definition of ".format()"
    ? What does {} do in the string? - within ".format()" at suffix


Exercise 3

Exercise 4
    Scenario
        If False: Count the number (i+=)
        If True: Break out of loof
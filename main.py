from patterns import Patterns

# review: you can use python's argparse to create beautiful help menus
# http://docs.python.org/dev/library/argparse.html
def print_menu():

    # review: prints don't need paranthesis. A more pythonic/minimalistic approach is this syntax:
    #   print "Welcome to Game of Life"
    print('Welcome to Game of life') 
    print('------------------------')
    print("Please Enter the number of the pattern that you want")
    print("1. Blinker")
    print("2. Toad")
    print("3. Beacon")

if __name__ == '__main__':

    # review: usually it's wise to use wrap only the minimal amount of code in a try-catch block
    # see Programming Recommendations under PEP-8
    # http://www.python.org/dev/peps/pep-0008/#programming-recommendations
    # however, your usage may force a very broad try-catch due to the fact that you catch keyboard interruptions
    try:
        print_menu()
        choice = raw_input()

        # review: I'd probably cast the choice into an int and check the `if` statement against the singleton value of the int. This is a bit more consistent with PEP 8
        # http://www.python.org/dev/peps/pep-0008/#programming-recommendations
        # For example
        #   choice = int( choice )
        #   if choice is 1:
        #       ...
        #   

        # review: consider moving this logic to a more generic method that will allow running the game separately from the `main` block
        # (for example via the interteractive shell)
        if (choice == '1'): 
            Patterns.blinker().draw_matrix_forever()
        elif (choice == '2'):
            Patterns.toad().draw_matrix_forever()
        elif (choice == '3'):
            Patterns.beacon().draw_matrix_forever()
        else:

            # review: consider re-using this block of code to a separate method as it's used in the `catch` block as well
            print('bye...')

            # review: you didn't import sys, interrupting causes an error:
            #   NameError: name 'sys' is not defined
            sys.exit()

    except KeyboardInterrupt:

        # review: not sure if this is really needed, as you don't do any resource cleanups here, so maybe it's best to just
        # let the exception propogate. Not sure.
        print('bye...')
        sys.exit()


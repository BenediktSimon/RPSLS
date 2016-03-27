# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

#import

numb

# helper functions
def name_to_number(name):

    number = None
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print("%s is not defined please choose: rock, Spock, paper, lizard or scissors" %name)
    return (number)


def number_to_name(number):
    name = None
    if number == "0":
        name = "rock"
    elif number == "1":
        name = "Spock"
    elif number == "2":
        name = "paper"
    elif number == "3":
        name = "lizard"
    elif number == "4":
        name = "scissors"
    return (name)


def rpsls(player_choice):

    from random import randrange
    # print out the message for the player's choice
    print 'Player choose', player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(str(comp_number))

    # print out the message for computer's choice
    print 'Computer choose', comp_choice

    # compute difference of comp_number and player_number modulo five
    diff = (player_number - comp_number) % 5

    # use if/elif/else to determine winner, print winner message
    if diff == 1 or diff == 2:
        print "Player wins!"

    elif diff == 3 or diff == 4:
        print "Computer wins"

    else:
        print "Player and Computer tie!"
    print 
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

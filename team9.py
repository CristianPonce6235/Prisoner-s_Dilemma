from __future__ import print_function
import random

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: Trust points algorithm
#     strategy_description: Assigns trust points to make decisions off of
#     move: A function that returns 'c' or 'b'
####

team_name = 'OscarPonce' # Only 10 chars displayed.
strategy_name = 'Trust Move'
strategy_description = """Assigns variable to keep track of trust and makes 
decisions based off of that"""

# Trust move algortihm that determines based off of variable
def trustmove(their_history):
    points = 100 # Assigned to 100
    their_history = 'b' #Assigned as betray
    if their_history == 'b': #Tells program what to do if betray
        points -= 20
        if points > 100:
            return 'c'
        if points < 100 or points == 100:
            return 'b'
    if their_history == 'c': #Tells program what to do if collude
        points += 10
        if points > 100:
            return 'c'
        if points < 100 or points == 100:
            return 'b'

# Most-recent algorithm, will only make a decision based on the other prisoner's previous move
def move2(my_history, their_history, my_score, their_score):
    if their_history[-1]=='c':
        return 'b' # betray if they colluded on the last turn
    if their_history[-1]=='c':
        return 'c' # collude if they betrayed on the last turn

# Points to possibility algorithm, will add or decuct points from the possibility to collude based on other player's choice
def move3(my_history, their_history, my_score, their_score, n):
    n = 100 # initial range
    n1 = random.randint(0, n) # range changes based on betrayals and collusions
    if n1 > 50:
        return 'c'
    if n1 < 50:
        if their_history[-1]=='c':
            n = n + 10 # add points to possibility to collude
        if their_history[-1]=='b':
            n = n - 10 # deduct points from possibility to collude
    

def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             
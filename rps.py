# Rock Paper Scissors

# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

def rps(p1, p2):
    p1 =['rock', 'scissors', 'paper'] 
    p2 = ['paper', 'scissors', 'paper']
    if p1 > p2:
        return'Player 1 won'
    elif p2 > p1:
        return 'Player 2 won'
    else:
        return 'Draw!'

print(rps('rock', 'scissors'))
import random
# this is a placeholder list of players to test the code. The real program should start with
# random ranks, and then use a database to permanently store data 
players = [['Daisy', 4], ['Mickey', 2], ['Minnie', 1], ['Donald', 8], ['Garfield', 7], ['Sailor', 5], ['Darkwing', 3], ['Goofy', 6]]   

# this is just so that I can easily test my code. I wonder if there is a unique identifier I could use in a database to replace this?
Daisy = players[0]
Mickey = players[1]
Donald = players[2]
Garfield = players[3]
Sailor = players[4]
Darkwing = players[5]
Goofy = players[6]



def populatePlayers():
    ''' user should be able to enter a list of players, one by one.
    Once submitting all players, it will randomly assign ranks. This will likely be run once a year (or the first time the program is run)
    The players list should look like this once finished: players = [['name', rank], ['name2', rank]] '''
    c = 'y'
    list = []
    while c != 'n':
        name = input('enter player name: \n')
        list.append(name)
        c = input('continue? (y/n) \n')
    print(list)
    ranks = []
    length = len(list)
    for i in range(1, length + 1):
        ranks.append(i)
    random.shuffle(ranks)
    print(ranks)
    for i in range(len(list)):
        players.append([list[i], ranks[i]]) 
    print(players)
    return players

def canTheyPlay(user1, user2):
    ''' players can only challenge a player who is 1, 2, 3, or 4 ranks above them.'''

    if (user1[1] - user2[1]) > 4 or (user1[1] - user2[1] < -4):
        return False
    else:
        return True


def updateRanks(winner, loser):
    ''' if rank of winner is greater than loser, do nothing.
    If rank of winner is less than loser, than winner replaces loser and all other misplaced scores move down.
    If there is a draw, lower ranked player moves one rank below winner. All other misplaced scores move down.'''
    print(winner, loser)
    print(winner[1], loser[1])
    if winner[1] > loser[1]:
        print('no change - winner ranked higher')
    else:
        print('need to update ranks - loser ranked higher')
        for player in players:
            for rank in range(len(players)):
                if players[rank][1] == (winner[1] + 1):
                    players[rank][1] = winner[1]
                    winner[1] = winner[1] + 1
                    if winner[1] > loser[1]:
                        return players


def updateRanksDraw(user1, user2):
    '''if there is a draw, lower ranked player moves one rank below winner. All other misplaced scores move down.'''
    # work out which player is ranked lower
    if user1[1] < user2[1]:
        lowestRank = user1
        highestRank = user2
    else:
        lowestRank = user2
        highestRank = user1
    for player in players:
        for rank in range(len(players)):
            if players[rank][1]==lowestRank[1] + 1:
                players[rank][1] = lowestRank[1]
                lowestRank[1] = lowestRank[1] + 1
                if lowestRank[1] == highestRank[1] - 1:
                    return players

def play():
    # who is playing
    # how do we create a user interface that allows our user to only select names that are already in our database?
    player1 = input("who is player 1? ")
    for player in players:
        if player[0] == player1:
            player1 = player
    player2 = input("who is player 2? ")
    for player in players:
        if player[0] == player2:
            player2 = player

    if canTheyPlay(player1, player2) == True:
        print('This game is allowed. Enjoy your game!')
        # who won?
        winner = input("Enter the name of the player who won, or press 'd' for a draw \n")
        if winner == 'd':
            updateRanksDraw(player1, player2)
            print('Congratulations. Ranks have been updated.')
        else:
            if winner == player1[0]:
                winner = player1
                loser = player2
            else:
                winner = player2
                loser = player1
            updateRanks(winner, loser)
            print('Congratulations. Ranks updated.')
    else:
        print('This game is not allowed. Please choose a player closer in rank to you.')


play()
print(players)
# chessLadder
A chess ladder is an ongoing ranking of chess players so that they can be paired up with opponents of similar ability.
## RULES
A player may challenge another player who is 1, 2, 3, or 4 ranks above him/her
If there is sufficient time to play, the challenged player MUST play, or they will be recorded as the loser of the game.

- If the lower-ranked player wins, they take the spot of the higher ranked player and the higher-ranked player moves down by one rank
- If the lower-ranked player loses, nothing changes to the ranks as the higher-ranked player will keep their score.
- If there is a draw, the lower-ranked player moves to one rank below the higher-ranked player. 

# Technical proposal
You must create a graphical user interface that will store the player usernames and rankings
**This application should:**
- allow the administrator to set up the initial usernames on the initiation of the ladder. Rankings should be assigned randomly in this instance. 
- check to see whether or not a game is allowed (based on how many ranks are between competitors)
- record the winner and loser of a game, which will allow it to update the rankings accordingly
- update the players' rankings on the event of a draw
- allow players to interact with the application via an easy-to-use graphical user interface (GUI)

## What you need to do
- You will need to add a permanent storage solution for the ranks so that we can close the program and reopen it without having to worry about the usernames or ranks being deleted
- Create a setup file that will be run by the administrator when setting up the ladder for the first time. This will create the sqlite database with the player table.
- Allow the administrator to add all usernames to the database for the first time using. Your program should randomly assign ranks to all users. 
- Adjust the main.py program so that any time a rank is changed, the database is updated. 
- Thoroughly test your code
- Design a user-interface with PySimpleGUI that is simple for the administrator and players to use. (Please make this as simple and intuitive for your user as possible)

## How to start
- You have been given some distribution code. Read this!
- Highlight the functions and annotate with their purpose.
- Draw a flowchart or sketch that shows how the database will be updated. 
- Draw a mockup/wireframe of your GUI
- Create a paper prototype of your GUI using the wireframes you created. Test your paper prototype on several test cases to see how it works. Ask your parents or other students (ideally those who are not in your DT class) to test it to see if they understand how it works without you needing to explain. 
- create the required database table(s)
- add the test data (insert)
- modify the code for SQL
- create the user interface
- evaluate your solution with regards to useability, efficiency of code, maintainability




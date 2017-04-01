# FIFA
simple app to create FIFA tournaments with friends


=============
enter results
=============

player1 name: 
player2 name:
goals player 1: 
goals player 2:
team player 1:
team player 2:
date by defualt: 
tournament name:


======
LEAGUE
======

tournament name: friends fifa night
tournament type: league
no of players: 5
players:
games against each player: 3



table - frinens fifa night
-----

name  played   won  draw   lost   points  goals  home_goals away_goals
-----------------------------------------------------------------------

pra   12       9    1      2      28      28       18        10
san   11       10   1      0      31      24       11        13


when all players finish (no of players -1 * games against each player) games, first compare points 
if points tie, compare goals, if goals tie, compare away goals, if away goals tie, compare home goals, if everything fails, declare multiple winners


+ click to see summary

===========
GROUP GAMES
===========

no of groups for now, restricted to 2

tournament name: east vs west
tournament type: group
no of players per group: 3
players in group 1:
players in group 2: 
games against each player: 3

group  played   won  draw   lost   points  goals  home_goals away_goals
-----------------------------------------------------------------------

east   12       9    1      2      28      28       18        10
west   11       10   1      0      31      24       11        13

name  played   won  draw   lost   points  goals  home_goals away_goals  group
-------------------------------------------------------------------------------

pra   12       9    1      2      28      28       18        10         east
sra   11       10   1      0      31      24       11        13         west

+ click to see summary


=============
SUMMARY TABLE
=============

Summary table for all tournaments

DATE PLAYER1  PLAYER2  TEAM1  TEAM2  GOALS  WINNER
--------------------------------------------------
APR1  PRA      SAN      RM     LIV   3-5    SAN









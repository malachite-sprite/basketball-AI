basketball-ai:

This is a first time attempt to use machine learning. The idea is to simulate a game similar to basketball with players that individually learn how to play.

files:

README.md
Position.py
Pattern.py
PAR.py
board.txt

overview of players:

Players can, at any time when they have the ball, perform one of the following actions:
 -move up/down/left/right (I'm assuming a grid based court, for simplicity)
 -shoot
 -hold (position)

Players on offense without the ball cannot shot (for obvious reasons), but can request the ball from the player with the ball. For simplicity, a request for the ball cannot be denied and will result in a pass from the player with the ball.

Players on defense can neither shoot nor request a pass, but they automatically "jump" in attempt to intercept a pass near them (in their square or an adjacent square), as well as attempt to steal the ball from someone moving next to them.

Each player will have a list of different pattern-action-result triplets (PAR) that act like memories.
 -A pattern consists of the positions of each player on the court, as well as a tolerance of variance for each player (in what area they can be, basically)

 -An result could be (in order from best to worst):
   4	-team basket
   3	-assist? (to implemented later)
   2	-intercepted enemy basket
   1	-successful pass
   0	-neutral
  -1	-missed basket
  -2	-stolen
  -3 	-intercepted team basket
  -4	-enemy basket
  
 -Each PAR would have an result number. The result number is the expected success level of the action in that pattern. Although the action could be shooting (which by the above table could only result in a 4, -1, or -3 result), the result number could be a 2.5 because of the probability of success. Results could possibly be greater than a 4, if they repeatedly succeed, but hopefully game balancing would prevent this from happening (it would be a broken game that had a strategy that succeeded so easily). 

 -Each time step, a player would compare the current game's pattern to their list of PAR triplets. If a PAR pattern would match the current game's pattern, then the player would take the action dictated by the PAR. If the result returns as expected, then the result number would be adjusted positively. If the result returns against the expected, then the tolerances, positions, or result number will be adjusted.

 
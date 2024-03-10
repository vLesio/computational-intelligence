from copy import deepcopy
import random
from easyAI import TwoPlayerGame
import time



class Nim(TwoPlayerGame):
    """
    The game starts with 4 piles of 5 pieces. In turn the players
    remove as much pieces as they want, but from one pile only. The
    player that removes the last piece loses.

    Parameters
    ----------

    players
      List of the two players e.g. [HumanPlayer(), HumanPlayer()]

    piles:
      The piles the game starts with. With piles=[2,3,4,4] the
      game will start with 1 pile of 2 pieces, 1 pile of 3 pieces, and 2
      piles of 4 pieces.

    max_removals_per_turn
      Max number of pieces you can remove in a turn. Default is no limit.

    """

    def __init__(self, players=None, max_removals_per_turn=None, piles=(5, 5, 5, 5)):
        """ Default for `piles` is 5 piles of 5 pieces. """
        self.players = players
        self.piles = list(piles)
        self.max_removals_per_turn = max_removals_per_turn
        self.current_player = 1  # player 1 starts.

    def possible_moves(self):
        return [
            "%d,%d" % (i + 1, j)
            for i in range(len(self.piles))
            for j in range(
                1,
                self.piles[i] + 1
                if self.max_removals_per_turn is None
                else min(self.piles[i] + 1, self.max_removals_per_turn),
            )
        ]

    def make_move(self, move):
        move = list(map(int, move.split(",")))
        self.piles[move[0] - 1] -= move[1]

    def unmake_move(self, move):  # optional, speeds up the AI
        move = list(map(int, move.split(",")))
        self.piles[move[0] - 1] += move[1]

    def show(self):
        print(" ".join(map(str, self.piles)))

    def win(self):
        return max(self.piles) == 0

    def is_over(self):
        return self.win()

    def scoring(self):
        return 100 if self.win() else 0

    def ttentry(self):
        return tuple(self.piles)  # optional, speeds up AI
    
    def setNewPiles(self, piles=(5, 5, 5, 5)):
        self.piles = list(piles)
        
    def rollStartingPlayer(self):
        self.current_player = random.randint(1, 2)
    
    def play(self, nmoves=1000, verbose=True):
        history = []

        if verbose:
            self.show()

        for self.nmove in range(1, nmoves + 1):

            if self.is_over():
                break

            move = self.player.ask_move(self)
            # debug_string = f'[DEBUG] ai wanted to: {move}, but needed to do: '
            # # awesome logic
            # if(random.random() <= 0.1):
            #     string_move = move.split(',')
            #     string_move[1] = str(int(string_move[1]) - 1)
            #     move = ",".join(string_move)
            #     debug_string+=move
            #     print(debug_string)
            
            history.append((deepcopy(self), move))
            self.make_move(move)

            if verbose:
                print(
                    "\nMove #%d: player %d plays %s :"
                    % (self.nmove, self.current_player, str(move))
                )
                self.show()

            self.switch_player()

        history.append(deepcopy(self))

        return history
        
        
class NimProba(TwoPlayerGame):
    """
    The game starts with 4 piles of 5 pieces. In turn the players
    remove as much pieces as they want, but from one pile only. The
    player that removes the last piece loses.

    Parameters
    ----------

    players
      List of the two players e.g. [HumanPlayer(), HumanPlayer()]

    piles:
      The piles the game starts with. With piles=[2,3,4,4] the
      game will start with 1 pile of 2 pieces, 1 pile of 3 pieces, and 2
      piles of 4 pieces.

    max_removals_per_turn
      Max number of pieces you can remove in a turn. Default is no limit.

    """

    def __init__(self, players=None, max_removals_per_turn=None, piles=(5, 5, 5, 5)):
        """ Default for `piles` is 5 piles of 5 pieces. """
        self.players = players
        self.piles = list(piles)
        self.max_removals_per_turn = max_removals_per_turn
        self.current_player = 1  # player 1 starts.

    def possible_moves(self):
        return [
            "%d,%d" % (i + 1, j)
            for i in range(len(self.piles))
            for j in range(
                1,
                self.piles[i] + 1
                if self.max_removals_per_turn is None
                else min(self.piles[i] + 1, self.max_removals_per_turn),
            )
        ]

    def make_move(self, move):
        move = list(map(int, move.split(",")))
        self.piles[move[0] - 1] -= move[1]

    def unmake_move(self, move):  # optional, speeds up the AI
        move = list(map(int, move.split(",")))
        self.piles[move[0] - 1] += move[1]

    def show(self):
        print(" ".join(map(str, self.piles)))

    def win(self):
        return max(self.piles) == 0

    def is_over(self):
        return self.win()

    def scoring(self):
        return 100 if self.win() else 0

    def ttentry(self):
        return tuple(self.piles)  # optional, speeds up AI
    
    def setNewPiles(self, piles=(5, 5, 5, 5)):
        self.piles = list(piles)
        
    def rollStartingPlayer(self):
        self.current_player = random.randint(1, 2)
    
    def play(self, nmoves=1000, verbose=True):
        history = []

        if verbose:
            self.show()

        for self.nmove in range(1, nmoves + 1):

            if self.is_over():
                break

            move = self.player.ask_move(self)
            debug_string = f'[DEBUG] ai wanted to: {move}, but needed to do: '
            # awesome logic
            if(random.random() <= 0.1):
                string_move = move.split(',')
                string_move[1] = str(int(string_move[1]) - 1)
                move = ",".join(string_move)
                debug_string+=move
                print(debug_string)
            
            history.append((deepcopy(self), move))
            self.make_move(move)

            if verbose:
                print(
                    "\nMove #%d: player %d plays %s :"
                    % (self.nmove, self.current_player, str(move))
                )
                self.show()

            self.switch_player()

        history.append(deepcopy(self))

        return history
        


if __name__ == "__main__":
    # IN WHAT FOLLOWS WE SOLVE THE GAME AND START A MATCH AGAINST THE AI

    from easyAI import AI_Player, Human_Player, Negamax, solve_with_iterative_deepening
    from easyAI.AI import TranspositionTable

    # we first solve the game
    # w, d, m, tt = solve_with_iterative_deepening(Nim(), range(5, 20), win_score=80)
    # w, d, len(tt.d)
    # the previous line prints -1, 16 which shows that if the
    # computer plays second with an AI depth of 16 (or 15) it will
    # always win in 16 (total) moves or less.

    # Now let's play (and lose !) against the AI
    
    number_of_games = 20
    
    print(f'=========== Deterministic game ===========')
    
    winCounter = {1: 0, 2: 0}
    ai = Negamax(8)
    game = Nim([AI_Player(ai), AI_Player(ai)])
    print(f'Max deep 8')

    time_of_games = time.time()
    for i in range(number_of_games):
        print(f'\n\n Game {i+1} starts\n')
        game.setNewPiles((5, 5, 5, 5))
        game.rollStartingPlayer()
        print(f'starting player: {game.current_player}')
        game.play()
        winCounter[game.current_player] += 1
        print("\n\n\nplayer %d wins\n\n\n" % game.current_player)
        print(f'current score:\n \t1st player: {winCounter[1]}\n \t2nd player: {winCounter[2]}\n {i+1} games played')
    
    with open('./outputs/deterministic', 'a') as f:
        f.write(f'Deterministic, game_duration={time.time() - time_of_games}, depth 8. P1: {winCounter[1]} | P2: {winCounter[2]}\n')
        
        
    print(f'=========== Probabilistic game ===========')
    winCounter = {1: 0, 2: 0}
    ai = Negamax(8)
    game = NimProba([AI_Player(ai), AI_Player(ai)])
    print(f'Max deep 8')
    
    time_of_games = time.time()
    for i in range(number_of_games):
        print(f'\n\n Game {i+1} starts\n')
        game.setNewPiles((5, 5, 5, 5))
        game.rollStartingPlayer()
        print(f'starting player: {game.current_player}')
        game.play()
        winCounter[game.current_player] += 1
        print("\n\n\nplayer %d wins\n\n\n" % game.current_player)
        print(f'current score:\n \t1st player: {winCounter[1]}\n \t2nd player: {winCounter[2]}\n {i+1} games played')

    with open('./outputs/probabilistic', 'a') as f:
        f.write(f'Probabilistic, game_duration={time.time() - time_of_games}, depth 8. P1: {winCounter[1]} | P2: {winCounter[2]}\n')


    print(f'=========== Deterministic game ===========')
    
    winCounter = {1: 0, 2: 0}
    ai = Negamax(4)
    game = Nim([AI_Player(ai), AI_Player(ai)])
    print(f'Max deep 4')

    time_of_games = time.time()
    for i in range(number_of_games):
        print(f'\n\n Game {i+1} starts\n')
        game.setNewPiles((5, 5, 5, 5))
        game.rollStartingPlayer()
        print(f'starting player: {game.current_player}')
        game.play()
        winCounter[game.current_player] += 1
        print("\n\n\nplayer %d wins\n\n\n" % game.current_player)
        print(f'current score:\n \t1st player: {winCounter[1]}\n \t2nd player: {winCounter[2]}\n {i+1} games played')

    with open('./outputs/deterministic', 'a') as f:
        f.write(f'Deterministic, game_duration={time.time() - time_of_games}, depth 4. P1: {winCounter[1]} | P2: {winCounter[2]}\n')
        
        
    print(f'=========== Probabilistic game ===========')
    winCounter = {1: 0, 2: 0}
    ai = Negamax(4)
    game = NimProba([AI_Player(ai), AI_Player(ai)])
    print(f'Max deep 4')
    
    time_of_games = time.time()
    for i in range(number_of_games):
        print(f'\n\n Game {i+1} starts\n')
        game.setNewPiles((5, 5, 5, 5))
        game.rollStartingPlayer()
        print(f'starting player: {game.current_player}')
        game.play()
        winCounter[game.current_player] += 1
        print("\n\n\nplayer %d wins\n\n\n" % game.current_player)
        print(f'current score:\n \t1st player: {winCounter[1]}\n \t2nd player: {winCounter[2]}\n {i+1} games played')

    with open('./outputs/probabilistic', 'a') as f:
        f.write(f'Probabilistic, game_duration={time.time() - time_of_games}, depth 4. P1: {winCounter[1]} | P2: {winCounter[2]}\n')
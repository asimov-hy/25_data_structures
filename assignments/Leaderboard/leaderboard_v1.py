# hint: bin search tree

# You're developing a gaming leaderboard for an online multiplayer game. 
# Players report their scores in real-time. 
# You need to maintain a dynamic data structure that can 
#   efficiently add a player's score, 
#   get the rank of a player, 
#   and get the k-th ranked score.

# Implement the following methods for the Leaderboard class:

class leaderboard:

    # define item
    class _score:
        __slots__ = ['player_id', 'score']

        def __init__(self, player_id, score):
            self.player_id = player_id
            self.score = score

    def __init__(self):
        self._scoreboard = []  # key(player_id): value(score)

# add_score(player_id: int, score: int) 
#   -> int: Adds a player's score to the leaderboard. If the player already exists, their score is updated. 
#       The method should return the player's rank after adding the score.
    def add_score(self, player_id: int, score: int):
        # find player_id and overwrite, if not add
        for score in self._scoreboard:              #O(n)
            if score.player_id == player_id:    
                score.score = score
                break
            else:
                self._scoreboard.append(self._score(player_id, score))
                break
        # sort and find rank - same rank is possible
        self._scoreboard.sort(key=lambda x: x.score, reverse=True)
        return rank

# get_rank(player_id: int) 
#   -> int: Returns the **rank** of the player with the given player_id. If the player does not exist, return -1.
    def get_rank(self, player_id: int):
        # player exists
        return rank
        # no player
        return -1

# get_score_by_rank(rank: int) 
#   -> int: Returns the **score** of the player with the given rank. 
#       If the rank is invalid (greater than the number of players), return -1.
    def get_score_by_rank(self, rank:int):
        ranking = list(self.scoreboard.items())
        max_rank = len(ranking) + 1
        if 1 <= rank <= max_rank:
            # rank exists
            return ranking[rank-1][1]
        else:
            # no rank
            return -1

    


# Output specification
# For each call to add_score(player_id, score), 
#   output the rank of the player after the score is added or updated, followed by a single newline.

# For each call to get_rank(player_id), 
#   output the current rank of the player with the given player_id, 
#   or -1 if the player does not exist, followed by a single newline.

# For each call to get_score_by_rank(rank), 
#   output the score of the player with the given rank, 
#   or -1 if the rank is invalid, followed by a single newline.


if __name__ == "__main__":

    leaderboard_instance = leaderboard()

    with open("test.0.0.in", "r") as file:
        commands = file.readlines()

    with open("test.0.0.out", "w") as output_file:
        for command in commands:
            parts = command.strip().split()
            cmd = parts[0]

            if cmd == "add_score":
                player_id = int(parts[1])
                score = int(parts[2])
                output_file.write(f"{leaderboard_instance.add_score(player_id, score)}\n")

            elif cmd == "get_rank":
                player_id = int(parts[1])
                output_file.write(f"{leaderboard_instance.get_rank(player_id)}\n")

            elif cmd == "get_score_by_rank":
                rank = int(parts[1])
                output_file.write(f"{leaderboard_instance.get_score_by_rank(rank)}\n")
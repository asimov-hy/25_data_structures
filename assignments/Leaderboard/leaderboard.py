# hint: bin search tree

# You're developing a gaming leaderboard for an online multiplayer game. 
# Players report their scores in real-time. 
# You need to maintain a dynamic data structure that can 
#   efficiently add a player's score, 
#   get the rank of a player, 
#   and get the k-th ranked score.

# Implement the following methods for the Leaderboard class:

class leaderboard:

    # define node for BST
    class _score_Node:
        __slots__ = ['score', 'count', 'size', 'left', 'right']

        def __init__(self, score):
            self.score = score
            self.count = 1
            self.size = 1
            self.left = None
            self.right = None


    def __init__(self):
        # id and score for player database
        self._scoreboard = {}  # key(player_id): value(score)

        # sorted scores for rank
        self._ranktoscore = []


# add_score(player_id: int, score: int) 
#   -> int: Adds a player's score to the leaderboard. If the player already exists, their score is updated. 
#       The method should return the player's rank after adding the score.
    def add_score(self, player_id: int, score: int):

        # update scoreboard
        old_score = self._scoreboard.get(player_id)
        self._scoreboard[player_id] = score

        # remove 
        if old_score is not None:
            # remove old score from _ranktoscore
            for i in range(len(self._ranktoscore)):
                if self._ranktoscore[i][0] == player_id:
                    self._ranktoscore.pop(i)
                    break
        
        # update _ranktoscore
        inserted = False
        # if score is higher than the lowest score in _ranktoscore
        for i, (_, s) in enumerate(self._ranktoscore):
            # if score is higher than the current score
            if score > s:
                self._ranktoscore.insert(i, (player_id, score))
                inserted = True
                break
        # if score is lower than the highest score in _ranktoscore
        if not inserted:
            self._ranktoscore.append((player_id, score))
        

        # else add
        # Return rank (1-based)
        for i, (pid, s) in enumerate(self._ranktoscore):
            if pid == player_id:
                return i + 1

# get_rank(player_id: int) 
#   -> int: Returns the **rank** of the player with the given player_id. If the player does not exist, return -1.
    def get_rank(self, player_id: int):
        # no player exists
        if player_id not in self._scoreboard:
            return -1
        # player exists
        for i, (pid, _) in enumerate(self._ranktoscore):
            if pid == player_id:
                return i + 1

# get_score_by_rank(rank: int) 
#   -> int: Returns the **score** of the player with the given rank. 
#       If the rank is invalid (greater than the number of players), return -1.
    def get_score_by_rank(self, rank:int):
        if 1 <= rank <= len(self._ranktoscore):
            return self._ranktoscore[rank - 1][1]
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
    while True:
        try:
            user_input = input().split()
        except EOFError:
            break  # Stop the loop when input ends

        if not user_input:
            continue

        cmd = user_input[0]

        if cmd == "add_score":
            player_id = int(user_input[1])
            score = int(user_input[2])
            print(leaderboard_instance.add_score(player_id, score))
        elif cmd == "get_rank":
            player_id = int(user_input[1])
            print(leaderboard_instance.get_rank(player_id))
        elif cmd == "get_score_by_rank":
            rank = int(user_input[1])
            print(leaderboard_instance.get_score_by_rank(rank))

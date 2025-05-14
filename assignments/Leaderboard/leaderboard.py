# hint: bin search tree

# You're developing a gaming leaderboard for an online multiplayer game. 
# Players report their scores in real-time. 
# You need to maintain a dynamic data structure that can 
#   efficiently add a player's score, 
#   get the rank of a player, 
#   and get the k-th ranked score.

# Implement the following methods for the Leaderboard class:

class BST:

    class Node:
        __slots__ = ['score', 'players', 'size', 'left', 'right']

        def __init__(self, score):
            self.score = score
            self.players = 1  # players with score
            self.size = 1   # size of subtree
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, score):
        
        # node default
        node = self.root
        path = []   # for size

        # if tree is empty set root
        if not node:
            self.root = BST.Node(score)
            return


        while node:
            path.append(node)
            if score < node.score:
                if not node.left:
                    node.left = BST.Node(score)
                    break
                node = node.left
            elif score > node.score:
                if not node.right:
                    node.right = BST.Node(score)
                    break
                node = node.right
            else:
                node.players += 1
                break

        # Update size
        for n in reversed(path):
            left_size = 0
            if n.left:
                left_size = n.left.size

            right_size = 0
            if n.right:
                right_size = n.right.size

            n.size = 1 + left_size + right_size

    def delete(self, score):

        # node default
        node = self.root
        parent = None   # since root no parent
        stack = []  # for size update

        # find node
        while node:

            stack.append(node)  # append not to stack
            if score < node.score:  # if score is lower go left
                parent = node
                node = node.left

            elif score > node.score:    # if score is higher go right
                parent = node
                node = node.right
            else:   # score is same
                break

        # delete node
        if node.players > 1:  # if more than one player with score
            node.players -= 1

        # if single player -> node must be deleted
        elif not node.left:  # if no left child

            if not parent:  # if node is root - then set root to right child
                self.root = node.right 

            elif parent.left == node:   # if left child - then set right child is parent left
                parent.left = node.right
            else:   # if node is right child - then set right child is parent right
                parent.right = node.right

            stack.pop() # pop from stack

        elif not node.right:    # if no right child
            if not parent:
                self.root = node.left
            elif parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left

            stack.pop()

        else:   # if both children exist -> find smallest in right subtree

            # temp for parent and new node
            path_to_new = []
            new_parent = node
            new = node.right

            # find smallest (= left-ist)
            while new.left: # find left
                path_to_new.append(new_parent)
                new_parent = new    # to update size and help delete
                new = new.left
            path_to_new.append(new_parent)

            node.score = new.score
            node.players = new.players
            new.players = 0

            stack.extend(path_to_new)  # include full path for size update

            # delete node
            if new_parent.left == new:
                new_parent.left = new.right
            else:
                new_parent.right = new.right

        # update size
        for n in reversed(stack):
            left_size = 0
            if n.left:
                left_size = n.left.size

            right_size = 0
            if n.right:
                right_size = n.right.size

            n.size = 1 + left_size + right_size




class leaderboard:
    def __init__(self):
        # id and score for player database
        self._scoreboard = {}  # key(player_id): value(score)

        # sorted scores for rank
        self._bst = BST()


# add_score(player_id: int, score: int) 
#   -> int: Adds a player's score to the leaderboard. If the player already exists, their score is updated. 
#       The method should return the player's rank after adding the score.
    def add_score(self, player_id: int, score: int) -> int:

        old_score = self._scoreboard.get(player_id)

        # if existing player remove old score
        if old_score is not None:
            self._bst.delete(old_score)

        # add new score
        self._scoreboard[player_id] = score # dictionary is updated - old is auto replaced
        self._bst.insert(score) # add to BST

        return self.get_rank(player_id)


# get_rank(player_id: int) 
#   -> int: Returns the **rank** of the player with the given player_id. If the player does not exist, return -1.
    def get_rank(self, player_id: int):
        
        #get score
        score = self._scoreboard.get(player_id)

        # no player
        if score is None:
            return -1

        # player exists

        # set node and rank default
        node = self._bst.root
        rank = 0

        # binary search
        while node: # while node is not None:

            # if score is lower then current node
            if score < node.score: 
                # all in right and this node count are higher
                
                if node.right:
                    # add right subtree size to rank
                    rank += node.right.size
                rank += 1

                # go left to find node
                node = node.left
            
            # if score is higher than current node
            elif score > node.score:
                node = node.right
            
            # if score == current
            else:
                if node.right:
                    # add right subtree size to rank
                    rank += node.right.size
                rank += 1
                break

        return rank

# get_score_by_rank(rank: int) 
#   -> int: Returns the **score** of the player with the given rank. 
#       If the rank is invalid (greater than the number of players), return -1.
    def get_score_by_rank(self, rank: int) -> int:
        if not self._bst.root or rank < 1 or rank > self._bst.root.size:
            return -1

        node = self._bst.root
        rank_counter = rank  # we track rank through `k`

        while node:

            right_size = 0

            # right_size = node.right.size if node.right else 0
            if node.right:
                right_size = node.right.size
            
            if rank_counter <= right_size:
                node = node.right

            elif rank_counter == right_size + 1:
                return node.score
            else:
                rank_counter -= right_size + 1
                node = node.left

        return -1  # invalid rank

    


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

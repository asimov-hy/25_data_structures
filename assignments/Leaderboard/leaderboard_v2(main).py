class BST:

    class score_node:
        __slots__ = ['score', 'players', 'size', 'left', 'right']

        def __init__(self, score):
            self.score = score  # key = score of node
            self.players = 1  # players with score
            self.size = 1   # size of subtree (including self)
            self.left = None
            self.right = None

    def __init__(self): # init as empty tree
        self.root = None

    def insert(self, score):
        
        # set node to root (set starting point)
        node = self.root

        # 1. if tree is empty then set as root
        if not node:
            self.root = BST.score_node(score)
            return
        
        # 2. tree is not empty

        path = []   # to update size

        while node:                 # while node is not empty

            # record in path for size update
            path.append(node)

            # if score is smaller -> go left
            if score < node.score:

                # if no left child -> insert
                if not node.left:
                    node.left = BST.score_node(score)
                    break

                # if left child exists -> go left
                node = node.left
                continue

            # if score is larger -> go right
            elif score > node.score:

                # if no right child -> insert
                if not node.right:
                    node.right = BST.score_node(score)
                    break

                # if right child exists -> go right
                node = node.right
                continue
            
            # if score is same -> increase players
            node.players += 1
            break

        # Update size
        for node in reversed(path):

            # defualt not child
            left_size = 0
            # but if left child exists then update size
            if node.left:
                left_size = node.left.size 

            # same to right
            right_size = 0
            if node.right:
                right_size = node.right.size 

            # size is updated as: self(number of players with score) + left size + right size
            node.size = left_size + right_size + node.players

    def delete(self, score):

        # node default
        node = self.root
        parent = None   # since root no parent
        stack = []  # for size update

        # find node
        while node:

            stack.append(node)  # append not to stack

            if score < node.score:  # score is lower -> go left
                parent = node
                node = node.left

            elif score > node.score:    # score is higher ->  go right
                parent = node
                node = node.right
            else:                       # score is same -> found
                break

        # delete node

        # 1) if score has more than one player
        if node.players > 1:
            node.players -= 1   # decrease player by one

        # 2) if single player -> node must be deleted

        # 2-1) if no left child -> replace with right child
        elif not node.left:

            if not parent:  # if node is root - then set root to right child
                self.root = node.right 

            elif parent.left == node:   # if node is left child - then set right child is parent left
                parent.left = node.right

            else:                       # if node is right child - then set right child is parent right
                parent.right = node.right

            stack.pop() # pop from stack

        # 2-2) if no right child -> replace with left child
        elif not node.right:    # if no right child

            if not parent:
                self.root = node.left

            elif parent.left == node:
                parent.left = node.left

            else:
                parent.right = node.left

            stack.pop()

        # 2-3) if both children exist -> find smallest in right subtree
        else:   

            # temp for parent and new node
            path_to_smallest = []
            
            smallest_parent = node   # parent node of smallest node

            # begin search at right child
            smallest = node.right    # new = smallest node

            # find smallest (= left-ist)
            while smallest.left: # while left node exists

                path_to_smallest.append(smallest_parent)

                smallest_parent = smallest
                smallest = smallest.left    
            # --> smallest is left-most node

            path_to_smallest.append(smallest_parent)

            # overwrite deleted node data with smallest node data
            node.score = smallest.score     # overwrite score
            node.players = smallest.players # overwrite players with score
            smallest.players = 0    # set smallest players to 0 == deleting

            stack.extend(path_to_smallest)  # stack = path to node + path to smallest

            # delete node
            if smallest_parent.left == smallest:    # left child was smallest
                smallest_parent.left = smallest.right
            else:
                smallest_parent.right = smallest.right

        # Update size
        for node in reversed(stack):

            # defualt not child
            left_size = 0
            # but if left child exists then update size
            if node.left:
                left_size = node.left.size 

            # same to right
            right_size = 0
            if node.right:
                right_size = node.right.size 

            # size is updated as: self(number of players with score) + left size + right size
            node.size = left_size + right_size + node.players

class Leaderboard:
    def __init__(self):

        self.player_scores = {}  # Dictionary to store player scores

        self.scores = BST()  # BST to store scores

        
    # add_score(player_id: int, score: int) 
    #   -> int: Adds a player's score to the leaderboard. If the player already exists, their score is updated. 
    #       The method should return the player's rank after adding the score.
    def add_score(self, player_id, score):
        # if player exists
        if player_id in self.player_scores:
            
            # if new score bigger than old
            old = self.player_scores[player_id]
            if score > old:
                # remove old score
                self.scores.delete(old)
                # add back new score
                self.player_scores[player_id] = score
                self.scores.insert(score)

        else:
            # if player does not exist
            self.player_scores[player_id] = score
            self.scores.insert(score)

        return self.get_rank(player_id)
    
    # get_rank(player_id: int) 
    #   -> int: Returns the **rank** of the player with the given player_id. If the player does not exist, return -1.
    def get_rank(self, player_id):

        # no player_id
        if player_id not in self.player_scores:
            return -1
        
        # player exists
        score = self.player_scores.get(player_id)
        node = self.scores.root
        rank = 1

        while node:
            if score < node.score:
                if node.right:
                    rank += node.right.size

                rank += node.players

                node = node.left

            elif score > node.score:
                node = node.right
            else:
                if node.right:
                    return rank + node.right.size
                else:
                    return rank
        return 0000 # for debug
            
    # get_score_by_rank(rank: int) 
    #   -> int: Returns the **score** of the player with the given rank. 
    #       If the rank is invalid (greater than the number of players), return -1.
    def get_score_by_rank(self, rank):

        rank_count = self.scores.root.size  # remaining players
        # check if rank is valid
        if rank < 1 or rank > rank_count:
            return -1

        # find the score by rank
        
        node = self.scores.root # find node
        while node:
            higher = 0
            if node.right:
                higher = node.right.size
                
            # if more players in right size than rank -> move to right
            if rank <= higher:
                node = node.right
                continue

            # if less players in right size than rank -> move left
            elif rank > higher + node.players:
                rank -= (higher + node.players)
                node = node.left
                continue
            # if equal or between?
            else:
                return node.score

        return 1111  # debug
    
    def print_scoreboard(self):
        # Sort players by score descending (and by player_id for ties, if you like)
        sorted_players = sorted(
            self.player_scores.items(),
            key=lambda item: (-item[1], item[0])
        )

        # Print header
        print(f"\n{'Player ID':>10}  {'Score':>5}  {'Rank':>4}")
        print("-" * 24)

        # Print each line
        for player_id, score in sorted_players:
            rank = self.get_rank(player_id)
            print(f"{player_id:>10}  {score:>5}  {rank:>4}")



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

    leaderboard_instance = Leaderboard()

    # mode: 1: for output file, 2: print to console, 3: debug to console, 4: debug to file
    mode = 1

    
    with open(r"assignments\Leaderboard\input.in", "r") as file:
        commands = file.readlines()

    with open("mytestout.out", "w") as output_file:
        if mode == 1:  # output file only
            for command in commands:
                parts = command.strip().split()
                cmd = parts[0]
                # print(command.strip())
                if cmd == "add_score":
                    player_id = int(parts[1])
                    score = int(parts[2])
                    output_file.write(f"{leaderboard_instance.add_score(player_id, score)}\n")
                    # print(f"{leaderboard_instance.add_score(player_id, score)}")
                    # leaderboard_instance.print_scoreboard()

                elif cmd == "get_rank":
                    player_id = int(parts[1])
                    output_file.write(f"{leaderboard_instance.get_rank(player_id)}\n")
                    # print(f"{leaderboard_instance.get_rank(player_id)}")

                elif cmd == "get_score_by_rank":    
                    rank = int(parts[1])
                    output_file.write(f"{leaderboard_instance.get_score_by_rank(rank)}\n")
                    # print(f"{leaderboard_instance.get_score_by_rank(rank)}")
                # print("-" * 30)
        elif mode == 2:  # print to console only
            for command in commands:
                parts = command.strip().split()
                cmd = parts[0]
                # print(command.strip())
                if cmd == "add_score":
                    player_id = int(parts[1])
                    score = int(parts[2])
                    print(f"{leaderboard_instance.add_score(player_id, score)}")
                    # leaderboard_instance.print_scoreboard()

                elif cmd == "get_rank":
                    player_id = int(parts[1])
                    print(f"{leaderboard_instance.get_rank(player_id)}")

                elif cmd == "get_score_by_rank":
                    rank = int(parts[1])
                    print(f"{leaderboard_instance.get_score_by_rank(rank)}")
                # print("-" * 30)
        elif mode == 3:
            for command in commands:
                parts = command.strip().split()
                cmd = parts[0]
                print("-" * 30)
                print("\ninput> " + command.strip())
                if cmd == "add_score":
                    player_id = int(parts[1])
                    score = int(parts[2])
                    print(f"output> {leaderboard_instance.add_score(player_id, score)}")
                    leaderboard_instance.print_scoreboard()


                elif cmd == "get_rank":
                    player_id = int(parts[1])
                    print(f"output> {leaderboard_instance.get_rank(player_id)}")

                elif cmd == "get_score_by_rank":
                    rank = int(parts[1])
                    print(f"output> {leaderboard_instance.get_score_by_rank(rank)}")
            print("-" * 30)
        elif mode == 4:
            for command in commands:
                parts = command.strip().split()
                cmd   = parts[0]

                # separator
                output_file.write("-" * 30 + "\n")
                # echo the input
                output_file.write("input> " + command.strip() + "\n")

                if cmd == "add_score":
                    pid, sc  = int(parts[1]), int(parts[2])
                    out_rank = leaderboard_instance.add_score(pid, sc)
                    output_file.write(f"output> {out_rank}\n")
                    # now dump the full scoreboard to file
                    for pid, score in sorted(leaderboard_instance.player_scores.items(),
                                            key=lambda kv: (-kv[1], kv[0])):
                        rank = leaderboard_instance.get_rank(pid)
                        output_file.write(f"Player {pid}: score={score}, rank={rank}\n")

                elif cmd == "get_rank":
                    pid = int(parts[1])
                    output_file.write(f"output> {leaderboard_instance.get_rank(pid)}\n")

                elif cmd == "get_score_by_rank":
                    r = int(parts[1])
                    output_file.write(f"output> {leaderboard_instance.get_score_by_rank(r)}\n")

            # final separator
            output_file.write("-" * 30 + "\n")



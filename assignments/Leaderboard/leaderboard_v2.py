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
        for n in reversed(path):

            # defualt not child
            left_size = 0
            # but if left child exists then update size
            if n.left:
                left_size = n.left.size

            # same to right
            right_size = 0
            if n.right:
                right_size = n.right.size

            # size is updated as: self(=1) + left size + right size
            n.size = 1 + left_size + right_size

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

        # update size
        for n in reversed(stack):
            left_size = 0
            if n.left:
                left_size = n.left.size

            right_size = 0
            if n.right:
                right_size = n.right.size

            n.size = 1 + left_size + right_size



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

    with open(r"assignments\Leaderboard\input.in", "r") as file:
        commands = file.readlines()

    with open("mytestout.out", "w") as output_file:
        for command in commands:
            parts = command.strip().split()
            cmd = parts[0]
            # print(command.strip())
            if cmd == "add_score":
                player_id = int(parts[1])
                score = int(parts[2])
                output_file.write(f"{leaderboard_instance.add_score(player_id, score)}\n")
                #print(f"{leaderboard_instance.add_score(player_id, score)}")
                #leaderboard_instance.print_scoreboard()

            elif cmd == "get_rank":
                player_id = int(parts[1])
                output_file.write(f"{leaderboard_instance.get_rank(player_id)}\n")
                # print(f"{leaderboard_instance.get_rank(player_id)}")

            elif cmd == "get_score_by_rank":
                rank = int(parts[1])
                output_file.write(f"{leaderboard_instance.get_score_by_rank(rank)}\n")                
                # print(f"{leaderboard_instance.get_score_by_rank(rank)}")
            # print("-" * 30)
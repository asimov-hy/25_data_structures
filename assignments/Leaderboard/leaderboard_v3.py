class BST:
    class score_node:
        __slots__ = ['score', 'players', 'size', 'left', 'right']

        def __init__(self, score):
            self.score   = score     # the key
            self.players = 1         # how many players have exactly this score
            self.size    = 1         # distinct‐node count in this subtree
            self.left    = None
            self.right   = None

    def __init__(self):
        self.root = None

    def insert(self, score):
        if not self.root:
            self.root = BST.score_node(score)
            return

        node = self.root
        path = []   # track all ancestors to fix up size

        # 1) walk to where this score lives (or would live)
        while True:
            path.append(node)
            if score < node.score:
                if not node.left:
                    node.left = BST.score_node(score)
                    path.append(node.left)
                    break
                node = node.left

            elif score > node.score:
                if not node.right:
                    node.right = BST.score_node(score)
                    path.append(node.right)
                    break
                node = node.right

            else:
                # duplicate score → just bump players, no new distinct node
                node.players += 1
                # no change to distinct‐node sizes
                return

        # 2) if we fell out by creating a new node, fix distinct‐size up the path
        for n in reversed(path):
            left_sz  = n.left.size  if n.left  else 0
            right_sz = n.right.size if n.right else 0
            n.size   = 1 + left_sz + right_sz

    def delete(self, score):
        """
        Remove exactly one occurrence of `score`.  If players>1 at that node, just decrement;
        otherwise delete the node and fix BST links, then fix distinct‐size up the path.
        """
        node   = self.root
        parent = None
        path   = []

        # 1) find the node
        while node and node.score != score:
            path.append(node)
            parent = node
            if score < node.score:
                node = node.left
            else:
                node = node.right

        if not node:
            return  # nothing to delete

        # 2) if tied players>1, just decrement
        if node.players > 1:
            node.players -= 1
            return     # distinct structure unchanged

        # 3) we have to remove the distinct node entirely
        path.append(node)

        # helper to splice out `node` given its parent
        def replace_in_parent(parent, node, new_child):
            if not parent:
                self.root = new_child
            elif parent.left is node:
                parent.left = new_child
            else:
                parent.right = new_child

        # 3a) no left child → promote right
        if not node.left:
            replace_in_parent(parent, node, node.right)

        # 3b) no right child → promote left
        elif not node.right:
            replace_in_parent(parent, node, node.left)

        # 3c) two children → steal from inorder‐successor
        else:
            # find leftmost in right subtree
            succ_parent = node
            succ = node.right
            while succ.left:
                path.append(succ_parent)
                succ_parent = succ
                succ = succ.left
            path.append(succ)

            # copy data from succ → node
            node.score   = succ.score
            node.players = succ.players

            # unlink succ
            replace_in_parent(succ_parent, succ, succ.right)

        # 4) fix up distinct‐size along the path
        for n in reversed(path):
            left_sz  = n.left.size  if n.left  else 0
            right_sz = n.right.size if n.right else 0
            n.size   = 1 + left_sz + right_sz


class Leaderboard:
    def __init__(self):
        self.player_scores = {}  # player_id -> score
        self.scores         = BST()

    def add_score(self, player_id, score):
        # if updating an existing player, delete their old score
        if player_id in self.player_scores:
            old = self.player_scores[player_id]
            self.scores.delete(old)

        # record new score and insert into BST
        self.player_scores[player_id] = score
        self.scores.insert(score)

        return self.get_rank(player_id)

    def get_rank(self, player_id):
        """
        Dense rank = (# of distinct scores strictly greater than this player's) + 1
        """
        if player_id not in self.player_scores:
            return -1

        target = self.player_scores[player_id]
        node   = self.scores.root
        rank   = 1

        while node:
            if target < node.score:
                # this node + its right subtree are all > target
                right_sz = node.right.size if node.right else 0
                rank    += right_sz + 1
                node     = node.left

            elif target > node.score:
                node = node.right

            else:
                # equal: only nodes in right subtree are > target
                right_sz = node.right.size if node.right else 0
                rank    += right_sz
                return rank

        # should never get here if the tree is consistent
        return -1

    def get_score_by_rank(self, rank):
        """
        Return the score that has the given dense rank (1 = highest distinct score).
        If rank is out of bounds, return -1.
        """
        root = self.scores.root
        if not root or rank < 1 or rank > root.size:
            return -1

        node = root
        while node:
            right_sz = node.right.size if node.right else 0

            if rank <= right_sz:
                node = node.right
            elif rank == right_sz + 1:
                return node.score
            else:
                rank -= (right_sz + 1)
                node = node.left

        return -1  # unreachable if inputs are valid




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
                    # for pid, score in sorted(leaderboard_instance.player_scores.items(),
                    #                         key=lambda kv: (-kv[1], kv[0])):
                    #     rank = leaderboard_instance.get_rank(pid)
                    #     output_file.write(f"Player {pid}: score={score}, rank={rank}\n")

                elif cmd == "get_rank":
                    pid = int(parts[1])
                    output_file.write(f"output> {leaderboard_instance.get_rank(pid)}\n")

                elif cmd == "get_score_by_rank":
                    r = int(parts[1])
                    output_file.write(f"output> {leaderboard_instance.get_score_by_rank(r)}\n")

            # final separator
            output_file.write("-" * 30 + "\n")



class Leaderboard:
    class _Node:
        __slots__ = ('score', 'count', 'size', 'left', 'right')
        def __init__(self, score):
            self.score = score      # the score value
            self.count = 1          # how many players have this exact score
            self.size = 1           # total players in this subtree (including duplicates)
            self.left = None        # lower scores
            self.right = None       # higher scores

    def __init__(self):
        self._root = None
        self._player_score = {}  # player_id -> current score

    def _update_size(self, node):
        left_sz = node.left.size if node.left else 0
        right_sz = node.right.size if node.right else 0
        node.size = left_sz + right_sz + node.count

    def _insert(self, node, score):
        if node is None:
            return Leaderboard._Node(score)
        if score < node.score:
            node.left = self._insert(node.left, score)
        elif score > node.score:
            node.right = self._insert(node.right, score)
        else:
            node.count += 1
        self._update_size(node)
        return node

    def _delete_all(self, node, score):
        if node is None:
            return None
        if score < node.score:
            node.left = self._delete_all(node.left, score)
        elif score > node.score:
            node.right = self._delete_all(node.right, score)
        else:
            # remove this node entirely
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # two children: replace with in-order successor
            succ = node.right
            while succ.left:
                succ = succ.left
            node.score, node.count = succ.score, succ.count
            node.right = self._delete_all(node.right, succ.score)
        self._update_size(node)
        return node

    def _delete_one(self, node, score):
        if node is None:
            return None
        if score < node.score:
            node.left = self._delete_one(node.left, score)
        elif score > node.score:
            node.right = self._delete_one(node.right, score)
        else:
            if node.count > 1:
                node.count -= 1
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.score, node.count = succ.score, succ.count
                node.right = self._delete_all(node.right, succ.score)
        self._update_size(node)
        return node

    def _count_higher(self, node, score):
        if node is None:
            return 0
        if score < node.score:
            right_sz = node.right.size if node.right else 0
            return right_sz + node.count + self._count_higher(node.left, score)
        elif score > node.score:
            return self._count_higher(node.right, score)
        else:
            return node.right.size if node.right else 0

    def _find_by_rank(self, node, k):
        if node is None:
            return None
        right_sz = node.right.size if node.right else 0
        if k <= right_sz:
            return self._find_by_rank(node.right, k)
        if k <= right_sz + node.count:
            return node.score
        return self._find_by_rank(node.left, k - right_sz - node.count)

    def add_score(self, player_id, score):
        # remove old if exists
        if player_id in self._player_score:
            old = self._player_score[player_id]
            self._root = self._delete_one(self._root, old)
        # insert new
        self._root = self._insert(self._root, score)
        self._player_score[player_id] = score
        higher = self._count_higher(self._root, score)
        return higher + 1

    def get_rank(self, player_id):
        if player_id not in self._player_score:
            return -1
        score = self._player_score[player_id]
        higher = self._count_higher(self._root, score)
        return higher + 1

    def get_score_by_rank(self, rank):
        if self._root is None or rank < 1 or rank > self._root.size:
            return -1
        res = self._find_by_rank(self._root, rank)
        return res if res is not None else -1

    def print_scoreboard(self):
            # Sort all players by score descending, then by player_id ascending
            players = sorted(self._scoreboard.items(), key=lambda x: (-x[1], x[0]))
            for player_id, score in players:
                print(f"Rank {self.get_rank(player_id)}:\tScore {score}")



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
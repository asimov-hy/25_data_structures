# Problem a: Binary Search Tree

이진 탐색 트리(BST, Binary Search Tree)는 각 노드가 키(key)와 값(value)을 가지며, 왼쪽 자식의 키는 부모 노드의 키보다 작고, 오른쪽 자식의 키는 부모 노드의 키보다 큰 이진 트리입니다.

다음은 이진 탐색 트리의 예시입니다:

```plaintext
         (5, 1)
        /      \
    (3, 9)      (7, 8)
    /    \      / 
(1, 6)(4, 2) (6, 1)
```

`TreeMapSkeleton` 클래스의 기본 구조가 제공되어 있으니 참고하여 문제를 해결하세요.

## Problem a1: Searching for a Key

(중간 난이도, 8점)

`TreeMapBase1` 클래스를 완성하세요. 현재 `_subtree_search` 메서드는 완전히 구현되어 있지 않습니다. 이 메서드를 구현하여 `TreeMapBase1` 클래스를 완성하세요.

- `_subtree_search(self, node: Node, key: int) -> Node`: 이 함수는 특정 `node`와 찾고자 하는 `key`를 입력으로 받아, 해당 노드를 루트로 하는 서브트리 내에서 해당 키를 가진 노드를 반환합니다.

  만약 지정한 `key`가 해당 서브트리에 존재하지 않는다면, 탐색이 끝난 위치의 노드(즉, 해당 키가 삽입되어야 할 위치의 노드)를 반환해야 합니다.

  예를 들어, 위 트리에서 `_subtree_search(self.root, 4)`는 키가 4인 노드를 반환해야 하고, `_subtree_search(self.root, 2)`는 키 2를 찾을 수 없으므로 키가 1인 노드를 반환해야 합니다.

## Problem a2: Inserting or Updating a Node

(중간 난이도, 8점)

`TreeMapBase2` 클래스에 다음 함수를 구현하세요:

- `__setitem__(self, key: int, value: Any)`: 이 함수는 삽입하거나 갱신할 `key`와 `value`를 입력으로 받아, 해당 키와 값을 가진 새로운 노드를 이진 탐색 트리에 삽입합니다. 만약 해당 키를 가진 노드가 이미 존재하면, 기존 노드의 값을 갱신해야 합니다.

  예를 들어, 위 트리에서 `__setitem__(4, 9)`는 키가 4인 노드의 값을 9로 갱신해야 하고, `__setitem__(8, 3)`은 키 8, 값 3을 가지는 새로운 노드를 삽입해야 합니다.

  참고: 먼저 `_subtree_search` 함수를 사용하여 키를 검색해야 합니다. 키가 존재하면 값을 갱신하고, 존재하지 않으면 새로운 노드를 삽입하세요.

  참고 2: 새로운 노드는 제공된 `Node` 클래스를 사용하여 생성할 수 있습니다:
  `self.Node(key: int, value: Any, parent: Node | None)`

## Problem a3: Finding the Node with the Minimum Key

(쉬움, 5점)

다음 함수를 구현하세요:

- `_subtree_first_node(node: Node) -> Node`: 이 함수는 `node`를 입력으로 받아, 해당 노드를 루트로 하는 서브트리 내에서 가장 작은 키를 가진 노드를 반환합니다.

  예를 들어, `_subtree_first_node(self.root)`는 키가 1인 노드를 반환해야 합니다.

# Problem a4: What's next?

(어려움, 10점)

다음 함수를 구현하세요:

- `after(node: Node) -> Node`: 이 함수는 `node`를 입력으로 받아, 이진 탐색 트리를 중위 순회(in-order traversal)했을 때 해당 노드 다음에 오는 노드를 반환합니다. 만약 주어진 노드가 순회의 마지막 노드라면, `None`을 반환해야 합니다.

  예를 들어, `after(self.root)`는 키가 6인 노드를 반환해야 하고, `after(self.root.left)`는 키가 4인 노드를 반환해야 하며, `after(self.root.right)`는 `None`을 반환해야 합니다.

  힌트: 중위 순회에서 다음 노드를 찾는 규칙은 다음과 같습니다:

  1. 주어진 노드에 오른쪽 자식이 있다면, 다음 노드는 오른쪽 서브트리에서 가장 왼쪽에 있는 노드입니다.

  2. 그렇지 않은 경우, 부모 노드를 따라 올라가면서 해당 노드가 부모의 왼쪽 자식인 경우를 찾습니다. 이때의 부모 노드가 다음의 노드입니다.

     - 루트 노드의 부모는 `None`이므로, 루트에 도달하면 탐색을 중단해야 합니다.

# Problem b: Graph

그래프(graph)는 유한한 정점(vertex)들의 집합과 정점 쌍을 연결하는 간선(edge)들의 집합으로 구성된 자료구조입니다.

다음은 두 개의 그래프 예시입니다:

```plaintext
그래프 A:
    1
   / \
  2 - 3 - 5
 /     \
4       6
```

```plaintext
그래프 B:
    1        5
   /          \
  2 - 3        6
 /            / \
4            7   8 - 9
```

이 문제에서는 인접 리스트(adjacency list) 방식으로 구현된 `Graph` 클래스와, `Vertex` 클래스 및 `Edge` 클래스의 뼈대 코드가 제공됩니다.

## Problem b1: Bredth-First Search (BFS)

(중간 난이도, 8점)

너비 우선 탐색(BFS, Breadth-First Search)은 그래프 자료구조를 탐색하거나 순회하는 데에 사용되는 기본 알고리즘입니다. BFS는 한 정점에서 시작하여 인접한 모든 정점을 먼저 탐색한 후, 그 다음 레벨의 정점들을 순차적으로 탐색합니다. BFS에서는 간선을 다음 세 가지 유형으로 분류합니다:

- `UNEXPLORED`: 아직 탐색되지 않은 간선
- `DISCOVERY`: 처음 방문하는 정점으로 이어지는 간선
- `CROSS`: 이미 방문한 두 정점을 연결하는 간선

`bfs_v` 함수를 완성하세요. `bfs` 함수는 이미 구현되어 있으며 수정해서는 안 됩니다.

- `bfs_v(graph: Graph, v: Vertex)`: 이 함수는 정점 `v`에서 시작하여 BFS를 수행해야 합니다. 정점을 `VISITED`로 표시하고, 인접한 정점들을 반복적으로 탐색하세요. BFS 순회 과정에서 간선을 `UNEXPLORED`, `DISCOVERY`, `CROSS` 중 하나로 분류해야 합니다.

## Problem b2: Detecting a Cycle

(쉬움, 5점)

다음 함수를 구현하세요:

- `has_cycle(graph: Graph) -> bool`: 이 함수는 `graph`에 사이클이 존재하면 `True`, 존재하지 않으면 `False`를 반환해야 합니다.

예를 들어, `has_cycle(graphA)`는 사이클 1 -> 2 -> 3 -> 1이 있으므로 `True`를 반환해야 합니다. 반면, `has_cycle(graphB)`는 사이클이 없으므로 `False`를 반환해야 합니다.

힌트: 이전 문제에서 구현한 BFS 알고리즘을 사용하세요. BFS 순회 중 `CROSS` 간선을 만나면 사이클이 존재한다는 것을 의미합니다.

## Problem b3: Shortest Path

(중간 난이도, 8점)

다음 함수를 구현하세요:

- `shortest_path(graph: Graph, start: Vertex, end: Vertex) -> int`: 이 함수는 `start` 정점에서 `end` 정점까지의 최단 경로 길이를 반환해야 합니다.

두 정점 사이에 경로가 존재하지 않으면 `-1`을 반환하세요.

예를 들어, `shortest_path(graphA, Vertex 1, Vertex 6)`은 정점 1에서 6까지의 최단 경로가 1 -> 3 -> 6이므로 `2`를 반환해야 합니다. 반면, `shortest_path(graphB, Vertex 1, Vertex 9)`는 경로가 존재하지 않으므로 `-1`을 반환해야 합니다.

from a_skeleton import HeapSkeleton
# Problem a1: Up and Down
# Finish implementing the `HeapBase` class. 
# Currently, the `_upheap` and `_downheap` methods are not fully implemented. 
# Implement these methods to complete the `HeapBase` class.

# - `_upheap(self, j: int)`: This method should move the node at index `j` up the heap until the heap-order property is satisfied. 
#                               This method returns nothing.

# - `_downheap(self, j: int)`: This method should move the node at index `j` down the heap until the 
#                               heap-order property is satisfied. This method returns nothing.


# parent, left, right in skeleton code!!! -> should change if time
# 일단 파일 내에서 해결결

class HeapBase(HeapSkeleton):
    # todo: implement this
    def _upheap(self, j):
        # 부모 노드 구하기기
        parent = (j - 1) // 2

        # 부모 노드보다다 더 크다면 바꾸기
        if j > 0 and self._data[j] > self._data[parent]:        # j가 0 보다 크다(유효한 노드), 부모노드가 더 작다
            self._data[j], self._data[parent] = self._data[parent], self._data[j]   # 바꾸기기
            # 부모노드로 올라가기기
            self._upheap(parent)
        # 만약 정렬되어 있다면 나머지도 정렬되어 있다고 가정을 함함
        
    
    # todo: implement this
    def _downheap(self, j):
        biggestNode = j
        # 자식 주소 구하기기
        left = self._left(j)
        right = self._right(j)

        # if self._data[left] > self._data[biggestNode] or self._data[right] > self._data[biggestNode]
        #   if self._data[left] > self._data[right]:
        #       biggestNode = left
        #   else:
        #       biggestNode = right

        # 왼쪽 자식과 큰지 비교교
        if self._has_left and self._data[left] > self._data[biggestNode]:
            biggestNode = left

        # 오른쪽 자식 과 비교교
        if self._has_right and self._data[right] > self._data[biggestNode]:
            biggestNode = right

        # 차이가 있다면 변환하기기
        if biggestNode != j:
            # self._data[j], self._data[biggestNode] = self._data[biggestNode], self._data[j] # 변환하기
            self._swap(self._data[j], self._data[biggestNode])
            self._downheap(biggestNode) # 아래로 계속 재귀귀


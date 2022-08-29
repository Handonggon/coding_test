class MinHeap:
    def __init__(self):
        self.heap_list = [None]

    def insert(self, value):
        list_1 =  self.heap_list
        idx = len(list_1)
        list_1.append(value)
        while True:
            if idx > 1 and list_1[idx] < list_1[idx // 2]:
                list_1[idx], list_1[idx // 2] = list_1[idx // 2], list_1[idx]
                idx = idx // 2
                continue
            break
    
    def delete(self):
        list_1 = self.heap_list
        list_1[1] ,list_1[-1] = list_1[-1] ,list_1[1]
        min = list_1.pop()
        idx = len(list_1) - 1
        parent = 1
        while True:
            sibling_left = parent * 2
            sibling_right = (parent * 2) + 1
            get_idx = parent
            if sibling_left <= idx and list_1[get_idx] > list_1[sibling_left]:
                get_idx = sibling_left
            if sibling_right <= idx and list_1[get_idx] > list_1[sibling_right]:
                get_idx = sibling_right

            if get_idx == parent:
                break

            list_1[get_idx], list_1[parent] = list_1[parent], list_1[get_idx]
            parent = get_idx
        return min
    
def solution(scoville, K):
    heap = MinHeap()
    for i in scoville :
        heap.insert(i)
    result = 0
    while heap.heap_list[1] < K :
        if len(heap.heap_list) == 2 :
            return -1
        result += 1
        temp = heap.delete() + (heap.delete()*2)
        heap.insert(temp)
        
    return result
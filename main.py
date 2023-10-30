from Stack import LStack
from Queue import LQueue, LDequeue
from Heap import MinHeap, MaxHeap
from random import randint as ri

if __name__ == "__main__":
    # pass

    # S = LStack()
    # S.push(5)
    # S.push(10)
    # print(S.pop())
    # print(S.pop())
    # print(S.is_empty())
    # S.push("Hello World")
    # print(S.is_empty())
    # print(S.peek())
    # print(S.is_empty())
    # print(S.pop())
    # print(S.is_empty())

    # Q = LQueue()
    # Q.enqueue(5)
    # Q.enqueue(6)
    # Q.enqueue(7)
    # print(Q.dequeue())
    # print(Q.dequeue())
    # print(Q.is_empty())
    # print(Q.peek())
    # print(Q.dequeue())
    # print(Q.is_empty())
    # print(Q.dequeue())

    # Dequeue is bugged
    # dequeue = LDequeue()
    # dequeue.add_first(5)
    # dequeue.add_first(4)
    # print(dequeue.delete_first())
    # print(dequeue.delete_first())
    # print(dequeue.delete_first())
    # print(dequeue.is_empty())

    # test_arr = [1, 2, 3, 4, 9, 10, 11]
    # print(test_arr)
    # heap = MaxHeap(test_arr)
    # heap.heapify()
    # print(heap.heap)
    # heap.delete(1)
    # print(heap.heap)
    # heap.heapsort()
    # heap.heap = [1.5, 1.3, 1.6, 5.2]
    # heap.heap = []
    # heap.heapify()
    # # heap.heapsort()
    # # print(heap.heap)
    #
    # print(heap.heap)

    # test_arr = [101, 89, 50, 40, 5, 4, 3]
    # print(test_arr)
    # heap = MinHeap(test_arr)
    # heap.heapify()
    # print(heap)
    # heap.heapsort()
    # print(heap.peek())
    # print(heap)
    #
    # heap.add(10)
    # print(heap)
    # print(heap.heapsort())

    packets = [
        {"timestamp": 0, "priority":2, "data": "Packet 1"},
        {"timestamp": 5, "priority": 3, "data": "Packet 2"},
        {"timestamp": 2, "priority": 1, "data": "Packet 3"},
        {"timestamp": 1, "priority": 1, "data": "Packet 4"},
        {"timestamp": 8, "priority": 5, "data": "Packet 5"},
        {"timestamp": 10, "priority": 4, "data": "Packet 6"},
        {"timestamp": 12, "priority": 3, "data": "Packet 7"},
        ]

    for i in packets:
        print(i)

    priority_queue = MinHeap(packets, key=lambda x: x['priority'])
    sorted_packets = (priority_queue.heapsort()).heap

    print("*" * 20)

    for i in sorted_packets:
        print(i)

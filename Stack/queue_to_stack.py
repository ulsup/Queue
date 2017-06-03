from arraystack import ArrayStack
from arrayqueue import ArrayQueue
import copy


def queue_to_stack(queue):
    stack = ArrayStack()
    new_queue = copy.deepcopy(queue)
    while not new_queue.isEmpty():
        stack.add(new_queue.pop())
    return stack


queue = ArrayQueue()
queue.add(2)
queue.add(3)
queue.add(6)
stack = queue_to_stack(queue)
print(stack.pop())
print(stack.pop())

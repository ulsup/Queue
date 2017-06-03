from arrayqueue import ArrayQueue
import copy


def stack_to_queue(stack):
    queue = ArrayQueue()
    new_stack = copy.deepcopy(stack)
    while not new_stack.isEmpty():
        queue.add(new_stack.pop())
    return queue

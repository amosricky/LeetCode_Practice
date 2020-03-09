# 【LeetCode】 641. Design Circular Deque

## Description
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

+ MyCircularDeque(k): Constructor, set the size of the deque to be k.
+ insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
+ insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
+ deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
+ deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
+ getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
+ getRear(): Gets the last item from Deque. If the deque is empty, return -1.
+ isEmpty(): Checks whether Deque is empty or not. 
+ isFull(): Checks whether Deque is full or not.

Note:

+ All values will be in the range of [0, 1000].
+ The number of operations will be in the range of [1, 1000].
+ Please do not use the built-in Deque library.

## Example:
```
MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4
```

## Solution
* Use list to implement.

### Code
```python
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.queue = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.queue) < self.size:
            self.queue.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.queue) > 0:
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.queue) == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.queue) == self.size
```

###### tags: `LeetCode` `python` `Design Circular Deque` 
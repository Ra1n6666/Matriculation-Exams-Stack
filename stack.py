from typing import List, Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    array: List[T]
    
    def __init__(self):
        self.array = []
  
    def push(self, value: T) -> None:
        self.array.append(value)

    def pop(self) -> T:
        return self.array.pop()

    def top(self) -> T:
        if len(self.array) <= 0:
            raise Exception("Array is empty")
        return self.array[-1]

    def is_empty(self) -> bool:
        return len(self.array) <= 0

    def print_stack(self):
        print(self.array)
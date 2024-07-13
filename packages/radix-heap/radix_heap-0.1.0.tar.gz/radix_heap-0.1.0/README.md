# Radix Heap for Python

This module provides a Python implementation of Radix Heap-like data structures, designed to function as monotone priority queues. The heavy-lifting for the heap operations is powered by the `radix-heap` Rust crate from [mpdn](https://github.com/mpdn/radix-heap) -- they did 99% of the hard work by implementing the data structure.

Monotone priority queues are useful for pathfinding in general (e.g., A*, Dijkstra's algorithm). A monotone priority queue must maintain the invariant where the extracted elements form a monotone sequence (e.g., for a max-heap, the extracted elements are in non-increasing order).

## Overview

A Radix Heap is a type of priority queue where the extracted elements form a monotone sequence. This module includes implementations for both maximum and minimum heaps for integer and float keys.

## Classes

- `RadixHeapLike[K, V]`: A generic base class for Radix Heap-like structures.
- `RadixMaxHeapInt[V]`: A radix max heap for integers.
- `RadixMinHeapInt[V]`: A radix min heap for integers.
- `RadixMaxHeap[V]`: A radix max heap for floats (or integers).
- `RadixMinHeap[V]`: A radix min heap for floats (or integers).

## Methods

- `push(key: K, value: V) -> None`: Adds a key-value pair to the heap.
- `pop() -> V`: Removes and returns the minimum value from the heap.
- `pop_with_key() -> tuple[K, V]`: Removes and returns the minimum key-value pair from the heap.
- `top() -> V | None`: Returns the minimum value from the heap without removing it.
- `clear() -> None`: Removes all elements from the heap.
- `__len__() -> int`: Returns the number of elements in the heap.

## Usage Examples

### Radix Max Heap for Integers

```python
from radix_heap import RadixMaxHeapInt

heap = RadixMaxHeapInt()
heap.push(10, "A")
heap.push(5, "B")
heap.push(8, "C")

while heap:
    print(heap.pop())
# Output: "A", "C", "B"
```

## Installation

To install the module, you can use pip:

```bash
pip install radix-heap
```

## Contributing

Contributions are welcome! Please check the repository and feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
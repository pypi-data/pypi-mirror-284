from __future__ import annotations

from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")

class RadixHeapLike(Generic[K, V]):
    """
    A generic class representing a Radix Heap-like data structure.

    A radix-heap is a monotone priority queue, where the extracted elements
    form a monotone sequence, e.g., for max-heap, the extracted elements are
    monotonically decreasing.

    Heavy-lifting done by https://github.com/mpdn/radix-heap.

    Attributes:
        None

    Methods:
        push: Add a key-value pair to the heap.
        pop: Remove and return the minimum value from the heap.
        pop_with_key: Remove and return the minimum key-value pair from the heap.
        top: Return the minimum value from the heap without removing it.
        clear: Remove all elements from the heap.
        __len__: Return the number of elements in the heap.

    """

    def push(self, key: K, value: V) -> None:
        """
        Pushes a key-value pair into the radix heap.

        Args:
            key (K): The key associated with the value.
            value (V): The value to be stored in the heap.

        Returns:
            None
        """
        ...
    def pop(self) -> V:
        """
        Remove and return the "top" element from the heap.

        Returns:
            V: The value of the top element.
        """
        ...
    def pop_with_key(self) -> tuple[K, V]:
        """
        Removes and returns the key-value pair with the "top" key from the heap.

        Returns:
            tuple[K, V]: A tuple containing the key and value of the removed item.
        """
        ...
    def top(self) -> V | None:
        """
        Returns the top element of the radix heap.

        Returns:
            The top element of the radix heap, or None if the heap is empty.
        """
        ...
    def clear(self) -> None:
        """
        Clears all elements from the radix heap.
        """
        ...
    def __len__(self) -> int: ...

class RadixMaxHeapInt(RadixHeapLike[int, V]):
    """
    A radix max heap implementation for integers.

    Usage:
    ------
    heap = RadixMaxHeapInt()
    heap.push(10, "A")
    heap.push(5, "B")
    heap.push(8, "C")

    while heap:
        print(heap.pop())
        # Output: "A", "C", "B"
    """

    ...

class RadixMinHeapInt(RadixHeapLike[int, V]):
    """
    A radix min heap implementation for integers.

    Usage:
    ------
    heap = RadixMinHeapInt()
    heap.push(10, "A")
    heap.push(5, "B")
    heap.push(8, "C")
    while heap:
        print(heap.pop())
        # Output: "B", "C", "A"
    """

    ...

class RadixMaxHeap(RadixHeapLike[float, V]):
    """
    A radix max heap implementation for floats (or integers).

    Usage:
    ------
    heap = RadixMaxHeap()
    heap.push(10.0, "A")
    heap.push(5.0, "B")
    heap.push(8, "C")

    while heap:
        print(heap.pop())
        # Output: "A", "C", "B"

    """

    ...

class RadixMinHeap(RadixHeapLike[float, V]):
    """
    A radix min heap implementation for floats (or integers).

    Usage:
    ------
    heap = RadixMinHeap()
    heap.push(10.0, "A")
    heap.push(5.0, "B")
    heap.push(8, "C")

    while heap:
        print(heap.pop())
        # Output: "B", "C", "A"
    """

    ...

"""Implements the Array ADT using array capabilities of the ctypes module,
the Array2D ADT and the DynamicArray ADT"""
import ctypes


class Array:
    """Represents an array with size elements."""
    def __init__(self, size):
        """
        (int) ->
        Initialize a size and elements of the array
        """
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        # Initialize each element.
        self.clear(None)

    def __len__(self):
        """
        () -> int
        Returns the size of the array.
        """
        return self._size

    def __getitem__(self, index):
        """
        (int) -> value
        Gets the contents of the index element.
        """
        assert 0 <= index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        (int, value) ->
        Puts the value in the array element at index position.
        """
        assert 0 <= index < len(self), "Array subscript out of range"
        self._elements[index] = value

    def __str__(self):
        """
        () -> str
        Returns string that represents an array
        """
        result = "["
        for i in range(len(self)):
            result += str(self._elements[i]) + ", "
        return result[:-2] + "]"

    def clear(self, value):
        """
        (value) ->
        Clears the array by setting each element to the given value.
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        () -> _ArrayIterator
        Returns the array's iterator for traversing the elements.
        """
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    """An iterator for the Array ADT."""
    def __init__(self, the_array):
        """
        (Array) ->
        Initialize an array
        """
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        """
        () -> _ArrayIterator
        Returns the array's iterator for traversing the elements.
        """
        return self

    def __next__(self):
        """
        () -> value
        Returns value from current position and
        changes _cur_index to the next iteration
        """
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        raise StopIteration


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        """
        () ->
        Create an empty array.
        """
        self._n = 0                                # count actual elements
        self._capacity = 1                         # default array capacity
        self._array = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """
        () -> int
        Return number of elements stored in the array.
        """
        return self._n

    def __getitem__(self, k):
        """
        (int) -> value
        Return element at index k.
        """
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._array[k]                          # retrieve from array

    def __str__(self):
        """
        () -> str
        Returns string that represents an array
        """
        result = "["
        for i in range(self._n):
            result += str(self._array[i]) + ", "
        return result[:-2] + "]"

    def append(self, obj):
        """
        (value) ->
        Add object to end of the array.
        """
        if self._n == self._capacity:              # not enough room
            self._resize(2 * self._capacity)       # so double capacity
        self._array[self._n] = obj
        self._n += 1

    def _resize(self, numb):                          # nonpublic utitity
        """
        (int) ->
        Resize internal array to capacity numb.
        """
        new_array = self._make_array(numb)                    # new (bigger) array
        for k in range(self._n):                   # for each existing value
            new_array[k] = self._array[k]
        self._array = new_array                                # use the bigger array
        self._capacity = numb

    @staticmethod
    def _make_array(numb):
        # nonpublic utitity
        """
        (int) -> py_object_Array
        Return new array with capacity numb.
        """
        return (numb * ctypes.py_object)()           # see ctypes documentation

    def insert(self, k, value):
        """
        (int, value) ->
        Insert value at index k, shifting subsequent values rightward.
        """
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:             # not enough room
            self._resize(2 * self._capacity)      # so double capacity
        for j in range(self._n, k, -1):           # shift rightmost first
            self._array[j] = self._array[j - 1]
        self._array[k] = value                        # store newest element
        self._n += 1

    def remove(self, value):
        """
        (value) ->
        Remove first occurrence of value( or  raise ValueError).
        """
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._array[k] == value:               # found a match!
                for j in range(k, self._n - 1):   # shift others to fill gap
                    self._array[j] = self._array[j + 1]
                self._array[self._n - 1] = None       # help garbage collection
                self._n -= 1                      # we have one less item

                return  # exit immediately
        raise ValueError("value not found")     # only reached if no match

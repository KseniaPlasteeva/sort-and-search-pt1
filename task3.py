class OrderedArrayIndexer:
    """
    Class for efficient searching of element indices in an array.
    
    Allows finding the index of a given element in O(log n) time using
    a preprocessing approach with a sorted index map, while keeping
    the original data unsorted.
    """
    
    def __init__(self, data=None):
        """
        Initializes the indexer with the provided data array.
        
        Args:
            data: Any array of data (default None - empty array)
        """
        self._original_data = data if data is not None else []
        self._index = self._create_index()


    def _create_index(self):
        index_map = {}
        for i, val in enumerate(self._original_data):
            if val not in index_map:
                index_map[val] = i
        return index_map


    def get(self, element):
        """
        Finds the index of an element in the original data array.
        
        If the element appears multiple times, returns the index
        of its first occurrence. If the element is not present, returns -1.
        
        Args:
            element: The element whose index needs to be found
            
        Returns:
            Index of the element in the original array or -1 if the element is not present
            
        Example:
            >>> indexer = OrderedArrayIndexer([7, 3, 1, 3, 5])
            >>> indexer.get(3)
            1
            >>> indexer.get(7)
            0
            >>> indexer.get(6)
            -1
        """
        if element in self._index:
            return self._index[element]
        else:
            return -1
    
    def update_data(self, new_data: list):
        """
        Updates the data array for indexing.
        
        Args:
            new_data: Any data array, sorted or unsorted
            
        Returns:
            None
        """
        self._original_data = new_data
        self._index = self._create_index()
    
    
    @property
    def size(self) -> int:
        """
        Property that returns the size of the current data array.
        
        Returns:
            Number of elements in the array
        """
        return len(self._original_data)
    
    @property
    def original_data(self) -> list:
        """
        Property that returns a copy of the original data array.
        
        Returns:
            Copy of the original unsorted data array
        """
        return self._original_data[:]
    
    @classmethod
    def from_unsorted(cls, unsorted_data: list):
        """
        Creates a new indexer from unsorted data.
        
        Args:
            unsorted_data: Unsorted data array
            
        Returns:
            OrderedArrayIndexer: New instance with the original data preserved
        """
        return cls(unsorted_data)
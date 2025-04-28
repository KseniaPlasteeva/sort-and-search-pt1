class MultTable:
    """
    A class representing a multiplication table that provides methods for efficiently finding
    the kth element in the sorted list of all values in the table.
    """
    
    def __init__(self, rows: int, cols: int):
        """
        Initializes a multiplication table of the specified size.
        
        Args:
            rows (int): Number of rows in the table (from 1 to rows)
            cols (int): Number of columns in the table (from 1 to cols)
            
        Raises:
            ValueError: If rows or cols are less than or equal to 0
        """
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and cols must be greater than 0")
        self._rows = rows
        self._cols = cols
    
    def find_kth_element(self, k: int) -> int:
        """
        Finds the kth element in the multiplication table when all elements are sorted in ascending order.
        
        Args:
            k (int): Position of the element to find (from 1 to rows*cols)
            
        Returns:
            int: The value of the kth element
            
        Raises:
            ValueError: If k is outside the valid range
            
        Examples:
            >>> table = MultTable(3, 3)
            >>> table.find_kth_element(7)
            6
            >>> table = MultTable(5, 3)
            >>> table.find_kth_element(11)
            8
        """
        if not (1 <= k <= self.size):
            raise ValueError
        
        low = 1
        high = self.size
        
        while low <= high:
            mid = (low + high) // 2
            count = self._count_less_equal(mid)
            
            if count < k:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
    

    def _count_less_equal(self, value: int) -> int:
        count = 0
        for i in range(1, self._rows + 1):
            count += min(value // i, self._cols)
        return count
    
    @property
    def size(self) -> int:
        """
        Property that returns the total number of elements in the table.
        
        Returns:
            int: Product of the number of rows and columns
        """
        return self._rows * self._cols
    
    def get_value(self, row: int, col: int) -> int:
        """
        Returns the value in the multiplication table cell with the given coordinates.
        
        Args:
            row (int): Row number (from 1 to rows)
            col (int): Column number (from 1 to cols)
            
        Returns:
            int: Product of row and col
            
        Raises:
            ValueError: If coordinates are outside the table
        """
        if not (1 <= row <= self._rows and 1 <= col <= self._cols):
            raise ValueError
        return row * col

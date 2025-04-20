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
        pass
    
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
        pass
    
    @property
    def size(self) -> int:
        """
        Property that returns the total number of elements in the table.
        
        Returns:
            int: Product of the number of rows and columns
        """
        pass
    
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
        pass

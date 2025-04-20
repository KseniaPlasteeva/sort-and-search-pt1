class ChocolateOptimizer:
    """
    A class for optimizing chocolate piece sizes.
    
    Allows finding the maximum possible piece size that enables
    dividing all available chocolates among a specified number of people.
    """
    
    def __init__(self, chocolates=None):
        """
        Initializes the optimizer with a given set of chocolates.
        
        Args:
            chocolates (list): List of chocolate lengths (default None - empty list)
        """
        pass
    
    def find_max_piece_size(self, friends: int) -> float:
        """
        Finds the maximum possible chocolate piece size.
        
        Args:
            friends (int): Number of friends to distribute chocolates to
            
        Returns:
            float: Maximum possible piece size or 0 if division is impossible
            
        Examples:
            >>> optimizer = ChocolateOptimizer([1, 2, 3, 4, 5])
            >>> optimizer.find_max_piece_size(3)
            3.0
            >>> optimizer = ChocolateOptimizer([10, 10, 10])
            >>> optimizer.find_max_piece_size(10)
            2.5
        """
        pass

    
    def update_chocolates(self, new_chocolates: list[int]) -> None:
        """
        Updates the list of chocolates.
        
        Args:
            new_chocolates (list): New list of chocolate lengths
            
        Returns:
            None
        """
        pass
    
    @property
    def total_length(self) -> int:
        """
        Property that returns the total length of all chocolates.
        
        Returns:
            int: Sum of all chocolate lengths
        """
        pass
    
    @property
    def chocolate_count(self) -> int:
        """
        Property that returns the number of chocolates.
        
        Returns:
            int: Number of chocolates
        """
        pass
    
    @classmethod
    def from_string(cls, chocolate_string: str) -> 'ChocolateOptimizer':
        """
        Creates an optimizer from a string of chocolate lengths separated by spaces.
        
        Args:
            chocolate_string (str): String of chocolate lengths, e.g., "1 2 3 4 5"
            
        Returns:
            ChocolateOptimizer: New instance with the specified chocolates
            
        Raises:
            ValueError: If the string contains invalid values
        """
        pass

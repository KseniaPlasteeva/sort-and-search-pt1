class ImpossibleToVisualize(Exception):
    """Exception that is raised when the array cannot be transformed into a wave pattern for visualization."""
    pass

class FinancialDataVisualizer:
    """
    Class for visualizing financial data using various transformations.
    
    Provides methods for transforming financial data into formats
    that improve visual representation and simplify analysis.
    """

    def transform_to_wave(self, data: list[float]) -> None:
        """
        Transforms an array into a wave pattern in-place.
        
        Wave pattern means:
        - Elements with odd indices (1, 3, 5, ...) should be greater than their neighbors
        - Elements with even indices (0, 2, 4, ...) should be less than their neighbors
        
        Arguments:
            data: List of numbers to transform
            
        Returns:
            None (the array is modified in-place)
            
        Raises:
            ImpossibleToVisualize: If the array cannot be transformed into a wave pattern
            
        Examples:
            >>> visualizer = FinancialDataVisualizer()
            >>> data = [6, 2, 3, 8, 11, 2]
            >>> visualizer.transform_to_wave(data)
            >>> data
            [3, 11, 2, 8, 2, 6]
        """
        if len(data) < 3:
            if len(data) == 1 or (len(data) == 2 and data[0] == data[1]):
                raise ImpossibleToVisualize("Невозможно преобразовать массив")
            else:
                return
            

        data_sorted = sorted(data)
        n = len(data)
        result = [0] * n

        mid = n // 2
        result[1::2] = data_sorted[mid:]
        result[0::2] = data_sorted[:mid]

        for i in range(n - 1):
            if (i % 2 == 0 and result[i] >= result[i+1]) or (i % 2 != 0 and result[i] <= result[i+1]):
                 raise ImpossibleToVisualize

        data[:] = result[:]
        

    def is_wave_pattern(self, data: list[float]) -> bool:
        """
        Checks if an array is in wave pattern.
        
        Arguments:
            data: List of numbers to check
            
        Returns:
            True if the array represents a wave pattern, False otherwise
            
        Examples:
            >>> visualizer = FinancialDataVisualizer()
            >>> visualizer.is_wave_pattern([3, 11, 2, 8, 2, 6])
            True
            >>> visualizer.is_wave_pattern([1, 2, 3, 4, 5])
            False
        """
        for i in range(len(data) - 1):
            if (i % 2 == 0 and data[i] >= data[i+1]) or (i % 2 != 0 and data[i] <= data[i+1]):
                return False

        return True
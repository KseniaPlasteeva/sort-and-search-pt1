class SatelliteCalculator:
    """
    Calculator for performing mathematical operations on mini-satellites.
    
    This class provides efficient implementations of mathematical functions
    optimized for processors with limited resources and
    without hardware support for floating-point operations.
    """
    
    def int_sqrt(self, x: int) -> int:
        """
        Calculates the integer part of the square root of x using binary search.
        
        Args:
            x: A non-negative integer
            
        Returns:
            The integer part of the square root of x
            
        Example:
             calc = SatelliteCalculator()
             calc.int_sqrt(16)
            4
             calc.int_sqrt(8)
            2
        """
        if x == 0:
            return 0
        
        min = 0
        max = x
        while min <= max:
            mid = (min + max) // 2
            check = mid * mid

            if check == x:
                return mid
            elif check > x:
                max -= 1 
            elif check < x:
                min += 1
            
        return max
    

class MathOperations:
    @staticmethod
    def add(a, b):
        """
        Adds two numbers and returns the result.
        
        Parameters:
        a (int, float): The first number.
        b (int, float): The second number.
        
        Returns:
        int, float: The sum of a and b.
        """
        return a + b

    @staticmethod
    def subtract(a, b):
        """
        Subtracts the second number from the first number and returns the result.
        
        Parameters:
        a (int, float): The first number.
        b (int, float): The second number.
        
        Returns:
        int, float: The difference of a and b.
        """
        return a - b

    @staticmethod
    def multiply(a, b):
        """
        Multiplies two numbers and returns the result.
        
        Parameters:
        a (int, float): The first number.
        b (int, float): The second number.
        
        Returns:
        int, float: The product of a and b.
        """
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Divides the first number by the second number and returns the result.
        
        Parameters:
        a (int, float): The first number.
        b (int, float): The second number.
        
        Returns:
        float: The quotient of a and b.
        
        Raises:
        ValueError: If the second number is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Performs addition.
        Does not access class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Performs multiplication.
        Accesses class-level data via 'cls'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

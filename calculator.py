class Calculator:
    def add(self, left, right):
        return left + right

    def divide(self, left, right):
        if right == 0:
            raise ZeroDivisionError("division by zero")
        return left / right

"""Python serial number generator."""

class SerialGenerator:
    
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.current + 1}>"

    
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Initialize the serial generator with the starting number"""
        self.start = start
        self.current = start

    def generate(self):
        """Return the next number (sequentially)"""
        self.current += 1
        return self.current

    def reset(self):
        """Reset number to the original start number"""
        self.current = self.start


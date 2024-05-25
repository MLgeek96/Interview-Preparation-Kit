class FibonacciSequence:
    def __init__(self):
       self.start = 1
       self.stop = 1

    def __iter__(self): 
        return self

    def __next__(self):
       current = self.start
       self.start, self.stop = self.stop, self.start + self.stop
       return current

if __name__ == "__main__":
    iterator = iter(FibonacciSequence())
    for i in range(20):
        print(next(iterator))
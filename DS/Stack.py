class Stack(object):
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        self.data.pop()

    def peek(self):
        return self.data[-1]

    def prints(self):
        for i in reversed(range(0, len(self.data))):
            print self.data[i]


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print s.peek()
    s.pop()
    print s.peek()
    s.prints()

if __name__ == "__main__":
    main()

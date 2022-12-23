
class Empty(RuntimeError):
    pass
class ListStack:
    def __init__(self):
        self.data = []


    def __len__(self):

        return len(self.data)


    def is_empty(self):
        return len(self.data) == 0


    def push(self,e):

        self.data.append(e)


    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")

        return self.data.pop()


    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")

        return self.data[-1]


if __name__ == '__main__':

    s = ListStack()

    for i in range(11):
        s.push(i)
    try:
        for i in range(50):
            print(s.pop())
    except Empty:
        pass

    print(len(s))
    

    

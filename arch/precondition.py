class Precondition(list):

    def __init__(self):
        super(Precondition, self).__init__()


if __name__ == "__main__":
    cond = Precondition()
    cond.append("ABC")
    cond.append("DEF")
    print(cond)
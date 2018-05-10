class Step(list):

    def __init__(self):
        super(Step, self).__init__()


if __name__ == "__main__":
    step = Step()
    step.append("ABC")
    step.append("DEF")
    print(step)
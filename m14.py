class Trainer:
    def __init__(self, name, max_level):
        self.name = name
        self.max_level = max_level


def read_data():
    found = set()
    trainers = []
    with open("contest.txt", "r") as file:
        for line in file:
            trainer, *pakuris = line.split(",")
            max_level = -1
            for pakuri in pakuris:
                name, level = pakuri.split("-")
                level = int(level)
                found.add(name)
                if level > max_level:
                    max_level = level
            trainers.append(Trainer(trainer, max_level))
    return trainers, found


def main():
    trainers, pakuri = read_data()
    winner = max(trainers, key=lambda t: t.max_level)
    with open("winner.txt", "w") as file:
        file.write(winner.name)
    with open("pakuri.txt", "w") as file:
        file.write("\n".join(sorted(pakuri)))


if __name__ == "__main__":
    main()
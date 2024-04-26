import shelve


class Save:

    def __init__(self) -> None:
        self.file = shelve.open('scores_data')

    def save(self, name, score):
        if name in self.file.keys():
            if score > self.file[name]:
                self.file[name] = score
        else:
            self.file[name] = score

    def print_table(self):
        highscores = sorted(self.file.items(), key=lambda item: item[1], reverse=True)
        return highscores

    def close(self):
        self.file.close()

class InputReader:

    def __init__(self):
        self.lines = []
        self.cars = {}

    def read_data(self, filepath):
        with open(filepath) as f:
            lines = f.readlines()
        for line in lines:
            self.lines.append(line.strip())

    def parse_lines(self):
        for line in self.lines:
            tokenized_line = line.split(",")
            data_str = [tokenized_line[0], tokenized_line[1], tokenized_line[2]]
            self.cars[tokenized_line[0]] = data_str

    def print_cars(self):
        print(self.cars)

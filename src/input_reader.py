class InputDatePlateData:

    def __init__(self):
        self.lines = []
        self.plate_str = ""
        self.date_str = ""
        self.hour_str = ""

    def read_data(self, filepath):
        with open(filepath) as f:
            lines = f.readlines()
        for line in lines:
            self.lines.append(line.strip())

    def parse_lines(self):
        for line in self.lines:
            tokenized_line = line.split(",")
            self.plate_str = str(tokenized_line[0].split(","))
            self.date_str = str(tokenized_line[1].split(","))
            self.hour_str = str(tokenized_line[2].split(","))


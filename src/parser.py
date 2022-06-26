from typing import List

from src.input_data import InputData


class Parser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.lines = []
        self.parsed_data = []

    def read_data(self):
        with open(self.filepath) as f:
            lines = f.readlines()
        for line in lines:
            self.lines.append(line.strip())

        for line in self.lines:
            tokenized_line = line.split(",")
            self.parsed_data.append(InputData(tokenized_line[0], tokenized_line[1], tokenized_line[2]))

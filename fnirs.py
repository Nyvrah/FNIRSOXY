import os

class Fnirs():
    old = [0,0]
    new = [0,0]
    change = ['gray','gray']

    def __init__(self):
        self.data_folder = "data/" + os.listdir('data')[0] + "/"
        self.nir_file = open(self.data_folder + [f for f in os.listdir(self.data_folder) if f.endswith('.oxy')][0], "r")
        for _ in range(10): self.next_line()
        self.size = len(self.line)-2

    def next_line(self):
        self.line = self.nir_file.readline().split()
    
    def get_avg(self):
        self.old = self.new
        self.new = [0,0]
        for i in range(1, 19):
            self.new[i%2-1] += float(self.line[i])/18
        for i in range(2):
            if self.new[i] > self.old[i]: self.change[i] = '#90EE90'
            elif self.new[i] < self.old[i]: self.change[i] = '#FFCCCB'
            else: self.change[i] = 'lightgray'
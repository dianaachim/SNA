import csv
import os
from _csv import writer
from csv import reader


class Reader:
    def __init__(self):
        self.country_codes_dict = {}
        self.nodes = []

    def mapCountryCodesToNrAndEliminateDuplicates(self):
        lista = []
        write_obj = open('final_result.csv', 'w+', newline='')
        csv_writer = writer(write_obj)
        with open('data.csv', 'r') as read_obj:
            csv_reader = reader(read_obj, delimiter=',')
            line = next(csv_reader)
            if line is not None:
                for row in csv_reader:
                    if [row[0], row[1]] not in lista:
                        lista.append([row[0], row[1]])
                        csv_writer.writerow([str(self.country_codes_dict[row[0]]), str(self.country_codes_dict[row[1]])])
                    if row[0] not in self.nodes:
                        self.nodes.append(row[0])
                    if row[1] not in self.nodes:
                        self.nodes.append(row[1])
            print(len(self.nodes)) #cate noduri avem

    def readCountryCode(self):
        with open('country-codes.csv', 'r') as read_obj:
            csv_reader = reader(read_obj, delimiter=',')
            line = next(csv_reader)
            idx = 0
            if line is not None:
                for row in csv_reader:
                    self.country_codes_dict[row[0]] = idx
                    idx += 1

    def readCSVFiles(self, filename): # nu folosim asta
        with open('20200130060000.export.CSV', 'r') as read_obj:
            csv_reader = reader(read_obj, delimiter='\t')
            line = next(csv_reader)
            if line is not None:
                for row in csv_reader:
                    if row[37] != '' and row[45] != '' and row[37] != row[45] and "coronavirus" in row[60]:
                        country_codes_news = row[37] + ' ' + row[45] + ' ' + row[60]
                        print(country_codes_news)

    def readCSV(selfself):
        write_obj = open('data.csv', 'w+', newline='')
        csv_writer = writer(write_obj)
        for file in os.listdir("C:\\Users\\Alexandra\\Desktop\\CoronaNews"):
            if file.endswith(".CSV"):
                os.chdir(r'C:\Users\Alexandra\Desktop\CoronaNews')
                with open(file, 'r', encoding='utf8') as read_obj:
                    csv_reader = reader(read_obj, delimiter='\t')
                    line = next(csv_reader)
                    if line is not None:
                        for row in csv_reader:
                            if row[37] != '' and row[45] != '' and row[37] != row[45] and "coronavirus" in row[60]:
                                csv_writer.writerow([row[37], row[45], row[60]])
        write_obj.close()


r = Reader()
r.readCountryCode()
r.mapCountryCodesToNrAndEliminateDuplicates()
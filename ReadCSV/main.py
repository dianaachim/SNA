from csv import reader


# skip first line i.e. read header first and then iterate over each row od csv as a list

class Reader:
    def __init__(self):
        self.country_codes_dict = {}
        self.nodes = []

    def readCountryCode(self):
        with open('country-codes.csv', 'r') as read_obj:
            csv_reader = reader(read_obj, delimiter=',')
            line = next(csv_reader)
            # Check file as empty
            idx = 0
            if line != None:
                # Iterate over each row after the header in the csv
                for row in csv_reader:
                    self.country_codes_dict[row[0]] = idx
                    idx += 1

    def readCSV(self):
        with open('20200130000000.export.CSV', 'r') as read_obj:
            csv_reader = reader(read_obj, delimiter='\t')
            line = next(csv_reader)
            # Check file as empty
            if line != None:
                # Iterate over each row after the header in the csv
                for row in csv_reader:
                    # row variable is a list that represents a row in csv
                    if row[37] != '' and row[45] != '' and row[37] != row[45] and \
                            ("emergency" in row[60] and "virus" in row[60]):
                        ceva = row[37] + ' ' + row[45] + ' ' + row[60]
                        print(ceva)
                        #self.nodes.append(ceva) dezactivam momentan sa putem copia liniile


r = Reader()
r.readCSV()
r.readCountryCode()
#print(r.nodes)
#print(r.country_codes_dict)
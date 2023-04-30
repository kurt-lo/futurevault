import csv
def getTerms(filename):
    terms = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if "INDEX" not in row[0]:
                terms.append(row[0])
    return terms 

def getPrograms(filename):
    programs = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            for header in row:
                if "INDEX" not in header and "TERM" not in header and "DATE" not in header and "ACADEMIC YEAR" not in header:
                    programs.append(header)
            break
    return programs

def getAllData(filename):
    data = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

# def getProgramIndex(program, data):
#     for 



def getTermIndex(term, data):
    for row in data:
        if term in row:
            return data.index(row)
    return None

def getProgramIndex(program, data):
    for row in data:
        if program in row:
            return row.index(program)
    return None

def clearFile(filename):
    with open(filename, "w") as csvfile:
        csvfile.truncate()


def writeData(write_from_file, write_to_file):
    from_data = getAllData(write_from_file)
    to_data = getAllData(write_to_file)
    programs = getPrograms(write_from_file)
    terms = getTerms(write_from_file)
    INDEX_TITLE = to_data[0][0]
    for term in terms:
        arr = []
        to_term_index = getTermIndex(term, to_data)
        from_term_index = getTermIndex(term, from_data)

        if to_term_index is None:
            to_data.append(from_data[from_term_index])
        else:
            for program in programs:
                from_program_index = getProgramIndex(program, from_data)
                from_program_data = from_data[from_term_index][from_program_index]
                to_program_index = getProgramIndex(program, to_data)
                to_data[to_term_index][to_program_index] = from_program_data
    
    to_data[0][0] = INDEX_TITLE

    with open(write_to_file, 'w', newline='') as f:
        writer = csv.writer(f)
        clearFile(write_to_file)

        #CHANGE "from_data" into "to_data" to write to the file without clearing other data
        # IF "from_data" is set it will override the whole data of the file
        # IF "to_data" is set it will manipulate the data of the file
        for data in from_data:
            writer.writerow(data)



def getFuture(terms):
    data = []
    term = terms[len(terms) - 1]
    splitted = term.split(":")
    years = splitted[1].strip().split("-")
    years[0] = int(years[0])
    years[1] = int(years[1])
    term_number = None
    for char in splitted[0]:
        if char.isdigit():
            term_number = int(char)
            break

    for i in range(4):
        if term_number == 3:
            term_number = 1
            years[0] += 1
            years[1] += 1
            data.append(f"TERM1 : {years[0]}-{years[1]}")
        else:
            term_number += 1
            data.append(f"TERM{term_number} : {years[0]}-{years[1]}")
    return data
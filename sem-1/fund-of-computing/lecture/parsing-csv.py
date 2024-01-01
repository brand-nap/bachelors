# Parsing a CSV

def main():
    readPath = "../resources/historical-census.csv"
    wPath = "../resources/parsed-data.csv"
    
    meta, db = csvToDict(readPath)
    meta, db = addIndex(meta, db)

    wFile = open(wPath, "w")
    print(','.join(meta), file=wFile)
    
    for index, row_id, name, area_type, inc_year, county_inc, pop_year, population, name_type in zip(db[meta[0]], db[meta[1]], db[meta[2]], db[meta[3]], db[meta[4]], db[meta[5]], db[meta[6]], db[meta[7]], db[meta[8]]):

        if pop_year == 1890:
            rowList = []
            for i in range(8):
                rowList.append(str(db[meta[i]][index]))
            print(','.join(rowList),file=wFile)
          
    wFile.close()
    
    '''
    simulates sql command:

            SELECT * FROM historical-census
            WHERE population_year == 1890;
    '''

def csvToDict(filePath):
    '''
    transforms a csv into a dictionary: keys are the metadata, values are lists of each column
    dict simulates a database with rows and columns

    parameter: the file path
    returns: a database with maleable values or false if file does not exist. 
    '''

    try: 
        file = open(filePath, "r")

        #create my dict with the metadata as the keys
        metadata = file.readline()
        metadata = metadata[0:-1] if metadata[-2:-1] == '\n' else metadata
        metadata = metadata.split(',')
        
        db = {k:[] for k in metadata}

        #read each line and store them in the appropriate columns
        line = file.readline()
        while line != '':
            row = line.split(',');
            for k, val in zip(metadata, row):
                # try to store as a number, otherwise store as string
                try:
                    db[k].append(eval(val))
                except:
                    val = removeSpaces(val)
                    db[k].append(val)
            line = file.readline()
            
        file.close()
        return metadata, db
    
    except FileNotFoundError:
        print("Read file doesn't exist at this file path.")
        
    except Exception as e:
        print(e, "\nWhat did you do?!? Stop trying to break me, hacker!")
        
    return False

def addIndex(meta, db):
    try:
        length = len(db[meta[0]])
        db['index'] = []
        meta = ['index'] + meta
        for i in range(length):
            db['index'].append(i)
            
    except Exception as e:
        print(e, "Error while adding Index")
        
    return meta, db
        
        
def removeSpaces(string):
    try:
        while string[-1] == ' ':
            string = string[0:-1]
    except:
        string = string #either an empty value or a value of exclusively spaces
    return string

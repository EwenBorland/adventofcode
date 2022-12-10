import sys

def getInputPath(year, day, part):
    return f'scripts/year_{year}/day_{day}/part_{part}/input.txt'

def loadInput(file_path):
    
    with open(file_path, 'r') as f:
        file_data = f.readlines()

    return [l.strip('\n') for l in file_data]

def parse_args():
    if len(sys.argv) != 4:
        # print("Incorrect number of arguments")
        return 0, 0, 0
    return sys.argv[1], sys.argv[2], sys.argv[3]

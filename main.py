import sys
import os

"""
Dont need a database service for this utility, too much overhead.
Also want to reduce complexity with additional dependency installations.
"""

class Player:
    def __init__(self, rating=1200, **args):
        # first_name, last_name, rating
        self.rating = rating
        self.__dict__.update(args)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.rating}"

class PlayerResult:
    def __init__(self, player, result):
        self.player = player
        self.result = result 

def parse(filepath):
    """
    Parse a file expected to contain crosstable results retrieved from swissonlinetournament
    """
    results = list()
    try:
        with open(filepath, 'r') as f:
            for line in f:
                atoms = line.split()
                player = Player(first_name=atoms[1], last_name=atoms[2])
                result = atoms[4:-2]
                results.append(PlayerResult(player, result))
    except Exception as e:
        print("Couldn't read input file", e)
        sys.exit(1)  
    return results

def process(results):
    """
    Calculate new ratings for each player
    """
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <file>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print("File does not exist")
        sys.exit(1)

    parse(filepath)
    print("OK")
    sys.exit(0)
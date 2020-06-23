import sys
import re

def countCode(string):
    result = re.findall("co.e", string)
    return len(result)

print(countCode(sys.argv[1]))   
import regex as re
import time

def match(test_str):
    regex_input = r'A(B|C+)+D'

    matches = re.finditer(regex_input, test_str)

    return matches

def printkey(matches):
    count = 0
    for match in matches:
        count +=1
    if count == 0:
        print("Match Not Found")
    else:
        print("Match Found")

def main():
    # time is in seconds
    start = time.time()
    text = input("Enter String to Match:")
    key = match(text)
    end = time.time()
    printkey(key)
    print(end - start)


main()

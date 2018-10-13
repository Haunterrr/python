import re

input_filename = "../dumpfile.txt"         # Path to datafile
result_filename = "../results.txt"

inputfile = open(input_filename, mode='r', encoding='Latin-1')
resultfile = open(result_file, mode='w', encoding='Latin-1')
mytext = inputfile.read()

lookfor = r"[\w.-]+@[A-Za-z-]+\.[\w.]+"                 # For Searching Mails
#lookfor = r"\w.+@[A-Za-z.-]+@[A-Za-z.-]+\.[\w.]+"


results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item + "\n")

print("Total: " + str(len(results)))

import os

f = open('index.md', 'w')

f.write("# Superintendents Report Archive\n\n\n")
f.write("\n-----------------\n\n")

for report_type in ['Week', 'Month']:
    folder = 'reports/' + report_type.lower() + "/"

    next = folder + 'next.txt'

    links = os.listdir(folder)

    links.remove('next.txt')
    links.sort()
    links.reverse()
    f.write("## " + report_type + "ly info:\n")
    f.write("[The next (unofficial) " + report_type.lower() +"ly report](" + next + ") \n")
    f.write("\n")
    if links:
        f.write("[The latest " + report_type.lower() +"ly report](" + folder + links.pop(0) + ") \n")
        f.write("\n")
        if links:
            f.write("The rest: \n")
            f.write("\n")
            for string in links:
               f.write("[" + string + "](" + folder + string + ") \n")
               f.write("\n")
    f.write("\n-----------------\n\n")
import os

f = open('index.md', 'w')

for type in ['week', 'month']:
    folder = 'reports/' + type + "/"

    next = folder + 'next.txt'

    links = os.listdir(folder)

    links.remove('next.txt')
    links.sort()
    links.reverse()

    f.write("Superintendents Report Archive:\n")

    f.write("[The next (unofficial) " + type +"ly report](" + next + ") \n")
    f.write("\n")
    if links:
        f.write("[The latest " + type +"ly report](" + folder + links.pop(0) + ") \n")
        f.write("\n")
        f.write("The rest: \n")
        f.write("\n")
        for string in links:
           f.write("[" + string + "](" + folder + string + ") \n")
           f.write("\n")
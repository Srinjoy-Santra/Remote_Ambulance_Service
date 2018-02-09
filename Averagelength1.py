import csv

orgpath = "TotalNHacc.csv"  # original file

with open(orgpath, "r") as file:
    csvr = csv.reader(file)
    orgpath = "NHlength.csv"
    with open(orgpath, "r") as file1:
        csvr1 = csv.reader(file)
        newpath = "NHlengthBlacklist.csv"  # new file
        with open(newpath, 'w') as nfile:
            csvw = csv.writer(nfile)

        header = next(csvr)
        avg = []
        dictionary = {"Growth Rate": "State/UT"}
        x = 0
        for line in csvr:
            x += 1
            try:
                avgl = int(str(line[-1])) - int(str(line[1]))
                avgl = avgl / (len(line) - 1)
                avg.append(avgl)
                dictionary[avgl] = str(line[0])

                # print (avgl,line[0])

            except:
                pass

        csvw.writerow(["State/UT", "Growth Rate"])

        avg.sort(reverse=True)
        for i in range(0, 5, 1):
            print(dictionary[avg[i]])
            csvw.writerow([dictionary[avg[i]], avg[i]])
            print([dictionary[avg[i]], avg[i]])
            # print("Redo")
            # print(dict,x)

    nfile.close()

file.close()

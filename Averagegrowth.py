import csv

orgpath ="TotalNHacc.csv"#original file
with open(orgpath,"r") as file :
    csvr=csv.reader(file)
    newpath ="TotalNHaccBlacklist.csv"#new file
    with open(newpath,'w') as nfile:
        csvw=csv.writer(nfile)


        header=next(csvr)
        avg=[]
        dict={"Growth Rate":"State/UT"}
        x=0
        for line in csvr:
            x+=1
            try :
                avgl=int(str(line[-1]))-int(str(line[1]))
                avgl=avgl/(len(line)-1)
                avg.append(avgl)
                dict[avgl]=str(line[0])
                
                #print (avgl,line[0])
                
            except :
                pass

        csvw.writerow(["State/UT","Growth Rate"])

        avg.sort(reverse=True)
        for i in range(0,len(avg),1):
            print(dict[avg[i]])
            csvw.writerow([dict[avg[i]],avg[i]])
            print([dict[avg[i]],avg[i]])
        #print("Redo")
        #print(dict,x)
        
    nfile.close()

file.close()



        
            
            





 


import csv,math

orgpath ="TotalNHaccBlacklist.csv"#original file
with open(orgpath,"r") as file :
    csvr=csv.DictReader(file)
    names=[]
    
    dict={"State/UT":"Length"}
    for f in csvr:
        names.append(str(f['State/UT']))
        print(f['State/UT'])
        
        
file.close()

'''names=set(names)
#names.remove('[]')
for f in names:
        if(str(f) is '[]'):
            remove(f)
#'''
#print(names)
    
orgpath ="NHlength.csv"#original file
with open(orgpath,"r") as dile :
    csvr=csv.reader(dile)
    newpath ="NHlengthBlacklist.csv"#new file
    with open(newpath,'w') as nfile:
        csvw=csv.writer(nfile)

        
        header=next(csvr)
        avg=[]
        #dict={"Growth Rate":"State/UT"}
        x=0
        csvw.writerow(["State/UT","Length in kms.","Proposed no.of centres"])
        for line in csvr:
            for ele in names:
                #print(str(ele),str(line),str(line[1]))
                #print(ele)
                if(str(ele)==str(line[0]))and ele is not list():
                    print(ele,line[1])
                    csvw.writerow([str(ele),str(line[1]),math.ceil(int(str(line[1]))*2/100)])
                    #print([str(ele),str(line[1])])


        print(23)
                
            


        
    nfile.close()

file.close()



        
            
            





 


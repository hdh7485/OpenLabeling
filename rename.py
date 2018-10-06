import os 
path = "/Users/dongheehan/Downloads/construct/"
for filename in os.listdir(path):
    #if filename[-3:] == "txt": 
    #print(filename[:12])
    #print(filename[12:])
    os.rename(path+filename, path+filename[:12]+"_"+filename[12:])

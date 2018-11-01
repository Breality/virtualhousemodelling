import glob
folders = glob.glob("C:\\Users\\MLH-Admin\\Desktop\\New Models\\*")
d = {} 
for item in folders:
    obj = glob.glob(item+"\\"+"*.obj")[0]
    obj = (obj.split("\\")[-1]).split(".")[0]
    
    d[obj]=item.split("\\")[-1]
    
string_to_print = "{"
for item in d:
    print(1)
    string_to_print+='{"'+d[item]+'" ,"'+item+'"},'
string_to_print+="}"

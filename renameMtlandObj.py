import glob
from shutil import copyfile
folders = glob.glob("C:\\Users\\MLH-Admin\\Desktop\\New Models\\*")
folder = "C:\\Users\\MLH-Admin\\Desktop\\Final Models\\"
for i in folders:
    filename = i.split("\\")[-1]
    print(filename)
    obj = glob.glob(i+"\\"+"*.obj")[0]
    mtl = glob.glob(i+"\\"+"*.mtl")[0]
    print(mtl,obj)

    copyfile(mtl,folder+filename+".mtl")
    copyfile(obj,folder+filename+".obj")

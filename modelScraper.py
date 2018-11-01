import glob,zipfile
zipFiles = glob.glob("C:\\Users\\MLH-Admin\\Desktop\\Models\\*")
for i in zipFiles:
    file = (i.split("\\")[-1]).split(".")[0]
    zipf = zipfile.ZipFile(i)
    zipf.extractall("C:\\Users\\MLH-Admin\\Desktop\\New Models\\"+file)
    zipf.close()

import fbx

# Create an SDK manager                                                                                           
manager = fbx.FbxManager.Create()

# Create a scene
scene = fbx.FbxScene.Create(manager, "")

# Create an importer object                                                                                                  
importer = fbx.FbxImporter.Create(manager, "")

# Path to the .obj file
milfalcon = "C:\\Users\\MLH-Admin\\Desktop\\New Models\\ANDV2361\\ANDV2361_v6_LOD2.obj"

# Specify the path and name of the file to be imported                                                                            
importstat = importer.Initialize(milfalcon, -1)

importstat = importer.Import(scene)

# Create an exporter object                                                                                                  
exporter = fbx.FbxExporter.Create(manager, "")

save_path = "C:\\Users\\MLH-Admin\\Desktop\\New Models\\ANDV2361\\ANDV2361_v6_LOD2.fbx"


# Specify the path and name of the file to be imported                                                                            
exportstat = exporter.Initialize(save_path, -1)

exportstat = exporter.Export(scene)

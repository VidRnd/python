import os

structure_folder = {"my_project":[
    {"settings": []},
    {"mainapp":[]},
    {"adminapp":[]},
    {"authappввв":[]},
    {"2":[]},
    {"3":[]}
]}
for project, foldders in structure_folder.items():
    for folder in foldders:
        print(folder)
        for i in folder.keys():
            print(i)
            os.makedirs(os.path.join( project,i),exist_ok = True)

# rename_folder = ["adminapp",'3']
# if os.path.exists("my_project\\"+rename_folder[0]) and not os.path.exists("my_project\\"+rename_folder[1]):
#     os.rename ( f'my_project\\{rename_folder[0]}' , f'my_project\\{rename_folder[1]}' )
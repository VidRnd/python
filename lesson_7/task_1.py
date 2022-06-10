import os

structure_folder = {"my_project":[
    {"settings": []},
    {"mainapp":[]},
    {"adminapp":[]},
    {"authappввв":[]},
    {"2":[]}
]}

dir_name = 'sample_dir'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

for project, foldders in structure_folder.items():
    print(project, foldders)
    for folder in foldders:
        print(folder)
        for i in folder.keys():
            print(i)
            os.makedirs(os.path.join( project,i),exist_ok = True)



rename_folder = ["adminapp",'w']
if os.path.exists("my_project\\"+rename_folder[0]) and not os.path.exists("my_project\\"+rename_folder[1]):
    os.rename ( f'my_project\\{rename_folder[0]}' , f'my_project\\{rename_folder[1]}' )
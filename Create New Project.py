import os

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    print(f"Folder created: {folder_path}")

def create_premiere_project_file(folder_path, project_name):
    project_file = os.path.join(folder_path, project_name + ".prproj")
    with open(project_file, "w") as f:
        f.write("Adobe Premiere project file")
    print(f"Project file created: {project_file}")

def create_folder_with_subfolders_and_project_file(folder_name, subfolder_names, project_name):
    count = 0
    while os.path.exists(folder_name):
        count += 1
        folder_name = f"{folder_name}_{count}"
        
    os.makedirs(folder_name)
    for subfolder_name in subfolder_names:
        create_folder(os.path.join(folder_name, subfolder_name))
    create_premiere_project_file(folder_name, project_name)

folder_name = "Untitled"
subfolder_names = ["Videos", "Sounds", "Assets"]
project_name = "Untitled"
create_folder_with_subfolders_and_project_file(folder_name, subfolder_names, project_name)

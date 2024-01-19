# Import modules
import os
import shutil

def create_parent_dir(path):
    """ Create main parent directory
    Parameters:
        Path(required) - where user want to create parent directory
    return:
        successfull - if directory created it return the path of that directory 
    """ 
    try:
        if path.startswith(("\\", "/")):
            path = path[1:]
        os.mkdir(path)
        return os.getcwd() + "\\" + path
    except Exception as e:
        return f"Failed- {e}"

def remove_dir(starting_characters_of_dir, empty_dir=True):
    
    dir_available: list[str] = [dir for dir in os.listdir() if dir.startswith(starting_characters_of_dir)]
    for dir in dir_available:
        if empty_dir:
            os.removedir(dir)
        else:
            shutil.rmtree(dir)


def create_subdir_files(parent_dir, pythonclasses = 20):
    # ==============Create subfolders in the main directory
    for i in range(2, int(pythonclasses)+1):  # need 19 folders
        new_dir_name: str = f"{parent_dir}/class_{i}" # Set the path
        # Create specfied subfolder
        os.mkdir(new_dir_name)
        # List of names of those files that you want to add in each folder
        file_names_in_each_dir: list[str] = [f"class_{i}.py",
                                            f"class_{i}.ipynb",
                                            f"notes.txt"]
        # Iterate through each file
        for file_name in file_names_in_each_dir:
            # Create specfied file in subfolder
            with open(f"{new_dir_name}/{file_name}", "w") as f:
                """If you want to add some content in a file you can add file name here
                otherwise it will create empty file
                """
                if file_name == "notes.txt": # File_name
                    # Content that want to add in specific file
                    content_of_txt = f"""{'='*20}What we cover in the class {i}{'='*20}
-
-
{"="*20}What's new in python 3.12.0{"="*20}
-
-
"""
                    f.write(content_of_txt)


def main():
    directory_usr_input: str = input("Enter name of parent directory: ")
    parent_folder = create_parent_dir(directory_usr_input)
    if not parent_folder.startswith("Failed"):
        create_subdir_files(parent_folder, 19)
    else:
        print(parent_folder)

if __name__ == '__main__':
    main()
    # remove_dir("python")
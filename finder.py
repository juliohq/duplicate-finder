import os

basedir = ""
namelist = []

def remove(path, ask=True):
    if ask:
        if not input(f"Do you want to remove file/directory '{path}'? [Yes, No]\n") in ["y", "Y"]:
            return
    
    # if os.path.isfile(path):
    os.remove(path)
    print(f"Removed '{path}'")

def remove_all():
    for name in namelist:
        path = basedir.join(name)
        remove(path)

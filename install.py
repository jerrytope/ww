import subprocess

def install_libraries():
    with open('requirements.txt', 'r') as file:
        libraries = file.read().splitlines()
    
    for library in libraries:
        try:
            subprocess.check_call(['pip', 'install', library])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {library}: {e}")
            continue

install_libraries()

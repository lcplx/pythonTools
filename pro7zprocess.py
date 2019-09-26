import subprocess,os
os.environ['COMSPEC']
srcPath="C:/Users/liangx/Desktop/Documents/PythonTool/download/data_objects/"
replacepath="C:/Users/liangx/Desktop/Documents/PythonTool/download/metadata/xml/data_objects/"

def extract7z(srcPath,replacepath):
    os.chdir(srcPath)
    subprocess.call(['7z','x','.\\*','-o'+replacepath,'-aoa'], shell=True)


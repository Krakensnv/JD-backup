import zipfile
from zipfile import ZipFile
import os

zip_folder = 'E:\\Shared\\DOWNLOADED\\c.zip'
destination = 'E:\\Shared\\DOWNLOADED'
pwd = '<YOUR_PASSWORD>'

with zipfile.ZipFile(zip_folder) as zf:
    zf.extractall(
        destination, pwd=pwd.encode())
        
        
# specifying the name of the zip file
file = "archive.zip"
  
# open the zip file in read mode
with ZipFile(file, 'r') as zip: 
    # list all the contents of the zip file
    zip.printdir() 
  
    # extract all files
    print('extraction...') 
    zip.extractall() 
    print('Done!')        
    
    
    
# import zipfile
# import os

os.getcwd()
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32'

myzipfile= zipfile.ZipFile('documents.zip')
myzipfile.extractall()
myzipfile.close()    
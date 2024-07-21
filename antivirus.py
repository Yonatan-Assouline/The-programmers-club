from virustotal_python import Virustotal
import os
from pprint import pprint 

folder_path=input('input the path of the file you want to scan')

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path=os.path.join(root, file)

        files = {"file": (os.path.basename(file_path), open(os.path.abspath(file_path), "rb"))}
        with Virustotal("2b1c6b561fb72a7dba657ffbe973b7de58acd7238fe11b7e7fba02424485c881") as vtotal:
            resp = vtotal.request("files", files=files, method="POST")
            pprint(resp.json())
        
        
        
       
  
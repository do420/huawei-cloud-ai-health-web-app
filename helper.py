import requests
import os
import shutil
from random import sample



def predict(file_name,parent_name,token):
    url = "https://f7bcf3d99ed24c4cbb2b30f352011bc6.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/31c96886-6656-4d08-9db5-333f7a08d406"

    
    payload = {}
    
    files=[
        ('images',(file_name,open(os.path.join(parent_name,file_name),'rb'),'image/jpeg'))
        ]
    headers = {
  'X-Auth-Token':token
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
    



import shutil
from random import sample

def randsample(folder_path,sample_no,class_name):
    shuffled_dataset_train=sample(os.listdir(os.path.join(folder_path,class_name)),sample_no)

    for file in shuffled_dataset_train:
    
        file_to_copy = os.path.join(folder_path,file)

        destination_directory_train = (os.path.join(folder_path,"shuffled","shuffled_train",class_name))
        
        shutil.move(file_to_copy, destination_directory_train)


    shuffled_dataset_val=sample(os.listdir(os.path.join(folder_path,class_name)),sample_no)

    for file in shuffled_dataset_val:
    
        file_to_copy = os.path.join(folder_path,file)

        destination_directory_val = (os.path.join(folder_path,"shuffled","shuffled_validation",class_name))
        
        shutil.move(file_to_copy, destination_directory_val)


class_names=["Benign","Malignant-early-Pre-B","Malignant-Pre-B","Malignant-Pro-B"]

for class_name in class_names:
    
  randsample(folder_path="./",sample_no=1,class_name=class_name)

     

     

     
     
     
     
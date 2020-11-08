# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import shutil

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def  CreateDirectory(path,libraryname):
     
    path = path + "/"+ libraryname
    try:
        os.mkdir(path)
    except OSError:
        print ("the directory is already exsit")
    else:
        print ("Successfully created the directory %s " % path) 
    return
      

def main():
    path2 =path() #Creating the directories
    CopyAndDisplayImages(path2) #copying images and displaying them
    
    
    
    
    
def path():
    print ("please type path: ")
    path= input()
    if path == "": 
        path = "C:/Users/oribd/Desktop"              
    print ("please type library name:" )
    libraryname =input()
    pathTrain=path+ "/"+ libraryname
    pathTest=path+ "/"+ libraryname
    CreateDirectory(path,libraryname)# creating the directory       
    pathtrain = CreateDirectory(pathTrain,"train") #creating the sub-directory train
    pathtest= CreateDirectory(pathTest,"test") #creating the sub-directory test
    return path+"/"+libraryname

def CopyAndDisplayImages(path2):
    path_to_your_files = "C:/Users/oribd/Desktop/Elay" #the path to the original images
    copy_to_path = path2 +"/test" # the path to the new sub_directory train or test
    files_list = os.listdir(path_to_your_files)#creating the list of the images
    if "/train" in copy_to_path:#if the chosen sub-directory iss train
        length=int(len(files_list)*0.7)#copying only 70% of the images
        for i in range(length):
            file = files_list[i]
            shutil.copyfile(os.path.join(path_to_your_files, file), os.path.join(copy_to_path, file))#copying the images                        
    else: # if the chosen sub-directory is test  
        for i in files_list:#copying all of the images
            file=i
            shutil.copyfile(os.path.join(path_to_your_files, file), os.path.join(copy_to_path, file)) #copying the images
    images=os.listdir(copy_to_path)#creating a list of images in the new sub-directory
    for element in images:
        img = mpimg.imread("C:/Users/oribd/Desktop/Elay/"+element)
        imgplot = plt.imshow(img)#displaying the images
        plt.show()#displaying the images
        print(element)#printing the name of the images    
        
    
   
    
    
    
    
    

if __name__ == "__main__":
    main()    
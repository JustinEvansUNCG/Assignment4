# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:08:24 2024

@author: Justin Evans
"""

import pandas as pd
import numpy as np

# This program allows a person to store their Name, major, and age into a 
# csv for safekeeping. A user can also delete, modify, and view the data in the csv 
def main() :
    req_type = input("Input I to input data, D to delete data, M to modify data, S to show data, or anything else to exit the program: ")
    
    while 1 == 1 :
        
        
        if req_type == 'I' :
            input_data()
        elif req_type == 'D' :
            delete_data()  
        elif req_type == 'M' :
            modify_data()    
        elif req_type == 'S' :
            print(pd.read_csv('UserData.csv'))
            
        else :
            break
        req_type = input("Input another command: ")
    
#Inputs a person, their major and age to a csv
def input_data() :
    
    data = pd.read_csv('UserData.csv')
    print(data)

    data.loc[len(data.index)] = [input("Input name: "), input("Input Major: "), input("Input Age: ")]
    
    
    data.to_csv('UserData.csv',index=False)
    
    
    return

#This method removes the first instance of the name a user inputs
def delete_data() :
    
    data = pd.read_csv('UserData.csv')
    
    names = data['Name']
    
    deleteRequest = input("Input the name of the person you want to remove from the system: ")
    
    for i in range(len(names)) :
        if names[i] == deleteRequest :
            data = data.drop([i])
            data.to_csv('UserData.csv', index=False)
    
    return



#Method asks for what you who and then what to modify, which is case sensitive in both instances, and then overwrites the old data 
def modify_data() :
    
    data = pd.read_csv('UserData.csv')
    
    #print(data)
    
    names = data['Name']
    major = data['Major']
    ages = data['Age']
     
    modifyRequest = input("Input the person you want to modifies data: ")
    
    for i in range(len(names)) :
        if names[i] == modifyRequest :
            modifyObject = input("What do you want to modify? (Name, Major, or Age) ")
            
            if modifyObject == "Name" :
                names = np.array(names)
                names[i] = input("Enter new name: ")
            if modifyObject == "Major" :
                major = np.array(major)
                major[i] = input("Enter new major: ")
            if modifyObject == "Age" :
                ages = np.array(ages)
                ages[i] = input("Enter new age: ")
                
            data = pd.DataFrame(list(zip(names, major, ages)))
            data.columns = ["Name", "Major", "Age"]
            data.to_csv('UserData.csv', index=False)
    
    
    
    return

#This function makes the csv and its formatting, is more of a testing function
def config_csv() :
    
    tdata = {'Name': "Josh", 'Major' : "Nutrition", 'Age' : 20}
    
    dataset = pd.DataFrame(data=tdata, index=[0])
    
    dataset.to_csv('UserData.csv',index=False)
    
    
    return




if __name__ == "__main__" :
    main()

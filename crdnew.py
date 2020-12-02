import socket


from _thread import *

import time
import sys
import json
import os.path 
from os import path


ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1222

try:
    ServerSocket1 = socket.socket()
    ServerSocket1.bind((host, port))
    ServerSocket1.close()    
except socket.error as e:
    print(str("Another Data Store Running:-Close it"))
    exit()

ServerSocket.bind((host, port))

l=[]
starttime=[]
exp=[]
dictionary ={} 
k={}


def create(key,value,time1=0):# creating and appending to json file
    if (path.exists("sample.json")):
        with open("sample.json", "r") as outfile: 
            json_object = json.load(outfile) 
        
    else:
        json_object = json.dumps(dictionary, indent = 4) 
        with open("sample.json", "w") as outfile: #initialization of the json file 
	        outfile.write(json_object) 
    if key in json_object:
        print("error-this key already exists")
    else:
        if (key.isalpha()):
            with open("sample.json", "r") as outfile: 
                json_object = json.load(outfile) 
            
            if(sys.getsizeof(json_object)<(1024*1024*1024)) and ((sys.getsizeof(value))<(16*1024*1024)):
                l={}
                l[key]=value
                
                with open("sample.json", "w") as outfile:
                    json_object.update(l)
                    json.dump(json_object,outfile)
                if(time1!=0):
                    k[key]=time.time()+time1
                    o={}
                    o[key]=k[key]
                    with open("expire.json", "w") as outfile:
                        exp.update(o)
                        json.dump(exp,outfile)

            else:
                print("Memory limit exceeded!! ")#error message when memory more than specified
        else:
            print("Invalind key !! key must be only alphabets and not special characters or numbers")#error messagewhen key is invalid


def read(key):
    if (path.exists("sample.json")):
        with open("sample.json", "r") as outfile: 
	        json_object= json.load(outfile) 
        
    else:
        open("sample.json", "r")
    if key not in json_object:
        print("given key does not exist in database. Please enter a valid key") #error key does not exist
    else:
        if(key in k):
            if(k[key]<time.time()):
                print("the key  has expired")#key is expired
            else:      

                b=json_object[key]
                stri=str(key)+":"+str(b) #to return the value in the format of JasonObject "
                return stri
        else:            
            b=json_object[key]
            stri=str(key)+":"+str(b) #to return the value in the format of JasonObject "
            return stri
            

def delete(key):
    
    if (path.exists("sample.json")):
        with open("sample.json", "r") as outfile: 
	        json_object= json.load(outfile) 
        if key not in json_object:
            print("given key does not exist in database. Please enter a valid key") #error key does not exist
        else:
            if(key in k):
                if(k[key]>time.time()):
                    print("the key  has expired")
                else:
                    del json_object[key]
                    del k[key]
                    print("key is successfully deleted")   
            else:
                    del json_object[key]
                    del k[key]
                    print("key is successfully deleted")     
                

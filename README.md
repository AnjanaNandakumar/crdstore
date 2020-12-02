# crdstore 

This file contains code for 
1.It will reliably create itself in a reasonable location on the laptop.
2. A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.
3. If Create is invoked for an existing key, an appropriate error must be returned.
4. A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.
5. A Delete operation can be performed by providing the key.
6. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds
the key must be retained in the dataThis file co store. Once the Time-To-Live for a key has expired,
the key will no longer be available for Read or Delete operations.
7. Appropriate error responses must always



How to Test it :
Example:

1.Import crdnew as c  #this will  import the python file 

2.c.create(“anj”,{“NAME”:ANJANA,”age”=21})    #this creates the json key and value and dump it into the json file names sample.json  

3. .c.create(“anj”,{“NAME”:ANJANA,”age”=21},20)    #with expiry of the key 

 Thus the syntac to create is c.create(key,value,optional(time of live)
 
4.c.read(“anj”) # reads the key and returns json object and displays it

5.c.delete(“anj”) # deleted the key 

6. We cannot read or delete once the time to live is expired (the expired keys are inserted into a dictionary)

7.As  the  socket is  creating a local host only single process or import is possible at a time.


Libraries imported :import time, socket, sys, json, os.path 
Language used: python (3.6.8)






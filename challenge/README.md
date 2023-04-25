COMPLETE README FILE


a.) IDEA AND INGENUITY IN DESIGNING FILE STORAGE SERVER USING COMMAND LINE INTERFACE


 The Idea of Server implementation, creating a file storage server with command line interface with the files on server where all clients can upload files to a designated folder through cli on the server manage files 
with list of files, deleting any file or file reterive.

This server is written in Python using flask framework.
The code is built in Flask request ,  it handles errors and modules
 Flask-CORS extension is used for Cross-Origin Resource Sharing (CORS) on the server, and enabling CORS., which accepts the request from external users

This file storage Server will automatically create a repository named "files" from the folder it is starting.

The code defines three modules

1.) Post : this function allows he user to upload a file through command line interface. 
you can upload any file formats such as .txt, .pdf, .xml, png, jpg, jpeg, gif, doc, docs, xls, xlsx 
It checks if a file was included in the request, and if the file is valid based on its extension. If the file is valid, it is saved to the designated folder.

# CLI command : python fsstore2.py Post ms.pdf 

# ms.pdf is the sample file name to upload, fsstore2.py is the client request server.

2.) Delete:  This function will delete the file which  is uploaded. first it checks that the file exists in the folder where it is uploaded , then it deletes.

# CLI command : python fsstore2.py Delete ms.pdf 

# ms.pdf is the sample file name to delete from the uploaded folder,  fsstore2.py is the file name of client request server.

3.) Get : This function will show the files listed in the folder present there. if file is uploaded then deleted it is not listed
 It retrieves a list of all files in the designated folder and returns the list in JSON format.

# CLI command : python fsstore2.py Get 

In terms of ingenuity, the code is relatively simple and straightforward, focusing on the core functionality of file management. 
It uses built-in Flask and Python libraries and does not require any external dependencies.
It also includes basic error handling and input validation to ensure the server operates as expected.

b). INSTRUCTIONS ON HOW TO BUILD AND RUN (DISTRIBUTE) THIS CODE

install all libraries and Dependencies used such as flask, request, urandom, wekzeug, fire

flask 2.2.2 
werkzeug 2.2.2 
fire 0.4.0 
requests 2.27.1

Run and test it on python version  : 3.9.16

Run this code using following commands :
1.) First run the server, using python fsstore1.py 

2.) Second, run the request using python fsstore2.py 

3.) to upload a file , run a command : python fsstore2.py Post ms.pdf 
upload one more file python fsstore2.py Post t1.pdf 

4.) to delete a file , run a command : python fsstore2.py Delete ms.pdf 

5.) to list a file , run a command : python fsstore2.py Get

Next Features Sorting by name functionality Post, delete, Get function on request of client

Distribution of this code in production for the client usage  : there are several things to consider 
-security, scalability, user interface

In linux - create a executeServer.sh file calling the fsstore1.py and 
make that file executable(chmod +x) crontab -e > @reboot executeServer.sh

Using Windows - Copy and paste the shortcut to the app from the file location to the Startup folder.
When Windows boots, server will start.


C.) FRAMEWORK AND TOOL/KIT USED

Flask:  written in Python used to build web applications and creating file storage servers. 
 define the server routes and handle HTTP requests and responses to the client

Flask-CORS: A Flask extension that provides Cross-Origin Resource Sharing (CORS) support for the server. 
It is used in this code to allow external domains to access the server resources.

Werkzeug: A Python toolkit that provides utilities for building web applications. It is used in this code to handle secure file uploads using the secure_filename function.

os: A Python module that provides a way of using operating system dependent functionality. 
It is used in this code to interact with the file system, such as creating and deleting directories and files.


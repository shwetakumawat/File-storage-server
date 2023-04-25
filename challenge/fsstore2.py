#IMPLEMENTAION OF COMMAND LINE INTERFACE (CLI) TO INTERACT WITH SERVER.
#ITS SUPPORTS THREE FUNCTIONS AS A SERVER

import requests
import fire

def Post(path):
    url = "http://localhost:8081/files"
    files = {'file': open(path, 'rb')}
    response = requests.post(url, files=files)
    return response.text
	
def Delete(filename):
    url = "http://localhost:8081/files/" + filename
    response = requests.delete(url)
    return response.text

def Get():
    url = "http://localhost:8081/files"
    response = requests.get(url)
    return response.text

if __name__ == '__main__':  
    fire.Fire()
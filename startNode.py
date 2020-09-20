import requests
import json
from createProject import testBedProject, gns3Creds

baseUrl = "http://localhost:3080/v2/"
username = gns3Creds['username']
password = gns3Creds['password']
projectId = testBedProject['project_id']

def startProject():
    requests.post(url=baseUrl+'projects/'+projectId+'/open', auth=(username, password))
    requests.post(url=baseUrl+'projects/'+projectId+'/nodes/start', auth=(username, password))



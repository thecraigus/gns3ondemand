import requests
import json

baseUrl = "http://localhost:3080/v2/"

testBedProject = {
    "name": "OnDemandTestBed",
    "project_id": "b8c070f7-f34c-4b7b-ba6f-be3d26ed0747",
}

gns3Creds = {
    "username": "admin",
    "password": "9tWWt0f0BKegpMcsLzieT8L1MTEuCGnqMnmaazMMjz0skR2axc6vj4LE4YdA48zE",
}


createProject = requests.post (url=baseUrl+'projects', auth=(gns3Creds['username'],gns3Creds['password']), data=json.dumps(testBedProject))


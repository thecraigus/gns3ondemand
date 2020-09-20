import time
import json
import requests
from createProject import testBedProject, gns3Creds
from createProject import createProject
from addNodes import createNodes
from startNode import startProject

baseUrl = "http://localhost:3080/v2/"
username = gns3Creds['username']
password = gns3Creds['password']
projectId = testBedProject['project_id']

def buildTestBed():
    createProject

    createNodes()

    nodedict = {}
    nodes = requests.get (url=baseUrl+'projects/'+projectId+'/nodes', auth=(username,password)).json()
    for node in nodes:
        nodedict[node['name']] = node['node_id']
    
    rtr01Id = nodedict['RTR01']
    rtr02Id = nodedict['RTR02']
    mgmtId = nodedict['MGTSW01']
    cloudId = nodedict['cloud']

    routerPeer = {
        "nodes": [
            {
                "adapter_number": 0,
                "node_id": "{}".format(rtr01Id),
                "port_number": 0
            },
            {
                "adapter_number": 0,
                "node_id": "{}".format(rtr02Id),
                "port_number": 0
            }
        ]
    }

    rtr01Mgmt = {
        "nodes": [
            {
                "adapter_number": 3,
                "node_id": "{}".format(rtr01Id),
                "port_number": 0
            },
            {
                "adapter_number": 0,
                "node_id": "{}".format(mgmtId),
                "port_number": 0
            }
        ]
    }

    rtr02Mgmt = {
        "nodes": [
            {
                "adapter_number": 3,
                "node_id": "{}".format(rtr02Id),
                "port_number": 0
            },
            {
                "adapter_number": 0,
                "node_id": "{}".format(mgmtId),
                "port_number": 1
            }
        ]
    }

    mgmtCloud = {
        "nodes": [
            {
                "adapter_number": 1,
                "node_id": "{}".format(mgmtId),
                "port_number": 3
            },
            {
                "adapter_number": 0,
                "node_id": "{}".format(cloudId),
                "port_number": 1
            }
        ]
    }

    requests.post (url=baseUrl+'projects/'+projectId+'/links', data=json.dumps(routerPeer), auth=(username,password))
    requests.post (url=baseUrl+'projects/'+projectId+'/links', data=json.dumps(rtr01Mgmt), auth=(username,password))
    requests.post (url=baseUrl+'projects/'+projectId+'/links', data=json.dumps(rtr02Mgmt), auth=(username,password))
    requests.post (url=baseUrl+'projects/'+projectId+'/links', data=json.dumps(mgmtCloud), auth=(username,password))

    startProject()
    
def main():
    buildTestBed()

main()
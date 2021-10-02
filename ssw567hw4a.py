import requests
import json

def getCommits(ID):
  if not isinstance(ID, str):
    return "User ID is not valid"
  repo = 'https://api.github.com/users/' + ID + '/repos'
  get = requests.get(repo)
  jason = json.loads(get.text)
  names = []

  for obj in jason:
    names.append(obj["name"])

  counter = 0

  for i in names:
    comms = 'https://api.github.com/repos/' + ID + '/' + i + '/commits'
    com = requests.get(comms)
    grayson = json.loads(com.text)
    print('Repo: ' + i + ' Number of commits: ' + str(len(grayson)))
    counter = counter + len(grayson)

  total = len(names) + counter
  return total

print(getCommits("BarlesCharkley75"))
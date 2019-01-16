import urllib2
import json, ast

def getAllDependencies(packageName):
  url = "http://registry.npmjs.org/" + packageName + "/latest"
  try:
    urlResult = urllib2.urlopen(url)
    contents = urlResult.read()
    data_json = json.loads(contents)
    result = []
    for e in data_json['dependencies']:
        result.append(e)
    print(json.dumps(result))
    return result
  except urllib2.HTTPError, e:
    print("Invalid URL")


fileName = raw_input("Enter dependency file name: ")
getAllDependencies(fileName)

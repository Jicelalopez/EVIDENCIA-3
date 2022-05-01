import json

fileObject=open("data.json","r")
jsonconect=fileObject.read()
aList=json.loads(jsonconect)
print(aList)
print(aList['a'])
print(aList['b'])
print(aList['c'])
      
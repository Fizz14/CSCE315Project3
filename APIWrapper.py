import sys
#from typing import KeysView; print(sys.executable)
import json
import requests

# response = requests.get("https://api.thedogapi.com/v1/images/search")

# #print(response.text)
# responseAsDictionary = json.loads(response.text)

# print(type(responseAsDictionary))
# print(type(responseAsDictionary[0]))
# print(responseAsDictionary[0].keys())

#for x in responseAsDictionary[0]:
    #print(x.get())

# for x in responseAsDictionary.values:
#     print(x)

class APIWrapper:
    def __init__(self, endpoint = "https://api.thedogapi.com/v1/images/search"):

        # Run API call and put the data into a json object
        response = requests.get(endpoint)
        APIWrapper.responseAsListOfDictionaries = json.loads(response.text)

        # API requests return a list of dictionaries, and this list often has only one dictionary
        # this data holds the length of that list to prevent errors in fetching data
        APIWrapper.numberOfDicts = len(APIWrapper.responseAsListOfDictionaries)

        # this data holds the keys of the first dict in the list.  
        # I expect that later dictionaries will have similar keys but I don't know yet
        # Easily this could be extended to be a list of keys corresponding to each dictionary
        APIWrapper.keys = list(APIWrapper.responseAsListOfDictionaries[0].keys())


    # a trivial way to get data from the APIWrapper object
    # get the data from dictionary number [whichDictionary] and key [whatKey]
    def get(self, whatKey = "id", whichDictionary = 0):
        return APIWrapper.responseAsListOfDictionaries[whichDictionary].get(whatKey)

    
    def getKeys(self):
        return APIWrapper.keys



        


        
        
MyAPIW = APIWrapper()
print(APIWrapper.get(MyAPIW, "width"))
print(APIWrapper.getKeys(MyAPIW))
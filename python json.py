# to be able to access and use a json file on python, use this command

import json
json.loads()

json.dumps()  #converting from python to json

#use indent parameter to be able to indent the json file through python
json.dumps(x, indent=4)  #x could be anything

#use sort_keys to specity if the result should be sorted r not
json.dumps(x, indent=2, sort_keys=True)


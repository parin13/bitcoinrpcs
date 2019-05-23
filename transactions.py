import json
import requests
from . import hd
url =  'http://user:password@127.0.0.1:18443'



def rpc_requests(method,params=[]):
	headers = {'Content-type': 'application/json'}
	payload = {'jsonrpc': '2.0', 'id': 1}
	payload['method']= method
	payload['params'] = params

	response =  requests.post(url,headers=headers,data=json.dumps(payload))
	if response.status_code == 200:
		return json.loads(response.text)
            

def listaddressgroupings():
	method = "listaddressgroupings"
	return(rpc_requests(method=method))

def validate_address(address):
	method = "validateaddress"
	params = [address]
	resp = rpc_requests(method,params)
	return resp.get('result')









# print (listaddressgroupings())
# print(validate_address("moj7hVfiYtcezNVePQ128Y557VHJktKebc"))
# print (listaddressgroupings())

hd_class.create_address()
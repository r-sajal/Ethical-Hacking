import os
import urllib3
import json 

ip = input("Enter target IP: ")
url = "http://ip-api.com/json/"
http = urllib3.PoolManager()
response=http.request("GET",url+ip)
print(response.status)
data=response.read()
values=json.loads(response.data)
print("-------------------------------------------------------")
print("IP: "+values["query"])
print("City: "+values["city"])
print("Country: "+values["country"])
print("Region: "+values["region"])
print("ISP: "+values["isp"])
print("Timezone: "+values["timezone"])
print("-------------------------------------------------------")

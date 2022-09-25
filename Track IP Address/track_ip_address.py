import os
import urllib2
import json 

ip = input("Enter target IP: ")
url = "http://ip-api.com/json/"
response=urllib2.urlopen(url+ip)
data=response.read()
values=json.loads(data)
print("-------------------------------------------------------")
print("IP: "+values["query"])
print("City: "+values["city"])
print("Country: "+values["country"])
print("Region: "+values["region"])
print("ISP: "+values["isp"])
print("Timezone: "+values["timezone"])
print("-------------------------------------------------------")

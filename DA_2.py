print("test")


#Use the Request library
import requests
# Set the target Webpage
url = "https://brickset.com/sets/year-2011"
r = requests.get(url)

#This will get the status code
print("Status Code:")
print("\t*", r.status_code, "ok")

#This will just get the headers
h = requests.head(url)
print("Headers :")
print("**********")
#To print line by line
for x in h.headers:
    print("\t", x, ".", h.headers[x])
print("**********")

# This will modify the headers user-agent
headers = {
    'User-Agent' : "Mobile"
}

#Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2,headers=headers)
print(rh.text)
#program to list all firewalls for a gcp project

import httplib2


print(httplib2.__version__)
print(httplib2.__copyright__)
print(httplib2.__doc__)

http = httplib2.Http()
content = http.request("https://www.googleapis.com/compute/v1/projects/horizon-228521/global/firewalls")[1]

print(content.decode())
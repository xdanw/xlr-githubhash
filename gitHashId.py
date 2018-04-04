
import sys

import httplib
import json

apiServer = "api.github.com";
path = "/repos/" + repoOwner + "/" + repoNane + "/commits"

connection = httplib.HTTPSConnection(apiServer);
headers = {"User-Agent": "XLRTestScript/xdanw@github"};
connection.request("GET", path, "", headers);
response1 = connection.getresponse();

data = response1.read()
responseDict = json.loads(data);

print "[0,sha] is: " + responseDict[0]["sha"];

commitHash = responseDict[0]["sha"];

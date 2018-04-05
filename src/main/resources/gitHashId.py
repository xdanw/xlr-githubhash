
import sys

import httplib
import json

apiServer = "api.github.com";
path = "/repos/" + repoOwner + "/" + repoName + "/commits"

connection = httplib.HTTPSConnection(apiServer);
headers = {"User-Agent": "XLRTestScript/xdanw@github"};
connection.request("GET", path, "", headers);
response1 = connection.getresponse();

data = response1.read()
responseDict = json.loads(data);

print "sha (full) is: " + responseDict[0]["sha"];

commitHash = responseDict[0]["sha"];


# github convention is to refer to first 7 digits
thisRelease = getCurrentRelease();
print "Current title: " + thisRelease.title;
thisRelease.title = thisRelease.title + "(" + repoName + "/" + commitHash[0:7] + ")";
releaseApi.updateRelease(thisRelease);

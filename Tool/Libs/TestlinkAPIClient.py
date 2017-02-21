#!/usr/bin/env python

import xmlrpclib
from time import strftime

class TestlinkAPIClient:
    # substitute your server URL Here
    SERVER_URL = "http://192.168.1.15:8080/testlink/lib/api/xmlrpc/v1/xmlrpc.php"

    def __init__(self, devKey, testplanID, buildNotes):
        self.server = xmlrpclib.Server(self.SERVER_URL)
        self.devKey = devKey
        self.testplanID = testplanID
        self.buildNotes = buildNotes
        buildName = strftime("%Y-%m-%d_%H%M%S")
        self.buildName = buildName

    def reportTCResult(self, tcid, buildid, status, testRunNotes):
        data = {"devKey":self.devKey, "testcaseid":tcid, "testplanid":self.testplanID, "buildid":buildid, "status":status, "notes":testRunNotes}
        return self.server.tl.reportTCResult(data)

    def getInfo(self):
        return self.server.tl.about()

    def createBuild(self):
        data = {"devKey":self.devKey, "testplanid":self.testplanID, "buildname":self.buildName, "buildnotes":self.buildNotes}
        print "Build Name %s created" % data["buildname"]
        x = self.server.tl.createBuild(data)
        out = x[0]
        buildID = out['id']
        print "Build ID is %s" % buildID
        return (buildID)

    def getTestCaseIDFromTestName(self, testcaseName):
        x1 = testcaseName.split("]")
        x2 = x1[0]
        x3 = x2.split("[")
        testcaseID = x3[1]
        return (testcaseID)

    def existingBuild(self):
        data = {"devKey":self.devKey, "testplanid":self.testplanID}
        existingBuild = self.server.tl.getLatestBuildForTestPlan(data)
        return existingBuild['id']

##a = TestlinkAPIClient('a84c530ba11a54b88b9485fe59e701ef', 19555, '')
##b = a.reportTCResult(19382, 179, 'p', '')
##raw_input('end...')

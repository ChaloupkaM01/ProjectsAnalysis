import json


def createTableRow(project):
    row = {}
    row["projectID"] = project["id"]
    row["projectName"] = project["name"]
    row["startDate"] = project["startdate"]
    row["endDate"] = project["enddate"]
    row["validity"] = project["valid"]

    row["projectTypeID"] = project["projectType"]["id"]
    row["projectType"] = project["projectType"]["name"]

    row["milestonesCount"] = len(project['milestones'])

    row["groupID"] = project["group"]["id"]
    row["groupName"] = project["group"]["name"]
    
    return row


with open('dataFake.json', encoding='utf-8') as inputFile:
    data = json.load(inputFile)


sourceTable = []


for project in data["data"]["projectPage"]:
    row = createTableRow(project)
    sourceTable.append(row)


with open('resultFake.json', "w", encoding='utf-8') as outputFile:
    json.dump(sourceTable, outputFile)

import json

with open('data.json', encoding='utf-8') as inputFile:
    data = json.load(inputFile)

sourceTable = []

for project in data["data"]["projectPage"]:
    row = {}
    row["projectID"] = project["id"]
    row["projectName"] = project["name"]
    row["startDate"] = project["startdate"]
    row["endDate"] = project["enddate"]
    row["validity"] = project["valid"]

    row["projectTypeID"] = project["projectType"]["id"]
    row["projectType"] = project["projectType"]["name"]

    row["milestonesCount"] = len(project['milestones'])

    row["teamID"] = project["team"]["id"]
    row["teamName"] = project["team"]["name"]

    sourceTable.append(row)

with open('result.json',"w", encoding='utf-8') as outputFile:
    json.dump(sourceTable, outputFile)
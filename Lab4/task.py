import csv
cityDataFile = open('AcademicSchedule.csv')

cityDataReader= csv.reader(cityDataFile)
cityDataCSV = list(cityDataReader)

startDateCol = cityDataCSV[0].index("StartDate")
endDateCol = cityDataCSV[0].index("EndDate")
activityCol = cityDataCSV[0].index("Activity")

cityData =[]
activities = {}
for rows in cityDataCSV[1:]:
    data = {}
    data["StartDate"] = rows[startDateCol]
    data["EndDate"] = rows[endDateCol]
    data["Activity"] = rows[activityCol]
    cityData.append(data)

    if(not rows[activityCol] in activities.keys()):
        activities[rows[activityCol]] = 0




priorityDataFile = open('PriorityTable.csv')

priorityDataReader= csv.reader(priorityDataFile)
priorityDataCSV = list(priorityDataReader)

priorityActivityCol = priorityDataCSV[0].index("Activity")
priorityCol = priorityDataCSV[0].index("Priority")
userCol = priorityDataCSV[0].index("User")

priorityData =[]
for rows in priorityDataCSV[1:]:
    data = {}
    data["Activity"] = rows[priorityActivityCol]
    data["Priority"] = rows[priorityCol]
    data["User"] = rows[userCol]
    priorityData.append(data)


resultData = []

activitiesPerDay = []


for rows in cityData[1:]:
    data ={}
    # print rows["StartDate"]
    if (rows["StartDate"] not in data.keys()):
        data[rows["StartDate"]] = []
        for rows in cityData[1:]:
            if (rows["StartDate"] in data.keys()):
                data[rows["StartDate"]].append(rows["Activity"])
    activitiesPerDay.append(data)

for rows in activitiesPerDay:

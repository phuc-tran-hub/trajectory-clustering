# Name: Phuc Tran
# Date: January 17th, 2022
# Title: preprocess.c
# Description: preprocess an AIS file to fit into a list of ship objects

import pandas
import csv
import numpy
from ship import Ship

def preprocess(fileName, nRows):
	# Storing the ship names onto a list
	# Only testing 200 rows for now
	AIS_csv_data = pandas.read_csv(fileName, nrows=nRows)
	shipNameList = list(AIS_csv_data["Name"])
	# the first line is identifying the column name

	# Storing it into a numpy array for convenience sake
	shipNameList = numpy.unique(numpy.copy(shipNameList))

	# Start the pandas dataframe for the csv file
	shipObjectList = []
	shipOccurenceList = []
	AIS_csv_data_df = pandas.DataFrame(AIS_csv_data)
	# Iterate through the first n-rows:
	for idx, row in AIS_csv_data_df.iterrows():
		if str(row["Name"]) == "nan":
			continue

		if str(row["Name"]) in shipNameList:
			if str(row["Name"]) not in shipOccurenceList:
				newShip = Ship(str(row["Name"]))			
				shipObjectList.append(newShip)
				shipOccurenceList.append(str(row["Name"]))
			
			# Inefficient right now, but being used for purely testing prototype
			newLocation = [str(row["Timestamp"]), round(float(row["Latitude"]), 2), round(float(row["Longitude"]), 2)]
			for shipObject in shipObjectList:
				if str(row["Name"]) == shipObject.shipName:
					if len(shipObject.positionList) > 0:

						latestLocation = shipObject.positionList[len(shipObject.positionList) - 1]
						# If the ship is at the same location, ignore that position
						if latestLocation[1] == newLocation[1] and latestLocation[2] == newLocation[2]:
							continue

					# Update the ship's position
					shipObject.addNewPosition(newLocation)
					# print("{} shipName {} position list {} \n".format(idx, shipObject.shipName, shipObject.positionList))

	# Iterate through the ship object list
	# Printing out the ship's name and its past locations
	shipObjectFile = open("shipObjectAndLocation.txt", "w")
	for shipObject in shipObjectList:
		shipObjectFile.write(shipObject.shipName + "\n")
		shipObjectFile.write(str(shipObject.positionList) + "\n")

	shipObjectFile.close()

	return shipObjectList




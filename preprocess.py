# Name: Phuc Tran
# Date: January 17th, 2022
# Title: preprocess.c
# Description: pulling out data from a AIS csv file to store into line segments

import pandas
import csv
import numpy
from ship import Ship

# Storing the ship names onto a list
# Only testing 200 rows for now
col_list = ["Timestamp", "Type of mobile" , "MMSI" , "Latitude" , "Longitude" , "Navigational status" , "ROT" , "SOG" , "COG" , "Heading" , "IMO" , "Callsign" ,
        "Name" , "Ship type" , "Cargo type" , "Width" , "Length" , "Type of position fixing device" , "Draught" , "Destination" , "ETA" , "Data source type"]
AIS_csv_data = pandas.read_csv('AIS.csv', nrows=200, usecols=col_list)
shipNameList = list(AIS_csv_data["Name"])
# the first line is identifying the column name

# Storing it into a numpy array for convenience sake
shipNameList = numpy.unique(numpy.copy(shipNameList))

shipNameFile = open("shipName.txt", "w")
for shipName in shipNameList:
        if str(shipName) != "nan":  
                shipNameFile.write(str(shipName) + "\n")

shipNameFile.close()

shipObjectList = []
AIS_csv_data_df = pandas.DataFrame(AIS_csv_data)
# Iterate through the first n-rows:
for idx, row in AIS_csv_data_df.iterrows():
        if str(row["Name"]) == "nan":
                continue

        if str(row["Name"]) in shipNameList:
                if str(row["Name"]) not in shipObjectList:
                        newShip = Ship(str(row["Name"]))
                        shipObjectList.append(newShip)
                
                # Inefficient right now, but being used for purely testing prototype
                newLocation = [str(row["Timestamp"]), str(row["Latitude"]), str(row["Longitude"])]
                for shipObject in shipObjectList:
                        if str(row["Name"]) == shipObject.shipName:
                                shipObject.addNewPosition(newLocation)
                                print("{} shipName {} position list {} \n".format(idx, shipObject.shipName, shipObject.positionList))

# Iterate through the ship object list
shipObjectFile = open("shipObjectAndLocation.txt", "w")
for shipObject in shipObjectList:
        shipObjectFile.write(shipObject.shipName + "\n")
        shipObjectFile.write(str(shipObject.positionList) + "\n")

shipObjectFile.close()




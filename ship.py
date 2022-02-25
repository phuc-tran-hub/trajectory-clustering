class Ship: 

    def __init__(self, shipName):
        self.shipName = shipName
        self.positionList = []
    
    def addNewPosition(self, newLocationList):
        self.positionList.append(newLocationList)

# Each workout repersents a class that encodes the data that is a child of a object with methods to add the data to a text file
# Upon opening the text file you should be able to regain all of the objects and their properties in a later version

# Topsets are parsed via the standard: (weight)x(reps)

class FitnessObj:
    def __init__(self, type:str, time:str):
        self.__ColumnTitles__ = ["Type", "Time"]
        self.time = time #military time and date
        self.type = type

    #this is the generalized function for appending the object to a given text file
    def addDataToFile(self, file:str):
        Attributes = [getattr(self,attr) for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        Attributes = list(reversed(Attributes))
        Attributes = (str(Attributes).replace("[","")).replace("]","")
        Attributes = Attributes.replace("'","", 1000000000)
        with open(file, 'a') as currentFile:
            currentFile.write(f"{Attributes}\n")

class LegDay(FitnessObj):
    def __init__(self, time:str, squatTopset:str, RDLTopset:str):
        super().__init__("Leg Day", time)

        newcolumntitles = ["Squat Topset", "RDL Topset"]
        for item in newcolumntitles:
            self.__ColumnTitles__.append(item)

        self.squatTopset = squatTopset
        self.RDLTopset = RDLTopset

class ArmDay(FitnessObj):
    def __init__(self, time:str, militaryPressTopset:str, preacherCurlTopset:str):
        super().__init__("Arm Day", time)

        newcolumntitles = ["Military Press Topset", "Preacher Curl Topset"]
        for item in newcolumntitles:
            self.__ColumnTitles__.append(item)

        self.militaryPressTopset = militaryPressTopset
        self.preacherCurlTopset = preacherCurlTopset

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day1 = LegDay("10:00","315x10","225x11")
    day1.addDataToFile("workoutData.txt")
    day2 = ArmDay("8:00","135x3","100x10")
    day2.addDataToFile("workoutData.txt")
    print(day1.__ColumnTitles__)
    print(day2.__ColumnTitles__)
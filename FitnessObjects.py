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

class TrailRun(FitnessObj):
    def __init__(self, time:str, distance:str, timeToCompletion:str):
        super().__init__("Trail Run", time)

        newcolumntitles = ["Distance", "Time To Completion"]
        for item in newcolumntitles:
            self.__ColumnTitles__.append(item)

        self.distance = distance
        self.timeToCompletion = timeToCompletion

class Run(FitnessObj):
    def __init__(self, time:str, distance:str, timeToCompletion:str):
        super().__init__("Run", time)

        newcolumntitles = ["Distance", "Time To Completion"]
        for item in newcolumntitles:
            self.__ColumnTitles__.append(item)

        self.distance = distance
        self.timeToCompletion = timeToCompletion

# ----------------------------------------------------------------------------------------------------------------------
# Workout program generator
# -----------------------

maxBenchGoal = 315
currentBench = 225
maxSquatGoal = 405
currentSquat = 285
maxDeadliftGoal = 525
currentDeadlift = 385

totalDaysToComplete = 28*8 # may is in 7 months, 7 times 30 = ...
trainingCycleTime = 28 # 30 days
trainingSubCycle = trainingCycleTime/4
startingDayInCurrentYear = 301

BenchIncreasePerCycle = (maxBenchGoal - currentBench)/7
SquatIncreasePerCycle = (maxSquatGoal - currentSquat)/7
DeadliftIncreasePerCycle = (maxDeadliftGoal - currentDeadlift)/7


#Max Increase Function
def generalMaxIncreaseFunc(trainingCycleLength, IncreasePerCycle, startingMax, CurrentDay):

    return (IncreasePerCycle/trainingCycleLength)*(CurrentDay) + startingMax


DaysOfTheTrainingCycleToWorkout = [0, 2, 4, 5] # 0 is monday 5 is saturday
DaysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# M* Tu  W* Th F* Sat* Sun M* Tu W*
# 0  1   2  3  4  5    6   7  8  9
# --------------------------------
percentsPerSetBench = [60,70,80,80,80,90,90,60]
repCountForPercentsBench = [8,8,5,5,5,2,1,6]
percentsPerSetSquat = [60,70,80,80,80,90,90,60]
repCountForPercentsSquat = [8,8,5,5,5,2,1,6]
percentsPerSetDeadlift = [60,70,80,80,80,90,90,60]
repCountForPercentsDeadlift = [8,8,5,5,5,2,1,6]

# Bench Squat day 1
# Bench Deadlift day 2
# Deadlift Squat day 3
# Bench Squat Deadlift day 4

FirstLayerDays = ["B", "B", "D", "B"]
SecondLayerDays = ["S", "D", "S", "S D"]

workoutPlan = []
workoutDay = []

def interalDayLayerLogic(typeOfDay, dayOfMonth):
    listOfRepsPerSet = []
    listOfRepsPerSet2 = []
    returnstring = ""
    if typeOfDay == "B":

        currentMax = generalMaxIncreaseFunc(trainingCycleTime, BenchIncreasePerCycle, currentBench, dayOfMonth)

        for i in range(len(percentsPerSetBench)):
            listOfRepsPerSet.append(f"{int(currentMax*(percentsPerSetBench[i]/100))}x{repCountForPercentsBench[i]}")

        returnstring = f"Bench: {listOfRepsPerSet}"

    if typeOfDay == "S":

        currentMax = generalMaxIncreaseFunc(trainingCycleTime, SquatIncreasePerCycle, currentSquat, dayOfMonth)

        for i in range(len(percentsPerSetSquat)):
            listOfRepsPerSet.append(f"{int(currentMax*(percentsPerSetSquat[i]/100))}x{repCountForPercentsSquat[i]}")
        returnstring = f"Squat: {listOfRepsPerSet}"
    if typeOfDay == "D":

        currentMax = generalMaxIncreaseFunc(trainingCycleTime, DeadliftIncreasePerCycle, currentDeadlift, dayOfMonth)

        for i in range(len(percentsPerSetDeadlift)):
            listOfRepsPerSet.append(f"{int(currentMax*(percentsPerSetDeadlift[i]/100))}x{repCountForPercentsDeadlift[i]}")
        returnstring = f"Deadlift: {listOfRepsPerSet}"
    if typeOfDay == "S D":

        currentMax = generalMaxIncreaseFunc(trainingCycleTime, DeadliftIncreasePerCycle, currentDeadlift, dayOfMonth)

        for i in range(len(percentsPerSetDeadlift)):
            listOfRepsPerSet.append(f"{int(currentMax * (percentsPerSetDeadlift[i] / 100))}x{repCountForPercentsDeadlift[i]}")


        currentMax = generalMaxIncreaseFunc(trainingCycleTime, SquatIncreasePerCycle, currentSquat, dayOfMonth)

        for i in range(len(percentsPerSetSquat)):
            listOfRepsPerSet2.append(f"{int(currentMax * (percentsPerSetSquat[i] / 100))}x{repCountForPercentsSquat[i]}")

        returnstring = f"Deadlift: {listOfRepsPerSet} Squat: {listOfRepsPerSet2}"

    return returnstring



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for iteration in range(int(trainingCycleTime / trainingSubCycle)):
        for dayIndicator in range(len(DaysOfTheTrainingCycleToWorkout)):
            workoutDay = []
            day = iteration * trainingSubCycle + DaysOfTheTrainingCycleToWorkout[dayIndicator]+1
            workoutDay.append(DaysOfTheWeek[DaysOfTheTrainingCycleToWorkout[dayIndicator]])
            workoutDay.append(f"Day: {day}")
            workoutDay.append(interalDayLayerLogic(FirstLayerDays[dayIndicator],day))
            workoutDay.append(interalDayLayerLogic(SecondLayerDays[dayIndicator],day))
            print(workoutDay)
            workoutPlan.append(workoutDay)

    print(f"Goal bench increase for this cycle:{BenchIncreasePerCycle}")
    print(f"Goal squat increase for this cycle:{SquatIncreasePerCycle}")
    print(f"Goal deadlift increase for this cycle:{DeadliftIncreasePerCycle}")
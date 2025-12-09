#!/usr/bin/env python3

### Make sure that misty.py is in the experiment folder
### Begin Experiment
import misty

usrAvg = 0
msg = ""
eq = ""
corCount = 0
inCorCount = 0
meanRT = [10,10,10,10,10,10] 
time = 10
totalCor = 0
difficulty = "easy1"
timeCoef = 1

### Begin Routine
msg = ""
timer = core.CountdownTimer(time)
x = misty.MistSums()
x.make_equation(difficulty)
eq = "%s = ?" %(x.equation)
ans = int(x.ans)
timeout = False

### Each Frame
if timer.getTime() <= 0:
    continueRoutine = False
    timeout = True
    
### End Routine
if slider.getRating() == ans: 
        msg = "Correct"                #For correct trials add one to 
        corCount = corCount + 1       #correct counter
        totalCor=totalCor + 1           #and total correct.
        usrAvg = usrAvg - 0.005         #increase userAverage pointer by 0.05
elif (timeout == True):
    msg = "Time-Out"
    if corCount > 0:
        corCount = 0 #combo-breakakaka
    corCount -= 1
    usrAvg= usrAvg+0.1

elif (slider.getRating() != ans): #For incorrect answers
    msg = type(this_ans)
    if corCount > 0:
        corCount = 0
    corCount -= 1 # minus one from correct counter
    usrAvg = usrAvg + 0.1 #add 0.1 to userAverage pointer (1-userAv)


if slider.getRT() == None:
    RT = time
else:
    RT = slider.getRT()

if corCount == 3: #every 3 correct answers reduces the mean time by 10%
    timeCoef = (timeCoef * 0.9)
    corCount = 0 #resets the counter

if corCount == -3: #every three incorrect answers
    timeCoef = (timeCoef / 0.9) #time is increased by 10%
    corCount = 0 #resets counter

if totalCor < 5: #Sets difficulty of sums at four steps
    difficulty = "easy1" #just +- sums, 2 integers 0-9
elif totalCor == 5:
    difficulty = "easy2" #just +- sums, 3 integers 0-9
elif totalCor == 10:
    difficulty = "med1" # +-* sums, 3 integers 0-9
elif totalCor == 15:
    difficulty = "med2" # +-* sums, 3 integers 0-99
elif totalCor == 20: 
    difficulty = "hard" # +-/* sums, 3 integers 0-99

#print(corCount)
#print(time)

meanRT.append(RT)
time = np.mean(meanRT) * timeCoef

if usrAvg >= 1.8:
    usrAvg = 1.8

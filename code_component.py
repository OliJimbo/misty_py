#!/usr/bin/env python3

"""
Code component for misty psychopy implementation
Make sure that misty.py is in the experiment folder

"""

# Begin Experiment
import misty

# Set variables
pointer_pos = 0  # x position of pointer
msg = ""  # feedback message
eq = ""  # equation string
streak_count = 0  # current streak
total_cor = 0  # total number of correct answers
rt_list = []  # list of reaction times
time = 10  # starting value for trial time
difficulty = "easy1"  # diffculty of equation
time_coef = 1  # amount to reduce trial time by
trial_counter = 0  # current trial

# Begin Routine
# Set countdown timer
# Create equation

msg = ""
timer = core.CountdownTimer(time)
x = misty.MistSums()
x.make_equation(difficulty)
eq = "%s = ?" %(x.equation)
ans = int(x.ans)
timeout = False

# Each Frame
if timer.getTime() <= 0:
    continueRoutine = False
    timeout = True

# End Routine
# Set variables and adjust pointer
this_key = "emp"
if len(key_resp.keys) > 0:
    this_key = int(key_resp.keys[0])
this_resp =[slider.getRating(), this_key]

if  ans in this_resp:
        msg = "Correct!"  # For correct trials add one to
        streak_count += 1   # correct counter
        total_cor += 1     # and total correct.
        pointer_pos -= 0.005  # increase userAverage pointer by 0.05

elif (timeout is True):
    msg = "Time-Out!"
    if streak_count < 0:
        streak_count = 0 # combo-breakakaka
        streak_count -= 1
        pointer_pos += 0.1

elif ans not in this_resp: # For incorrect answers
    msg = "Incorrect!"
    if streak_count > 0:
        streak_count = 0    
        streak_count -= 1  # set streak to 0 and minus 1 (count incorrect)
        pointer_pos += 0.1  # add 0.1 to userAverage pointer (1-userAv)

if pointer_pos >= 1.8:
    pointer_pos = 1.8

if timeout:
    RT = time
else:
    if slider.getRT() is None:
        RT = key_resp.rt
    else:
        RT = slider.getRT()
if total_cor < 5:  # Sets difficulty of sums at four steps
    difficulty = "easy1"  # just +- sums, 2 integers 0-9
elif total_cor == 5:
    difficulty = "easy2"  # just +- sums, 3 integers 0-9
elif total_cor == 10:
    difficulty = "med1"  # +-* sums, 3 integers 0-9
elif total_cor == 15:
    difficulty = "med2"  # +-* sums, 3 integers 0-99
elif total_cor == 20:
    difficulty = "hard"  # +-/* sums, 3 integers 0-99

# print(corCount)
# print(time)

trial_counter += 1
rt_list.append(RT)

if trial_counter > 5:
    time = np.mean(rt_list) * time_coef
    if streak_count == 3:  # every 3 correct answers reduces the mean time by 10%
        time_coef = (time_coef * 0.9)
        streak_count = 0  # resets the counter

    if streak_count == -3:  # every three incorrect answers
        time_coef = (time_coef / 0.9) # time is increased by 10%
        cor_count = 0  # resets counter

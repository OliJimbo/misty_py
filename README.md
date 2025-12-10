# misty
An implementation of the Montreal Imaging Stress Task. An arithmetic generator designed after the MIST - Dedovic, K., Renwick, R., Mahani, N. K., Engert, V., Lupien, S. J., &amp; Pruessner, J. C. (2005). The Montreal Imaging Stress Task: using functional imaging to investigate the effects of perceiving and processing psychosocial stress in the human brain. Journal of Psychiatry and Neuroscience, 30(5), 319. For use in PsychoPy builder.

## misty_py
The routines for producing equations are defined by the class `MistSums`.
A `MistSums` object generates equations through the `misty.MistSums.make_equation(difficulty)` function, where difficulty is one of the following strings: "easy1", "easy2", "med1", "med2" "hard".
The subsequent equation and the corresponding answer are stored as `misty.MistSums.eq` and `misty.MistSums.ans` respectively.

``` python
import misty

x = misty.MistSums()
x.make_equation("hard")
print("%s = %s" %(x.equation, x.ans))
```


## PsychoPy Experiments
There are two versions:  misty_aio.psyexp is messier and has all functions within a code component; misty_modular imports most of the code from misty.py

- Participants are initially given 10 seconds to answer increasingly challenging sums,
- all answers are numbers between 0-9,
- the time limit adapts to the speed in which they respond,
- they are given visual "performance" feedback that compares their scores with a fictitious norm group (controlled by the 'pointer_pos' variable),
- researchers should give verbal reminders that participants need to perform at least at the average compared with the norm group.


If you are using the misty_modular.psyexp file, ensure that misty.py is in the experiment folder as this is imported by the code component.

To change the rules of the task, you can edit the variables and statements in the 'End Routine' section of the code component.

## Variables
[code_component.py lines 13-22](https://github.com/OliJimbo/misty_py/blob/e6e290768db68a52c6d571e81b91b9856e517ead/code_component.py#L11C13-L22C1)
- streak_count (integer, current streak of correct answers),
- total_cor (integer, total number of correct answers),
- pointer_pos (float, position of the performance pointer),
- time_coef (float, rate at which trial time is decreased),
- difficulty (string array, controls the complexity of the equations),
- rt_list (float array, stores response times to take average. Starting value set at several 10's).

## Performance Feedback
[code_component.py lines 48-69](https://github.com/OliJimbo/misty_py/blob/e6e290768db68a52c6d571e81b91b9856e517ead/code_component.py#L48C1-L69C1)
The rules are currently set to the following:
- Each correct answer:
-- increases the streak_count variable by 1,
-- decreases pointer_pos by a small amount (shifts pointer to the right) 
- Each incorrect answer:
-- Sets streak_count to 0 and subtracts 1,
-- increases pointer_pos by a larger amount (shifts pointer to left)

## Difficulty of Equations
[code_component.py lines 71-80](https://github.com/OliJimbo/misty_py/blob/e6e290768db68a52c6d571e81b91b9856e517ead/code_component.py#L71C1-L80C1)
- If there are three consecutive correct answers, participants time is reduced by 10%,
- If there are three incorrect answers in a row, participants time is increased by 10%,
- If the total number of correct answers:
-- less than 5, then equations are the easiest (easy1), (two integers between 0-9; only addition or subtraction),
-- between 5-9, then equations are easy (easy2), (three integers between 0-9; only addition or subtraction),
-- between 10 and 15, then equations are set to med1, (three integers between 0-99; only addition or subtraction),
-- between 15 and 20, then equations are set to med2, (three integers between 0-99; addition, subtraction, multiplication),
-- over 20, then equations are set to med1, (three integers between 0-99; addition, subtraction, multiplication, division).

## Trial Time
[code_component.py lines 85-104](https://github.com/OliJimbo/misty_py/blob/e6e290768db68a52c6d571e81b91b9856e517ead/code_component.py#L85C1-L104C1)
- Participants start with 10 seconds per equation,
- response time is saved for each trial,
- after the first 5 trials,
-- trial time is set to the participants mean response time, 
-- for every three correct answers, the amount of time for each trial is reduced by 10%,
-- for every three incorrect answers, the amount of time for each trial is increased by 10%.



Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

<picture>
<img alt="Picture of Misty from Pokemon scaring Brock, Ash, and Pikachu" src="./img/header.jpg">
</picture>

<h1> <img src="./img/logo.png", alt="Misty", width="100"/> </h1>

<p> 
    <img src="./img/logo.png" alt="Misty" width="50" /> is an implementation of the Montreal Imaging Stress Task (MIST) described by Dedovic et al (2005)<sup><a href="#ref-1" id="cite-1" aria-describedby="reference-label">1</a> </sup>.
</p>

MIST is based on one of the most commonly used stress inducement protocols, the Trier Social Stress Test (TSST) <sup><a href="#ref-2" id="cite-2" aria-describedby="reference-label">2</a> </sup>.

The TSST requires subjects to prepare and perform a speech and answer a series of mental arithmetic questions in front of a small audience, a procedure that is not feasible in e.g. fMRI studies in which tasks are necessarily performed in a large, noisy tube. 

The MIST was developed to allow stress to be induced whilst subjects are scanned, and focuses on the arithmetic element of the TSST.

In brief, participants are required to answer mental arithmetic questions under conditions that become progressively adverse over several dimensions.
First, the time limit per question is adaptive.
Participants average solution times are initially estimated and set as the time limit, and the more questions they get correct, the faster the timer decreases.
Secondly, the more questions subjects get right, the harder the questions become.
At their easiest, questions involve a single basic elementary operation (either + or )- on integers between 1-9, with the hardest questions having any two elementary operations (+, -, ×, or ÷) on integers between 1-99.
Third, and most importantly, the participant constantly evaluates, and is evaluated on, performance. 
They are presented with a progress bar that represents their performance relative to a fictitious norm group.
Their position decreases faster than it increases, and they should be reminded periodically by the researcher that they must maintain an average (or above) performance.
Crucially, the main stressor is not the questions themselves (although these may be for people who have maths anxiety...), but the "public" performance of the questions.

<img src="./img/logo.png", alt="Misty", width="50"/> implements this procedure in PsychoPy so that it may be used in imaging studies or in the lab.
It is distributed as a PsychoPy .psyexp file so that it can be used immediately, and adapted easily.

It also comes as a module so that it can be used with the PsychoPy API, or in Python more broadly.

Issues, pull requests, and comments are all very welcome.

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

<h1>References</h1>
    <ol>
        <li id="ref-1">
            [1] Dedovic, K., Renwick, R., Mahani, N. K., Engert, V., Lupien, S. J., &amp; Pruessner, J. C. (2005). The Montreal Imaging Stress Task: using functional imaging to investigate the effects of perceiving and processing psychosocial stress in the human brain. Journal of Psychiatry and Neuroscience, 30(5), 319.
    <a href="#cite-1" aria-label="Back to reference 1">↩</a>
        </li>
    </ol>

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

# misty
An implementation of the Montreal Imaging Stress Task. An arithmetic generator designed after the MIST - Dedovic, K., Renwick, R., Mahani, N. K., Engert, V., Lupien, S. J., &amp; Pruessner, J. C. (2005). The Montreal Imaging Stress Task: using functional imaging to investigate the effects of perceiving and processing psychosocial stress in the human brain. Journal of Psychiatry and Neuroscience, 30(5), 319. For use in PsychoPy builder.

- Participants are initially given 10 seconds to answer increasingly challenging sums.
- All answers are numbers between 0-9
- The time limit adapts to the speed in which they respond.
- They are given visual "performance" feedback that compares their scores with a fictitious norm group (controlled by the 'usrAvg' variable).
- Researchers should give verbal reminders that participants need to perform at least at the average compared with the norm group

If using the misty_modular.psyexp file, ensure that misty.py is in the experiment folder as this is imported by the code component.


Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

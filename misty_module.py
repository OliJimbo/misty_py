#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.2.4),
    on Wed  4 Feb 17:22:55 2026
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.2.4'
expName = 'misty_module'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/hackerman/misty_py/misty_module.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "wait_screen" ---
    # Run 'Begin Experiment' code from setup_exp
    import serial
    from misty import misty
    # Create misty sum object
    eq_gen = misty.MistSums()
    eq_gen.make_equation("easy1")
    print(eq_gen.equation)
    # Check for serial connection
    evntlg = 'sr' in locals() or 'sr' in globals()
    if evntlg :    difbyt="02".encode()
    try:
        sr = serial.Serial("INSERTCOMHERE", 115200, timeout=1)
        print("Serial Connected")
    except serial.serialutil.SerialException:
        print("Serial Not Connected")
    
    evntlg = 'sr' in locals() or 'sr' in globals()
    
    # Set full containeer variables for experiment 
    # appearance variables
    pointer_pos = .8  # x position of pointer
    msg = ""  # feedback message
    eq = ""  # equation string
    
    # Set placeholder variables for experiment
    # Behaviour
    streak_count = 0  # current streak
    total_cor = 0  # total number of correct answers
    rtDict = {} # Dictionary for lists of reaction times
    expDict={}
    time = 20  # starting value for trial time
    difficulty = "easy1"  # diffculty of equation
    time_coef = .9  # amount to reduce trial time by
    trial_counter = 0  # current trial
    perf=""
    text = visual.TextStim(win=win, name='text',
        text="Please wait for the researcher\\'s instructions.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_2 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "instructions" ---
    intstructs = visual.TextStim(win=win, name='intstructs',
        text='Please answer the following artimetic questions to the best of your ability.\n\nYou will be measured on both speed and accuracy.\n\nTo ensure that we can use your results and complete our research we need you to perform at the level of your peers (indicated by the red arrow)\n\nYou will now have a few practice trials.\n\nPress space to start',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_to_cont = keyboard.Keyboard(deviceName='defaultKeyboard')
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "fixation" ---
    fix = visual.TextStim(win=win, name='fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "practice_trials" ---
    equation_practice_1 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='equation_practice_1',
         depth=-1, autoLog=True,
    )
    slider_3 = visual.Slider(win=win, name='slider_3',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units='norm',
        labels=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=0.0,
        style='choice', styleTweaks=[], opacity=None,
        labelColor=(-1.0000, 0.0039, 0.0039), markerColor=(1.0000, -0.4588, -1.0000), lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-2, readOnly=False)
    key_resp_4 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "feedback" ---
    feedback_practice_1 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='feedback_practice_1',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "new_ui" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='The next three trials will include the full user interface.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_8 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "fixation" ---
    fix = visual.TextStim(win=win, name='fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "practice_trials_2" ---
    prog_3 = visual.Progress(
        win, name='prog_3',
        progress=0.0,
        pos=(0.5, 0.5), size=(-1, 0.1), anchor='top-left', units='norm',
        barColor=(-1.0000, 0.5373, -1.0000), backColor=(1.0000, -1.0000, -1.0000), borderColor='white', colorSpace='rgb',
        lineWidth=4.0, opacity=1.0, ori=0.0,
        depth=-1
    )
    redbar_3 = visual.Rect(
        win=win, name='redbar_3',units='norm', 
        width=(2,0.1)[0], height=(2,0.1)[1],
        ori=0.0, pos=(-1, 0.7), draggable=False, anchor='center-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=(1.0000, -1.0000, -1.0000),
        opacity=None, depth=-2.0, interpolate=True)
    yellowbar_3 = visual.Rect(
        win=win, name='yellowbar_3',units='norm', 
        width=(1, 0.1)[0], height=(1, 0.1)[1],
        ori=0.0, pos=(0, 0.7), draggable=False, anchor='center-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=(1.0000, 1.0000, -1.0000),
        opacity=None, depth=-3.0, interpolate=True)
    greenbar_3 = visual.Rect(
        win=win, name='greenbar_3',units='norm', 
        width=(0.3, 0.1)[0], height=(0.3, 0.1)[1],
        ori=0.0, pos=(0.7, 0.7), draggable=False, anchor='center-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=(-1.0000, 0.0039, -1.0000),
        opacity=None, depth=-4.0, interpolate=True)
    arrow_3 = visual.ShapeStim(
        win=win, name='arrow_3', vertices='arrow',units='norm', 
        size=(0.05, 0.05),
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    arrow_4 = visual.ShapeStim(
        win=win, name='arrow_4', vertices='arrow',units='norm', 
        size=(0.05, 0.05),
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    targlab = visual.TextBox2(
         win, text='Target', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.7, 0.55), draggable=False, units='norm',     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='targlab',
         depth=-7, autoLog=True,
    )
    yourperf = visual.TextBox2(
         win, text='You', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[0,0], draggable=False, units='norm',     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='yourperf',
         depth=-8, autoLog=True,
    )
    slider_4 = visual.Slider(win=win, name='slider_4',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units='norm',
        labels=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=0.0,
        style='choice', styleTweaks=[], opacity=None,
        labelColor=(-1.0000, 0.0039, 0.0039), markerColor=(1.0000, -0.4588, -1.0000), lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-9, readOnly=False)
    key_resp_5 = keyboard.Keyboard(deviceName='defaultKeyboard')
    textbox_5 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_5',
         depth=-11, autoLog=True,
    )
    
    # --- Initialize components for Routine "feedback" ---
    feedback_practice_1 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='feedback_practice_1',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "training_instructions" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Training instructions here',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_9 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "fixation" ---
    fix = visual.TextStim(win=win, name='fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "training_routine_1" ---
    textbox_3 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_3',
         depth=-1, autoLog=True,
    )
    slider_training = visual.Slider(win=win, name='slider_training',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units='norm',
        labels=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=0.0,
        style='choice', styleTweaks=[], opacity=None,
        labelColor=(-1.0000, 0.0039, 0.0039), markerColor=(1.0000, -0.4588, -1.0000), lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-2, readOnly=False)
    key_resp_train = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "feedback" ---
    feedback_practice_1 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='feedback_practice_1',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "next_block" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='Please press space to move onto the next block',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "start_experiment" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='Press Space to Start experiment',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_7 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "fixation" ---
    fix = visual.TextStim(win=win, name='fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "sum_routine1" ---
    prog = visual.Progress(
        win, name='prog',
        progress=0.0,
        pos=(0.5, 0.5), size=(-1, 0.1), anchor='top-left', units='norm',
        barColor=(1.0000, -1.0000, -1.0000), backColor=(-1.0000, 0.5373, -1.0000), borderColor='white', colorSpace='rgb',
        lineWidth=4.0, opacity=1.0, ori=0.0,
        depth=-1
    )
    redbar = visual.Rect(
        win=win, name='redbar',units='norm', 
        width=(2, 0.1)[0], height=(2, 0.1)[1],
        ori=0.0, pos=(-1, 0.7), draggable=False, anchor='center-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=(1.0000, -1.0000, -1.0000),
        opacity=None, depth=-2.0, interpolate=True)
    yellowbar = visual.Rect(
        win=win, name='yellowbar',units='norm', 
        width=(1, 0.1)[0], height=(1, 0.1)[1],
        ori=0.0, pos=(0, 0.7), draggable=False, anchor='center-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=(1.0000, 1.0000, -1.0000),
        opacity=None, depth=-3.0, interpolate=True)
    greenbar = visual.Rect(
        win=win, name='greenbar',units='norm', 
        width=(0.3, 0.1)[0], height=(0.3, 0.1)[1],
        ori=0.0, pos=(0.7, 0.7), draggable=False, anchor='center-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=(-1.0000, 0.0039, -1.0000),
        opacity=None, depth=-4.0, interpolate=True)
    targarrow = visual.ShapeStim(
        win=win, name='targarrow', vertices='arrow',units='norm', 
        size=(0.05, 0.05),
        ori=0.0, pos=(0.7,0.6), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    userArrow = visual.ShapeStim(
        win=win, name='userArrow', vertices='arrow',units='norm', 
        size=(0.05, 0.05),
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    yourperfexp = visual.TextBox2(
         win, text='You', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[0,0], draggable=False, units='norm',     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='yourperfexp',
         depth=-7, autoLog=True,
    )
    tarlabexp = visual.TextBox2(
         win, text='Target', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.7, 0.55), draggable=False, units='norm',     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='tarlabexp',
         depth=-8, autoLog=True,
    )
    textbox = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox',
         depth=-9, autoLog=True,
    )
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units='norm',
        labels=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=0.0,
        style='choice', styleTweaks=[], opacity=None,
        labelColor=(-1.0000, 0.0039, 0.0039), markerColor=(1.0000, -0.4588, -1.0000), lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-10, readOnly=False)
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard')
    norm_arrow = visual.ShapeStim(
        win=win, name='norm_arrow', vertices='arrow',
        size=(0.05, 0.05),
        ori=0.0, pos=(0.7, 0.6), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-12.0, interpolate=True)
    
    # --- Initialize components for Routine "feedback" ---
    feedback_practice_1 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='feedback_practice_1',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "perf_feedback" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_6 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "thanks" ---
    text_7 = visual.TextStim(win=win, name='text_7',
        text='The task is now over.  Thank you for participating.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_10 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # set up handler to look after randomisation of conditions etc
    testmode = data.TrialHandler2(
        name='testmode',
        nReps=0.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(testmode)  # add the loop to the experiment
    thisTestmode = testmode.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestmode.rgb)
    if thisTestmode != None:
        for paramName in thisTestmode:
            globals()[paramName] = thisTestmode[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTestmode in testmode:
        testmode.status = STARTED
        if hasattr(thisTestmode, 'status'):
            thisTestmode.status = STARTED
        currentLoop = testmode
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTestmode.rgb)
        if thisTestmode != None:
            for paramName in thisTestmode:
                globals()[paramName] = thisTestmode[paramName]
        
        # --- Prepare to start Routine "wait_screen" ---
        # create an object to store info about Routine wait_screen
        wait_screen = data.Routine(
            name='wait_screen',
            components=[text, key_resp_2],
        )
        wait_screen.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from setup_exp
        if evntlg :
            sr.write("RR".encode())
            core.wait(0.025) #wait 25 mS after resetting
            sr.write("0F".encode()) #Exp started
            core.wait(0.10) #wait 100MS resetting
            sr.write("00".encode()) #Exp started
            
        # create starting attributes for key_resp_2
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # store start times for wait_screen
        wait_screen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        wait_screen.tStart = globalClock.getTime(format='float')
        wait_screen.status = STARTED
        thisExp.addData('wait_screen.started', wait_screen.tStart)
        wait_screen.maxDuration = None
        # keep track of which components have finished
        wait_screenComponents = wait_screen.components
        for thisComponent in wait_screen.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "wait_screen" ---
        thisExp.currentRoutine = wait_screen
        wait_screen.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTestmode, 'status') and thisTestmode.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=wait_screen,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                wait_screen.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if wait_screen.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in wait_screen.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wait_screen" ---
        for thisComponent in wait_screen.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for wait_screen
        wait_screen.tStop = globalClock.getTime(format='float')
        wait_screen.tStopRefresh = tThisFlipGlobal
        thisExp.addData('wait_screen.stopped', wait_screen.tStop)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        testmode.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            testmode.addData('key_resp_2.rt', key_resp_2.rt)
            testmode.addData('key_resp_2.duration', key_resp_2.duration)
        # the Routine "wait_screen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "instructions" ---
        # create an object to store info about Routine instructions
        instructions = data.Routine(
            name='instructions',
            components=[intstructs, space_to_cont, mouse],
        )
        instructions.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for space_to_cont
        space_to_cont.keys = []
        space_to_cont.rt = []
        _space_to_cont_allKeys = []
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        gotValidClick = False  # until a click is received
        # store start times for instructions
        instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        instructions.tStart = globalClock.getTime(format='float')
        instructions.status = STARTED
        thisExp.addData('instructions.started', instructions.tStart)
        instructions.maxDuration = None
        # keep track of which components have finished
        instructionsComponents = instructions.components
        for thisComponent in instructions.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "instructions" ---
        thisExp.currentRoutine = instructions
        instructions.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTestmode, 'status') and thisTestmode.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *intstructs* updates
            
            # if intstructs is starting this frame...
            if intstructs.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intstructs.frameNStart = frameN  # exact frame index
                intstructs.tStart = t  # local t and not account for scr refresh
                intstructs.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intstructs, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'intstructs.started')
                # update status
                intstructs.status = STARTED
                intstructs.setAutoDraw(True)
            
            # if intstructs is active this frame...
            if intstructs.status == STARTED:
                # update params
                pass
            
            # *space_to_cont* updates
            waitOnFlip = False
            
            # if space_to_cont is starting this frame...
            if space_to_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                space_to_cont.frameNStart = frameN  # exact frame index
                space_to_cont.tStart = t  # local t and not account for scr refresh
                space_to_cont.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space_to_cont, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'space_to_cont.started')
                # update status
                space_to_cont.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(space_to_cont.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(space_to_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if space_to_cont.status == STARTED and not waitOnFlip:
                theseKeys = space_to_cont.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
                _space_to_cont_allKeys.extend(theseKeys)
                if len(_space_to_cont_allKeys):
                    space_to_cont.keys = _space_to_cont_allKeys[-1].name  # just the last key pressed
                    space_to_cont.rt = _space_to_cont_allKeys[-1].rt
                    space_to_cont.duration = _space_to_cont_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        pass
                        x, y = mouse.getPos()
                        mouse.x.append(float(x))
                        mouse.y.append(float(y))
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                        
                        continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=instructions,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                instructions.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if instructions.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in instructions.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "instructions" ---
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for instructions
        instructions.tStop = globalClock.getTime(format='float')
        instructions.tStopRefresh = tThisFlipGlobal
        thisExp.addData('instructions.stopped', instructions.tStop)
        # check responses
        if space_to_cont.keys in ['', [], None]:  # No response was made
            space_to_cont.keys = None
        testmode.addData('space_to_cont.keys',space_to_cont.keys)
        if space_to_cont.keys != None:  # we had a response
            testmode.addData('space_to_cont.rt', space_to_cont.rt)
            testmode.addData('space_to_cont.duration', space_to_cont.duration)
        # store data for testmode (TrialHandler)
        testmode.addData('mouse.x', mouse.x)
        testmode.addData('mouse.y', mouse.y)
        testmode.addData('mouse.leftButton', mouse.leftButton)
        testmode.addData('mouse.midButton', mouse.midButton)
        testmode.addData('mouse.rightButton', mouse.rightButton)
        testmode.addData('mouse.time', mouse.time)
        # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        prac_trials = data.TrialHandler2(
            name='prac_trials',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('practice_difficulty.xlsx'), 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(prac_trials)  # add the loop to the experiment
        thisPrac_trial = prac_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
        if thisPrac_trial != None:
            for paramName in thisPrac_trial:
                globals()[paramName] = thisPrac_trial[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisPrac_trial in prac_trials:
            prac_trials.status = STARTED
            if hasattr(thisPrac_trial, 'status'):
                thisPrac_trial.status = STARTED
            currentLoop = prac_trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
            if thisPrac_trial != None:
                for paramName in thisPrac_trial:
                    globals()[paramName] = thisPrac_trial[paramName]
            
            # --- Prepare to start Routine "fixation" ---
            # create an object to store info about Routine fixation
            fixation = data.Routine(
                name='fixation',
                components=[fix],
            )
            fixation.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fix_pulse
            if evntlg :  sr.write("01".encode()) #Fixation signal
            
            # store start times for fixation
            fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            fixation.tStart = globalClock.getTime(format='float')
            fixation.status = STARTED
            thisExp.addData('fixation.started', fixation.tStart)
            fixation.maxDuration = None
            # keep track of which components have finished
            fixationComponents = fixation.components
            for thisComponent in fixation.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fixation" ---
            thisExp.currentRoutine = fixation
            fixation.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # if trial has changed, end Routine now
                if hasattr(thisPrac_trial, 'status') and thisPrac_trial.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fix* updates
                
                # if fix is starting this frame...
                if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fix.frameNStart = frameN  # exact frame index
                    fix.tStart = t  # local t and not account for scr refresh
                    fix.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix.started')
                    # update status
                    fix.status = STARTED
                    fix.setAutoDraw(True)
                
                # if fix is active this frame...
                if fix.status == STARTED:
                    # update params
                    pass
                
                # if fix is stopping this frame...
                if fix.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fix.tStop = t  # not accounting for scr refresh
                        fix.tStopRefresh = tThisFlipGlobal  # on global time
                        fix.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix.stopped')
                        # update status
                        fix.status = FINISHED
                        fix.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=fixation,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    fixation.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if fixation.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in fixation.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation" ---
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for fixation
            fixation.tStop = globalClock.getTime(format='float')
            fixation.tStopRefresh = tThisFlipGlobal
            thisExp.addData('fixation.stopped', fixation.tStop)
            # Run 'End Routine' code from fix_pulse
            if evntlg :    sr.write("00".encode()) #set lines to zero
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if fixation.maxDurationReached:
                routineTimer.addTime(-fixation.maxDuration)
            elif fixation.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            
            # --- Prepare to start Routine "practice_trials" ---
            # create an object to store info about Routine practice_trials
            practice_trials = data.Routine(
                name='practice_trials',
                components=[equation_practice_1, slider_3, key_resp_4],
            )
            practice_trials.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from practice_code
            # If serial object is loaded then use it
            # Practice trials are all easy1
            if evntlg :    sr.write("03".encode())
            print(eq_gen.__class__)
            # Feedback message starts empty
            msg = ""
            
            #Set sum for this repetition
            eq_gen.make_equation("easy1")
            eq = "%s = ?" %(eq_gen.equation)
            ans = int(eq_gen.ans)
            equation_practice_1.reset()
            equation_practice_1.setText(eq)
            slider_3.reset()
            # create starting attributes for key_resp_4
            key_resp_4.keys = []
            key_resp_4.rt = []
            _key_resp_4_allKeys = []
            # store start times for practice_trials
            practice_trials.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            practice_trials.tStart = globalClock.getTime(format='float')
            practice_trials.status = STARTED
            thisExp.addData('practice_trials.started', practice_trials.tStart)
            practice_trials.maxDuration = None
            # keep track of which components have finished
            practice_trialsComponents = practice_trials.components
            for thisComponent in practice_trials.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "practice_trials" ---
            thisExp.currentRoutine = practice_trials
            practice_trials.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisPrac_trial, 'status') and thisPrac_trial.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *equation_practice_1* updates
                
                # if equation_practice_1 is starting this frame...
                if equation_practice_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    equation_practice_1.frameNStart = frameN  # exact frame index
                    equation_practice_1.tStart = t  # local t and not account for scr refresh
                    equation_practice_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(equation_practice_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'equation_practice_1.started')
                    # update status
                    equation_practice_1.status = STARTED
                    equation_practice_1.setAutoDraw(True)
                
                # if equation_practice_1 is active this frame...
                if equation_practice_1.status == STARTED:
                    # update params
                    pass
                
                # if equation_practice_1 is stopping this frame...
                if equation_practice_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > equation_practice_1.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        equation_practice_1.tStop = t  # not accounting for scr refresh
                        equation_practice_1.tStopRefresh = tThisFlipGlobal  # on global time
                        equation_practice_1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'equation_practice_1.stopped')
                        # update status
                        equation_practice_1.status = FINISHED
                        equation_practice_1.setAutoDraw(False)
                
                # *slider_3* updates
                
                # if slider_3 is starting this frame...
                if slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    slider_3.frameNStart = frameN  # exact frame index
                    slider_3.tStart = t  # local t and not account for scr refresh
                    slider_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'slider_3.started')
                    # update status
                    slider_3.status = STARTED
                    slider_3.setAutoDraw(True)
                
                # if slider_3 is active this frame...
                if slider_3.status == STARTED:
                    # update params
                    pass
                
                # if slider_3 is stopping this frame...
                if slider_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > slider_3.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        slider_3.tStop = t  # not accounting for scr refresh
                        slider_3.tStopRefresh = tThisFlipGlobal  # on global time
                        slider_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'slider_3.stopped')
                        # update status
                        slider_3.status = FINISHED
                        slider_3.setAutoDraw(False)
                
                # Check slider_3 for response to end Routine
                if slider_3.getRating() is not None and slider_3.status == STARTED:
                    continueRoutine = False
                
                # *key_resp_4* updates
                waitOnFlip = False
                
                # if key_resp_4 is starting this frame...
                if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_4.frameNStart = frameN  # exact frame index
                    key_resp_4.tStart = t  # local t and not account for scr refresh
                    key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_4.started')
                    # update status
                    key_resp_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if key_resp_4 is stopping this frame...
                if key_resp_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_4.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_4.tStop = t  # not accounting for scr refresh
                        key_resp_4.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                        # update status
                        key_resp_4.status = FINISHED
                        key_resp_4.status = FINISHED
                if key_resp_4.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_4.getKeys(keyList=["1","2","3","4","5","6","7","8","9","0","s"], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_4_allKeys.extend(theseKeys)
                    if len(_key_resp_4_allKeys):
                        key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                        key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                        key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=practice_trials,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    practice_trials.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if practice_trials.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in practice_trials.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "practice_trials" ---
            for thisComponent in practice_trials.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for practice_trials
            practice_trials.tStop = globalClock.getTime(format='float')
            practice_trials.tStopRefresh = tThisFlipGlobal
            thisExp.addData('practice_trials.stopped', practice_trials.tStop)
            # Run 'End Routine' code from practice_code
            if evntlg:  sr.write("00".encode())
            
            # Set variables and adjust pointer
            this_key = "emp"
            if len(key_resp_4.keys) > 0:
                if  "s" in key_resp_4.keys:
                    prac_trials.finished=True
                    continueRoutine=False
                else:
                    this_key = int(key_resp_4.keys[0])
            this_resp =[slider_3.getRating(), this_key]
            
            if  ans in this_resp:
                msg = "Correct!"  # For correct trials add one to
                    
            elif ans not in this_resp: # For incorrect answers
                msg = "Incorrect!"
            prac_trials.addData('slider_3.response', slider_3.getRating())
            prac_trials.addData('slider_3.rt', slider_3.getRT())
            # check responses
            if key_resp_4.keys in ['', [], None]:  # No response was made
                key_resp_4.keys = None
            prac_trials.addData('key_resp_4.keys',key_resp_4.keys)
            if key_resp_4.keys != None:  # we had a response
                prac_trials.addData('key_resp_4.rt', key_resp_4.rt)
                prac_trials.addData('key_resp_4.duration', key_resp_4.duration)
            # the Routine "practice_trials" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback" ---
            # create an object to store info about Routine feedback
            feedback = data.Routine(
                name='feedback',
                components=[feedback_practice_1],
            )
            feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            feedback_practice_1.reset()
            feedback_practice_1.setText(msg)
            # store start times for feedback
            feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback.tStart = globalClock.getTime(format='float')
            feedback.status = STARTED
            thisExp.addData('feedback.started', feedback.tStart)
            feedback.maxDuration = None
            # keep track of which components have finished
            feedbackComponents = feedback.components
            for thisComponent in feedback.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback" ---
            thisExp.currentRoutine = feedback
            feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # if trial has changed, end Routine now
                if hasattr(thisPrac_trial, 'status') and thisPrac_trial.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_practice_1* updates
                
                # if feedback_practice_1 is starting this frame...
                if feedback_practice_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_practice_1.frameNStart = frameN  # exact frame index
                    feedback_practice_1.tStart = t  # local t and not account for scr refresh
                    feedback_practice_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_practice_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_practice_1.started')
                    # update status
                    feedback_practice_1.status = STARTED
                    feedback_practice_1.setAutoDraw(True)
                
                # if feedback_practice_1 is active this frame...
                if feedback_practice_1.status == STARTED:
                    # update params
                    pass
                
                # if feedback_practice_1 is stopping this frame...
                if feedback_practice_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_practice_1.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_practice_1.tStop = t  # not accounting for scr refresh
                        feedback_practice_1.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_practice_1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_practice_1.stopped')
                        # update status
                        feedback_practice_1.status = FINISHED
                        feedback_practice_1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=feedback,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    feedback.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if feedback.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback" ---
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback
            feedback.tStop = globalClock.getTime(format='float')
            feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback.stopped', feedback.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback.maxDurationReached:
                routineTimer.addTime(-feedback.maxDuration)
            elif feedback.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            # mark thisPrac_trial as finished
            if hasattr(thisPrac_trial, 'status'):
                thisPrac_trial.status = FINISHED
            # if awaiting a pause, pause now
            if prac_trials.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                prac_trials.status = STARTED
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'prac_trials'
        prac_trials.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "new_ui" ---
        # create an object to store info about Routine new_ui
        new_ui = data.Routine(
            name='new_ui',
            components=[text_2, key_resp_8],
        )
        new_ui.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_8
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        # store start times for new_ui
        new_ui.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        new_ui.tStart = globalClock.getTime(format='float')
        new_ui.status = STARTED
        thisExp.addData('new_ui.started', new_ui.tStart)
        new_ui.maxDuration = None
        # keep track of which components have finished
        new_uiComponents = new_ui.components
        for thisComponent in new_ui.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "new_ui" ---
        thisExp.currentRoutine = new_ui
        new_ui.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTestmode, 'status') and thisTestmode.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_8* updates
            waitOnFlip = False
            
            # if key_resp_8 is starting this frame...
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_8.started')
                # update status
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                    key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                    key_resp_8.duration = _key_resp_8_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=new_ui,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                new_ui.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if new_ui.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in new_ui.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "new_ui" ---
        for thisComponent in new_ui.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for new_ui
        new_ui.tStop = globalClock.getTime(format='float')
        new_ui.tStopRefresh = tThisFlipGlobal
        thisExp.addData('new_ui.stopped', new_ui.tStop)
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
        testmode.addData('key_resp_8.keys',key_resp_8.keys)
        if key_resp_8.keys != None:  # we had a response
            testmode.addData('key_resp_8.rt', key_resp_8.rt)
            testmode.addData('key_resp_8.duration', key_resp_8.duration)
        # the Routine "new_ui" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        prac_trial2 = data.TrialHandler2(
            name='prac_trial2',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('practice_difficulty.xlsx'), 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(prac_trial2)  # add the loop to the experiment
        thisPrac_trial2 = prac_trial2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial2.rgb)
        if thisPrac_trial2 != None:
            for paramName in thisPrac_trial2:
                globals()[paramName] = thisPrac_trial2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisPrac_trial2 in prac_trial2:
            prac_trial2.status = STARTED
            if hasattr(thisPrac_trial2, 'status'):
                thisPrac_trial2.status = STARTED
            currentLoop = prac_trial2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial2.rgb)
            if thisPrac_trial2 != None:
                for paramName in thisPrac_trial2:
                    globals()[paramName] = thisPrac_trial2[paramName]
            
            # --- Prepare to start Routine "fixation" ---
            # create an object to store info about Routine fixation
            fixation = data.Routine(
                name='fixation',
                components=[fix],
            )
            fixation.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fix_pulse
            if evntlg :  sr.write("01".encode()) #Fixation signal
            
            # store start times for fixation
            fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            fixation.tStart = globalClock.getTime(format='float')
            fixation.status = STARTED
            thisExp.addData('fixation.started', fixation.tStart)
            fixation.maxDuration = None
            # keep track of which components have finished
            fixationComponents = fixation.components
            for thisComponent in fixation.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fixation" ---
            thisExp.currentRoutine = fixation
            fixation.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # if trial has changed, end Routine now
                if hasattr(thisPrac_trial2, 'status') and thisPrac_trial2.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fix* updates
                
                # if fix is starting this frame...
                if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fix.frameNStart = frameN  # exact frame index
                    fix.tStart = t  # local t and not account for scr refresh
                    fix.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix.started')
                    # update status
                    fix.status = STARTED
                    fix.setAutoDraw(True)
                
                # if fix is active this frame...
                if fix.status == STARTED:
                    # update params
                    pass
                
                # if fix is stopping this frame...
                if fix.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fix.tStop = t  # not accounting for scr refresh
                        fix.tStopRefresh = tThisFlipGlobal  # on global time
                        fix.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix.stopped')
                        # update status
                        fix.status = FINISHED
                        fix.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=fixation,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    fixation.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if fixation.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in fixation.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation" ---
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for fixation
            fixation.tStop = globalClock.getTime(format='float')
            fixation.tStopRefresh = tThisFlipGlobal
            thisExp.addData('fixation.stopped', fixation.tStop)
            # Run 'End Routine' code from fix_pulse
            if evntlg :    sr.write("00".encode()) #set lines to zero
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if fixation.maxDurationReached:
                routineTimer.addTime(-fixation.maxDuration)
            elif fixation.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            
            # --- Prepare to start Routine "practice_trials_2" ---
            # create an object to store info about Routine practice_trials_2
            practice_trials_2 = data.Routine(
                name='practice_trials_2',
                components=[prog_3, redbar_3, yellowbar_3, greenbar_3, arrow_3, arrow_4, targlab, yourperf, slider_4, key_resp_5, textbox_5],
            )
            practice_trials_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from practice_code_2
            msg = ""
            time=20
            timer = core.CountdownTimer(time)
            
            #Set sum for this repetition
            eq_gen.make_equation("easy1")
            eq = "%s = ?" %(eq_gen.equation)
            ans = int(eq_gen.ans)
            timeout = False
            
            # If serial object is loaded then use it
            if evntlg :    sr.write(difbyt)
            arrow_3.setPos((1-pointer_pos, 0.6))
            arrow_4.setPos((0.7,0.6))
            targlab.reset()
            yourperf.reset()
            yourperf.setPos((1-pointer_pos, 0.55))
            slider_4.reset()
            # create starting attributes for key_resp_5
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            textbox_5.reset()
            textbox_5.setText(eq)
            # store start times for practice_trials_2
            practice_trials_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            practice_trials_2.tStart = globalClock.getTime(format='float')
            practice_trials_2.status = STARTED
            thisExp.addData('practice_trials_2.started', practice_trials_2.tStart)
            practice_trials_2.maxDuration = None
            # keep track of which components have finished
            practice_trials_2Components = practice_trials_2.components
            for thisComponent in practice_trials_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "practice_trials_2" ---
            thisExp.currentRoutine = practice_trials_2
            practice_trials_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisPrac_trial2, 'status') and thisPrac_trial2.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from practice_code_2
                if timer.getTime() <= 0:
                    timeout = True
                    continueRoutine = False
                    
                
                # *prog_3* updates
                
                # if prog_3 is starting this frame...
                if prog_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    prog_3.frameNStart = frameN  # exact frame index
                    prog_3.tStart = t  # local t and not account for scr refresh
                    prog_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(prog_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prog_3.started')
                    # update status
                    prog_3.status = STARTED
                    prog_3.setAutoDraw(True)
                
                # if prog_3 is active this frame...
                if prog_3.status == STARTED:
                    # update params
                    prog_3.setProgress(0 + (timer.getTime()/time), log=False)
                
                # if prog_3 is stopping this frame...
                if prog_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > prog_3.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        prog_3.tStop = t  # not accounting for scr refresh
                        prog_3.tStopRefresh = tThisFlipGlobal  # on global time
                        prog_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'prog_3.stopped')
                        # update status
                        prog_3.status = FINISHED
                        prog_3.setAutoDraw(False)
                
                # *redbar_3* updates
                
                # if redbar_3 is starting this frame...
                if redbar_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    redbar_3.frameNStart = frameN  # exact frame index
                    redbar_3.tStart = t  # local t and not account for scr refresh
                    redbar_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(redbar_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'redbar_3.started')
                    # update status
                    redbar_3.status = STARTED
                    redbar_3.setAutoDraw(True)
                
                # if redbar_3 is active this frame...
                if redbar_3.status == STARTED:
                    # update params
                    pass
                
                # if redbar_3 is stopping this frame...
                if redbar_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > redbar_3.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        redbar_3.tStop = t  # not accounting for scr refresh
                        redbar_3.tStopRefresh = tThisFlipGlobal  # on global time
                        redbar_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'redbar_3.stopped')
                        # update status
                        redbar_3.status = FINISHED
                        redbar_3.setAutoDraw(False)
                
                # *yellowbar_3* updates
                
                # if yellowbar_3 is starting this frame...
                if yellowbar_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    yellowbar_3.frameNStart = frameN  # exact frame index
                    yellowbar_3.tStart = t  # local t and not account for scr refresh
                    yellowbar_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(yellowbar_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'yellowbar_3.started')
                    # update status
                    yellowbar_3.status = STARTED
                    yellowbar_3.setAutoDraw(True)
                
                # if yellowbar_3 is active this frame...
                if yellowbar_3.status == STARTED:
                    # update params
                    pass
                
                # if yellowbar_3 is stopping this frame...
                if yellowbar_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > yellowbar_3.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        yellowbar_3.tStop = t  # not accounting for scr refresh
                        yellowbar_3.tStopRefresh = tThisFlipGlobal  # on global time
                        yellowbar_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'yellowbar_3.stopped')
                        # update status
                        yellowbar_3.status = FINISHED
                        yellowbar_3.setAutoDraw(False)
                
                # *greenbar_3* updates
                
                # if greenbar_3 is starting this frame...
                if greenbar_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    greenbar_3.frameNStart = frameN  # exact frame index
                    greenbar_3.tStart = t  # local t and not account for scr refresh
                    greenbar_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(greenbar_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'greenbar_3.started')
                    # update status
                    greenbar_3.status = STARTED
                    greenbar_3.setAutoDraw(True)
                
                # if greenbar_3 is active this frame...
                if greenbar_3.status == STARTED:
                    # update params
                    pass
                
                # if greenbar_3 is stopping this frame...
                if greenbar_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > greenbar_3.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        greenbar_3.tStop = t  # not accounting for scr refresh
                        greenbar_3.tStopRefresh = tThisFlipGlobal  # on global time
                        greenbar_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'greenbar_3.stopped')
                        # update status
                        greenbar_3.status = FINISHED
                        greenbar_3.setAutoDraw(False)
                
                # *arrow_3* updates
                
                # if arrow_3 is starting this frame...
                if arrow_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    arrow_3.frameNStart = frameN  # exact frame index
                    arrow_3.tStart = t  # local t and not account for scr refresh
                    arrow_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(arrow_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'arrow_3.started')
                    # update status
                    arrow_3.status = STARTED
                    arrow_3.setAutoDraw(True)
                
                # if arrow_3 is active this frame...
                if arrow_3.status == STARTED:
                    # update params
                    pass
                
                # if arrow_3 is stopping this frame...
                if arrow_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > arrow_3.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        arrow_3.tStop = t  # not accounting for scr refresh
                        arrow_3.tStopRefresh = tThisFlipGlobal  # on global time
                        arrow_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'arrow_3.stopped')
                        # update status
                        arrow_3.status = FINISHED
                        arrow_3.setAutoDraw(False)
                
                # *arrow_4* updates
                
                # if arrow_4 is starting this frame...
                if arrow_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    arrow_4.frameNStart = frameN  # exact frame index
                    arrow_4.tStart = t  # local t and not account for scr refresh
                    arrow_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(arrow_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'arrow_4.started')
                    # update status
                    arrow_4.status = STARTED
                    arrow_4.setAutoDraw(True)
                
                # if arrow_4 is active this frame...
                if arrow_4.status == STARTED:
                    # update params
                    pass
                
                # if arrow_4 is stopping this frame...
                if arrow_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > arrow_4.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        arrow_4.tStop = t  # not accounting for scr refresh
                        arrow_4.tStopRefresh = tThisFlipGlobal  # on global time
                        arrow_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'arrow_4.stopped')
                        # update status
                        arrow_4.status = FINISHED
                        arrow_4.setAutoDraw(False)
                
                # *targlab* updates
                
                # if targlab is starting this frame...
                if targlab.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    targlab.frameNStart = frameN  # exact frame index
                    targlab.tStart = t  # local t and not account for scr refresh
                    targlab.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(targlab, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'targlab.started')
                    # update status
                    targlab.status = STARTED
                    targlab.setAutoDraw(True)
                
                # if targlab is active this frame...
                if targlab.status == STARTED:
                    # update params
                    pass
                
                # if targlab is stopping this frame...
                if targlab.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > targlab.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        targlab.tStop = t  # not accounting for scr refresh
                        targlab.tStopRefresh = tThisFlipGlobal  # on global time
                        targlab.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'targlab.stopped')
                        # update status
                        targlab.status = FINISHED
                        targlab.setAutoDraw(False)
                
                # *yourperf* updates
                
                # if yourperf is starting this frame...
                if yourperf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    yourperf.frameNStart = frameN  # exact frame index
                    yourperf.tStart = t  # local t and not account for scr refresh
                    yourperf.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(yourperf, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'yourperf.started')
                    # update status
                    yourperf.status = STARTED
                    yourperf.setAutoDraw(True)
                
                # if yourperf is active this frame...
                if yourperf.status == STARTED:
                    # update params
                    pass
                
                # if yourperf is stopping this frame...
                if yourperf.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > yourperf.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        yourperf.tStop = t  # not accounting for scr refresh
                        yourperf.tStopRefresh = tThisFlipGlobal  # on global time
                        yourperf.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'yourperf.stopped')
                        # update status
                        yourperf.status = FINISHED
                        yourperf.setAutoDraw(False)
                
                # *slider_4* updates
                
                # if slider_4 is starting this frame...
                if slider_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    slider_4.frameNStart = frameN  # exact frame index
                    slider_4.tStart = t  # local t and not account for scr refresh
                    slider_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(slider_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'slider_4.started')
                    # update status
                    slider_4.status = STARTED
                    slider_4.setAutoDraw(True)
                
                # if slider_4 is active this frame...
                if slider_4.status == STARTED:
                    # update params
                    pass
                
                # if slider_4 is stopping this frame...
                if slider_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > slider_4.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        slider_4.tStop = t  # not accounting for scr refresh
                        slider_4.tStopRefresh = tThisFlipGlobal  # on global time
                        slider_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'slider_4.stopped')
                        # update status
                        slider_4.status = FINISHED
                        slider_4.setAutoDraw(False)
                
                # Check slider_4 for response to end Routine
                if slider_4.getRating() is not None and slider_4.status == STARTED:
                    continueRoutine = False
                
                # *key_resp_5* updates
                waitOnFlip = False
                
                # if key_resp_5 is starting this frame...
                if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_5.frameNStart = frameN  # exact frame index
                    key_resp_5.tStart = t  # local t and not account for scr refresh
                    key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_5.started')
                    # update status
                    key_resp_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if key_resp_5 is stopping this frame...
                if key_resp_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_5.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_5.tStop = t  # not accounting for scr refresh
                        key_resp_5.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_5.stopped')
                        # update status
                        key_resp_5.status = FINISHED
                        key_resp_5.status = FINISHED
                if key_resp_5.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_5.getKeys(keyList=["1","2","3","4","5","6","7","8","9","0","s"], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_5_allKeys.extend(theseKeys)
                    if len(_key_resp_5_allKeys):
                        key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                        key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                        key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *textbox_5* updates
                
                # if textbox_5 is starting this frame...
                if textbox_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textbox_5.frameNStart = frameN  # exact frame index
                    textbox_5.tStart = t  # local t and not account for scr refresh
                    textbox_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textbox_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_5.started')
                    # update status
                    textbox_5.status = STARTED
                    textbox_5.setAutoDraw(True)
                
                # if textbox_5 is active this frame...
                if textbox_5.status == STARTED:
                    # update params
                    pass
                
                # if textbox_5 is stopping this frame...
                if textbox_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textbox_5.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        textbox_5.tStop = t  # not accounting for scr refresh
                        textbox_5.tStopRefresh = tThisFlipGlobal  # on global time
                        textbox_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textbox_5.stopped')
                        # update status
                        textbox_5.status = FINISHED
                        textbox_5.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=practice_trials_2,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    practice_trials_2.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if practice_trials_2.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in practice_trials_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "practice_trials_2" ---
            for thisComponent in practice_trials_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for practice_trials_2
            practice_trials_2.tStop = globalClock.getTime(format='float')
            practice_trials_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('practice_trials_2.stopped', practice_trials_2.tStop)
            # Run 'End Routine' code from practice_code_2
            # Set serial to 0 if running
            if evntlg:  sr.write("00".encode())
            
            # Set variables and adjust pointer
            this_key = "emp"
            if len(key_resp_5.keys) > 0:
                if  "s" in key_resp_5.keys:
                    prac_trial2.finished=True
                    continueRoutine=False
                else:
                    this_key = int(key_resp_5.keys[0])
                    this_resp =[slider_4.getRating(), this_key]
            
            if  ans in this_resp:
                msg = "Correct!"  # For correct trials add one to
            
            if  "s" in this_resp:
                prac_trials2.finished=True
                    
            elif (timeout is True):
                msg = "Time-Out!"
            
            elif ans not in this_resp: # For incorrect answers
                msg = "Incorrect!"
            prac_trial2.addData('slider_4.response', slider_4.getRating())
            prac_trial2.addData('slider_4.rt', slider_4.getRT())
            # check responses
            if key_resp_5.keys in ['', [], None]:  # No response was made
                key_resp_5.keys = None
            prac_trial2.addData('key_resp_5.keys',key_resp_5.keys)
            if key_resp_5.keys != None:  # we had a response
                prac_trial2.addData('key_resp_5.rt', key_resp_5.rt)
                prac_trial2.addData('key_resp_5.duration', key_resp_5.duration)
            # the Routine "practice_trials_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback" ---
            # create an object to store info about Routine feedback
            feedback = data.Routine(
                name='feedback',
                components=[feedback_practice_1],
            )
            feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            feedback_practice_1.reset()
            feedback_practice_1.setText(msg)
            # store start times for feedback
            feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback.tStart = globalClock.getTime(format='float')
            feedback.status = STARTED
            thisExp.addData('feedback.started', feedback.tStart)
            feedback.maxDuration = None
            # keep track of which components have finished
            feedbackComponents = feedback.components
            for thisComponent in feedback.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback" ---
            thisExp.currentRoutine = feedback
            feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # if trial has changed, end Routine now
                if hasattr(thisPrac_trial2, 'status') and thisPrac_trial2.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_practice_1* updates
                
                # if feedback_practice_1 is starting this frame...
                if feedback_practice_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_practice_1.frameNStart = frameN  # exact frame index
                    feedback_practice_1.tStart = t  # local t and not account for scr refresh
                    feedback_practice_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_practice_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_practice_1.started')
                    # update status
                    feedback_practice_1.status = STARTED
                    feedback_practice_1.setAutoDraw(True)
                
                # if feedback_practice_1 is active this frame...
                if feedback_practice_1.status == STARTED:
                    # update params
                    pass
                
                # if feedback_practice_1 is stopping this frame...
                if feedback_practice_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_practice_1.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_practice_1.tStop = t  # not accounting for scr refresh
                        feedback_practice_1.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_practice_1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_practice_1.stopped')
                        # update status
                        feedback_practice_1.status = FINISHED
                        feedback_practice_1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=feedback,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    feedback.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if feedback.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback" ---
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback
            feedback.tStop = globalClock.getTime(format='float')
            feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback.stopped', feedback.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback.maxDurationReached:
                routineTimer.addTime(-feedback.maxDuration)
            elif feedback.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            # mark thisPrac_trial2 as finished
            if hasattr(thisPrac_trial2, 'status'):
                thisPrac_trial2.status = FINISHED
            # if awaiting a pause, pause now
            if prac_trial2.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                prac_trial2.status = STARTED
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'prac_trial2'
        prac_trial2.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "training_instructions" ---
        # create an object to store info about Routine training_instructions
        training_instructions = data.Routine(
            name='training_instructions',
            components=[text_3, key_resp_9],
        )
        training_instructions.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_9
        key_resp_9.keys = []
        key_resp_9.rt = []
        _key_resp_9_allKeys = []
        # store start times for training_instructions
        training_instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        training_instructions.tStart = globalClock.getTime(format='float')
        training_instructions.status = STARTED
        thisExp.addData('training_instructions.started', training_instructions.tStart)
        training_instructions.maxDuration = None
        # keep track of which components have finished
        training_instructionsComponents = training_instructions.components
        for thisComponent in training_instructions.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "training_instructions" ---
        thisExp.currentRoutine = training_instructions
        training_instructions.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTestmode, 'status') and thisTestmode.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # *key_resp_9* updates
            waitOnFlip = False
            
            # if key_resp_9 is starting this frame...
            if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.tStart = t  # local t and not account for scr refresh
                key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_9.started')
                # update status
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_9.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_9_allKeys.extend(theseKeys)
                if len(_key_resp_9_allKeys):
                    key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                    key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                    key_resp_9.duration = _key_resp_9_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=training_instructions,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                training_instructions.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if training_instructions.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in training_instructions.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "training_instructions" ---
        for thisComponent in training_instructions.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for training_instructions
        training_instructions.tStop = globalClock.getTime(format='float')
        training_instructions.tStopRefresh = tThisFlipGlobal
        thisExp.addData('training_instructions.stopped', training_instructions.tStop)
        # check responses
        if key_resp_9.keys in ['', [], None]:  # No response was made
            key_resp_9.keys = None
        testmode.addData('key_resp_9.keys',key_resp_9.keys)
        if key_resp_9.keys != None:  # we had a response
            testmode.addData('key_resp_9.rt', key_resp_9.rt)
            testmode.addData('key_resp_9.duration', key_resp_9.duration)
        # the Routine "training_instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        training_trials = data.TrialHandler2(
            name='training_trials',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('training.csv'), 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(training_trials)  # add the loop to the experiment
        thisTraining_trial = training_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTraining_trial.rgb)
        if thisTraining_trial != None:
            for paramName in thisTraining_trial:
                globals()[paramName] = thisTraining_trial[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTraining_trial in training_trials:
            training_trials.status = STARTED
            if hasattr(thisTraining_trial, 'status'):
                thisTraining_trial.status = STARTED
            currentLoop = training_trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTraining_trial.rgb)
            if thisTraining_trial != None:
                for paramName in thisTraining_trial:
                    globals()[paramName] = thisTraining_trial[paramName]
            
            # set up handler to look after randomisation of conditions etc
            trials_2 = data.TrialHandler2(
                name='trials_2',
                nReps=1000.0, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
                isTrials=True, 
            )
            thisExp.addLoop(trials_2)  # add the loop to the experiment
            thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    globals()[paramName] = thisTrial_2[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisTrial_2 in trials_2:
                trials_2.status = STARTED
                if hasattr(thisTrial_2, 'status'):
                    thisTrial_2.status = STARTED
                currentLoop = trials_2
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
                if thisTrial_2 != None:
                    for paramName in thisTrial_2:
                        globals()[paramName] = thisTrial_2[paramName]
                
                # --- Prepare to start Routine "fixation" ---
                # create an object to store info about Routine fixation
                fixation = data.Routine(
                    name='fixation',
                    components=[fix],
                )
                fixation.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from fix_pulse
                if evntlg :  sr.write("01".encode()) #Fixation signal
                
                # store start times for fixation
                fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                fixation.tStart = globalClock.getTime(format='float')
                fixation.status = STARTED
                thisExp.addData('fixation.started', fixation.tStart)
                fixation.maxDuration = None
                # keep track of which components have finished
                fixationComponents = fixation.components
                for thisComponent in fixation.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "fixation" ---
                thisExp.currentRoutine = fixation
                fixation.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 0.5:
                    # if trial has changed, end Routine now
                    if hasattr(thisTrial_2, 'status') and thisTrial_2.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fix* updates
                    
                    # if fix is starting this frame...
                    if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fix.frameNStart = frameN  # exact frame index
                        fix.tStart = t  # local t and not account for scr refresh
                        fix.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix.started')
                        # update status
                        fix.status = STARTED
                        fix.setAutoDraw(True)
                    
                    # if fix is active this frame...
                    if fix.status == STARTED:
                        # update params
                        pass
                    
                    # if fix is stopping this frame...
                    if fix.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            fix.tStop = t  # not accounting for scr refresh
                            fix.tStopRefresh = tThisFlipGlobal  # on global time
                            fix.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fix.stopped')
                            # update status
                            fix.status = FINISHED
                            fix.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=fixation,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # has a Component requested the Routine to end?
                    if not continueRoutine:
                        fixation.forceEnded = routineForceEnded = True
                    # has the Routine been forcibly ended?
                    if fixation.forceEnded or routineForceEnded:
                        break
                    # has every Component finished?
                    continueRoutine = False
                    for thisComponent in fixation.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "fixation" ---
                for thisComponent in fixation.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for fixation
                fixation.tStop = globalClock.getTime(format='float')
                fixation.tStopRefresh = tThisFlipGlobal
                thisExp.addData('fixation.stopped', fixation.tStop)
                # Run 'End Routine' code from fix_pulse
                if evntlg :    sr.write("00".encode()) #set lines to zero
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if fixation.maxDurationReached:
                    routineTimer.addTime(-fixation.maxDuration)
                elif fixation.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.500000)
                
                # --- Prepare to start Routine "training_routine_1" ---
                # create an object to store info about Routine training_routine_1
                training_routine_1 = data.Routine(
                    name='training_routine_1',
                    components=[textbox_3, slider_training, key_resp_train],
                )
                training_routine_1.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from training_code
                msg = ""
                if trials_2.thisN==0:
                    blockTimer=core.CountdownTimer(train_time)
                    rtDict[train_diff]=[]
                
                #Generate response
                eq_gen.make_equation(train_diff)
                eq = "%s = ?" %(eq_gen.equation)
                ans = int(eq_gen.ans)
                
                # If serial object is loaded then use it
                if evntlg :    sr.write(difbyt)
                textbox_3.reset()
                textbox_3.setText(eq)
                slider_training.reset()
                # create starting attributes for key_resp_train
                key_resp_train.keys = []
                key_resp_train.rt = []
                _key_resp_train_allKeys = []
                # store start times for training_routine_1
                training_routine_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                training_routine_1.tStart = globalClock.getTime(format='float')
                training_routine_1.status = STARTED
                thisExp.addData('training_routine_1.started', training_routine_1.tStart)
                training_routine_1.maxDuration = None
                # keep track of which components have finished
                training_routine_1Components = training_routine_1.components
                for thisComponent in training_routine_1.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "training_routine_1" ---
                thisExp.currentRoutine = training_routine_1
                training_routine_1.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisTrial_2, 'status') and thisTrial_2.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Run 'Each Frame' code from training_code
                    if blockTimer.getTime() <= 0:
                        endblock=True
                        continueRoutine = False
                        trials_2.finished = True
                    else:
                        endblock=False
                    
                    # *textbox_3* updates
                    
                    # if textbox_3 is starting this frame...
                    if textbox_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        textbox_3.frameNStart = frameN  # exact frame index
                        textbox_3.tStart = t  # local t and not account for scr refresh
                        textbox_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(textbox_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textbox_3.started')
                        # update status
                        textbox_3.status = STARTED
                        textbox_3.setAutoDraw(True)
                    
                    # if textbox_3 is active this frame...
                    if textbox_3.status == STARTED:
                        # update params
                        pass
                    
                    # *slider_training* updates
                    
                    # if slider_training is starting this frame...
                    if slider_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_training.frameNStart = frameN  # exact frame index
                        slider_training.tStart = t  # local t and not account for scr refresh
                        slider_training.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_training, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'slider_training.started')
                        # update status
                        slider_training.status = STARTED
                        slider_training.setAutoDraw(True)
                    
                    # if slider_training is active this frame...
                    if slider_training.status == STARTED:
                        # update params
                        pass
                    
                    # Check slider_training for response to end Routine
                    if slider_training.getRating() is not None and slider_training.status == STARTED:
                        continueRoutine = False
                    
                    # *key_resp_train* updates
                    waitOnFlip = False
                    
                    # if key_resp_train is starting this frame...
                    if key_resp_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_train.frameNStart = frameN  # exact frame index
                        key_resp_train.tStart = t  # local t and not account for scr refresh
                        key_resp_train.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_train, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_train.started')
                        # update status
                        key_resp_train.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_train.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_train.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_train.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_train.getKeys(keyList=["1","2","3","4","5","6","7","8","9","0","s"], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_train_allKeys.extend(theseKeys)
                        if len(_key_resp_train_allKeys):
                            key_resp_train.keys = _key_resp_train_allKeys[-1].name  # just the last key pressed
                            key_resp_train.rt = _key_resp_train_allKeys[-1].rt
                            key_resp_train.duration = _key_resp_train_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=training_routine_1,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # has a Component requested the Routine to end?
                    if not continueRoutine:
                        training_routine_1.forceEnded = routineForceEnded = True
                    # has the Routine been forcibly ended?
                    if training_routine_1.forceEnded or routineForceEnded:
                        break
                    # has every Component finished?
                    continueRoutine = False
                    for thisComponent in training_routine_1.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "training_routine_1" ---
                for thisComponent in training_routine_1.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for training_routine_1
                training_routine_1.tStop = globalClock.getTime(format='float')
                training_routine_1.tStopRefresh = tThisFlipGlobal
                thisExp.addData('training_routine_1.stopped', training_routine_1.tStop)
                # Run 'End Routine' code from training_code
                # Set serial to 0 if running
                if evntlg:  sr.write("00".encode())
                if not endblock:
                    this_key = "emp"
                    if len(key_resp_train.keys) > 0:
                        if  "s" in key_resp_train.keys:
                            rtDict[train_diff].append(10)
                            trials_2.finished=True
                            continueRoutine=False
                        else:
                            this_key = int(key_resp_train.keys[0])
                            this_resp =[slider_training.getRating(), this_key]
                
                    if  ans in this_resp:
                        msg = "Correct!"  # For correct trials add one to
                        
                    elif ans not in this_resp: # For incorrect answers
                        msg = "Incorrect!"
                  
                    if slider.getRT() is None:
                        RT = key_resp_train.rt
                    else:
                        RT = slider_training.getRT()
                    #Save rt to dictionary
                    rtDict[train_diff].append(RT)
                
                    ### save message (Corr, Timeout, Incor
                    thisExp.addData('trial.outcome', msg)
                else:
                    msg="End of block"
                
                
                trials_2.addData('slider_training.response', slider_training.getRating())
                trials_2.addData('slider_training.rt', slider_training.getRT())
                # check responses
                if key_resp_train.keys in ['', [], None]:  # No response was made
                    key_resp_train.keys = None
                trials_2.addData('key_resp_train.keys',key_resp_train.keys)
                if key_resp_train.keys != None:  # we had a response
                    trials_2.addData('key_resp_train.rt', key_resp_train.rt)
                    trials_2.addData('key_resp_train.duration', key_resp_train.duration)
                # the Routine "training_routine_1" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "feedback" ---
                # create an object to store info about Routine feedback
                feedback = data.Routine(
                    name='feedback',
                    components=[feedback_practice_1],
                )
                feedback.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                feedback_practice_1.reset()
                feedback_practice_1.setText(msg)
                # store start times for feedback
                feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                feedback.tStart = globalClock.getTime(format='float')
                feedback.status = STARTED
                thisExp.addData('feedback.started', feedback.tStart)
                feedback.maxDuration = None
                # keep track of which components have finished
                feedbackComponents = feedback.components
                for thisComponent in feedback.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "feedback" ---
                thisExp.currentRoutine = feedback
                feedback.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # if trial has changed, end Routine now
                    if hasattr(thisTrial_2, 'status') and thisTrial_2.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *feedback_practice_1* updates
                    
                    # if feedback_practice_1 is starting this frame...
                    if feedback_practice_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        feedback_practice_1.frameNStart = frameN  # exact frame index
                        feedback_practice_1.tStart = t  # local t and not account for scr refresh
                        feedback_practice_1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(feedback_practice_1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_practice_1.started')
                        # update status
                        feedback_practice_1.status = STARTED
                        feedback_practice_1.setAutoDraw(True)
                    
                    # if feedback_practice_1 is active this frame...
                    if feedback_practice_1.status == STARTED:
                        # update params
                        pass
                    
                    # if feedback_practice_1 is stopping this frame...
                    if feedback_practice_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > feedback_practice_1.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            feedback_practice_1.tStop = t  # not accounting for scr refresh
                            feedback_practice_1.tStopRefresh = tThisFlipGlobal  # on global time
                            feedback_practice_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'feedback_practice_1.stopped')
                            # update status
                            feedback_practice_1.status = FINISHED
                            feedback_practice_1.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=feedback,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # has a Component requested the Routine to end?
                    if not continueRoutine:
                        feedback.forceEnded = routineForceEnded = True
                    # has the Routine been forcibly ended?
                    if feedback.forceEnded or routineForceEnded:
                        break
                    # has every Component finished?
                    continueRoutine = False
                    for thisComponent in feedback.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "feedback" ---
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for feedback
                feedback.tStop = globalClock.getTime(format='float')
                feedback.tStopRefresh = tThisFlipGlobal
                thisExp.addData('feedback.stopped', feedback.tStop)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if feedback.maxDurationReached:
                    routineTimer.addTime(-feedback.maxDuration)
                elif feedback.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                # mark thisTrial_2 as finished
                if hasattr(thisTrial_2, 'status'):
                    thisTrial_2.status = FINISHED
                # if awaiting a pause, pause now
                if trials_2.status == PAUSED:
                    thisExp.status = PAUSED
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[globalClock], 
                    )
                    # once done pausing, restore running status
                    trials_2.status = STARTED
                thisExp.nextEntry()
                
            # completed 1000.0 repeats of 'trials_2'
            trials_2.status = FINISHED
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # --- Prepare to start Routine "next_block" ---
            # create an object to store info about Routine next_block
            next_block = data.Routine(
                name='next_block',
                components=[text_4, key_resp_3],
            )
            next_block.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for key_resp_3
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            # store start times for next_block
            next_block.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            next_block.tStart = globalClock.getTime(format='float')
            next_block.status = STARTED
            thisExp.addData('next_block.started', next_block.tStart)
            next_block.maxDuration = None
            # keep track of which components have finished
            next_blockComponents = next_block.components
            for thisComponent in next_block.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "next_block" ---
            thisExp.currentRoutine = next_block
            next_block.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisTraining_trial, 'status') and thisTraining_trial.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_4* updates
                
                # if text_4 is starting this frame...
                if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.tStart = t  # local t and not account for scr refresh
                    text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.started')
                    # update status
                    text_4.status = STARTED
                    text_4.setAutoDraw(True)
                
                # if text_4 is active this frame...
                if text_4.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_3* updates
                waitOnFlip = False
                
                # if key_resp_3 is starting this frame...
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_3.started')
                    # update status
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                        key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                        key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=next_block,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    next_block.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if next_block.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in next_block.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "next_block" ---
            for thisComponent in next_block.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for next_block
            next_block.tStop = globalClock.getTime(format='float')
            next_block.tStopRefresh = tThisFlipGlobal
            thisExp.addData('next_block.stopped', next_block.tStop)
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
                key_resp_3.keys = None
            training_trials.addData('key_resp_3.keys',key_resp_3.keys)
            if key_resp_3.keys != None:  # we had a response
                training_trials.addData('key_resp_3.rt', key_resp_3.rt)
                training_trials.addData('key_resp_3.duration', key_resp_3.duration)
            # the Routine "next_block" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisTraining_trial as finished
            if hasattr(thisTraining_trial, 'status'):
                thisTraining_trial.status = FINISHED
            # if awaiting a pause, pause now
            if training_trials.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                training_trials.status = STARTED
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'training_trials'
        training_trials.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # mark thisTestmode as finished
        if hasattr(thisTestmode, 'status'):
            thisTestmode.status = FINISHED
        # if awaiting a pause, pause now
        if testmode.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            testmode.status = STARTED
        thisExp.nextEntry()
        
    # completed 0.0 repeats of 'testmode'
    testmode.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "start_experiment" ---
    # create an object to store info about Routine start_experiment
    start_experiment = data.Routine(
        name='start_experiment',
        components=[text_6, key_resp_7],
    )
    start_experiment.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_7
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # store start times for start_experiment
    start_experiment.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    start_experiment.tStart = globalClock.getTime(format='float')
    start_experiment.status = STARTED
    thisExp.addData('start_experiment.started', start_experiment.tStart)
    start_experiment.maxDuration = None
    # keep track of which components have finished
    start_experimentComponents = start_experiment.components
    for thisComponent in start_experiment.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start_experiment" ---
    thisExp.currentRoutine = start_experiment
    start_experiment.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # *key_resp_7* updates
        waitOnFlip = False
        
        # if key_resp_7 is starting this frame...
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_7.started')
            # update status
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=start_experiment,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            start_experiment.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if start_experiment.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in start_experiment.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start_experiment" ---
    for thisComponent in start_experiment.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for start_experiment
    start_experiment.tStop = globalClock.getTime(format='float')
    start_experiment.tStopRefresh = tThisFlipGlobal
    thisExp.addData('start_experiment.stopped', start_experiment.tStop)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    thisExp.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        thisExp.addData('key_resp_7.rt', key_resp_7.rt)
        thisExp.addData('key_resp_7.duration', key_resp_7.duration)
    thisExp.nextEntry()
    # the Routine "start_experiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    experimental_trials = data.TrialHandler2(
        name='experimental_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('experiment_difficulty.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(experimental_trials)  # add the loop to the experiment
    thisExperimental_trial = experimental_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExperimental_trial.rgb)
    if thisExperimental_trial != None:
        for paramName in thisExperimental_trial:
            globals()[paramName] = thisExperimental_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisExperimental_trial in experimental_trials:
        experimental_trials.status = STARTED
        if hasattr(thisExperimental_trial, 'status'):
            thisExperimental_trial.status = STARTED
        currentLoop = experimental_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisExperimental_trial.rgb)
        if thisExperimental_trial != None:
            for paramName in thisExperimental_trial:
                globals()[paramName] = thisExperimental_trial[paramName]
        
        # set up handler to look after randomisation of conditions etc
        trials_3 = data.TrialHandler2(
            name='trials_3',
            nReps=1000.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(trials_3)  # add the loop to the experiment
        thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_3 in trials_3:
            trials_3.status = STARTED
            if hasattr(thisTrial_3, 'status'):
                thisTrial_3.status = STARTED
            currentLoop = trials_3
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    globals()[paramName] = thisTrial_3[paramName]
            
            # --- Prepare to start Routine "fixation" ---
            # create an object to store info about Routine fixation
            fixation = data.Routine(
                name='fixation',
                components=[fix],
            )
            fixation.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fix_pulse
            if evntlg :  sr.write("01".encode()) #Fixation signal
            
            # store start times for fixation
            fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            fixation.tStart = globalClock.getTime(format='float')
            fixation.status = STARTED
            thisExp.addData('fixation.started', fixation.tStart)
            fixation.maxDuration = None
            # keep track of which components have finished
            fixationComponents = fixation.components
            for thisComponent in fixation.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fixation" ---
            thisExp.currentRoutine = fixation
            fixation.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # if trial has changed, end Routine now
                if hasattr(thisTrial_3, 'status') and thisTrial_3.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fix* updates
                
                # if fix is starting this frame...
                if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fix.frameNStart = frameN  # exact frame index
                    fix.tStart = t  # local t and not account for scr refresh
                    fix.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix.started')
                    # update status
                    fix.status = STARTED
                    fix.setAutoDraw(True)
                
                # if fix is active this frame...
                if fix.status == STARTED:
                    # update params
                    pass
                
                # if fix is stopping this frame...
                if fix.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fix.tStop = t  # not accounting for scr refresh
                        fix.tStopRefresh = tThisFlipGlobal  # on global time
                        fix.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix.stopped')
                        # update status
                        fix.status = FINISHED
                        fix.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=fixation,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    fixation.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if fixation.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in fixation.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation" ---
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for fixation
            fixation.tStop = globalClock.getTime(format='float')
            fixation.tStopRefresh = tThisFlipGlobal
            thisExp.addData('fixation.stopped', fixation.tStop)
            # Run 'End Routine' code from fix_pulse
            if evntlg :    sr.write("00".encode()) #set lines to zero
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if fixation.maxDurationReached:
                routineTimer.addTime(-fixation.maxDuration)
            elif fixation.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            
            # --- Prepare to start Routine "sum_routine1" ---
            # create an object to store info about Routine sum_routine1
            sum_routine1 = data.Routine(
                name='sum_routine1',
                components=[prog, redbar, yellowbar, greenbar, targarrow, userArrow, yourperfexp, tarlabexp, textbox, slider, key_resp, norm_arrow],
            )
            sum_routine1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code
            # If serial object is loaded then use it
            if evntlg :    sr.write(diffbyt.encode())
            msg = ""
            ## Set first trial conditions
            if trials_3.thisRepN == 0:
                #No pointer on first trial
                pointer_pos=-2
                expDict[exp_diff]=[]
                endblock=False
                blockTimer=core.CountdownTimer(exp_time)
                if testmode.nreps==0:      
                    time = 10       
                else:
                    rtDict[exp_diff] = list(filter(None, rtDict[exp_diff]))
                    time = np.mean(rtDict[exp_diff]) * time_coef
                    ### Reduce average trial time by 10%
                
                trial_counter=0
                thisdiffcor=0
            
            timer = core.CountdownTimer(time)
            eq_gen.make_equation(exp_diff)
            eq = "%s = ?" %(eq_gen.equation)
            ans = int(eq_gen.ans)
            timeout = False
            userArrow.setPos((1-pointer_pos, 0.6))
            yourperfexp.reset()
            yourperfexp.setPos((1-pointer_pos, 0.55))
            tarlabexp.reset()
            textbox.reset()
            textbox.setText(eq)
            slider.reset()
            # create starting attributes for key_resp
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            # store start times for sum_routine1
            sum_routine1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            sum_routine1.tStart = globalClock.getTime(format='float')
            sum_routine1.status = STARTED
            thisExp.addData('sum_routine1.started', sum_routine1.tStart)
            sum_routine1.maxDuration = None
            # keep track of which components have finished
            sum_routine1Components = sum_routine1.components
            for thisComponent in sum_routine1.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "sum_routine1" ---
            thisExp.currentRoutine = sum_routine1
            sum_routine1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisTrial_3, 'status') and thisTrial_3.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code
                if timer.getTime() <= 0:
                    continueRoutine = False
                    timeout = True
                if blockTimer.getTime() <=0:
                    trials_3.finished=True
                    continueRoutine=False
                    timeout=False
                    endblock=True
                
                # *prog* updates
                
                # if prog is starting this frame...
                if prog.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    prog.frameNStart = frameN  # exact frame index
                    prog.tStart = t  # local t and not account for scr refresh
                    prog.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(prog, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prog.started')
                    # update status
                    prog.status = STARTED
                    prog.setAutoDraw(True)
                
                # if prog is active this frame...
                if prog.status == STARTED:
                    # update params
                    prog.setProgress(0 + (timer.getTime()/time), log=False)
                
                # if prog is stopping this frame...
                if prog.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > prog.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        prog.tStop = t  # not accounting for scr refresh
                        prog.tStopRefresh = tThisFlipGlobal  # on global time
                        prog.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'prog.stopped')
                        # update status
                        prog.status = FINISHED
                        prog.setAutoDraw(False)
                
                # *redbar* updates
                
                # if redbar is starting this frame...
                if redbar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    redbar.frameNStart = frameN  # exact frame index
                    redbar.tStart = t  # local t and not account for scr refresh
                    redbar.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(redbar, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'redbar.started')
                    # update status
                    redbar.status = STARTED
                    redbar.setAutoDraw(True)
                
                # if redbar is active this frame...
                if redbar.status == STARTED:
                    # update params
                    pass
                
                # if redbar is stopping this frame...
                if redbar.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > redbar.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        redbar.tStop = t  # not accounting for scr refresh
                        redbar.tStopRefresh = tThisFlipGlobal  # on global time
                        redbar.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'redbar.stopped')
                        # update status
                        redbar.status = FINISHED
                        redbar.setAutoDraw(False)
                
                # *yellowbar* updates
                
                # if yellowbar is starting this frame...
                if yellowbar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    yellowbar.frameNStart = frameN  # exact frame index
                    yellowbar.tStart = t  # local t and not account for scr refresh
                    yellowbar.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(yellowbar, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'yellowbar.started')
                    # update status
                    yellowbar.status = STARTED
                    yellowbar.setAutoDraw(True)
                
                # if yellowbar is active this frame...
                if yellowbar.status == STARTED:
                    # update params
                    pass
                
                # if yellowbar is stopping this frame...
                if yellowbar.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > yellowbar.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        yellowbar.tStop = t  # not accounting for scr refresh
                        yellowbar.tStopRefresh = tThisFlipGlobal  # on global time
                        yellowbar.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'yellowbar.stopped')
                        # update status
                        yellowbar.status = FINISHED
                        yellowbar.setAutoDraw(False)
                
                # *greenbar* updates
                
                # if greenbar is starting this frame...
                if greenbar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    greenbar.frameNStart = frameN  # exact frame index
                    greenbar.tStart = t  # local t and not account for scr refresh
                    greenbar.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(greenbar, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'greenbar.started')
                    # update status
                    greenbar.status = STARTED
                    greenbar.setAutoDraw(True)
                
                # if greenbar is active this frame...
                if greenbar.status == STARTED:
                    # update params
                    pass
                
                # if greenbar is stopping this frame...
                if greenbar.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > greenbar.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        greenbar.tStop = t  # not accounting for scr refresh
                        greenbar.tStopRefresh = tThisFlipGlobal  # on global time
                        greenbar.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'greenbar.stopped')
                        # update status
                        greenbar.status = FINISHED
                        greenbar.setAutoDraw(False)
                
                # *targarrow* updates
                
                # if targarrow is starting this frame...
                if targarrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    targarrow.frameNStart = frameN  # exact frame index
                    targarrow.tStart = t  # local t and not account for scr refresh
                    targarrow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(targarrow, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'targarrow.started')
                    # update status
                    targarrow.status = STARTED
                    targarrow.setAutoDraw(True)
                
                # if targarrow is active this frame...
                if targarrow.status == STARTED:
                    # update params
                    pass
                
                # if targarrow is stopping this frame...
                if targarrow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > targarrow.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        targarrow.tStop = t  # not accounting for scr refresh
                        targarrow.tStopRefresh = tThisFlipGlobal  # on global time
                        targarrow.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'targarrow.stopped')
                        # update status
                        targarrow.status = FINISHED
                        targarrow.setAutoDraw(False)
                
                # *userArrow* updates
                
                # if userArrow is starting this frame...
                if userArrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    userArrow.frameNStart = frameN  # exact frame index
                    userArrow.tStart = t  # local t and not account for scr refresh
                    userArrow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(userArrow, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'userArrow.started')
                    # update status
                    userArrow.status = STARTED
                    userArrow.setAutoDraw(True)
                
                # if userArrow is active this frame...
                if userArrow.status == STARTED:
                    # update params
                    pass
                
                # if userArrow is stopping this frame...
                if userArrow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > userArrow.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        userArrow.tStop = t  # not accounting for scr refresh
                        userArrow.tStopRefresh = tThisFlipGlobal  # on global time
                        userArrow.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'userArrow.stopped')
                        # update status
                        userArrow.status = FINISHED
                        userArrow.setAutoDraw(False)
                
                # *yourperfexp* updates
                
                # if yourperfexp is starting this frame...
                if yourperfexp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    yourperfexp.frameNStart = frameN  # exact frame index
                    yourperfexp.tStart = t  # local t and not account for scr refresh
                    yourperfexp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(yourperfexp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'yourperfexp.started')
                    # update status
                    yourperfexp.status = STARTED
                    yourperfexp.setAutoDraw(True)
                
                # if yourperfexp is active this frame...
                if yourperfexp.status == STARTED:
                    # update params
                    pass
                
                # if yourperfexp is stopping this frame...
                if yourperfexp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > yourperfexp.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        yourperfexp.tStop = t  # not accounting for scr refresh
                        yourperfexp.tStopRefresh = tThisFlipGlobal  # on global time
                        yourperfexp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'yourperfexp.stopped')
                        # update status
                        yourperfexp.status = FINISHED
                        yourperfexp.setAutoDraw(False)
                
                # *tarlabexp* updates
                
                # if tarlabexp is starting this frame...
                if tarlabexp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    tarlabexp.frameNStart = frameN  # exact frame index
                    tarlabexp.tStart = t  # local t and not account for scr refresh
                    tarlabexp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(tarlabexp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tarlabexp.started')
                    # update status
                    tarlabexp.status = STARTED
                    tarlabexp.setAutoDraw(True)
                
                # if tarlabexp is active this frame...
                if tarlabexp.status == STARTED:
                    # update params
                    pass
                
                # if tarlabexp is stopping this frame...
                if tarlabexp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > tarlabexp.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        tarlabexp.tStop = t  # not accounting for scr refresh
                        tarlabexp.tStopRefresh = tThisFlipGlobal  # on global time
                        tarlabexp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'tarlabexp.stopped')
                        # update status
                        tarlabexp.status = FINISHED
                        tarlabexp.setAutoDraw(False)
                
                # *textbox* updates
                
                # if textbox is starting this frame...
                if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textbox.frameNStart = frameN  # exact frame index
                    textbox.tStart = t  # local t and not account for scr refresh
                    textbox.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox.started')
                    # update status
                    textbox.status = STARTED
                    textbox.setAutoDraw(True)
                
                # if textbox is active this frame...
                if textbox.status == STARTED:
                    # update params
                    pass
                
                # if textbox is stopping this frame...
                if textbox.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textbox.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        textbox.tStop = t  # not accounting for scr refresh
                        textbox.tStopRefresh = tThisFlipGlobal  # on global time
                        textbox.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textbox.stopped')
                        # update status
                        textbox.status = FINISHED
                        textbox.setAutoDraw(False)
                
                # *slider* updates
                
                # if slider is starting this frame...
                if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    slider.frameNStart = frameN  # exact frame index
                    slider.tStart = t  # local t and not account for scr refresh
                    slider.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'slider.started')
                    # update status
                    slider.status = STARTED
                    slider.setAutoDraw(True)
                
                # if slider is active this frame...
                if slider.status == STARTED:
                    # update params
                    pass
                
                # if slider is stopping this frame...
                if slider.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > slider.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        slider.tStop = t  # not accounting for scr refresh
                        slider.tStopRefresh = tThisFlipGlobal  # on global time
                        slider.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'slider.stopped')
                        # update status
                        slider.status = FINISHED
                        slider.setAutoDraw(False)
                
                # Check slider for response to end Routine
                if slider.getRating() is not None and slider.status == STARTED:
                    continueRoutine = False
                
                # *key_resp* updates
                waitOnFlip = False
                
                # if key_resp is starting this frame...
                if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp.frameNStart = frameN  # exact frame index
                    key_resp.tStart = t  # local t and not account for scr refresh
                    key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.started')
                    # update status
                    key_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if key_resp is stopping this frame...
                if key_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp.tStop = t  # not accounting for scr refresh
                        key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp.stopped')
                        # update status
                        key_resp.status = FINISHED
                        key_resp.status = FINISHED
                if key_resp.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp.getKeys(keyList=["1","2","3","4","5","6","7","8","9","0","s"], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_allKeys.extend(theseKeys)
                    if len(_key_resp_allKeys):
                        key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                        key_resp.rt = _key_resp_allKeys[-1].rt
                        key_resp.duration = _key_resp_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *norm_arrow* updates
                
                # if norm_arrow is starting this frame...
                if norm_arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    norm_arrow.frameNStart = frameN  # exact frame index
                    norm_arrow.tStart = t  # local t and not account for scr refresh
                    norm_arrow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(norm_arrow, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'norm_arrow.started')
                    # update status
                    norm_arrow.status = STARTED
                    norm_arrow.setAutoDraw(True)
                
                # if norm_arrow is active this frame...
                if norm_arrow.status == STARTED:
                    # update params
                    pass
                
                # if norm_arrow is stopping this frame...
                if norm_arrow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > norm_arrow.tStartRefresh + time-frameTolerance:
                        # keep track of stop time/frame for later
                        norm_arrow.tStop = t  # not accounting for scr refresh
                        norm_arrow.tStopRefresh = tThisFlipGlobal  # on global time
                        norm_arrow.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'norm_arrow.stopped')
                        # update status
                        norm_arrow.status = FINISHED
                        norm_arrow.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=sum_routine1,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    sum_routine1.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if sum_routine1.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in sum_routine1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "sum_routine1" ---
            for thisComponent in sum_routine1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for sum_routine1
            sum_routine1.tStop = globalClock.getTime(format='float')
            sum_routine1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('sum_routine1.stopped', sum_routine1.tStop)
            # Run 'End Routine' code from code
            # Set serial to 0 if running
            if evntlg:  sr.write("00".encode())
            
            # Set variables and adjust pointer
            if not endblock:
                ## Save responses
                thisExp.addData('streak.count', streak_count)
                thisExp.addData('time', time_coef)
                thisExp.addData('time.coef', time_coef)
                thisExp.addData('total.cor', total_cor)
                thisExp.addData('trial.count', trial_counter)
                ##  Create placeholder this_key
                this_key = "emp"
                if len(key_resp.keys) > 0:
                    ## Cheat code
                    if  "s" in key_resp.keys:
                        trials_3.finished=True
                        continueRoutine=False
                    else:
                        this_key = int(key_resp.keys[0])
                        this_resp =[slider.getRating(), this_key]
                        ## When correct
                        if  ans in this_resp:
                            msg = "Correct!"  # For correct trials add one to
                            streak_count += 1   # correct counter
                            total_cor += 1 
                            thisdiffcor += 1 
                            # and total correct.
                            if trial_counter <= 5: ##for first trials increase perf
                                pointer_pos -= 0.02  # increase userAverage pointer by 0.05
                                #if pointer_pos <= .4: ## Don't go over 80%
                                #    pointer_pos = .4
                            elif trial_counter > 5: ## After trial 5, only decrease perf
                                pointer_pos += 0.02
                                if pointer_pos >= 1.8:
                                    pointer_pos = 1.8
                        ##  When incorrect
                        elif ans not in this_resp: # For incorrect answers
                            msg = "Incorrect!"
                        if slider.getRT() is None:
                            RT = key_resp.rt
                        else:
                            RT = slider.getRT()
                ## When timed out
                elif timeout:
                        msg = "Timed Out!"
                        RT = time
            
                if timeout or msg == "Incorrect!":
                    pointer_pos += 0.1  # add 0.1 (5%) to userAverage pointer (1-userAv)
                    if streak_count > 0:
                        streak_count = 0
                        streak_count -= 1  # set streak to 0 and minus 1 (count incorrect)
                    if pointer_pos >= 1.8:
                        pointer_pos = 1.8
                ### Set next trial times if needed
                if streak_count == 3:  # every 3 correct answers reduces the mean time by 10%
                    time = (time * time_coef)
                    streak_count = 0  # resets the counter
            
                if streak_count == -3:  # every three incorrect answers
                    time = (time/time_coef) # time is increased by 10%
                    streak_count = 0  # resets counter
            
                ### save message (Corr, Timeout, Incor
                thisExp.addData('trial.outcome', msg)
            
                if trial_counter == 1:
                    if streak_count == 2:
                        pointer_pos=0.45
                    elif streak_count < 2:
                        pointer_pos=0.9
                trial_counter += 1
            else:
                msg="End of block"
                perf= f"You scored {thisdiffcor} out of {trial_counter} on this block \n\n Please press space to continue."
            trials_3.addData('slider.response', slider.getRating())
            trials_3.addData('slider.rt', slider.getRT())
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
            trials_3.addData('key_resp.keys',key_resp.keys)
            if key_resp.keys != None:  # we had a response
                trials_3.addData('key_resp.rt', key_resp.rt)
                trials_3.addData('key_resp.duration', key_resp.duration)
            # the Routine "sum_routine1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback" ---
            # create an object to store info about Routine feedback
            feedback = data.Routine(
                name='feedback',
                components=[feedback_practice_1],
            )
            feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            feedback_practice_1.reset()
            feedback_practice_1.setText(msg)
            # store start times for feedback
            feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback.tStart = globalClock.getTime(format='float')
            feedback.status = STARTED
            thisExp.addData('feedback.started', feedback.tStart)
            feedback.maxDuration = None
            # keep track of which components have finished
            feedbackComponents = feedback.components
            for thisComponent in feedback.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback" ---
            thisExp.currentRoutine = feedback
            feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # if trial has changed, end Routine now
                if hasattr(thisTrial_3, 'status') and thisTrial_3.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_practice_1* updates
                
                # if feedback_practice_1 is starting this frame...
                if feedback_practice_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_practice_1.frameNStart = frameN  # exact frame index
                    feedback_practice_1.tStart = t  # local t and not account for scr refresh
                    feedback_practice_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_practice_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_practice_1.started')
                    # update status
                    feedback_practice_1.status = STARTED
                    feedback_practice_1.setAutoDraw(True)
                
                # if feedback_practice_1 is active this frame...
                if feedback_practice_1.status == STARTED:
                    # update params
                    pass
                
                # if feedback_practice_1 is stopping this frame...
                if feedback_practice_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_practice_1.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_practice_1.tStop = t  # not accounting for scr refresh
                        feedback_practice_1.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_practice_1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_practice_1.stopped')
                        # update status
                        feedback_practice_1.status = FINISHED
                        feedback_practice_1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=feedback,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    feedback.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if feedback.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback" ---
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback
            feedback.tStop = globalClock.getTime(format='float')
            feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback.stopped', feedback.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback.maxDurationReached:
                routineTimer.addTime(-feedback.maxDuration)
            elif feedback.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            # mark thisTrial_3 as finished
            if hasattr(thisTrial_3, 'status'):
                thisTrial_3.status = FINISHED
            # if awaiting a pause, pause now
            if trials_3.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                trials_3.status = STARTED
            thisExp.nextEntry()
            
        # completed 1000.0 repeats of 'trials_3'
        trials_3.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "perf_feedback" ---
        # create an object to store info about Routine perf_feedback
        perf_feedback = data.Routine(
            name='perf_feedback',
            components=[text_5, key_resp_6],
        )
        perf_feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_5.setText(perf)
        # create starting attributes for key_resp_6
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # store start times for perf_feedback
        perf_feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        perf_feedback.tStart = globalClock.getTime(format='float')
        perf_feedback.status = STARTED
        thisExp.addData('perf_feedback.started', perf_feedback.tStart)
        perf_feedback.maxDuration = None
        # keep track of which components have finished
        perf_feedbackComponents = perf_feedback.components
        for thisComponent in perf_feedback.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "perf_feedback" ---
        thisExp.currentRoutine = perf_feedback
        perf_feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisExperimental_trial, 'status') and thisExperimental_trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_6* updates
            waitOnFlip = False
            
            # if key_resp_6 is starting this frame...
            if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_6.started')
                # update status
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=perf_feedback,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                perf_feedback.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if perf_feedback.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in perf_feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "perf_feedback" ---
        for thisComponent in perf_feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for perf_feedback
        perf_feedback.tStop = globalClock.getTime(format='float')
        perf_feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('perf_feedback.stopped', perf_feedback.tStop)
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
        experimental_trials.addData('key_resp_6.keys',key_resp_6.keys)
        if key_resp_6.keys != None:  # we had a response
            experimental_trials.addData('key_resp_6.rt', key_resp_6.rt)
            experimental_trials.addData('key_resp_6.duration', key_resp_6.duration)
        # the Routine "perf_feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisExperimental_trial as finished
        if hasattr(thisExperimental_trial, 'status'):
            thisExperimental_trial.status = FINISHED
        # if awaiting a pause, pause now
        if experimental_trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            experimental_trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'experimental_trials'
    experimental_trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "thanks" ---
    # create an object to store info about Routine thanks
    thanks = data.Routine(
        name='thanks',
        components=[text_7, key_resp_10],
    )
    thanks.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_10
    key_resp_10.keys = []
    key_resp_10.rt = []
    _key_resp_10_allKeys = []
    # store start times for thanks
    thanks.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    thanks.tStart = globalClock.getTime(format='float')
    thanks.status = STARTED
    thisExp.addData('thanks.started', thanks.tStart)
    thanks.maxDuration = None
    # keep track of which components have finished
    thanksComponents = thanks.components
    for thisComponent in thanks.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "thanks" ---
    thisExp.currentRoutine = thanks
    thanks.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # *key_resp_10* updates
        waitOnFlip = False
        
        # if key_resp_10 is starting this frame...
        if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_10.started')
            # update status
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_10.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_10_allKeys.extend(theseKeys)
            if len(_key_resp_10_allKeys):
                key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                key_resp_10.duration = _key_resp_10_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=thanks,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            thanks.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if thanks.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in thanks.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thanks" ---
    for thisComponent in thanks.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for thanks
    thanks.tStop = globalClock.getTime(format='float')
    thanks.tStopRefresh = tThisFlipGlobal
    thisExp.addData('thanks.stopped', thanks.tStop)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    thisExp.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        thisExp.addData('key_resp_10.rt', key_resp_10.rt)
        thisExp.addData('key_resp_10.duration', key_resp_10.duration)
    thisExp.nextEntry()
    # the Routine "thanks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # Run 'End Experiment' code from setup_exp
    if evntlg :
        sr.flush()
        sr.close()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)

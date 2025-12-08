#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.2.3),
    on Mon 08 Dec 2025 07:04:58 PM GMT
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
psychopyVersion = '2025.2.3'
expName = 'misty_py'  # from the Builder filename that created this script
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
        originPath='/home/hackerman/MIST_v1.0/misty_py.py',
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
    
    # --- Initialize components for Routine "sum_routine1" ---
    # Run 'Begin Experiment' code from code
    import random
    import itertools
    import numexpr
    class eqGenTools(object):
        def __init__(self, diff, intQty=0, ops=0):
            self.intQty = intQty #this refers to how many integers you want to create
            self.ops = ops
        def intTool(self, intQty, diff): #creates a dictionary and fills it with integ values
            self.intDic=[]
            if diff == "med2":
                integers = [9,9,99,99]
                random.shuffle(integers)
                self.ops = ('*', '-', '*')
            elif diff == "med1":
                integers = [9,9,9,9]
                self.ops = ('+', '-', '*')
            elif diff =="easy1":
                integers = [9,9]
                self.ops = ('+','-')
            elif diff == "easy2":
                 integers = [9,9,9]
                 self.ops = ('+', '-')
            elif diff == "hard":
                integers = [99,99,99,99]
                self.ops = ('+','-','/','*')
            self.intQty = len(integers)
     
            for i, val in enumerate(integers):
                    num = range(1,integers[i])
                    temp = float(random.choice(num))
                    self.intDic.append(temp)
             
                 
        def optGenTool(self, ops):
            self.opDic=[]
            temp = 0
            for i in range(0,(self.intQty-1)):
                 temp = str(random.choice(self.ops))
                 self.opDic.append(temp)
        
        def eqGenerator(self, dictlist, optlist):
            
            while True:
                self.intTool(self.intQty, self.diff)
                self.equation = [x for x in itertools.chain.from_iterable(itertools.zip_longest(self.intDic,self.opDic, fillvalue=''))]
                self.equation = ' '.join(str(e) for e in self.equation)
                
                if ("/0" not in self.equation):
                    break
            self.ans = eval(self.equation)
    
    class MISTEasy1(eqGenTools):
        def __init__(self, ans=0, equation=0, diff="med", intQty=0, opQty=0, ops=0, dictlist=[], optlist=[]):
            eqGenTools.__init__(self, diff, intQty, opQty)
            self.equation = equation
            self.ans = ans
            self.diff = diff
            self.intQty = intQty
            self.ops = ops
        
        def EasyOps1(self):
            while True:
                self.intTool(self.intQty, self.diff)
                self.optGenTool(self.ops)
                self.eqGenerator(self.intDic, self.opDic)
                if ((float(self.ans).is_integer()) and (self.ans>=0) and (self.ans <=9)):
                    self.equation = self.equation.replace('.0','')
                    self.ans = str(self.ans).replace('.0','')
                    break
    
    usrAvg = 0
    msg = ""
    eq = ""
    corCount = 0
    inCorCount = 0
    meanRT = []
    time = 10
    totalCor = 0
    difficulty = "easy1"
    timeCoef = 1
    
    prog = visual.Progress(
        win, name='prog',
        progress=0.0,
        pos=(-0.5, 0.5), size=(1, 0.1), anchor='top-left', units='norm',
        barColor=(1.0000, -1.0000, -1.0000), backColor=(-1.0000, 0.5373, -1.0000), borderColor='white', colorSpace='rgb',
        lineWidth=4.0, opacity=1.0, ori=0.0,
        depth=-1
    )
    greenbar = visual.Rect(
        win=win, name='greenbar',units='norm', 
        width=(2/3, 0.1)[0], height=(2/3, 0.1)[1],
        ori=0.0, pos=(1/3, 0.7), draggable=False, anchor='center-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=(-1.0000, 0.0039, -1.0000),
        opacity=None, depth=-2.0, interpolate=True)
    yellowbar = visual.Rect(
        win=win, name='yellowbar',units='norm', 
        width=(2/3, 0.1)[0], height=(2/3, 0.1)[1],
        ori=0.0, pos=(-1/3, 0.7), draggable=False, anchor='center-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=(1.0000, 1.0000, -1.0000),
        opacity=None, depth=-3.0, interpolate=True)
    redbar = visual.Rect(
        win=win, name='redbar',units='norm', 
        width=(2/3, 0.1)[0], height=(2/3, 0.1)[1],
        ori=0.0, pos=(-1, 0.7), draggable=False, anchor='center-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=(1.0000, -1.0000, -1.0000),
        opacity=None, depth=-4.0, interpolate=True)
    arrow = visual.ShapeStim(
        win=win, name='arrow', vertices='arrow',units='norm', 
        size=(0.05, 0.05),
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
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
         depth=-6, autoLog=True,
    )
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
        labels=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=0.0,
        style='choice', styleTweaks=[], opacity=None,
        labelColor=(-1.0000, 0.0039, 0.0039), markerColor=(1.0000, -0.4588, -1.0000), lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-7, readOnly=False)
    
    # --- Initialize components for Routine "feedback" ---
    textbox_2 = visual.TextBox2(
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
         name='textbox_2',
         depth=0, autoLog=True,
    )
    
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
    trials = data.TrialHandler2(
        name='trials',
        nReps=10.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        trials.status = STARTED
        if hasattr(thisTrial, 'status'):
            thisTrial.status = STARTED
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "sum_routine1" ---
        # create an object to store info about Routine sum_routine1
        sum_routine1 = data.Routine(
            name='sum_routine1',
            components=[prog, greenbar, yellowbar, redbar, arrow, textbox, slider],
        )
        sum_routine1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        msg = ""
        timer = core.CountdownTimer(time)
        x = MISTEasy1( diff = difficulty)
        x.EasyOps1()
        eq = "%s = ?" %(x.equation)
        ans = int(x.ans)
        timeout = False
        arrow.setPos((1-usrAvg, 0.6))
        textbox.reset()
        textbox.setText(eq)
        slider.reset()
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
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
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
            
            # *arrow* updates
            
            # if arrow is starting this frame...
            if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow.frameNStart = frameN  # exact frame index
                arrow.tStart = t  # local t and not account for scr refresh
                arrow.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arrow.started')
                # update status
                arrow.status = STARTED
                arrow.setAutoDraw(True)
            
            # if arrow is active this frame...
            if arrow.status == STARTED:
                # update params
                pass
            
            # if arrow is stopping this frame...
            if arrow.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > arrow.tStartRefresh + time-frameTolerance:
                    # keep track of stop time/frame for later
                    arrow.tStop = t  # not accounting for scr refresh
                    arrow.tStopRefresh = tThisFlipGlobal  # on global time
                    arrow.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'arrow.stopped')
                    # update status
                    arrow.status = FINISHED
                    arrow.setAutoDraw(False)
            
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
        # Run 'End Routine' code from code
        if slider.getRating() == ans: 
                msg = "Correct"                #For correct trials add one to 
                corCount = corCount + 1       #correct counter
                totalCor=totalCor + 1           #and total correct.
                #usrAvg = usrAvg - 0.05         #increase userAverage pointer by 0.05
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
        
        # store stop times for sum_routine1
        sum_routine1.tStop = globalClock.getTime(format='float')
        sum_routine1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('sum_routine1.stopped', sum_routine1.tStop)
        trials.addData('slider.response', slider.getRating())
        trials.addData('slider.rt', slider.getRT())
        # the Routine "sum_routine1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        # create an object to store info about Routine feedback
        feedback = data.Routine(
            name='feedback',
            components=[textbox_2],
        )
        feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textbox_2.reset()
        textbox_2.setText(msg)
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
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textbox_2* updates
            
            # if textbox_2 is starting this frame...
            if textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_2.frameNStart = frameN  # exact frame index
                textbox_2.tStart = t  # local t and not account for scr refresh
                textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_2.started')
                # update status
                textbox_2.status = STARTED
                textbox_2.setAutoDraw(True)
            
            # if textbox_2 is active this frame...
            if textbox_2.status == STARTED:
                # update params
                pass
            
            # if textbox_2 is stopping this frame...
            if textbox_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_2.tStop = t  # not accounting for scr refresh
                    textbox_2.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_2.stopped')
                    # update status
                    textbox_2.status = FINISHED
                    textbox_2.setAutoDraw(False)
            
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
        # mark thisTrial as finished
        if hasattr(thisTrial, 'status'):
            thisTrial.status = FINISHED
        # if awaiting a pause, pause now
        if trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'trials'
    trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
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

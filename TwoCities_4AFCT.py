#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on június 16, 2022, at 10:23
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'Hippopolis_4AFCT'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Users\\USER\\Desktop\\Hippopolis\\TwoCities_4AFCT.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=(1.0000, 1.0000, 1.0000), colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()
ID = expInfo['participant']
city_list = './stimuli/subj_files/' + ID + '_city_list.csv'
repetitions = 0

# Initialize components for Routine "test_instructions"
test_instructionsClock = core.Clock()
learning_instructions_text = visual.TextStim(win=win, name='learning_instructions_text',
    text='A következőkben 4 kép közül kell kiválasztania, melyiket látta legutóbb a megadott utcában.\n\nAz utcanevet a képernyő tetején tüntetjük fel, ez alatt jelennek meg a választható képek. \nA D, F, J és K billentyűk segítségével válasszon a képek közül. \n\nA SZÓKÖZ lenyomásával elindul a feladat.',
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1400.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro_key = keyboard.Keyboard()

# Initialize components for Routine "city_name"
city_nameClock = core.Clock()
cityname_text = visual.TextStim(win=win, name='cityname_text',
    text='',
    font='Open Sans',
    pos=(0, 400), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
city_image = visual.ImageStim(
    win=win,
    name='city_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -100), size=(1200, 630),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
target = 0
lure = 0
dist1 = 0
dist2 = 0

repetitions = 0

# Initialize components for Routine "fixation_cross"
fixation_crossClock = core.Clock()
fx_cross = visual.TextStim(win=win, name='fx_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "test_trial"
test_trialClock = core.Clock()
plate_updating = visual.ImageStim(
    win=win,
    name='plate_updating', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 350), size=(513, 215),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
city_text_updating = visual.TextStim(win=win, name='city_text_updating',
    text='',
    font='Open Sans',
    pos=(0, 400), height=36.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
street_text_updating = visual.TextStim(win=win, name='street_text_updating',
    text='',
    font='Open Sans',
    pos=(0, 320), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
test_image1 = visual.ImageStim(
    win=win,
    name='test_image1', 
    image='sin', mask=None,
    ori=0.0, pos=(-512, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
test_image2 = visual.ImageStim(
    win=win,
    name='test_image2', 
    image='sin', mask=None,
    ori=0.0, pos=(-192, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
test_image3 = visual.ImageStim(
    win=win,
    name='test_image3', 
    image='sin', mask=None,
    ori=0.0, pos=(192, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
test_image4 = visual.ImageStim(
    win=win,
    name='test_image4', 
    image='sin', mask=None,
    ori=0.0, pos=(512, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
button_d = visual.ImageStim(
    win=win,
    name='button_d', 
    image='stimuli\\\\test_4afc_d.png', mask=None,
    ori=0.0, pos=(-512, -350), size=(99, 94),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
button_f = visual.ImageStim(
    win=win,
    name='button_f', 
    image='stimuli\\\\test_4afc_f.png', mask=None,
    ori=0.0, pos=(-192,-350), size=(99, 94),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
button_j = visual.ImageStim(
    win=win,
    name='button_j', 
    image='stimuli\\\\test_4afc_j.png', mask=None,
    ori=0.0, pos=(192, -350), size=(99, 94),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
button_k = visual.ImageStim(
    win=win,
    name='button_k', 
    image='stimuli\\\\test_4afc_k.png', mask=None,
    ori=0.0, pos=(512, -350), size=(99, 94),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "short_break"
short_breakClock = core.Clock()
short_break_text = visual.TextStim(win=win, name='short_break_text',
    text='Rövid szünet....\n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
short_break_key = keyboard.Keyboard()

# Initialize components for Routine "take_a_break"
take_a_breakClock = core.Clock()
break_text = visual.TextStim(win=win, name='break_text',
    text='Szünet....\nA szünet után a másik város következik. \n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break_key_resp = keyboard.Keyboard()

# Initialize components for Routine "end_task"
end_taskClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Vége a vizsgálatnak! \n\nKöszönjük a részvételt!',
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1000.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test_instructions"-------
continueRoutine = True
# update component parameters for each repeat
intro_key.keys = []
intro_key.rt = []
_intro_key_allKeys = []
# keep track of which components have finished
test_instructionsComponents = [learning_instructions_text, intro_key]
for thisComponent in test_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test_instructions"-------
while continueRoutine:
    # get current time
    t = test_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *learning_instructions_text* updates
    if learning_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        learning_instructions_text.frameNStart = frameN  # exact frame index
        learning_instructions_text.tStart = t  # local t and not account for scr refresh
        learning_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learning_instructions_text, 'tStartRefresh')  # time at next scr refresh
        learning_instructions_text.setAutoDraw(True)
    
    # *intro_key* updates
    waitOnFlip = False
    if intro_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key.frameNStart = frameN  # exact frame index
        intro_key.tStart = t  # local t and not account for scr refresh
        intro_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key, 'tStartRefresh')  # time at next scr refresh
        intro_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key.status == STARTED and not waitOnFlip:
        theseKeys = intro_key.getKeys(keyList=['space'], waitRelease=False)
        _intro_key_allKeys.extend(theseKeys)
        if len(_intro_key_allKeys):
            intro_key.keys = _intro_key_allKeys[-1].name  # just the last key pressed
            intro_key.rt = _intro_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test_instructions"-------
for thisComponent in test_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('learning_instructions_text.started', learning_instructions_text.tStartRefresh)
thisExp.addData('learning_instructions_text.stopped', learning_instructions_text.tStopRefresh)
# check responses
if intro_key.keys in ['', [], None]:  # No response was made
    intro_key.keys = None
thisExp.addData('intro_key.keys',intro_key.keys)
if intro_key.keys != None:  # we had a response
    thisExp.addData('intro_key.rt', intro_key.rt)
thisExp.addData('intro_key.started', intro_key.tStartRefresh)
thisExp.addData('intro_key.stopped', intro_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "test_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
CityBlock = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(city_list),
    seed=None, name='CityBlock')
thisExp.addLoop(CityBlock)  # add the loop to the experiment
thisCityBlock = CityBlock.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCityBlock.rgb)
if thisCityBlock != None:
    for paramName in thisCityBlock:
        exec('{} = thisCityBlock[paramName]'.format(paramName))

for thisCityBlock in CityBlock:
    currentLoop = CityBlock
    # abbreviate parameter names if possible (e.g. rgb = thisCityBlock.rgb)
    if thisCityBlock != None:
        for paramName in thisCityBlock:
            exec('{} = thisCityBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "city_name"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    cityname_text.setText(CityName)
    city_image.setImage(CityImage)
    target = 0
    lure = 0
    dist1 = 0
    dist2 = 0
    
    trial_count = 0
    repetitions += 1
    
    # keep track of which components have finished
    city_nameComponents = [cityname_text, city_image]
    for thisComponent in city_nameComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    city_nameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "city_name"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = city_nameClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=city_nameClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cityname_text* updates
        if cityname_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cityname_text.frameNStart = frameN  # exact frame index
            cityname_text.tStart = t  # local t and not account for scr refresh
            cityname_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cityname_text, 'tStartRefresh')  # time at next scr refresh
            cityname_text.setAutoDraw(True)
        if cityname_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cityname_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                cityname_text.tStop = t  # not accounting for scr refresh
                cityname_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cityname_text, 'tStopRefresh')  # time at next scr refresh
                cityname_text.setAutoDraw(False)
        
        # *city_image* updates
        if city_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            city_image.frameNStart = frameN  # exact frame index
            city_image.tStart = t  # local t and not account for scr refresh
            city_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(city_image, 'tStartRefresh')  # time at next scr refresh
            city_image.setAutoDraw(True)
        if city_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > city_image.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                city_image.tStop = t  # not accounting for scr refresh
                city_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(city_image, 'tStopRefresh')  # time at next scr refresh
                city_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in city_nameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "city_name"-------
    for thisComponent in city_nameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    CityBlock.addData('cityname_text.started', cityname_text.tStartRefresh)
    CityBlock.addData('cityname_text.stopped', cityname_text.tStopRefresh)
    CityBlock.addData('city_image.started', city_image.tStartRefresh)
    CityBlock.addData('city_image.stopped', city_image.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    LearningTrials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(StimuliFile),
        seed=None, name='LearningTrials')
    thisExp.addLoop(LearningTrials)  # add the loop to the experiment
    thisLearningTrial = LearningTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLearningTrial.rgb)
    if thisLearningTrial != None:
        for paramName in thisLearningTrial:
            exec('{} = thisLearningTrial[paramName]'.format(paramName))
    
    for thisLearningTrial in LearningTrials:
        currentLoop = LearningTrials
        # abbreviate parameter names if possible (e.g. rgb = thisLearningTrial.rgb)
        if thisLearningTrial != None:
            for paramName in thisLearningTrial:
                exec('{} = thisLearningTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixation_cross"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        key = key_resp.keys
        response = 'invalid'
        
        if key == 'd':
            response = TestImage1Type
        elif key == 'f':
            response = TestImage2Type
        elif key == 'j':
            response = TestImage3Type
        elif key == 'k':
            response = TestImage4Type
        
        print(response)
        thisExp.addData('test_resp', response)
        if response == 'target':
            target += 1
        if response == 'lure':
            lure += 1
        if response == 'dist1':
            dist1 += 1
        if response == 'dist2':
            dist2 += 1
        
        
        
        # keep track of which components have finished
        fixation_crossComponents = [fx_cross]
        for thisComponent in fixation_crossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixation_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation_cross"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixation_crossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixation_crossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fx_cross* updates
            if fx_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fx_cross.frameNStart = frameN  # exact frame index
                fx_cross.tStart = t  # local t and not account for scr refresh
                fx_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fx_cross, 'tStartRefresh')  # time at next scr refresh
                fx_cross.setAutoDraw(True)
            if fx_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fx_cross.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fx_cross.tStop = t  # not accounting for scr refresh
                    fx_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fx_cross, 'tStopRefresh')  # time at next scr refresh
                    fx_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation_cross"-------
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LearningTrials.addData('fx_cross.started', fx_cross.tStartRefresh)
        LearningTrials.addData('fx_cross.stopped', fx_cross.tStopRefresh)
        
        # ------Prepare to start Routine "test_trial"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        plate_updating.setImage(StreetSign)
        city_text_updating.setText(CityName)
        street_text_updating.setText(Cue)
        test_image1.setImage(TestImage1)
        test_image2.setImage(TestImage2)
        test_image3.setImage(TestImage3)
        test_image4.setImage(TestImage4)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        test_trialComponents = [plate_updating, city_text_updating, street_text_updating, test_image1, test_image2, test_image3, test_image4, button_d, button_f, button_j, button_k, key_resp]
        for thisComponent in test_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        test_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "test_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = test_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=test_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *plate_updating* updates
            if plate_updating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                plate_updating.frameNStart = frameN  # exact frame index
                plate_updating.tStart = t  # local t and not account for scr refresh
                plate_updating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(plate_updating, 'tStartRefresh')  # time at next scr refresh
                plate_updating.setAutoDraw(True)
            if plate_updating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > plate_updating.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    plate_updating.tStop = t  # not accounting for scr refresh
                    plate_updating.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(plate_updating, 'tStopRefresh')  # time at next scr refresh
                    plate_updating.setAutoDraw(False)
            
            # *city_text_updating* updates
            if city_text_updating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                city_text_updating.frameNStart = frameN  # exact frame index
                city_text_updating.tStart = t  # local t and not account for scr refresh
                city_text_updating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(city_text_updating, 'tStartRefresh')  # time at next scr refresh
                city_text_updating.setAutoDraw(True)
            if city_text_updating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > city_text_updating.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    city_text_updating.tStop = t  # not accounting for scr refresh
                    city_text_updating.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(city_text_updating, 'tStopRefresh')  # time at next scr refresh
                    city_text_updating.setAutoDraw(False)
            
            # *street_text_updating* updates
            if street_text_updating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                street_text_updating.frameNStart = frameN  # exact frame index
                street_text_updating.tStart = t  # local t and not account for scr refresh
                street_text_updating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(street_text_updating, 'tStartRefresh')  # time at next scr refresh
                street_text_updating.setAutoDraw(True)
            if street_text_updating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > street_text_updating.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    street_text_updating.tStop = t  # not accounting for scr refresh
                    street_text_updating.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(street_text_updating, 'tStopRefresh')  # time at next scr refresh
                    street_text_updating.setAutoDraw(False)
            
            # *test_image1* updates
            if test_image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_image1.frameNStart = frameN  # exact frame index
                test_image1.tStart = t  # local t and not account for scr refresh
                test_image1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_image1, 'tStartRefresh')  # time at next scr refresh
                test_image1.setAutoDraw(True)
            if test_image1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_image1.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    test_image1.tStop = t  # not accounting for scr refresh
                    test_image1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(test_image1, 'tStopRefresh')  # time at next scr refresh
                    test_image1.setAutoDraw(False)
            
            # *test_image2* updates
            if test_image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_image2.frameNStart = frameN  # exact frame index
                test_image2.tStart = t  # local t and not account for scr refresh
                test_image2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_image2, 'tStartRefresh')  # time at next scr refresh
                test_image2.setAutoDraw(True)
            if test_image2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_image2.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    test_image2.tStop = t  # not accounting for scr refresh
                    test_image2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(test_image2, 'tStopRefresh')  # time at next scr refresh
                    test_image2.setAutoDraw(False)
            
            # *test_image3* updates
            if test_image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_image3.frameNStart = frameN  # exact frame index
                test_image3.tStart = t  # local t and not account for scr refresh
                test_image3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_image3, 'tStartRefresh')  # time at next scr refresh
                test_image3.setAutoDraw(True)
            if test_image3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_image3.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    test_image3.tStop = t  # not accounting for scr refresh
                    test_image3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(test_image3, 'tStopRefresh')  # time at next scr refresh
                    test_image3.setAutoDraw(False)
            
            # *test_image4* updates
            if test_image4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_image4.frameNStart = frameN  # exact frame index
                test_image4.tStart = t  # local t and not account for scr refresh
                test_image4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_image4, 'tStartRefresh')  # time at next scr refresh
                test_image4.setAutoDraw(True)
            if test_image4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_image4.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    test_image4.tStop = t  # not accounting for scr refresh
                    test_image4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(test_image4, 'tStopRefresh')  # time at next scr refresh
                    test_image4.setAutoDraw(False)
            
            # *button_d* updates
            if button_d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                button_d.frameNStart = frameN  # exact frame index
                button_d.tStart = t  # local t and not account for scr refresh
                button_d.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_d, 'tStartRefresh')  # time at next scr refresh
                button_d.setAutoDraw(True)
            if button_d.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_d.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    button_d.tStop = t  # not accounting for scr refresh
                    button_d.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(button_d, 'tStopRefresh')  # time at next scr refresh
                    button_d.setAutoDraw(False)
            
            # *button_f* updates
            if button_f.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                button_f.frameNStart = frameN  # exact frame index
                button_f.tStart = t  # local t and not account for scr refresh
                button_f.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_f, 'tStartRefresh')  # time at next scr refresh
                button_f.setAutoDraw(True)
            if button_f.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_f.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    button_f.tStop = t  # not accounting for scr refresh
                    button_f.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(button_f, 'tStopRefresh')  # time at next scr refresh
                    button_f.setAutoDraw(False)
            
            # *button_j* updates
            if button_j.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                button_j.frameNStart = frameN  # exact frame index
                button_j.tStart = t  # local t and not account for scr refresh
                button_j.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_j, 'tStartRefresh')  # time at next scr refresh
                button_j.setAutoDraw(True)
            if button_j.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_j.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    button_j.tStop = t  # not accounting for scr refresh
                    button_j.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(button_j, 'tStopRefresh')  # time at next scr refresh
                    button_j.setAutoDraw(False)
            
            # *button_k* updates
            if button_k.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                button_k.frameNStart = frameN  # exact frame index
                button_k.tStart = t  # local t and not account for scr refresh
                button_k.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_k, 'tStartRefresh')  # time at next scr refresh
                button_k.setAutoDraw(True)
            if button_k.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_k.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    button_k.tStop = t  # not accounting for scr refresh
                    button_k.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(button_k, 'tStopRefresh')  # time at next scr refresh
                    button_k.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['d', 'f', 'j', 'k'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "test_trial"-------
        for thisComponent in test_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LearningTrials.addData('plate_updating.started', plate_updating.tStartRefresh)
        LearningTrials.addData('plate_updating.stopped', plate_updating.tStopRefresh)
        LearningTrials.addData('city_text_updating.started', city_text_updating.tStartRefresh)
        LearningTrials.addData('city_text_updating.stopped', city_text_updating.tStopRefresh)
        LearningTrials.addData('street_text_updating.started', street_text_updating.tStartRefresh)
        LearningTrials.addData('street_text_updating.stopped', street_text_updating.tStopRefresh)
        LearningTrials.addData('test_image1.started', test_image1.tStartRefresh)
        LearningTrials.addData('test_image1.stopped', test_image1.tStopRefresh)
        LearningTrials.addData('test_image2.started', test_image2.tStartRefresh)
        LearningTrials.addData('test_image2.stopped', test_image2.tStopRefresh)
        LearningTrials.addData('test_image3.started', test_image3.tStartRefresh)
        LearningTrials.addData('test_image3.stopped', test_image3.tStopRefresh)
        LearningTrials.addData('test_image4.started', test_image4.tStartRefresh)
        LearningTrials.addData('test_image4.stopped', test_image4.tStopRefresh)
        LearningTrials.addData('button_d.started', button_d.tStartRefresh)
        LearningTrials.addData('button_d.stopped', button_d.tStopRefresh)
        LearningTrials.addData('button_f.started', button_f.tStartRefresh)
        LearningTrials.addData('button_f.stopped', button_f.tStopRefresh)
        LearningTrials.addData('button_j.started', button_j.tStartRefresh)
        LearningTrials.addData('button_j.stopped', button_j.tStopRefresh)
        LearningTrials.addData('button_k.started', button_k.tStartRefresh)
        LearningTrials.addData('button_k.stopped', button_k.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        LearningTrials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            LearningTrials.addData('key_resp.rt', key_resp.rt)
        LearningTrials.addData('key_resp.started', key_resp.tStartRefresh)
        LearningTrials.addData('key_resp.stopped', key_resp.tStopRefresh)
        
        # ------Prepare to start Routine "short_break"-------
        continueRoutine = True
        # update component parameters for each repeat
        short_break_key.keys = []
        short_break_key.rt = []
        _short_break_key_allKeys = []
        trial_count += 1
        
        if trial_count < 40:
            continueRoutine = False
        else:
            trial_count = 0
            
        # keep track of which components have finished
        short_breakComponents = [short_break_text, short_break_key]
        for thisComponent in short_breakComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        short_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "short_break"-------
        while continueRoutine:
            # get current time
            t = short_breakClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=short_breakClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *short_break_text* updates
            if short_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                short_break_text.frameNStart = frameN  # exact frame index
                short_break_text.tStart = t  # local t and not account for scr refresh
                short_break_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(short_break_text, 'tStartRefresh')  # time at next scr refresh
                short_break_text.setAutoDraw(True)
            
            # *short_break_key* updates
            waitOnFlip = False
            if short_break_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                short_break_key.frameNStart = frameN  # exact frame index
                short_break_key.tStart = t  # local t and not account for scr refresh
                short_break_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(short_break_key, 'tStartRefresh')  # time at next scr refresh
                short_break_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(short_break_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(short_break_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if short_break_key.status == STARTED and not waitOnFlip:
                theseKeys = short_break_key.getKeys(keyList=['space'], waitRelease=False)
                _short_break_key_allKeys.extend(theseKeys)
                if len(_short_break_key_allKeys):
                    short_break_key.keys = _short_break_key_allKeys[-1].name  # just the last key pressed
                    short_break_key.rt = _short_break_key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in short_breakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "short_break"-------
        for thisComponent in short_breakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LearningTrials.addData('short_break_text.started', short_break_text.tStartRefresh)
        LearningTrials.addData('short_break_text.stopped', short_break_text.tStopRefresh)
        # check responses
        if short_break_key.keys in ['', [], None]:  # No response was made
            short_break_key.keys = None
        LearningTrials.addData('short_break_key.keys',short_break_key.keys)
        if short_break_key.keys != None:  # we had a response
            LearningTrials.addData('short_break_key.rt', short_break_key.rt)
        LearningTrials.addData('short_break_key.started', short_break_key.tStartRefresh)
        LearningTrials.addData('short_break_key.stopped', short_break_key.tStopRefresh)
        # the Routine "short_break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'LearningTrials'
    
    
    # ------Prepare to start Routine "take_a_break"-------
    continueRoutine = True
    # update component parameters for each repeat
    break_key_resp.keys = []
    break_key_resp.rt = []
    _break_key_resp_allKeys = []
    thisExp.addData('n_targets', target)
    thisExp.addData('n_lures', lure)
    thisExp.addData('n_dist1s', dist1)
    thisExp.addData('n_dist2s', dist2)
    if repetitions >= 2:
        continueRoutine = False
    # keep track of which components have finished
    take_a_breakComponents = [break_text, break_key_resp]
    for thisComponent in take_a_breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    take_a_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "take_a_break"-------
    while continueRoutine:
        # get current time
        t = take_a_breakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=take_a_breakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text* updates
        if break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_text.frameNStart = frameN  # exact frame index
            break_text.tStart = t  # local t and not account for scr refresh
            break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
            break_text.setAutoDraw(True)
        
        # *break_key_resp* updates
        waitOnFlip = False
        if break_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_key_resp.frameNStart = frameN  # exact frame index
            break_key_resp.tStart = t  # local t and not account for scr refresh
            break_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_key_resp, 'tStartRefresh')  # time at next scr refresh
            break_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(break_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(break_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if break_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = break_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _break_key_resp_allKeys.extend(theseKeys)
            if len(_break_key_resp_allKeys):
                break_key_resp.keys = _break_key_resp_allKeys[-1].name  # just the last key pressed
                break_key_resp.rt = _break_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in take_a_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "take_a_break"-------
    for thisComponent in take_a_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    CityBlock.addData('break_text.started', break_text.tStartRefresh)
    CityBlock.addData('break_text.stopped', break_text.tStopRefresh)
    # check responses
    if break_key_resp.keys in ['', [], None]:  # No response was made
        break_key_resp.keys = None
    CityBlock.addData('break_key_resp.keys',break_key_resp.keys)
    if break_key_resp.keys != None:  # we had a response
        CityBlock.addData('break_key_resp.rt', break_key_resp.rt)
    CityBlock.addData('break_key_resp.started', break_key_resp.tStartRefresh)
    CityBlock.addData('break_key_resp.stopped', break_key_resp.tStopRefresh)
    # the Routine "take_a_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'CityBlock'


# ------Prepare to start Routine "end_task"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
end_taskComponents = [end_text]
for thisComponent in end_taskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_task"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_taskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_taskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_text, 'tStopRefresh')  # time at next scr refresh
            end_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_task"-------
for thisComponent in end_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

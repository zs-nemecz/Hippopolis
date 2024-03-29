﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.2),
    on november 29, 2022, at 16:02
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.2'
expName = 'Hippopolis_Updating'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
# --- Show participant info dialog --
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
    originPath='D:\\Users\\USER\\Desktop\\Hippopolis\\TwoCities_UpdatingPhase_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=(1.0000, 1.0000, 1.0000), colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "setup" ---
# Run 'Begin Experiment' code from select_file
ID = expInfo['participant']
city_list = './stimuli/subj_files/' + ID + '_city_list.csv'
# Run 'Begin Experiment' code from block_counter
repetitions = 0

# --- Initialize components for Routine "update_instructions" ---
learning_instructions_text = visual.TextStim(win=win, name='learning_instructions_text',
    text='Eltelt három év, és Ön visszatér Hippopolisba és Camponelloba.\n\nHippopolis egy nagyváros, ezért gyorsan változik. Az utcák többségébe a korábban látottakhoz képest új képek kerültek. \nCamponello viszont egy kisváros, kevés a változás. Az utcák többségében ugyanazokat a képeket találja, mint régen.\n\nAz Ön feladata ismét az, hogy megjegyezze, melyik utcában milyen képet látott. \nA képernyő felső részén látja majd a város és az utca nevét, középen pedig a képet. Próbálja meg memorizálni az utcához tartozó képet!\n\nMiután végigjárta az utcákat, egy emlékezeti feladattal vizsgáljuk meg, mennyi utcára és képre emlékszik. \n\nA SZÓKÖZ lenyomásával elindul a feladat.',
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1400.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro_key = keyboard.Keyboard()

# --- Initialize components for Routine "city_name" ---
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
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -100), size=(750, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "fixation_cross" ---
fx_cross = visual.TextStim(win=win, name='fx_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "prediction_phase" ---
plate = visual.ImageStim(
    win=win,
    name='plate', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 350), size=(513, 215),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
city_text = visual.TextStim(win=win, name='city_text',
    text='',
    font='Open Sans',
    pos=(0, 400), height=36.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
street_text = visual.TextStim(win=win, name='street_text',
    text='',
    font='Open Sans',
    pos=(0, 320), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fx_cross_prediction = visual.TextStim(win=win, name='fx_cross_prediction',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "updating_phase" ---
plate_updating = visual.ImageStim(
    win=win,
    name='plate_updating', 
    image='sin', mask=None, anchor='center',
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
updating_image = visual.ImageStim(
    win=win,
    name='updating_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "short_break" ---
short_break_text = visual.TextStim(win=win, name='short_break_text',
    text='Rövid szünet.... Ugyanezzel a várossal folytatjuk.\n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
short_break_key = keyboard.Keyboard()

# --- Initialize components for Routine "take_a_break" ---
break_text = visual.TextStim(win=win, name='break_text',
    text='Szünet.... A szünet után a másik város következik.\n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "end_task" ---
end_text = visual.TextStim(win=win, name='end_text',
    text='Vége a feladat második részének.\nMost a teszt következik.\n\nTartson egy rövid szünetet!',
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1000.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "setup" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "setup" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setup" ---
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "update_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_key.keys = []
intro_key.rt = []
_intro_key_allKeys = []
# keep track of which components have finished
update_instructionsComponents = [learning_instructions_text, intro_key]
for thisComponent in update_instructionsComponents:
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

# --- Run Routine "update_instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learning_instructions_text.started')
        learning_instructions_text.setAutoDraw(True)
    
    # *intro_key* updates
    waitOnFlip = False
    if intro_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key.frameNStart = frameN  # exact frame index
        intro_key.tStart = t  # local t and not account for scr refresh
        intro_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_key.started')
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
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in update_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "update_instructions" ---
for thisComponent in update_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_key.keys in ['', [], None]:  # No response was made
    intro_key.keys = None
thisExp.addData('intro_key.keys',intro_key.keys)
if intro_key.keys != None:  # we had a response
    thisExp.addData('intro_key.rt', intro_key.rt)
thisExp.nextEntry()
# the Routine "update_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
CityBlock = data.TrialHandler(nReps=1.0, method='sequential', 
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
    
    # --- Prepare to start Routine "city_name" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    cityname_text.setText(CityName)
    city_image.setImage(CityImage)
    # Run 'Begin Routine' code from count_round
    repetitions += 1
    trial_count = 0
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
    frameN = -1
    
    # --- Run Routine "city_name" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cityname_text.started')
            cityname_text.setAutoDraw(True)
        if cityname_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cityname_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                cityname_text.tStop = t  # not accounting for scr refresh
                cityname_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cityname_text.stopped')
                cityname_text.setAutoDraw(False)
        
        # *city_image* updates
        if city_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            city_image.frameNStart = frameN  # exact frame index
            city_image.tStart = t  # local t and not account for scr refresh
            city_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(city_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'city_image.started')
            city_image.setAutoDraw(True)
        if city_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > city_image.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                city_image.tStop = t  # not accounting for scr refresh
                city_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'city_image.stopped')
                city_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in city_nameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "city_name" ---
    for thisComponent in city_nameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
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
        
        # --- Prepare to start Routine "fixation_cross" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
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
        frameN = -1
        
        # --- Run Routine "fixation_cross" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fx_cross.started')
                fx_cross.setAutoDraw(True)
            if fx_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fx_cross.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fx_cross.tStop = t  # not accounting for scr refresh
                    fx_cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fx_cross.stopped')
                    fx_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation_cross" ---
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "prediction_phase" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        plate.setImage(StreetSign)
        city_text.setText(CityName)
        street_text.setText(Cue)
        # keep track of which components have finished
        prediction_phaseComponents = [plate, city_text, street_text, fx_cross_prediction]
        for thisComponent in prediction_phaseComponents:
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
        
        # --- Run Routine "prediction_phase" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *plate* updates
            if plate.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                plate.frameNStart = frameN  # exact frame index
                plate.tStart = t  # local t and not account for scr refresh
                plate.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(plate, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'plate.started')
                plate.setAutoDraw(True)
            if plate.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > plate.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    plate.tStop = t  # not accounting for scr refresh
                    plate.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'plate.stopped')
                    plate.setAutoDraw(False)
            
            # *city_text* updates
            if city_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                city_text.frameNStart = frameN  # exact frame index
                city_text.tStart = t  # local t and not account for scr refresh
                city_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(city_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'city_text.started')
                city_text.setAutoDraw(True)
            if city_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > city_text.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    city_text.tStop = t  # not accounting for scr refresh
                    city_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'city_text.stopped')
                    city_text.setAutoDraw(False)
            
            # *street_text* updates
            if street_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                street_text.frameNStart = frameN  # exact frame index
                street_text.tStart = t  # local t and not account for scr refresh
                street_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(street_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'street_text.started')
                street_text.setAutoDraw(True)
            if street_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > street_text.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    street_text.tStop = t  # not accounting for scr refresh
                    street_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'street_text.stopped')
                    street_text.setAutoDraw(False)
            
            # *fx_cross_prediction* updates
            if fx_cross_prediction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fx_cross_prediction.frameNStart = frameN  # exact frame index
                fx_cross_prediction.tStart = t  # local t and not account for scr refresh
                fx_cross_prediction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fx_cross_prediction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fx_cross_prediction.started')
                fx_cross_prediction.setAutoDraw(True)
            if fx_cross_prediction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fx_cross_prediction.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fx_cross_prediction.tStop = t  # not accounting for scr refresh
                    fx_cross_prediction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fx_cross_prediction.stopped')
                    fx_cross_prediction.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prediction_phaseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prediction_phase" ---
        for thisComponent in prediction_phaseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        
        # --- Prepare to start Routine "updating_phase" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        plate_updating.setImage(StreetSign)
        city_text_updating.setText(CityName)
        street_text_updating.setText(Cue)
        updating_image.setImage(UpdateImage)
        # keep track of which components have finished
        updating_phaseComponents = [plate_updating, city_text_updating, street_text_updating, updating_image]
        for thisComponent in updating_phaseComponents:
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
        
        # --- Run Routine "updating_phase" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'plate_updating.started')
                plate_updating.setAutoDraw(True)
            if plate_updating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > plate_updating.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    plate_updating.tStop = t  # not accounting for scr refresh
                    plate_updating.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'plate_updating.stopped')
                    plate_updating.setAutoDraw(False)
            
            # *city_text_updating* updates
            if city_text_updating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                city_text_updating.frameNStart = frameN  # exact frame index
                city_text_updating.tStart = t  # local t and not account for scr refresh
                city_text_updating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(city_text_updating, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'city_text_updating.started')
                city_text_updating.setAutoDraw(True)
            if city_text_updating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > city_text_updating.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    city_text_updating.tStop = t  # not accounting for scr refresh
                    city_text_updating.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'city_text_updating.stopped')
                    city_text_updating.setAutoDraw(False)
            
            # *street_text_updating* updates
            if street_text_updating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                street_text_updating.frameNStart = frameN  # exact frame index
                street_text_updating.tStart = t  # local t and not account for scr refresh
                street_text_updating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(street_text_updating, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'street_text_updating.started')
                street_text_updating.setAutoDraw(True)
            if street_text_updating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > street_text_updating.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    street_text_updating.tStop = t  # not accounting for scr refresh
                    street_text_updating.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'street_text_updating.stopped')
                    street_text_updating.setAutoDraw(False)
            
            # *updating_image* updates
            if updating_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                updating_image.frameNStart = frameN  # exact frame index
                updating_image.tStart = t  # local t and not account for scr refresh
                updating_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(updating_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'updating_image.started')
                updating_image.setAutoDraw(True)
            if updating_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > updating_image.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    updating_image.tStop = t  # not accounting for scr refresh
                    updating_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'updating_image.stopped')
                    updating_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in updating_phaseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "updating_phase" ---
        for thisComponent in updating_phaseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "short_break" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        short_break_key.keys = []
        short_break_key.rt = []
        _short_break_key_allKeys = []
        # Run 'Begin Routine' code from need_a_break
        trial_count += 1
        
        if trial_count < 45:
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
        frameN = -1
        
        # --- Run Routine "short_break" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'short_break_text.started')
                short_break_text.setAutoDraw(True)
            
            # *short_break_key* updates
            waitOnFlip = False
            if short_break_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                short_break_key.frameNStart = frameN  # exact frame index
                short_break_key.tStart = t  # local t and not account for scr refresh
                short_break_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(short_break_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'short_break_key.started')
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
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in short_breakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "short_break" ---
        for thisComponent in short_breakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if short_break_key.keys in ['', [], None]:  # No response was made
            short_break_key.keys = None
        LearningTrials.addData('short_break_key.keys',short_break_key.keys)
        if short_break_key.keys != None:  # we had a response
            LearningTrials.addData('short_break_key.rt', short_break_key.rt)
        # the Routine "short_break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'LearningTrials'
    
    
    # --- Prepare to start Routine "take_a_break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    break_key_resp.keys = []
    break_key_resp.rt = []
    _break_key_resp_allKeys = []
    # Run 'Begin Routine' code from skip_if_task_ends
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
    frameN = -1
    
    # --- Run Routine "take_a_break" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'break_text.started')
            break_text.setAutoDraw(True)
        
        # *break_key_resp* updates
        waitOnFlip = False
        if break_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_key_resp.frameNStart = frameN  # exact frame index
            break_key_resp.tStart = t  # local t and not account for scr refresh
            break_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'break_key_resp.started')
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in take_a_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "take_a_break" ---
    for thisComponent in take_a_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if break_key_resp.keys in ['', [], None]:  # No response was made
        break_key_resp.keys = None
    CityBlock.addData('break_key_resp.keys',break_key_resp.keys)
    if break_key_resp.keys != None:  # we had a response
        CityBlock.addData('break_key_resp.rt', break_key_resp.rt)
    # the Routine "take_a_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'CityBlock'


# --- Prepare to start Routine "end_task" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "end_task" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_text.started')
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_text.stopped')
            end_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_task" ---
for thisComponent in end_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on június 13, 2022, at 21:42
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
expName = 'Hippopolis_Updating'  # from the Builder filename that created this script
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
    originPath='D:\\Users\\USER\\Desktop\\Hippopolis\\TwoCities_UpdatingPhase_lastrun.py',
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

# Initialize components for Routine "prediction_phase"
prediction_phaseClock = core.Clock()
plate = visual.ImageStim(
    win=win,
    name='plate', 
    image='sin', mask=None,
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

# Initialize components for Routine "updating_phase"
updating_phaseClock = core.Clock()
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
updating_image = visual.ImageStim(
    win=win,
    name='updating_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "fixation_cross"
fixation_crossClock = core.Clock()
fx_cross = visual.TextStim(win=win, name='fx_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "take_a_break"
take_a_breakClock = core.Clock()
break_text = visual.TextStim(win=win, name='break_text',
    text='Szünet....\n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break_key_resp = keyboard.Keyboard()

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
    
    # ------Prepare to start Routine "city_name"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    cityname_text.setText(CityName)
    city_image.setImage(CityImage)
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
        
        # ------Prepare to start Routine "prediction_phase"-------
        continueRoutine = True
        routineTimer.add(3.000000)
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
        prediction_phaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prediction_phase"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = prediction_phaseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=prediction_phaseClock)
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
                plate.setAutoDraw(True)
            if plate.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > plate.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    plate.tStop = t  # not accounting for scr refresh
                    plate.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(plate, 'tStopRefresh')  # time at next scr refresh
                    plate.setAutoDraw(False)
            
            # *city_text* updates
            if city_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                city_text.frameNStart = frameN  # exact frame index
                city_text.tStart = t  # local t and not account for scr refresh
                city_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(city_text, 'tStartRefresh')  # time at next scr refresh
                city_text.setAutoDraw(True)
            if city_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > city_text.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    city_text.tStop = t  # not accounting for scr refresh
                    city_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(city_text, 'tStopRefresh')  # time at next scr refresh
                    city_text.setAutoDraw(False)
            
            # *street_text* updates
            if street_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                street_text.frameNStart = frameN  # exact frame index
                street_text.tStart = t  # local t and not account for scr refresh
                street_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(street_text, 'tStartRefresh')  # time at next scr refresh
                street_text.setAutoDraw(True)
            if street_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > street_text.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    street_text.tStop = t  # not accounting for scr refresh
                    street_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(street_text, 'tStopRefresh')  # time at next scr refresh
                    street_text.setAutoDraw(False)
            
            # *fx_cross_prediction* updates
            if fx_cross_prediction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fx_cross_prediction.frameNStart = frameN  # exact frame index
                fx_cross_prediction.tStart = t  # local t and not account for scr refresh
                fx_cross_prediction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fx_cross_prediction, 'tStartRefresh')  # time at next scr refresh
                fx_cross_prediction.setAutoDraw(True)
            if fx_cross_prediction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fx_cross_prediction.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fx_cross_prediction.tStop = t  # not accounting for scr refresh
                    fx_cross_prediction.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fx_cross_prediction, 'tStopRefresh')  # time at next scr refresh
                    fx_cross_prediction.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prediction_phaseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prediction_phase"-------
        for thisComponent in prediction_phaseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LearningTrials.addData('plate.started', plate.tStartRefresh)
        LearningTrials.addData('plate.stopped', plate.tStopRefresh)
        LearningTrials.addData('city_text.started', city_text.tStartRefresh)
        LearningTrials.addData('city_text.stopped', city_text.tStopRefresh)
        LearningTrials.addData('street_text.started', street_text.tStartRefresh)
        LearningTrials.addData('street_text.stopped', street_text.tStopRefresh)
        LearningTrials.addData('fx_cross_prediction.started', fx_cross_prediction.tStartRefresh)
        LearningTrials.addData('fx_cross_prediction.stopped', fx_cross_prediction.tStopRefresh)
        
        # ------Prepare to start Routine "updating_phase"-------
        continueRoutine = True
        routineTimer.add(3.000000)
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
        updating_phaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "updating_phase"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = updating_phaseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=updating_phaseClock)
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
                if tThisFlipGlobal > plate_updating.tStartRefresh + 3.0-frameTolerance:
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
                if tThisFlipGlobal > city_text_updating.tStartRefresh + 3.0-frameTolerance:
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
                if tThisFlipGlobal > street_text_updating.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    street_text_updating.tStop = t  # not accounting for scr refresh
                    street_text_updating.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(street_text_updating, 'tStopRefresh')  # time at next scr refresh
                    street_text_updating.setAutoDraw(False)
            
            # *updating_image* updates
            if updating_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                updating_image.frameNStart = frameN  # exact frame index
                updating_image.tStart = t  # local t and not account for scr refresh
                updating_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(updating_image, 'tStartRefresh')  # time at next scr refresh
                updating_image.setAutoDraw(True)
            if updating_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > updating_image.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    updating_image.tStop = t  # not accounting for scr refresh
                    updating_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(updating_image, 'tStopRefresh')  # time at next scr refresh
                    updating_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in updating_phaseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "updating_phase"-------
        for thisComponent in updating_phaseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LearningTrials.addData('plate_updating.started', plate_updating.tStartRefresh)
        LearningTrials.addData('plate_updating.stopped', plate_updating.tStopRefresh)
        LearningTrials.addData('city_text_updating.started', city_text_updating.tStartRefresh)
        LearningTrials.addData('city_text_updating.stopped', city_text_updating.tStopRefresh)
        LearningTrials.addData('street_text_updating.started', street_text_updating.tStartRefresh)
        LearningTrials.addData('street_text_updating.stopped', street_text_updating.tStopRefresh)
        LearningTrials.addData('updating_image.started', updating_image.tStartRefresh)
        LearningTrials.addData('updating_image.stopped', updating_image.tStopRefresh)
        
        # ------Prepare to start Routine "fixation_cross"-------
        continueRoutine = True
        routineTimer.add(1.000000)
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
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'LearningTrials'
    
    
    # ------Prepare to start Routine "take_a_break"-------
    continueRoutine = True
    # update component parameters for each repeat
    break_key_resp.keys = []
    break_key_resp.rt = []
    _break_key_resp_allKeys = []
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

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on October 04, 2022, at 13:57
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
psychopyVersion = '2021.1.4'
expName = 'Hippopolis_Learning'  # from the Builder filename that created this script
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
    originPath='D:\\Zsuzsa\\HCCCL\\Hippopolis\\TwoCities_LearningPhase_lastrun.py',
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

# Initialize components for Routine "learning_instructions"
learning_instructionsClock = core.Clock()
learning_instructions_text = visual.TextStim(win=win, name='learning_instructions_text',
    text='A következőkben két várost fog megismerni. \nA városok neve Hippopolis és Camponello. \n\nA két város utcáiban képeket fog találni. Ezek egyesével lesznek bemutatva.\n\nAz Ön feladata, hogy megjegyezze, melyik utcában milyen képet látott. \nA képernyő felső részén látja majd a város és az utca nevét, középen pedig a képet. Próbálja meg memorizálni az utcához tartozó képet!\n\nMiután végigjárta az utcákat, egy emlékezeti feladattal vizsgáljuk meg, mennyi utcára és képre emlékszik. \n\nA SZÓKÖZ lenyomásával elindul a feladat.',
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

# Initialize components for Routine "fixation_cross"
fixation_crossClock = core.Clock()
fx_cross = visual.TextStim(win=win, name='fx_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learning_trial"
learning_trialClock = core.Clock()
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
learning_image = visual.ImageStim(
    win=win,
    name='learning_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

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

# Initialize components for Routine "test_intro"
test_introClock = core.Clock()
test_text = visual.TextStim(win=win, name='test_text',
    text='A teszt következik.\n\nA folytatáshoz nyomja le a SZÓKÖZ gombot.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "test_trial"
test_trialClock = core.Clock()
plate_test = visual.ImageStim(
    win=win,
    name='plate_test', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 350), size=(513, 215),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
city_text_test = visual.TextStim(win=win, name='city_text_test',
    text='',
    font='Open Sans',
    pos=(0, 400), height=36.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
street_text_test = visual.TextStim(win=win, name='street_text_test',
    text='',
    font='Open Sans',
    pos=(0, 320), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
test_question = visual.TextStim(win=win, name='test_question',
    text='Fel tudja idézni a képet?',
    font='Open Sans',
    pos=(0,0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
test_key_resp = keyboard.Keyboard()
button_image = visual.ImageStim(
    win=win,
    name='button_image', 
    image='stimuli\\\\buttons.png', mask=None,
    ori=0.0, pos=(0, -200), size=(660, 312),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# Initialize components for Routine "verbal_test"
verbal_testClock = core.Clock()
import random as rnd
recall = 0
plate_verbal = visual.ImageStim(
    win=win,
    name='plate_verbal', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 350), size=(513, 215),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
street_text_verbal = visual.TextStim(win=win, name='street_text_verbal',
    text='',
    font='Open Sans',
    pos=(0, 320), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
city_text_verbal = visual.TextStim(win=win, name='city_text_verbal',
    text='',
    font='Open Sans',
    pos=(0, 400), height=36.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
question_verbal = visual.TextStim(win=win, name='question_verbal',
    text='Írja körül, mit látott a képen.\n\nA folytatáshoz nyomja le a SZÓKÖZ gombot.',
    font='Open Sans',
    pos=(0,0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
verbal_test_key_resp = keyboard.Keyboard()

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
    text='Szünet....\n\nA szünet után a másik város következik. \n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break_key_resp = keyboard.Keyboard()

# Initialize components for Routine "end_task"
end_taskClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Vége a feladat első részének.\n\nTartson egy rövid szünetet!',
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

# ------Prepare to start Routine "learning_instructions"-------
continueRoutine = True
# update component parameters for each repeat
intro_key.keys = []
intro_key.rt = []
_intro_key_allKeys = []
# keep track of which components have finished
learning_instructionsComponents = [learning_instructions_text, intro_key]
for thisComponent in learning_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learning_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_instructions"-------
while continueRoutine:
    # get current time
    t = learning_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_instructionsClock)
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
    for thisComponent in learning_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_instructions"-------
for thisComponent in learning_instructionsComponents:
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
# the Routine "learning_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
CityBlock = data.TrialHandler(nReps=2.0, method='sequential', 
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
        
        # ------Prepare to start Routine "learning_trial"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        plate.setImage(StreetSign)
        city_text.setText(CityName)
        street_text.setText(Cue)
        learning_image.setImage(Image)
        # keep track of which components have finished
        learning_trialComponents = [plate, city_text, street_text, learning_image]
        for thisComponent in learning_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        learning_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learning_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_trialClock)
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
            
            # *learning_image* updates
            if learning_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learning_image.frameNStart = frameN  # exact frame index
                learning_image.tStart = t  # local t and not account for scr refresh
                learning_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learning_image, 'tStartRefresh')  # time at next scr refresh
                learning_image.setAutoDraw(True)
            if learning_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learning_image.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    learning_image.tStop = t  # not accounting for scr refresh
                    learning_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learning_image, 'tStopRefresh')  # time at next scr refresh
                    learning_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_trial"-------
        for thisComponent in learning_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LearningTrials.addData('plate.started', plate.tStartRefresh)
        LearningTrials.addData('plate.stopped', plate.tStopRefresh)
        LearningTrials.addData('city_text.started', city_text.tStartRefresh)
        LearningTrials.addData('city_text.stopped', city_text.tStopRefresh)
        LearningTrials.addData('street_text.started', street_text.tStartRefresh)
        LearningTrials.addData('street_text.stopped', street_text.tStopRefresh)
        LearningTrials.addData('learning_image.started', learning_image.tStartRefresh)
        LearningTrials.addData('learning_image.stopped', learning_image.tStopRefresh)
        
        # ------Prepare to start Routine "short_break"-------
        continueRoutine = True
        # update component parameters for each repeat
        short_break_key.keys = []
        short_break_key.rt = []
        _short_break_key_allKeys = []
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
    
    
    # ------Prepare to start Routine "test_intro"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    test_introComponents = [test_text, key_resp]
    for thisComponent in test_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test_intro"-------
    while continueRoutine:
        # get current time
        t = test_introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test_introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test_text* updates
        if test_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_text.frameNStart = frameN  # exact frame index
            test_text.tStart = t  # local t and not account for scr refresh
            test_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_text, 'tStartRefresh')  # time at next scr refresh
            test_text.setAutoDraw(True)
        
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
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
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
        for thisComponent in test_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test_intro"-------
    for thisComponent in test_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    CityBlock.addData('test_text.started', test_text.tStartRefresh)
    CityBlock.addData('test_text.stopped', test_text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    CityBlock.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        CityBlock.addData('key_resp.rt', key_resp.rt)
    CityBlock.addData('key_resp.started', key_resp.tStartRefresh)
    CityBlock.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "test_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(StimuliFile),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "test_trial"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        plate_test.setImage(StreetSign)
        city_text_test.setText(CityName)
        street_text_test.setText(Cue)
        test_key_resp.keys = []
        test_key_resp.rt = []
        _test_key_resp_allKeys = []
        # keep track of which components have finished
        test_trialComponents = [plate_test, city_text_test, street_text_test, test_question, test_key_resp, button_image]
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
            
            # *plate_test* updates
            if plate_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                plate_test.frameNStart = frameN  # exact frame index
                plate_test.tStart = t  # local t and not account for scr refresh
                plate_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(plate_test, 'tStartRefresh')  # time at next scr refresh
                plate_test.setAutoDraw(True)
            if plate_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > plate_test.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    plate_test.tStop = t  # not accounting for scr refresh
                    plate_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(plate_test, 'tStopRefresh')  # time at next scr refresh
                    plate_test.setAutoDraw(False)
            
            # *city_text_test* updates
            if city_text_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                city_text_test.frameNStart = frameN  # exact frame index
                city_text_test.tStart = t  # local t and not account for scr refresh
                city_text_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(city_text_test, 'tStartRefresh')  # time at next scr refresh
                city_text_test.setAutoDraw(True)
            if city_text_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > city_text_test.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    city_text_test.tStop = t  # not accounting for scr refresh
                    city_text_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(city_text_test, 'tStopRefresh')  # time at next scr refresh
                    city_text_test.setAutoDraw(False)
            
            # *street_text_test* updates
            if street_text_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                street_text_test.frameNStart = frameN  # exact frame index
                street_text_test.tStart = t  # local t and not account for scr refresh
                street_text_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(street_text_test, 'tStartRefresh')  # time at next scr refresh
                street_text_test.setAutoDraw(True)
            if street_text_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > street_text_test.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    street_text_test.tStop = t  # not accounting for scr refresh
                    street_text_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(street_text_test, 'tStopRefresh')  # time at next scr refresh
                    street_text_test.setAutoDraw(False)
            
            # *test_question* updates
            if test_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_question.frameNStart = frameN  # exact frame index
                test_question.tStart = t  # local t and not account for scr refresh
                test_question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_question, 'tStartRefresh')  # time at next scr refresh
                test_question.setAutoDraw(True)
            if test_question.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_question.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    test_question.tStop = t  # not accounting for scr refresh
                    test_question.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(test_question, 'tStopRefresh')  # time at next scr refresh
                    test_question.setAutoDraw(False)
            
            # *test_key_resp* updates
            waitOnFlip = False
            if test_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_key_resp.frameNStart = frameN  # exact frame index
                test_key_resp.tStart = t  # local t and not account for scr refresh
                test_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_key_resp, 'tStartRefresh')  # time at next scr refresh
                test_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(test_key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(test_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if test_key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_key_resp.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    test_key_resp.tStop = t  # not accounting for scr refresh
                    test_key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(test_key_resp, 'tStopRefresh')  # time at next scr refresh
                    test_key_resp.status = FINISHED
            if test_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = test_key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _test_key_resp_allKeys.extend(theseKeys)
                if len(_test_key_resp_allKeys):
                    test_key_resp.keys = _test_key_resp_allKeys[-1].name  # just the last key pressed
                    test_key_resp.rt = _test_key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *button_image* updates
            if button_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                button_image.frameNStart = frameN  # exact frame index
                button_image.tStart = t  # local t and not account for scr refresh
                button_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_image, 'tStartRefresh')  # time at next scr refresh
                button_image.setAutoDraw(True)
            if button_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_image.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    button_image.tStop = t  # not accounting for scr refresh
                    button_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(button_image, 'tStopRefresh')  # time at next scr refresh
                    button_image.setAutoDraw(False)
            
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
        trials.addData('plate_test.started', plate_test.tStartRefresh)
        trials.addData('plate_test.stopped', plate_test.tStopRefresh)
        trials.addData('city_text_test.started', city_text_test.tStartRefresh)
        trials.addData('city_text_test.stopped', city_text_test.tStopRefresh)
        trials.addData('street_text_test.started', street_text_test.tStartRefresh)
        trials.addData('street_text_test.stopped', street_text_test.tStopRefresh)
        trials.addData('test_question.started', test_question.tStartRefresh)
        trials.addData('test_question.stopped', test_question.tStopRefresh)
        # check responses
        if test_key_resp.keys in ['', [], None]:  # No response was made
            test_key_resp.keys = None
        trials.addData('test_key_resp.keys',test_key_resp.keys)
        if test_key_resp.keys != None:  # we had a response
            trials.addData('test_key_resp.rt', test_key_resp.rt)
        trials.addData('test_key_resp.started', test_key_resp.tStartRefresh)
        trials.addData('test_key_resp.stopped', test_key_resp.tStopRefresh)
        trials.addData('button_image.started', button_image.tStartRefresh)
        trials.addData('button_image.stopped', button_image.tStopRefresh)
        
        # ------Prepare to start Routine "verbal_test"-------
        continueRoutine = True
        # update component parameters for each repeat
        if test_key_resp.keys=='right':
            recall += 1
            print('Remembered trial.')
            dice = rnd.randint(1,100)
            print(dice)
            if dice < 90:
                continueRoutine = False
        else:
            print('Not remembered trial.')
            continueRoutine = False
        plate_verbal.setImage(StreetSign)
        street_text_verbal.setText(Cue)
        city_text_verbal.setText(CityName)
        verbal_test_key_resp.keys = []
        verbal_test_key_resp.rt = []
        _verbal_test_key_resp_allKeys = []
        # keep track of which components have finished
        verbal_testComponents = [plate_verbal, street_text_verbal, city_text_verbal, question_verbal, verbal_test_key_resp]
        for thisComponent in verbal_testComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        verbal_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "verbal_test"-------
        while continueRoutine:
            # get current time
            t = verbal_testClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=verbal_testClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *plate_verbal* updates
            if plate_verbal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                plate_verbal.frameNStart = frameN  # exact frame index
                plate_verbal.tStart = t  # local t and not account for scr refresh
                plate_verbal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(plate_verbal, 'tStartRefresh')  # time at next scr refresh
                plate_verbal.setAutoDraw(True)
            
            # *street_text_verbal* updates
            if street_text_verbal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                street_text_verbal.frameNStart = frameN  # exact frame index
                street_text_verbal.tStart = t  # local t and not account for scr refresh
                street_text_verbal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(street_text_verbal, 'tStartRefresh')  # time at next scr refresh
                street_text_verbal.setAutoDraw(True)
            
            # *city_text_verbal* updates
            if city_text_verbal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                city_text_verbal.frameNStart = frameN  # exact frame index
                city_text_verbal.tStart = t  # local t and not account for scr refresh
                city_text_verbal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(city_text_verbal, 'tStartRefresh')  # time at next scr refresh
                city_text_verbal.setAutoDraw(True)
            
            # *question_verbal* updates
            if question_verbal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_verbal.frameNStart = frameN  # exact frame index
                question_verbal.tStart = t  # local t and not account for scr refresh
                question_verbal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_verbal, 'tStartRefresh')  # time at next scr refresh
                question_verbal.setAutoDraw(True)
            
            # *verbal_test_key_resp* updates
            waitOnFlip = False
            if verbal_test_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                verbal_test_key_resp.frameNStart = frameN  # exact frame index
                verbal_test_key_resp.tStart = t  # local t and not account for scr refresh
                verbal_test_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(verbal_test_key_resp, 'tStartRefresh')  # time at next scr refresh
                verbal_test_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(verbal_test_key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(verbal_test_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if verbal_test_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = verbal_test_key_resp.getKeys(keyList=['space'], waitRelease=False)
                _verbal_test_key_resp_allKeys.extend(theseKeys)
                if len(_verbal_test_key_resp_allKeys):
                    verbal_test_key_resp.keys = _verbal_test_key_resp_allKeys[-1].name  # just the last key pressed
                    verbal_test_key_resp.rt = _verbal_test_key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in verbal_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "verbal_test"-------
        for thisComponent in verbal_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('plate_verbal.started', plate_verbal.tStartRefresh)
        trials.addData('plate_verbal.stopped', plate_verbal.tStopRefresh)
        trials.addData('street_text_verbal.started', street_text_verbal.tStartRefresh)
        trials.addData('street_text_verbal.stopped', street_text_verbal.tStopRefresh)
        trials.addData('city_text_verbal.started', city_text_verbal.tStartRefresh)
        trials.addData('city_text_verbal.stopped', city_text_verbal.tStopRefresh)
        trials.addData('question_verbal.started', question_verbal.tStartRefresh)
        trials.addData('question_verbal.stopped', question_verbal.tStopRefresh)
        # check responses
        if verbal_test_key_resp.keys in ['', [], None]:  # No response was made
            verbal_test_key_resp.keys = None
        trials.addData('verbal_test_key_resp.keys',verbal_test_key_resp.keys)
        if verbal_test_key_resp.keys != None:  # we had a response
            trials.addData('verbal_test_key_resp.rt', verbal_test_key_resp.rt)
        trials.addData('verbal_test_key_resp.started', verbal_test_key_resp.tStartRefresh)
        trials.addData('verbal_test_key_resp.stopped', verbal_test_key_resp.tStopRefresh)
        # the Routine "verbal_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
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
        trials.addData('fx_cross.started', fx_cross.tStartRefresh)
        trials.addData('fx_cross.stopped', fx_cross.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    
    # ------Prepare to start Routine "take_a_break"-------
    continueRoutine = True
    # update component parameters for each repeat
    break_key_resp.keys = []
    break_key_resp.rt = []
    _break_key_resp_allKeys = []
    if repetitions >= 4:
        continueRoutine = False
    
    thisExp.addData('n_remembered', recall)
    recall=0
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
# completed 2.0 repeats of 'CityBlock'


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

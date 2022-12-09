#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on December 09, 2022, at 17:34
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
psychopyVersion = '2022.2.4'
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
    originPath='D:\\Zsuzsa\\HCCCL\\Prediction-and-Memory\\Hippopolis\\TwoCities_UpdatingPhase.py',
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
test_list = './stimuli/subj_files/' + ID + '_4afct.csv'

# --- Initialize components for Routine "update_instructions" ---
learning_instructions_text = visual.TextStim(win=win, name='learning_instructions_text',
    text='Eltelt három év, és Ön visszatér Hippopolisba és Camponelloba.\n\nHippopolis egy nagyváros, ezért gyorsan változik. Az utcák többségébe a korábban látottakhoz képest új képek kerültek. \nCamponello viszont egy kisváros, kevés a változás. Az utcák többségében ugyanazokat a képeket találja, mint régen.\n\nAz Ön feladata ismét az, hogy megjegyezze, melyik utcában milyen képet látott. \nA képernyő felső részén látja majd a város és az utca nevét, középen pedig a képet. Próbálja meg memorizálni az utcához tartozó képet!\n\nMiután végigjárta az utcákat, egy emlékezeti feladattal vizsgáljuk meg, mennyi utcára és képre emlékszik. \n\nA SZÓKÖZ lenyomásával elindul a feladat.',
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1400.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro_key = keyboard.Keyboard()

# --- Initialize components for Routine "city_intro_updating" ---
cityname_text_intro = visual.TextStim(win=win, name='cityname_text_intro',
    text='',
    font='Open Sans',
    pos=(0, 400), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
city_image_update = visual.ImageStim(
    win=win,
    name='city_image_update', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -100), size=(750, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
load_video = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='load_video')

# --- Initialize components for Routine "satellite_video" ---
movie = visual.MovieStim(
    win, name='movie',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=(1920, 1080), units=None,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)
end_vid_key = keyboard.Keyboard()

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
key_resp_update = keyboard.Keyboard()
button_image_updating = visual.ImageStim(
    win=win,
    name='button_image_updating', 
    image='stimuli/buttons_category.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -200), size=(660, 312),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
# Run 'Begin Experiment' code from save_trial_success
cues = []
success = []

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

# --- Initialize components for Routine "end_updating" ---
end_text_updating = visual.TextStim(win=win, name='end_text_updating',
    text='Vége a feladat második részének.\nMost a teszt következik.\n\nTartson egy rövid szünetet!',
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1000.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "instructions_4afct" ---
learning_instructions_text_2 = visual.TextStim(win=win, name='learning_instructions_text_2',
    text="A következőkben 4 kép közül kell kiválasztania, melyiket látta legutóbb a megadott utcában.\n\nAz utcanevet a képernyő tetején tüntetjük fel, ez alatt jelennek meg a választható képek. \nA 'D', 'F', 'J' és 'K' billentyűk segítségével válasszon a képek közül. \n\nA SZÓKÖZ lenyomásával elindul a feladat.",
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1400.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro_key_2 = keyboard.Keyboard()

# --- Initialize components for Routine "fixation_cross" ---
fx_cross = visual.TextStim(win=win, name='fx_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "test_trial_4afct" ---
street_text_updating_2 = visual.TextStim(win=win, name='street_text_updating_2',
    text='',
    font='Open Sans',
    pos=(0, 320), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
test_image1 = visual.ImageStim(
    win=win,
    name='test_image1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-512, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
test_image2 = visual.ImageStim(
    win=win,
    name='test_image2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-192, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
test_image3 = visual.ImageStim(
    win=win,
    name='test_image3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(192, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
test_image4 = visual.ImageStim(
    win=win,
    name='test_image4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(512, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
button_d = visual.ImageStim(
    win=win,
    name='button_d', 
    image='stimuli/test_4afc_d.png', mask=None, anchor='center',
    ori=0.0, pos=(-512, -350), size=(99, 94),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
button_f = visual.ImageStim(
    win=win,
    name='button_f', 
    image='stimuli/test_4afc_f.png', mask=None, anchor='center',
    ori=0.0, pos=(-192,-350), size=(99, 94),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
button_j = visual.ImageStim(
    win=win,
    name='button_j', 
    image='stimuli/test_4afc_j.png', mask=None, anchor='center',
    ori=0.0, pos=(192, -350), size=(99, 94),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
button_k = visual.ImageStim(
    win=win,
    name='button_k', 
    image='stimuli/test_4afc_k.png', mask=None, anchor='center',
    ori=0.0, pos=(512, -350), size=(99, 94),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
key_resp_4afct = keyboard.Keyboard()
# Run 'Begin Experiment' code from check_response
target = 0
lure = 0
dist1 = 0
dist2 = 0
invalid = 0
clock0 = visual.ImageStim(
    win=win,
    name='clock0', 
    image='stimuli/stopwatch0.png', mask=None, anchor='center',
    ori=0.0, pos=(450, 350), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)

# --- Initialize components for Routine "short_break_4afct" ---
short_break_text_2 = visual.TextStim(win=win, name='short_break_text_2',
    text='Rövid szünet.... \n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
short_break_key_2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from need_a_break_2
trial_count = 0

# --- Initialize components for Routine "end_task" ---
end_text = visual.TextStim(win=win, name='end_text',
    text='Vége a vizsgálatnak! \n\nKöszönjük a részvételt!',
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
    
    # --- Prepare to start Routine "city_intro_updating" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    cityname_text_intro.setText(CityName)
    city_image_update.setImage(CityImage)
    # keep track of which components have finished
    city_intro_updatingComponents = [cityname_text_intro, city_image_update, load_video]
    for thisComponent in city_intro_updatingComponents:
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
    
    # --- Run Routine "city_intro_updating" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cityname_text_intro* updates
        if cityname_text_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cityname_text_intro.frameNStart = frameN  # exact frame index
            cityname_text_intro.tStart = t  # local t and not account for scr refresh
            cityname_text_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cityname_text_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cityname_text_intro.started')
            cityname_text_intro.setAutoDraw(True)
        if cityname_text_intro.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cityname_text_intro.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                cityname_text_intro.tStop = t  # not accounting for scr refresh
                cityname_text_intro.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cityname_text_intro.stopped')
                cityname_text_intro.setAutoDraw(False)
        
        # *city_image_update* updates
        if city_image_update.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            city_image_update.frameNStart = frameN  # exact frame index
            city_image_update.tStart = t  # local t and not account for scr refresh
            city_image_update.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(city_image_update, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'city_image_update.started')
            city_image_update.setAutoDraw(True)
        if city_image_update.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > city_image_update.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                city_image_update.tStop = t  # not accounting for scr refresh
                city_image_update.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'city_image_update.stopped')
                city_image_update.setAutoDraw(False)
        # *load_video* period
        if load_video.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            load_video.frameNStart = frameN  # exact frame index
            load_video.tStart = t  # local t and not account for scr refresh
            load_video.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(load_video, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('load_video.started', t)
            load_video.start(3)
        elif load_video.status == STARTED:  # one frame should pass before updating params and completing
            load_video.complete()  # finish the static period
            load_video.tStop = load_video.tStart + 3  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in city_intro_updatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "city_intro_updating" ---
    for thisComponent in city_intro_updatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "satellite_video" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    movie.setMovie(UpdatingVideoFile)
    end_vid_key.keys = []
    end_vid_key.rt = []
    _end_vid_key_allKeys = []
    # keep track of which components have finished
    satellite_videoComponents = [movie, end_vid_key]
    for thisComponent in satellite_videoComponents:
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
    
    # --- Run Routine "satellite_video" ---
    while continueRoutine and routineTimer.getTime() < 7.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movie* updates
        if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            movie.frameNStart = frameN  # exact frame index
            movie.tStart = t  # local t and not account for scr refresh
            movie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'movie.started')
            movie.setAutoDraw(True)
            movie.play()
        if movie.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > movie.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                movie.tStop = t  # not accounting for scr refresh
                movie.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'movie.stopped')
                movie.setAutoDraw(False)
                movie.stop()
        if movie.status == FINISHED:  # force-end the routine
            continueRoutine = False
        
        # *end_vid_key* updates
        waitOnFlip = False
        if end_vid_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_vid_key.frameNStart = frameN  # exact frame index
            end_vid_key.tStart = t  # local t and not account for scr refresh
            end_vid_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_vid_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_vid_key.started')
            end_vid_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_vid_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_vid_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_vid_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_vid_key.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                end_vid_key.tStop = t  # not accounting for scr refresh
                end_vid_key.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'end_vid_key.stopped')
                end_vid_key.status = FINISHED
        if end_vid_key.status == STARTED and not waitOnFlip:
            theseKeys = end_vid_key.getKeys(keyList=['p'], waitRelease=False)
            _end_vid_key_allKeys.extend(theseKeys)
            if len(_end_vid_key_allKeys):
                end_vid_key.keys = _end_vid_key_allKeys[-1].name  # just the last key pressed
                end_vid_key.rt = _end_vid_key_allKeys[-1].rt
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
        for thisComponent in satellite_videoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "satellite_video" ---
    for thisComponent in satellite_videoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    movie.stop()
    # check responses
    if end_vid_key.keys in ['', [], None]:  # No response was made
        end_vid_key.keys = None
    CityBlock.addData('end_vid_key.keys',end_vid_key.keys)
    if end_vid_key.keys != None:  # we had a response
        CityBlock.addData('end_vid_key.rt', end_vid_key.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-7.000000)
    
    # --- Prepare to start Routine "city_name" ---
    continueRoutine = True
    routineForceEnded = False
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
    UpdatingTrials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(StimuliFile),
        seed=None, name='UpdatingTrials')
    thisExp.addLoop(UpdatingTrials)  # add the loop to the experiment
    thisUpdatingTrial = UpdatingTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisUpdatingTrial.rgb)
    if thisUpdatingTrial != None:
        for paramName in thisUpdatingTrial:
            exec('{} = thisUpdatingTrial[paramName]'.format(paramName))
    
    for thisUpdatingTrial in UpdatingTrials:
        currentLoop = UpdatingTrials
        # abbreviate parameter names if possible (e.g. rgb = thisUpdatingTrial.rgb)
        if thisUpdatingTrial != None:
            for paramName in thisUpdatingTrial:
                exec('{} = thisUpdatingTrial[paramName]'.format(paramName))
        
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
        key_resp_update.keys = []
        key_resp_update.rt = []
        _key_resp_update_allKeys = []
        # keep track of which components have finished
        prediction_phaseComponents = [plate, city_text, street_text, fx_cross_prediction, key_resp_update, button_image_updating]
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
        while continueRoutine and routineTimer.getTime() < 4.0:
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
                if tThisFlipGlobal > plate.tStartRefresh + 4.0-frameTolerance:
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
                if tThisFlipGlobal > city_text.tStartRefresh + 4.0-frameTolerance:
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
                if tThisFlipGlobal > street_text.tStartRefresh + 4.0-frameTolerance:
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
                if tThisFlipGlobal > fx_cross_prediction.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fx_cross_prediction.tStop = t  # not accounting for scr refresh
                    fx_cross_prediction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fx_cross_prediction.stopped')
                    fx_cross_prediction.setAutoDraw(False)
            
            # *key_resp_update* updates
            waitOnFlip = False
            if key_resp_update.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_update.frameNStart = frameN  # exact frame index
                key_resp_update.tStart = t  # local t and not account for scr refresh
                key_resp_update.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_update, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_update.started')
                key_resp_update.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_update.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_update.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_update.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_update.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_update.tStop = t  # not accounting for scr refresh
                    key_resp_update.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_update.stopped')
                    key_resp_update.status = FINISHED
            if key_resp_update.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_update.getKeys(keyList=['left','right', 'down', 'up'], waitRelease=False)
                _key_resp_update_allKeys.extend(theseKeys)
                if len(_key_resp_update_allKeys):
                    key_resp_update.keys = _key_resp_update_allKeys[-1].name  # just the last key pressed
                    key_resp_update.rt = _key_resp_update_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_update.keys == str(CorrectResponse)) or (key_resp_update.keys == CorrectResponse):
                        key_resp_update.corr = 1
                    else:
                        key_resp_update.corr = 0
            
            # *button_image_updating* updates
            if button_image_updating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                button_image_updating.frameNStart = frameN  # exact frame index
                button_image_updating.tStart = t  # local t and not account for scr refresh
                button_image_updating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_image_updating, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_image_updating.started')
                button_image_updating.setAutoDraw(True)
            if button_image_updating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_image_updating.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    button_image_updating.tStop = t  # not accounting for scr refresh
                    button_image_updating.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_image_updating.stopped')
                    button_image_updating.setAutoDraw(False)
            
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
        # check responses
        if key_resp_update.keys in ['', [], None]:  # No response was made
            key_resp_update.keys = None
            # was no response the correct answer?!
            if str(CorrectResponse).lower() == 'none':
               key_resp_update.corr = 1;  # correct non-response
            else:
               key_resp_update.corr = 0;  # failed to respond (incorrectly)
        # store data for UpdatingTrials (TrialHandler)
        UpdatingTrials.addData('key_resp_update.keys',key_resp_update.keys)
        UpdatingTrials.addData('key_resp_update.corr', key_resp_update.corr)
        if key_resp_update.keys != None:  # we had a response
            UpdatingTrials.addData('key_resp_update.rt', key_resp_update.rt)
        # Run 'End Routine' code from save_trial_success
        cues.append(Cue)
        success.append(key_resp_update.corr)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        
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
        UpdatingTrials.addData('short_break_key.keys',short_break_key.keys)
        if short_break_key.keys != None:  # we had a response
            UpdatingTrials.addData('short_break_key.rt', short_break_key.rt)
        # the Routine "short_break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'UpdatingTrials'
    
    
    # --- Prepare to start Routine "take_a_break" ---
    continueRoutine = True
    routineForceEnded = False
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


# --- Prepare to start Routine "end_updating" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
end_updatingComponents = [end_text_updating]
for thisComponent in end_updatingComponents:
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

# --- Run Routine "end_updating" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text_updating* updates
    if end_text_updating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text_updating.frameNStart = frameN  # exact frame index
        end_text_updating.tStart = t  # local t and not account for scr refresh
        end_text_updating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text_updating, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_text_updating.started')
        end_text_updating.setAutoDraw(True)
    if end_text_updating.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text_updating.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            end_text_updating.tStop = t  # not accounting for scr refresh
            end_text_updating.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_text_updating.stopped')
            end_text_updating.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_updatingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_updating" ---
for thisComponent in end_updatingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "instructions_4afct" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_key_2.keys = []
intro_key_2.rt = []
_intro_key_2_allKeys = []
# keep track of which components have finished
instructions_4afctComponents = [learning_instructions_text_2, intro_key_2]
for thisComponent in instructions_4afctComponents:
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

# --- Run Routine "instructions_4afct" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *learning_instructions_text_2* updates
    if learning_instructions_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        learning_instructions_text_2.frameNStart = frameN  # exact frame index
        learning_instructions_text_2.tStart = t  # local t and not account for scr refresh
        learning_instructions_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learning_instructions_text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learning_instructions_text_2.started')
        learning_instructions_text_2.setAutoDraw(True)
    
    # *intro_key_2* updates
    waitOnFlip = False
    if intro_key_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key_2.frameNStart = frameN  # exact frame index
        intro_key_2.tStart = t  # local t and not account for scr refresh
        intro_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_key_2.started')
        intro_key_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_key_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key_2.status == STARTED and not waitOnFlip:
        theseKeys = intro_key_2.getKeys(keyList=['space'], waitRelease=False)
        _intro_key_2_allKeys.extend(theseKeys)
        if len(_intro_key_2_allKeys):
            intro_key_2.keys = _intro_key_2_allKeys[-1].name  # just the last key pressed
            intro_key_2.rt = _intro_key_2_allKeys[-1].rt
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
    for thisComponent in instructions_4afctComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_4afct" ---
for thisComponent in instructions_4afctComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_key_2.keys in ['', [], None]:  # No response was made
    intro_key_2.keys = None
thisExp.addData('intro_key_2.keys',intro_key_2.keys)
if intro_key_2.keys != None:  # we had a response
    thisExp.addData('intro_key_2.rt', intro_key_2.rt)
thisExp.nextEntry()
# the Routine "instructions_4afct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(test_list),
    seed=None, name='test_trials')
thisExp.addLoop(test_trials)  # add the loop to the experiment
thisTest_trial = test_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
if thisTest_trial != None:
    for paramName in thisTest_trial:
        exec('{} = thisTest_trial[paramName]'.format(paramName))

for thisTest_trial in test_trials:
    currentLoop = test_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
    if thisTest_trial != None:
        for paramName in thisTest_trial:
            exec('{} = thisTest_trial[paramName]'.format(paramName))
    
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
    
    # --- Prepare to start Routine "test_trial_4afct" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    street_text_updating_2.setText(Cue)
    test_image1.setImage(TestImage1)
    test_image2.setImage(TestImage2)
    test_image3.setImage(TestImage3)
    test_image4.setImage(TestImage4)
    key_resp_4afct.keys = []
    key_resp_4afct.rt = []
    _key_resp_4afct_allKeys = []
    # Run 'Begin Routine' code from check_response
    current_index = cues.index(Cue)
    reinstate_success = success[current_index]
    thisExp.addData('reinstated', reinstate_success)
    # keep track of which components have finished
    test_trial_4afctComponents = [street_text_updating_2, test_image1, test_image2, test_image3, test_image4, button_d, button_f, button_j, button_k, key_resp_4afct, clock0]
    for thisComponent in test_trial_4afctComponents:
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
    
    # --- Run Routine "test_trial_4afct" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *street_text_updating_2* updates
        if street_text_updating_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            street_text_updating_2.frameNStart = frameN  # exact frame index
            street_text_updating_2.tStart = t  # local t and not account for scr refresh
            street_text_updating_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(street_text_updating_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'street_text_updating_2.started')
            street_text_updating_2.setAutoDraw(True)
        if street_text_updating_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > street_text_updating_2.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                street_text_updating_2.tStop = t  # not accounting for scr refresh
                street_text_updating_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'street_text_updating_2.stopped')
                street_text_updating_2.setAutoDraw(False)
        
        # *test_image1* updates
        if test_image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_image1.frameNStart = frameN  # exact frame index
            test_image1.tStart = t  # local t and not account for scr refresh
            test_image1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_image1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_image1.started')
            test_image1.setAutoDraw(True)
        if test_image1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_image1.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                test_image1.tStop = t  # not accounting for scr refresh
                test_image1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_image1.stopped')
                test_image1.setAutoDraw(False)
        
        # *test_image2* updates
        if test_image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_image2.frameNStart = frameN  # exact frame index
            test_image2.tStart = t  # local t and not account for scr refresh
            test_image2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_image2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_image2.started')
            test_image2.setAutoDraw(True)
        if test_image2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_image2.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                test_image2.tStop = t  # not accounting for scr refresh
                test_image2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_image2.stopped')
                test_image2.setAutoDraw(False)
        
        # *test_image3* updates
        if test_image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_image3.frameNStart = frameN  # exact frame index
            test_image3.tStart = t  # local t and not account for scr refresh
            test_image3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_image3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_image3.started')
            test_image3.setAutoDraw(True)
        if test_image3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_image3.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                test_image3.tStop = t  # not accounting for scr refresh
                test_image3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_image3.stopped')
                test_image3.setAutoDraw(False)
        
        # *test_image4* updates
        if test_image4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_image4.frameNStart = frameN  # exact frame index
            test_image4.tStart = t  # local t and not account for scr refresh
            test_image4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_image4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_image4.started')
            test_image4.setAutoDraw(True)
        if test_image4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_image4.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                test_image4.tStop = t  # not accounting for scr refresh
                test_image4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_image4.stopped')
                test_image4.setAutoDraw(False)
        
        # *button_d* updates
        if button_d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_d.frameNStart = frameN  # exact frame index
            button_d.tStart = t  # local t and not account for scr refresh
            button_d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_d, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_d.started')
            button_d.setAutoDraw(True)
        if button_d.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > button_d.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                button_d.tStop = t  # not accounting for scr refresh
                button_d.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_d.stopped')
                button_d.setAutoDraw(False)
        
        # *button_f* updates
        if button_f.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_f.frameNStart = frameN  # exact frame index
            button_f.tStart = t  # local t and not account for scr refresh
            button_f.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_f, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_f.started')
            button_f.setAutoDraw(True)
        if button_f.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > button_f.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                button_f.tStop = t  # not accounting for scr refresh
                button_f.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_f.stopped')
                button_f.setAutoDraw(False)
        
        # *button_j* updates
        if button_j.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_j.frameNStart = frameN  # exact frame index
            button_j.tStart = t  # local t and not account for scr refresh
            button_j.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_j, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_j.started')
            button_j.setAutoDraw(True)
        if button_j.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > button_j.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                button_j.tStop = t  # not accounting for scr refresh
                button_j.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_j.stopped')
                button_j.setAutoDraw(False)
        
        # *button_k* updates
        if button_k.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_k.frameNStart = frameN  # exact frame index
            button_k.tStart = t  # local t and not account for scr refresh
            button_k.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_k, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_k.started')
            button_k.setAutoDraw(True)
        if button_k.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > button_k.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                button_k.tStop = t  # not accounting for scr refresh
                button_k.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_k.stopped')
                button_k.setAutoDraw(False)
        
        # *key_resp_4afct* updates
        waitOnFlip = False
        if key_resp_4afct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4afct.frameNStart = frameN  # exact frame index
            key_resp_4afct.tStart = t  # local t and not account for scr refresh
            key_resp_4afct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4afct, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4afct.started')
            key_resp_4afct.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4afct.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4afct.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4afct.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4afct.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4afct.tStop = t  # not accounting for scr refresh
                key_resp_4afct.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4afct.stopped')
                key_resp_4afct.status = FINISHED
        if key_resp_4afct.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4afct.getKeys(keyList=['d', 'f', 'j', 'k'], waitRelease=False)
            _key_resp_4afct_allKeys.extend(theseKeys)
            if len(_key_resp_4afct_allKeys):
                key_resp_4afct.keys = _key_resp_4afct_allKeys[-1].name  # just the last key pressed
                key_resp_4afct.rt = _key_resp_4afct_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *clock0* updates
        if clock0.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            clock0.frameNStart = frameN  # exact frame index
            clock0.tStart = t  # local t and not account for scr refresh
            clock0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clock0, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'clock0.started')
            clock0.setAutoDraw(True)
        if clock0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clock0.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                clock0.tStop = t  # not accounting for scr refresh
                clock0.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'clock0.stopped')
                clock0.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_trial_4afctComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "test_trial_4afct" ---
    for thisComponent in test_trial_4afctComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4afct.keys in ['', [], None]:  # No response was made
        key_resp_4afct.keys = None
    test_trials.addData('key_resp_4afct.keys',key_resp_4afct.keys)
    if key_resp_4afct.keys != None:  # we had a response
        test_trials.addData('key_resp_4afct.rt', key_resp_4afct.rt)
    # Run 'End Routine' code from check_response
    key = key_resp_4afct.keys
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
    thisExp.addData('test4afct_resp', response)
    if response == 'target':
        target += 1
    if response == 'lure':
        lure += 1
    if response == 'dist1':
        dist1 += 1
    if response == 'dist2':
        dist2 += 1
    if response == 'invalid':
        invalid += 1
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "short_break_4afct" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    short_break_key_2.keys = []
    short_break_key_2.rt = []
    _short_break_key_2_allKeys = []
    # Run 'Begin Routine' code from need_a_break_2
    trial_count += 1
    
    if trial_count < 45:
        continueRoutine = False
    else:
        trial_count = 0
        
    # keep track of which components have finished
    short_break_4afctComponents = [short_break_text_2, short_break_key_2]
    for thisComponent in short_break_4afctComponents:
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
    
    # --- Run Routine "short_break_4afct" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *short_break_text_2* updates
        if short_break_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            short_break_text_2.frameNStart = frameN  # exact frame index
            short_break_text_2.tStart = t  # local t and not account for scr refresh
            short_break_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(short_break_text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'short_break_text_2.started')
            short_break_text_2.setAutoDraw(True)
        
        # *short_break_key_2* updates
        waitOnFlip = False
        if short_break_key_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            short_break_key_2.frameNStart = frameN  # exact frame index
            short_break_key_2.tStart = t  # local t and not account for scr refresh
            short_break_key_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(short_break_key_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'short_break_key_2.started')
            short_break_key_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(short_break_key_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(short_break_key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if short_break_key_2.status == STARTED and not waitOnFlip:
            theseKeys = short_break_key_2.getKeys(keyList=['space'], waitRelease=False)
            _short_break_key_2_allKeys.extend(theseKeys)
            if len(_short_break_key_2_allKeys):
                short_break_key_2.keys = _short_break_key_2_allKeys[-1].name  # just the last key pressed
                short_break_key_2.rt = _short_break_key_2_allKeys[-1].rt
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
        for thisComponent in short_break_4afctComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "short_break_4afct" ---
    for thisComponent in short_break_4afctComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if short_break_key_2.keys in ['', [], None]:  # No response was made
        short_break_key_2.keys = None
    test_trials.addData('short_break_key_2.keys',short_break_key_2.keys)
    if short_break_key_2.keys != None:  # we had a response
        test_trials.addData('short_break_key_2.rt', short_break_key_2.rt)
    # the Routine "short_break_4afct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'test_trials'


# --- Prepare to start Routine "end_task" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from save_responses
thisExp.addData('n_targets', target)
thisExp.addData('n_lures', lure)
thisExp.addData('n_dist1s', dist1)
thisExp.addData('n_dist2s', dist2)
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

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on December 12, 2022, at 15:30
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
expName = 'MemoryLand'  # from the Builder filename that created this script
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
    originPath='D:\\Zsuzsa\\HCCCL\\Prediction-and-Memory\\Hippopolis\\MemoryLand.py',
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
# Run 'Begin Experiment' code from block_counter
repetitions = 0

# --- Initialize components for Routine "learning_instructions" ---
learning_instructions_text = visual.TextStim(win=win, name='learning_instructions_text',
    text='A következőkben két várost fog megismerni. \nA városok neve Hippopolis és Camponello. \n\nA két város utcáiban képeket fog találni. Ezek egyesével lesznek bemutatva.\n\nAz Ön feladata, hogy megjegyezze, melyik utcában milyen képet látott. \nA képernyő felső részén látja majd a város és az utca nevét, középen pedig a képet. Próbálja meg memorizálni az utcához tartozó képet!\n\nA városokat minden kör elején egy rövid videóval mutatjuk be. Ezután kezdődik a feladat.\n\nMiután végigjárta az utcákat, egy emlékezeti teszttel vizsgáljuk meg, mennyi utcára és képre emlékszik. \n\nA SZÓKÖZ lenyomásával elindul a vizsgálat.',
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1400.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro_key = keyboard.Keyboard()

# --- Initialize components for Routine "city_intro_learning" ---
learning_cityname_text = visual.TextStim(win=win, name='learning_cityname_text',
    text='',
    font='Open Sans',
    pos=(0, 400), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
learning_city_image = visual.ImageStim(
    win=win,
    name='learning_city_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -100), size=(750, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
# Run 'Begin Experiment' code from count_round
vid_num = '1.mp4'
load_video_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='load_video_2')

# --- Initialize components for Routine "intro_video" ---
learning_movie = visual.MovieStim(
    win, name='learning_movie',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=(1920, 1080), units=None,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)
learning_end_vid_key = keyboard.Keyboard()

# --- Initialize components for Routine "get_ready" ---
text_countdown = visual.TextStim(win=win, name='text_countdown',
    text='',
    font='Open Sans',
    pos=(0, 0), height=32.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
cityname_text_start = visual.TextStim(win=win, name='cityname_text_start',
    text='',
    font='Open Sans',
    pos=(0, 400), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "fixation_cross" ---
fx_cross = visual.TextStim(win=win, name='fx_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "learning_trial" ---
plate_learning = visual.ImageStim(
    win=win,
    name='plate_learning', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 350), size=(513, 215),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
learning_city_text = visual.TextStim(win=win, name='learning_city_text',
    text='',
    font='Open Sans',
    pos=(0, 400), height=36.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
learning_street_text = visual.TextStim(win=win, name='learning_street_text',
    text='',
    font='Open Sans',
    pos=(0, 320), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
learning_image = visual.ImageStim(
    win=win,
    name='learning_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(256, 256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
learning_skip_key = keyboard.Keyboard()

# --- Initialize components for Routine "short_break" ---
short_break_text = visual.TextStim(win=win, name='short_break_text',
    text='Rövid szünet.... Ugyanezzel a várossal folytatjuk.\n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
short_break_key = keyboard.Keyboard()

# --- Initialize components for Routine "test_intro" ---
learning_phase_test_text = visual.TextStim(win=win, name='learning_phase_test_text',
    text='A teszt következik. Döntse el, hogy TÁRGY vagy TÉR tartozik az utcanévhez, és válaszát a nyíl billentyűkkel jelölje.\n\nA folytatáshoz nyomja le a SZÓKÖZ gombot.',
    font='Open Sans',
    pos=(0, 0), height=34.0, wrapWidth=800.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
learning_phase_key = keyboard.Keyboard()
# Run 'Begin Experiment' code from set_max_written_test
import random as rnd
max_questions = 0

# --- Initialize components for Routine "get_ready" ---
text_countdown = visual.TextStim(win=win, name='text_countdown',
    text='',
    font='Open Sans',
    pos=(0, 0), height=32.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
cityname_text_start = visual.TextStim(win=win, name='cityname_text_start',
    text='',
    font='Open Sans',
    pos=(0, 400), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "fixation_cross" ---
fx_cross = visual.TextStim(win=win, name='fx_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "test_trial" ---
plate_test = visual.ImageStim(
    win=win,
    name='plate_test', 
    image='sin', mask=None, anchor='center',
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
    text='Tárgy vagy Tér?',
    font='Open Sans',
    pos=(0,0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
test_key_resp = keyboard.Keyboard()
button_image = visual.ImageStim(
    win=win,
    name='button_image', 
    image='stimuli/buttons_category.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -200), size=(660, 312),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "written_test" ---
# Run 'Begin Experiment' code from dice_roll
written_report = 0
plate_verbal = visual.ImageStim(
    win=win,
    name='plate_verbal', 
    image='sin', mask=None, anchor='center',
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
    text='Írja körül, mit látott a képen. \nA folytatáshoz kattintson a képernyőn bárhova az egérrel.',
    font='Open Sans',
    pos=(0,0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_response_test = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -300),     letterHeight=42.0,
     size=(600, 100), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='text_response_test',
     autoLog=True,
)
written_text_mouse = event.Mouse(win=win)
x, y = [None, None]
written_text_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "long_break1" ---
long_break1_break_text = visual.TextStim(win=win, name='long_break1_break_text',
    text='Szünet....\n\nA szünet után a másik város következik. \n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
long_break1_key = keyboard.Keyboard()

# --- Initialize components for Routine "end_learning_phase" ---
end_learning_text = visual.TextStim(win=win, name='end_learning_text',
    text='Vége a feladat első részének. Jelezze ezt a vizsgálatvezetőnek, majd tartson egy rövid szünetet!',
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1000.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue_updating_key = keyboard.Keyboard()

# --- Initialize components for Routine "update_instructions" ---
updating_instructions_text = visual.TextStim(win=win, name='updating_instructions_text',
    text='Eltelt három év, és Ön visszatér Hippopolisba és Camponelloba.\n\nHippopolis egy nagyváros, ezért gyorsan változik. Az utcák többségébe a korábban látottakhoz képest új képek kerültek. \nCamponello viszont egy kisváros, kevés a változás. Az utcák többségében ugyanazokat a képeket találja, mint régen.\n\nAz Ön feladata ismét az, hogy megjegyezze, melyik utcában milyen képet látott. \nA képernyő felső részén látja majd a város és az utca nevét, középen pedig a képet. Próbálja meg memorizálni az utcához tartozó képet!\n\nMiután végigjárta az utcákat, egy emlékezeti feladattal vizsgáljuk meg, mennyi utcára és képre emlékszik. \n\nA SZÓKÖZ lenyomásával elindul a feladat.',
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1400.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro_updating_key = keyboard.Keyboard()

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
# Run 'Begin Experiment' code from updating_block_counter
update_repetitions = 0

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
skip_key = keyboard.Keyboard()

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
skip_key_updating = keyboard.Keyboard()

# --- Initialize components for Routine "short_break" ---
short_break_text = visual.TextStim(win=win, name='short_break_text',
    text='Rövid szünet.... Ugyanezzel a várossal folytatjuk.\n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
short_break_key = keyboard.Keyboard()

# --- Initialize components for Routine "long_break2" ---
long_break2_text = visual.TextStim(win=win, name='long_break2_text',
    text='Szünet.... A szünet után a másik város következik.\n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
long_break2_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "end_updating" ---
end_text_updating = visual.TextStim(win=win, name='end_text_updating',
    text='Vége a feladat második részének.\nMost a teszt következik.\n\nJelezze a kísérletvezetőnek, hogy itt tart, majd tartson egy rövid szünetet a folytatás előtt!',
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1000.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue_key = keyboard.Keyboard()

# --- Initialize components for Routine "instructions_4afct" ---
instructions_4afct_text = visual.TextStim(win=win, name='instructions_4afct_text',
    text="A következőkben 4 kép közül kell kiválasztania, melyiket látta legutóbb a megadott utcában.\n\nAz utcanevet a képernyő tetején tüntetjük fel, ez alatt jelennek meg a választható képek. \nA 'D', 'F', 'J' és 'K' billentyűk segítségével válasszon a képek közül. \n\nA SZÓKÖZ lenyomásával elindul a feladat.",
    font='Open Sans',
    pos=(0, 0), height=35.0, wrapWidth=1400.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro_4afct_key = keyboard.Keyboard()

# --- Initialize components for Routine "fixation_cross" ---
fx_cross = visual.TextStim(win=win, name='fx_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "test_trial_4afct" ---
street_text_4afct = visual.TextStim(win=win, name='street_text_4afct',
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
short_break_4afct_text = visual.TextStim(win=win, name='short_break_4afct_text',
    text='Rövid szünet.... \n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font='Open Sans',
    pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
short_break_4afct_key = keyboard.Keyboard()
# Run 'Begin Experiment' code from need_a_break_4afct
trial_count = 0

# --- Initialize components for Routine "end_task" ---
end_experiment_text = visual.TextStim(win=win, name='end_experiment_text',
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

# --- Prepare to start Routine "learning_instructions" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "learning_instructions" ---
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
    for thisComponent in learning_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning_instructions" ---
for thisComponent in learning_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_key.keys in ['', [], None]:  # No response was made
    intro_key.keys = None
thisExp.addData('intro_key.keys',intro_key.keys)
if intro_key.keys != None:  # we had a response
    thisExp.addData('intro_key.rt', intro_key.rt)
thisExp.nextEntry()
# the Routine "learning_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
CityBlockLearning = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(city_list),
    seed=None, name='CityBlockLearning')
thisExp.addLoop(CityBlockLearning)  # add the loop to the experiment
thisCityBlockLearning = CityBlockLearning.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCityBlockLearning.rgb)
if thisCityBlockLearning != None:
    for paramName in thisCityBlockLearning:
        exec('{} = thisCityBlockLearning[paramName]'.format(paramName))

for thisCityBlockLearning in CityBlockLearning:
    currentLoop = CityBlockLearning
    # abbreviate parameter names if possible (e.g. rgb = thisCityBlockLearning.rgb)
    if thisCityBlockLearning != None:
        for paramName in thisCityBlockLearning:
            exec('{} = thisCityBlockLearning[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "city_intro_learning" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    learning_cityname_text.setText(CityName)
    learning_city_image.setImage(CityImage)
    # Run 'Begin Routine' code from count_round
    repetitions += 1
    if repetitions < 3:
        vid_num = '1.mp4'
    else:
        vid_num = '2.mp4'
    trial_count = 0
    video_file = LearningVideoFile + vid_num
    # keep track of which components have finished
    city_intro_learningComponents = [learning_cityname_text, learning_city_image, load_video_2]
    for thisComponent in city_intro_learningComponents:
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
    
    # --- Run Routine "city_intro_learning" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learning_cityname_text* updates
        if learning_cityname_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learning_cityname_text.frameNStart = frameN  # exact frame index
            learning_cityname_text.tStart = t  # local t and not account for scr refresh
            learning_cityname_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_cityname_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_cityname_text.started')
            learning_cityname_text.setAutoDraw(True)
        if learning_cityname_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > learning_cityname_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                learning_cityname_text.tStop = t  # not accounting for scr refresh
                learning_cityname_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learning_cityname_text.stopped')
                learning_cityname_text.setAutoDraw(False)
        
        # *learning_city_image* updates
        if learning_city_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learning_city_image.frameNStart = frameN  # exact frame index
            learning_city_image.tStart = t  # local t and not account for scr refresh
            learning_city_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_city_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_city_image.started')
            learning_city_image.setAutoDraw(True)
        if learning_city_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > learning_city_image.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                learning_city_image.tStop = t  # not accounting for scr refresh
                learning_city_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learning_city_image.stopped')
                learning_city_image.setAutoDraw(False)
        # *load_video_2* period
        if load_video_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            load_video_2.frameNStart = frameN  # exact frame index
            load_video_2.tStart = t  # local t and not account for scr refresh
            load_video_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(load_video_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('load_video_2.started', t)
            load_video_2.start(3)
        elif load_video_2.status == STARTED:  # one frame should pass before updating params and completing
            load_video_2.complete()  # finish the static period
            load_video_2.tStop = load_video_2.tStart + 3  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in city_intro_learningComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "city_intro_learning" ---
    for thisComponent in city_intro_learningComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "intro_video" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    learning_movie.setMovie(video_file)
    learning_end_vid_key.keys = []
    learning_end_vid_key.rt = []
    _learning_end_vid_key_allKeys = []
    # keep track of which components have finished
    intro_videoComponents = [learning_movie, learning_end_vid_key]
    for thisComponent in intro_videoComponents:
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
    
    # --- Run Routine "intro_video" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learning_movie* updates
        if learning_movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learning_movie.frameNStart = frameN  # exact frame index
            learning_movie.tStart = t  # local t and not account for scr refresh
            learning_movie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_movie, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_movie.started')
            learning_movie.setAutoDraw(True)
            learning_movie.play()
        if learning_movie.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > learning_movie.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                learning_movie.tStop = t  # not accounting for scr refresh
                learning_movie.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learning_movie.stopped')
                learning_movie.setAutoDraw(False)
                learning_movie.stop()
        if learning_movie.status == FINISHED:  # force-end the routine
            continueRoutine = False
        
        # *learning_end_vid_key* updates
        waitOnFlip = False
        if learning_end_vid_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learning_end_vid_key.frameNStart = frameN  # exact frame index
            learning_end_vid_key.tStart = t  # local t and not account for scr refresh
            learning_end_vid_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_end_vid_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_end_vid_key.started')
            learning_end_vid_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(learning_end_vid_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(learning_end_vid_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if learning_end_vid_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > learning_end_vid_key.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                learning_end_vid_key.tStop = t  # not accounting for scr refresh
                learning_end_vid_key.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learning_end_vid_key.stopped')
                learning_end_vid_key.status = FINISHED
        if learning_end_vid_key.status == STARTED and not waitOnFlip:
            theseKeys = learning_end_vid_key.getKeys(keyList=['p'], waitRelease=False)
            _learning_end_vid_key_allKeys.extend(theseKeys)
            if len(_learning_end_vid_key_allKeys):
                learning_end_vid_key.keys = _learning_end_vid_key_allKeys[-1].name  # just the last key pressed
                learning_end_vid_key.rt = _learning_end_vid_key_allKeys[-1].rt
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
        for thisComponent in intro_videoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro_video" ---
    for thisComponent in intro_videoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    learning_movie.stop()
    # check responses
    if learning_end_vid_key.keys in ['', [], None]:  # No response was made
        learning_end_vid_key.keys = None
    CityBlockLearning.addData('learning_end_vid_key.keys',learning_end_vid_key.keys)
    if learning_end_vid_key.keys != None:  # we had a response
        CityBlockLearning.addData('learning_end_vid_key.rt', learning_end_vid_key.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "get_ready" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    cityname_text_start.setText(CityName)
    # keep track of which components have finished
    get_readyComponents = [text_countdown, cityname_text_start]
    for thisComponent in get_readyComponents:
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
    
    # --- Run Routine "get_ready" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_countdown* updates
        if text_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_countdown.frameNStart = frameN  # exact frame index
            text_countdown.tStart = t  # local t and not account for scr refresh
            text_countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_countdown, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_countdown.started')
            text_countdown.setAutoDraw(True)
        if text_countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_countdown.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_countdown.tStop = t  # not accounting for scr refresh
                text_countdown.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_countdown.stopped')
                text_countdown.setAutoDraw(False)
        if text_countdown.status == STARTED:  # only update if drawing
            text_countdown.setText(str(3-int(t)), log=False)
        
        # *cityname_text_start* updates
        if cityname_text_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cityname_text_start.frameNStart = frameN  # exact frame index
            cityname_text_start.tStart = t  # local t and not account for scr refresh
            cityname_text_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cityname_text_start, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cityname_text_start.started')
            cityname_text_start.setAutoDraw(True)
        if cityname_text_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cityname_text_start.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                cityname_text_start.tStop = t  # not accounting for scr refresh
                cityname_text_start.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cityname_text_start.stopped')
                cityname_text_start.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in get_readyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "get_ready" ---
    for thisComponent in get_readyComponents:
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
        
        # --- Prepare to start Routine "learning_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        plate_learning.setImage(StreetSign)
        learning_city_text.setText(CityName)
        learning_street_text.setText(Cue)
        learning_image.setImage(Image)
        learning_skip_key.keys = []
        learning_skip_key.rt = []
        _learning_skip_key_allKeys = []
        # keep track of which components have finished
        learning_trialComponents = [plate_learning, learning_city_text, learning_street_text, learning_image, learning_skip_key]
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
        frameN = -1
        
        # --- Run Routine "learning_trial" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *plate_learning* updates
            if plate_learning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                plate_learning.frameNStart = frameN  # exact frame index
                plate_learning.tStart = t  # local t and not account for scr refresh
                plate_learning.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(plate_learning, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'plate_learning.started')
                plate_learning.setAutoDraw(True)
            if plate_learning.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > plate_learning.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    plate_learning.tStop = t  # not accounting for scr refresh
                    plate_learning.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'plate_learning.stopped')
                    plate_learning.setAutoDraw(False)
            
            # *learning_city_text* updates
            if learning_city_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learning_city_text.frameNStart = frameN  # exact frame index
                learning_city_text.tStart = t  # local t and not account for scr refresh
                learning_city_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learning_city_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learning_city_text.started')
                learning_city_text.setAutoDraw(True)
            if learning_city_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learning_city_text.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    learning_city_text.tStop = t  # not accounting for scr refresh
                    learning_city_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'learning_city_text.stopped')
                    learning_city_text.setAutoDraw(False)
            
            # *learning_street_text* updates
            if learning_street_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learning_street_text.frameNStart = frameN  # exact frame index
                learning_street_text.tStart = t  # local t and not account for scr refresh
                learning_street_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learning_street_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learning_street_text.started')
                learning_street_text.setAutoDraw(True)
            if learning_street_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learning_street_text.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    learning_street_text.tStop = t  # not accounting for scr refresh
                    learning_street_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'learning_street_text.stopped')
                    learning_street_text.setAutoDraw(False)
            
            # *learning_image* updates
            if learning_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learning_image.frameNStart = frameN  # exact frame index
                learning_image.tStart = t  # local t and not account for scr refresh
                learning_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learning_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learning_image.started')
                learning_image.setAutoDraw(True)
            if learning_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learning_image.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    learning_image.tStop = t  # not accounting for scr refresh
                    learning_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'learning_image.stopped')
                    learning_image.setAutoDraw(False)
            
            # *learning_skip_key* updates
            waitOnFlip = False
            if learning_skip_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learning_skip_key.frameNStart = frameN  # exact frame index
                learning_skip_key.tStart = t  # local t and not account for scr refresh
                learning_skip_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learning_skip_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learning_skip_key.started')
                learning_skip_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(learning_skip_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(learning_skip_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if learning_skip_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learning_skip_key.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    learning_skip_key.tStop = t  # not accounting for scr refresh
                    learning_skip_key.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'learning_skip_key.stopped')
                    learning_skip_key.status = FINISHED
            if learning_skip_key.status == STARTED and not waitOnFlip:
                theseKeys = learning_skip_key.getKeys(keyList=['p'], waitRelease=False)
                _learning_skip_key_allKeys.extend(theseKeys)
                if len(_learning_skip_key_allKeys):
                    learning_skip_key.keys = _learning_skip_key_allKeys[-1].name  # just the last key pressed
                    learning_skip_key.rt = _learning_skip_key_allKeys[-1].rt
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
            for thisComponent in learning_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "learning_trial" ---
        for thisComponent in learning_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if learning_skip_key.keys in ['', [], None]:  # No response was made
            learning_skip_key.keys = None
        LearningTrials.addData('learning_skip_key.keys',learning_skip_key.keys)
        if learning_skip_key.keys != None:  # we had a response
            LearningTrials.addData('learning_skip_key.rt', learning_skip_key.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        
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
    
    
    # --- Prepare to start Routine "test_intro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    learning_phase_key.keys = []
    learning_phase_key.rt = []
    _learning_phase_key_allKeys = []
    # Run 'Begin Routine' code from set_max_written_test
    if repetitions > 2:
        max_questions = rnd.randint(1,3)
    else:
        max_questions = rnd.randint(1,6)
        
    print(max_questions)
    # keep track of which components have finished
    test_introComponents = [learning_phase_test_text, learning_phase_key]
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
    frameN = -1
    
    # --- Run Routine "test_intro" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learning_phase_test_text* updates
        if learning_phase_test_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learning_phase_test_text.frameNStart = frameN  # exact frame index
            learning_phase_test_text.tStart = t  # local t and not account for scr refresh
            learning_phase_test_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_phase_test_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_phase_test_text.started')
            learning_phase_test_text.setAutoDraw(True)
        
        # *learning_phase_key* updates
        waitOnFlip = False
        if learning_phase_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learning_phase_key.frameNStart = frameN  # exact frame index
            learning_phase_key.tStart = t  # local t and not account for scr refresh
            learning_phase_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_phase_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_phase_key.started')
            learning_phase_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(learning_phase_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(learning_phase_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if learning_phase_key.status == STARTED and not waitOnFlip:
            theseKeys = learning_phase_key.getKeys(keyList=['space'], waitRelease=False)
            _learning_phase_key_allKeys.extend(theseKeys)
            if len(_learning_phase_key_allKeys):
                learning_phase_key.keys = _learning_phase_key_allKeys[-1].name  # just the last key pressed
                learning_phase_key.rt = _learning_phase_key_allKeys[-1].rt
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
        for thisComponent in test_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "test_intro" ---
    for thisComponent in test_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if learning_phase_key.keys in ['', [], None]:  # No response was made
        learning_phase_key.keys = None
    CityBlockLearning.addData('learning_phase_key.keys',learning_phase_key.keys)
    if learning_phase_key.keys != None:  # we had a response
        CityBlockLearning.addData('learning_phase_key.rt', learning_phase_key.rt)
    # the Routine "test_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "get_ready" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    cityname_text_start.setText(CityName)
    # keep track of which components have finished
    get_readyComponents = [text_countdown, cityname_text_start]
    for thisComponent in get_readyComponents:
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
    
    # --- Run Routine "get_ready" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_countdown* updates
        if text_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_countdown.frameNStart = frameN  # exact frame index
            text_countdown.tStart = t  # local t and not account for scr refresh
            text_countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_countdown, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_countdown.started')
            text_countdown.setAutoDraw(True)
        if text_countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_countdown.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_countdown.tStop = t  # not accounting for scr refresh
                text_countdown.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_countdown.stopped')
                text_countdown.setAutoDraw(False)
        if text_countdown.status == STARTED:  # only update if drawing
            text_countdown.setText(str(3-int(t)), log=False)
        
        # *cityname_text_start* updates
        if cityname_text_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cityname_text_start.frameNStart = frameN  # exact frame index
            cityname_text_start.tStart = t  # local t and not account for scr refresh
            cityname_text_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cityname_text_start, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cityname_text_start.started')
            cityname_text_start.setAutoDraw(True)
        if cityname_text_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cityname_text_start.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                cityname_text_start.tStop = t  # not accounting for scr refresh
                cityname_text_start.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cityname_text_start.stopped')
                cityname_text_start.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in get_readyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "get_ready" ---
    for thisComponent in get_readyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # set up handler to look after randomisation of conditions etc
    TestTrials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(StimuliFile),
        seed=None, name='TestTrials')
    thisExp.addLoop(TestTrials)  # add the loop to the experiment
    thisTestTrial = TestTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestTrial.rgb)
    if thisTestTrial != None:
        for paramName in thisTestTrial:
            exec('{} = thisTestTrial[paramName]'.format(paramName))
    
    for thisTestTrial in TestTrials:
        currentLoop = TestTrials
        # abbreviate parameter names if possible (e.g. rgb = thisTestTrial.rgb)
        if thisTestTrial != None:
            for paramName in thisTestTrial:
                exec('{} = thisTestTrial[paramName]'.format(paramName))
        
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
        
        # --- Prepare to start Routine "test_trial" ---
        continueRoutine = True
        routineForceEnded = False
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
        frameN = -1
        
        # --- Run Routine "test_trial" ---
        while continueRoutine and routineTimer.getTime() < 4.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'plate_test.started')
                plate_test.setAutoDraw(True)
            if plate_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > plate_test.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    plate_test.tStop = t  # not accounting for scr refresh
                    plate_test.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'plate_test.stopped')
                    plate_test.setAutoDraw(False)
            
            # *city_text_test* updates
            if city_text_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                city_text_test.frameNStart = frameN  # exact frame index
                city_text_test.tStart = t  # local t and not account for scr refresh
                city_text_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(city_text_test, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'city_text_test.started')
                city_text_test.setAutoDraw(True)
            if city_text_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > city_text_test.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    city_text_test.tStop = t  # not accounting for scr refresh
                    city_text_test.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'city_text_test.stopped')
                    city_text_test.setAutoDraw(False)
            
            # *street_text_test* updates
            if street_text_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                street_text_test.frameNStart = frameN  # exact frame index
                street_text_test.tStart = t  # local t and not account for scr refresh
                street_text_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(street_text_test, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'street_text_test.started')
                street_text_test.setAutoDraw(True)
            if street_text_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > street_text_test.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    street_text_test.tStop = t  # not accounting for scr refresh
                    street_text_test.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'street_text_test.stopped')
                    street_text_test.setAutoDraw(False)
            
            # *test_question* updates
            if test_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_question.frameNStart = frameN  # exact frame index
                test_question.tStart = t  # local t and not account for scr refresh
                test_question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_question, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_question.started')
                test_question.setAutoDraw(True)
            if test_question.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_question.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    test_question.tStop = t  # not accounting for scr refresh
                    test_question.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'test_question.stopped')
                    test_question.setAutoDraw(False)
            
            # *test_key_resp* updates
            waitOnFlip = False
            if test_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_key_resp.frameNStart = frameN  # exact frame index
                test_key_resp.tStart = t  # local t and not account for scr refresh
                test_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_key_resp.started')
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
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'test_key_resp.stopped')
                    test_key_resp.status = FINISHED
            if test_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = test_key_resp.getKeys(keyList=['left','right', 'down', 'up'], waitRelease=False)
                _test_key_resp_allKeys.extend(theseKeys)
                if len(_test_key_resp_allKeys):
                    test_key_resp.keys = _test_key_resp_allKeys[-1].name  # just the last key pressed
                    test_key_resp.rt = _test_key_resp_allKeys[-1].rt
                    # was this correct?
                    if (test_key_resp.keys == str(CorrectResponse)) or (test_key_resp.keys == CorrectResponse):
                        test_key_resp.corr = 1
                    else:
                        test_key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *button_image* updates
            if button_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                button_image.frameNStart = frameN  # exact frame index
                button_image.tStart = t  # local t and not account for scr refresh
                button_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_image.started')
                button_image.setAutoDraw(True)
            if button_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_image.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    button_image.tStop = t  # not accounting for scr refresh
                    button_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_image.stopped')
                    button_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test_trial" ---
        for thisComponent in test_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if test_key_resp.keys in ['', [], None]:  # No response was made
            test_key_resp.keys = None
            # was no response the correct answer?!
            if str(CorrectResponse).lower() == 'none':
               test_key_resp.corr = 1;  # correct non-response
            else:
               test_key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for TestTrials (TrialHandler)
        TestTrials.addData('test_key_resp.keys',test_key_resp.keys)
        TestTrials.addData('test_key_resp.corr', test_key_resp.corr)
        if test_key_resp.keys != None:  # we had a response
            TestTrials.addData('test_key_resp.rt', test_key_resp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        
        # --- Prepare to start Routine "written_test" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from dice_roll
        if test_key_resp.keys == CorrectResponse:
            dice = rnd.randint(1,10)
            print(dice)
            if written_report < max_questions:
                if dice < 2:
                    continueRoutine = False
                elif dice > 2:
                    written_report += 1
            else:
                    continueRoutine = False
        else:
            continueRoutine = False
        plate_verbal.setImage(StreetSign)
        street_text_verbal.setText(Cue)
        city_text_verbal.setText(CityName)
        text_response_test.reset()
        # setup some python lists for storing info about the written_text_mouse
        written_text_mouse.x = []
        written_text_mouse.y = []
        written_text_mouse.leftButton = []
        written_text_mouse.midButton = []
        written_text_mouse.rightButton = []
        written_text_mouse.time = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        written_testComponents = [plate_verbal, street_text_verbal, city_text_verbal, question_verbal, text_response_test, written_text_mouse]
        for thisComponent in written_testComponents:
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
        
        # --- Run Routine "written_test" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'plate_verbal.started')
                plate_verbal.setAutoDraw(True)
            
            # *street_text_verbal* updates
            if street_text_verbal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                street_text_verbal.frameNStart = frameN  # exact frame index
                street_text_verbal.tStart = t  # local t and not account for scr refresh
                street_text_verbal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(street_text_verbal, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'street_text_verbal.started')
                street_text_verbal.setAutoDraw(True)
            
            # *city_text_verbal* updates
            if city_text_verbal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                city_text_verbal.frameNStart = frameN  # exact frame index
                city_text_verbal.tStart = t  # local t and not account for scr refresh
                city_text_verbal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(city_text_verbal, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'city_text_verbal.started')
                city_text_verbal.setAutoDraw(True)
            
            # *question_verbal* updates
            if question_verbal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question_verbal.frameNStart = frameN  # exact frame index
                question_verbal.tStart = t  # local t and not account for scr refresh
                question_verbal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_verbal, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'question_verbal.started')
                question_verbal.setAutoDraw(True)
            
            # *text_response_test* updates
            if text_response_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_response_test.frameNStart = frameN  # exact frame index
                text_response_test.tStart = t  # local t and not account for scr refresh
                text_response_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_response_test, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_response_test.started')
                text_response_test.setAutoDraw(True)
            # *written_text_mouse* updates
            if written_text_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                written_text_mouse.frameNStart = frameN  # exact frame index
                written_text_mouse.tStart = t  # local t and not account for scr refresh
                written_text_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(written_text_mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('written_text_mouse.started', t)
                written_text_mouse.status = STARTED
                written_text_mouse.mouseClock.reset()
                prevButtonState = written_text_mouse.getPressed()  # if button is down already this ISN'T a new click
            if written_text_mouse.status == STARTED:  # only update if started and not finished!
                buttons = written_text_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        x, y = written_text_mouse.getPos()
                        written_text_mouse.x.append(x)
                        written_text_mouse.y.append(y)
                        buttons = written_text_mouse.getPressed()
                        written_text_mouse.leftButton.append(buttons[0])
                        written_text_mouse.midButton.append(buttons[1])
                        written_text_mouse.rightButton.append(buttons[2])
                        written_text_mouse.time.append(written_text_mouse.mouseClock.getTime())
                        
                        continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in written_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "written_test" ---
        for thisComponent in written_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TestTrials.addData('text_response_test.text',text_response_test.text)
        # store data for TestTrials (TrialHandler)
        TestTrials.addData('written_text_mouse.x', written_text_mouse.x)
        TestTrials.addData('written_text_mouse.y', written_text_mouse.y)
        TestTrials.addData('written_text_mouse.leftButton', written_text_mouse.leftButton)
        TestTrials.addData('written_text_mouse.midButton', written_text_mouse.midButton)
        TestTrials.addData('written_text_mouse.rightButton', written_text_mouse.rightButton)
        TestTrials.addData('written_text_mouse.time', written_text_mouse.time)
        # the Routine "written_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'TestTrials'
    
    
    # --- Prepare to start Routine "long_break1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    long_break1_key.keys = []
    long_break1_key.rt = []
    _long_break1_key_allKeys = []
    # Run 'Begin Routine' code from skip_if_learning_phase_ends
    if repetitions >= 4:
        continueRoutine = False
    
    written_report = 0
    # keep track of which components have finished
    long_break1Components = [long_break1_break_text, long_break1_key]
    for thisComponent in long_break1Components:
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
    
    # --- Run Routine "long_break1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *long_break1_break_text* updates
        if long_break1_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            long_break1_break_text.frameNStart = frameN  # exact frame index
            long_break1_break_text.tStart = t  # local t and not account for scr refresh
            long_break1_break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(long_break1_break_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'long_break1_break_text.started')
            long_break1_break_text.setAutoDraw(True)
        
        # *long_break1_key* updates
        waitOnFlip = False
        if long_break1_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            long_break1_key.frameNStart = frameN  # exact frame index
            long_break1_key.tStart = t  # local t and not account for scr refresh
            long_break1_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(long_break1_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'long_break1_key.started')
            long_break1_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(long_break1_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(long_break1_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if long_break1_key.status == STARTED and not waitOnFlip:
            theseKeys = long_break1_key.getKeys(keyList=['space'], waitRelease=False)
            _long_break1_key_allKeys.extend(theseKeys)
            if len(_long_break1_key_allKeys):
                long_break1_key.keys = _long_break1_key_allKeys[-1].name  # just the last key pressed
                long_break1_key.rt = _long_break1_key_allKeys[-1].rt
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
        for thisComponent in long_break1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "long_break1" ---
    for thisComponent in long_break1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if long_break1_key.keys in ['', [], None]:  # No response was made
        long_break1_key.keys = None
    CityBlockLearning.addData('long_break1_key.keys',long_break1_key.keys)
    if long_break1_key.keys != None:  # we had a response
        CityBlockLearning.addData('long_break1_key.rt', long_break1_key.rt)
    # the Routine "long_break1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2.0 repeats of 'CityBlockLearning'


# --- Prepare to start Routine "end_learning_phase" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
continue_updating_key.keys = []
continue_updating_key.rt = []
_continue_updating_key_allKeys = []
# keep track of which components have finished
end_learning_phaseComponents = [end_learning_text, continue_updating_key]
for thisComponent in end_learning_phaseComponents:
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

# --- Run Routine "end_learning_phase" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_learning_text* updates
    if end_learning_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_learning_text.frameNStart = frameN  # exact frame index
        end_learning_text.tStart = t  # local t and not account for scr refresh
        end_learning_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_learning_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_learning_text.started')
        end_learning_text.setAutoDraw(True)
    
    # *continue_updating_key* updates
    waitOnFlip = False
    if continue_updating_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_updating_key.frameNStart = frameN  # exact frame index
        continue_updating_key.tStart = t  # local t and not account for scr refresh
        continue_updating_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_updating_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_updating_key.started')
        continue_updating_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(continue_updating_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(continue_updating_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if continue_updating_key.status == STARTED and not waitOnFlip:
        theseKeys = continue_updating_key.getKeys(keyList=['p'], waitRelease=False)
        _continue_updating_key_allKeys.extend(theseKeys)
        if len(_continue_updating_key_allKeys):
            continue_updating_key.keys = _continue_updating_key_allKeys[-1].name  # just the last key pressed
            continue_updating_key.rt = _continue_updating_key_allKeys[-1].rt
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
    for thisComponent in end_learning_phaseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_learning_phase" ---
for thisComponent in end_learning_phaseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if continue_updating_key.keys in ['', [], None]:  # No response was made
    continue_updating_key.keys = None
thisExp.addData('continue_updating_key.keys',continue_updating_key.keys)
if continue_updating_key.keys != None:  # we had a response
    thisExp.addData('continue_updating_key.rt', continue_updating_key.rt)
thisExp.nextEntry()
# the Routine "end_learning_phase" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "update_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_updating_key.keys = []
intro_updating_key.rt = []
_intro_updating_key_allKeys = []
# keep track of which components have finished
update_instructionsComponents = [updating_instructions_text, intro_updating_key]
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
    
    # *updating_instructions_text* updates
    if updating_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        updating_instructions_text.frameNStart = frameN  # exact frame index
        updating_instructions_text.tStart = t  # local t and not account for scr refresh
        updating_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(updating_instructions_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'updating_instructions_text.started')
        updating_instructions_text.setAutoDraw(True)
    
    # *intro_updating_key* updates
    waitOnFlip = False
    if intro_updating_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_updating_key.frameNStart = frameN  # exact frame index
        intro_updating_key.tStart = t  # local t and not account for scr refresh
        intro_updating_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_updating_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_updating_key.started')
        intro_updating_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_updating_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_updating_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_updating_key.status == STARTED and not waitOnFlip:
        theseKeys = intro_updating_key.getKeys(keyList=['space'], waitRelease=False)
        _intro_updating_key_allKeys.extend(theseKeys)
        if len(_intro_updating_key_allKeys):
            intro_updating_key.keys = _intro_updating_key_allKeys[-1].name  # just the last key pressed
            intro_updating_key.rt = _intro_updating_key_allKeys[-1].rt
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
if intro_updating_key.keys in ['', [], None]:  # No response was made
    intro_updating_key.keys = None
thisExp.addData('intro_updating_key.keys',intro_updating_key.keys)
if intro_updating_key.keys != None:  # we had a response
    thisExp.addData('intro_updating_key.rt', intro_updating_key.rt)
thisExp.nextEntry()
# the Routine "update_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
CityBlockUpdating = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(city_list),
    seed=None, name='CityBlockUpdating')
thisExp.addLoop(CityBlockUpdating)  # add the loop to the experiment
thisCityBlockUpdating = CityBlockUpdating.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCityBlockUpdating.rgb)
if thisCityBlockUpdating != None:
    for paramName in thisCityBlockUpdating:
        exec('{} = thisCityBlockUpdating[paramName]'.format(paramName))

for thisCityBlockUpdating in CityBlockUpdating:
    currentLoop = CityBlockUpdating
    # abbreviate parameter names if possible (e.g. rgb = thisCityBlockUpdating.rgb)
    if thisCityBlockUpdating != None:
        for paramName in thisCityBlockUpdating:
            exec('{} = thisCityBlockUpdating[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "city_intro_updating" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    cityname_text_intro.setText(CityName)
    city_image_update.setImage(CityImage)
    # Run 'Begin Routine' code from updating_block_counter
    update_repetitions += 1
    trial_count = 0
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
    CityBlockUpdating.addData('end_vid_key.keys',end_vid_key.keys)
    if end_vid_key.keys != None:  # we had a response
        CityBlockUpdating.addData('end_vid_key.rt', end_vid_key.rt)
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
        skip_key.keys = []
        skip_key.rt = []
        _skip_key_allKeys = []
        # keep track of which components have finished
        prediction_phaseComponents = [plate, city_text, street_text, fx_cross_prediction, key_resp_update, button_image_updating, skip_key]
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
            
            # *skip_key* updates
            waitOnFlip = False
            if skip_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                skip_key.frameNStart = frameN  # exact frame index
                skip_key.tStart = t  # local t and not account for scr refresh
                skip_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(skip_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'skip_key.started')
                skip_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(skip_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(skip_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if skip_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > skip_key.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    skip_key.tStop = t  # not accounting for scr refresh
                    skip_key.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'skip_key.stopped')
                    skip_key.status = FINISHED
            if skip_key.status == STARTED and not waitOnFlip:
                theseKeys = skip_key.getKeys(keyList=['p'], waitRelease=False)
                _skip_key_allKeys.extend(theseKeys)
                if len(_skip_key_allKeys):
                    skip_key.keys = _skip_key_allKeys[-1].name  # just the last key pressed
                    skip_key.rt = _skip_key_allKeys[-1].rt
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
        # check responses
        if skip_key.keys in ['', [], None]:  # No response was made
            skip_key.keys = None
        UpdatingTrials.addData('skip_key.keys',skip_key.keys)
        if skip_key.keys != None:  # we had a response
            UpdatingTrials.addData('skip_key.rt', skip_key.rt)
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
        skip_key_updating.keys = []
        skip_key_updating.rt = []
        _skip_key_updating_allKeys = []
        # keep track of which components have finished
        updating_phaseComponents = [plate_updating, city_text_updating, street_text_updating, updating_image, skip_key_updating]
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
            
            # *skip_key_updating* updates
            waitOnFlip = False
            if skip_key_updating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                skip_key_updating.frameNStart = frameN  # exact frame index
                skip_key_updating.tStart = t  # local t and not account for scr refresh
                skip_key_updating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(skip_key_updating, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'skip_key_updating.started')
                skip_key_updating.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(skip_key_updating.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(skip_key_updating.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if skip_key_updating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > skip_key_updating.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    skip_key_updating.tStop = t  # not accounting for scr refresh
                    skip_key_updating.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'skip_key_updating.stopped')
                    skip_key_updating.status = FINISHED
            if skip_key_updating.status == STARTED and not waitOnFlip:
                theseKeys = skip_key_updating.getKeys(keyList=['p'], waitRelease=False)
                _skip_key_updating_allKeys.extend(theseKeys)
                if len(_skip_key_updating_allKeys):
                    skip_key_updating.keys = _skip_key_updating_allKeys[-1].name  # just the last key pressed
                    skip_key_updating.rt = _skip_key_updating_allKeys[-1].rt
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
        # check responses
        if skip_key_updating.keys in ['', [], None]:  # No response was made
            skip_key_updating.keys = None
        UpdatingTrials.addData('skip_key_updating.keys',skip_key_updating.keys)
        if skip_key_updating.keys != None:  # we had a response
            UpdatingTrials.addData('skip_key_updating.rt', skip_key_updating.rt)
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
    
    
    # --- Prepare to start Routine "long_break2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    long_break2_key_resp.keys = []
    long_break2_key_resp.rt = []
    _long_break2_key_resp_allKeys = []
    # Run 'Begin Routine' code from skip_if_updating_ends
    if update_repetitions >= 2:
        continueRoutine = False
    # keep track of which components have finished
    long_break2Components = [long_break2_text, long_break2_key_resp]
    for thisComponent in long_break2Components:
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
    
    # --- Run Routine "long_break2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *long_break2_text* updates
        if long_break2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            long_break2_text.frameNStart = frameN  # exact frame index
            long_break2_text.tStart = t  # local t and not account for scr refresh
            long_break2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(long_break2_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'long_break2_text.started')
            long_break2_text.setAutoDraw(True)
        
        # *long_break2_key_resp* updates
        waitOnFlip = False
        if long_break2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            long_break2_key_resp.frameNStart = frameN  # exact frame index
            long_break2_key_resp.tStart = t  # local t and not account for scr refresh
            long_break2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(long_break2_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'long_break2_key_resp.started')
            long_break2_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(long_break2_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(long_break2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if long_break2_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = long_break2_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _long_break2_key_resp_allKeys.extend(theseKeys)
            if len(_long_break2_key_resp_allKeys):
                long_break2_key_resp.keys = _long_break2_key_resp_allKeys[-1].name  # just the last key pressed
                long_break2_key_resp.rt = _long_break2_key_resp_allKeys[-1].rt
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
        for thisComponent in long_break2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "long_break2" ---
    for thisComponent in long_break2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if long_break2_key_resp.keys in ['', [], None]:  # No response was made
        long_break2_key_resp.keys = None
    CityBlockUpdating.addData('long_break2_key_resp.keys',long_break2_key_resp.keys)
    if long_break2_key_resp.keys != None:  # we had a response
        CityBlockUpdating.addData('long_break2_key_resp.rt', long_break2_key_resp.rt)
    # the Routine "long_break2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'CityBlockUpdating'


# --- Prepare to start Routine "end_updating" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
continue_key.keys = []
continue_key.rt = []
_continue_key_allKeys = []
# keep track of which components have finished
end_updatingComponents = [end_text_updating, continue_key]
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
while continueRoutine:
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
    
    # *continue_key* updates
    waitOnFlip = False
    if continue_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_key.frameNStart = frameN  # exact frame index
        continue_key.tStart = t  # local t and not account for scr refresh
        continue_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_key.started')
        continue_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(continue_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(continue_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if continue_key.status == STARTED and not waitOnFlip:
        theseKeys = continue_key.getKeys(keyList=['p'], waitRelease=False)
        _continue_key_allKeys.extend(theseKeys)
        if len(_continue_key_allKeys):
            continue_key.keys = _continue_key_allKeys[-1].name  # just the last key pressed
            continue_key.rt = _continue_key_allKeys[-1].rt
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
# check responses
if continue_key.keys in ['', [], None]:  # No response was made
    continue_key.keys = None
thisExp.addData('continue_key.keys',continue_key.keys)
if continue_key.keys != None:  # we had a response
    thisExp.addData('continue_key.rt', continue_key.rt)
thisExp.nextEntry()
# the Routine "end_updating" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_4afct" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_4afct_key.keys = []
intro_4afct_key.rt = []
_intro_4afct_key_allKeys = []
# keep track of which components have finished
instructions_4afctComponents = [instructions_4afct_text, intro_4afct_key]
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
    
    # *instructions_4afct_text* updates
    if instructions_4afct_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_4afct_text.frameNStart = frameN  # exact frame index
        instructions_4afct_text.tStart = t  # local t and not account for scr refresh
        instructions_4afct_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_4afct_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructions_4afct_text.started')
        instructions_4afct_text.setAutoDraw(True)
    
    # *intro_4afct_key* updates
    waitOnFlip = False
    if intro_4afct_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_4afct_key.frameNStart = frameN  # exact frame index
        intro_4afct_key.tStart = t  # local t and not account for scr refresh
        intro_4afct_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_4afct_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_4afct_key.started')
        intro_4afct_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_4afct_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_4afct_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_4afct_key.status == STARTED and not waitOnFlip:
        theseKeys = intro_4afct_key.getKeys(keyList=['space'], waitRelease=False)
        _intro_4afct_key_allKeys.extend(theseKeys)
        if len(_intro_4afct_key_allKeys):
            intro_4afct_key.keys = _intro_4afct_key_allKeys[-1].name  # just the last key pressed
            intro_4afct_key.rt = _intro_4afct_key_allKeys[-1].rt
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
if intro_4afct_key.keys in ['', [], None]:  # No response was made
    intro_4afct_key.keys = None
thisExp.addData('intro_4afct_key.keys',intro_4afct_key.keys)
if intro_4afct_key.keys != None:  # we had a response
    thisExp.addData('intro_4afct_key.rt', intro_4afct_key.rt)
thisExp.nextEntry()
# the Routine "instructions_4afct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Test4afctTrials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(test_list),
    seed=None, name='Test4afctTrials')
thisExp.addLoop(Test4afctTrials)  # add the loop to the experiment
thisTest4afctTrial = Test4afctTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest4afctTrial.rgb)
if thisTest4afctTrial != None:
    for paramName in thisTest4afctTrial:
        exec('{} = thisTest4afctTrial[paramName]'.format(paramName))

for thisTest4afctTrial in Test4afctTrials:
    currentLoop = Test4afctTrials
    # abbreviate parameter names if possible (e.g. rgb = thisTest4afctTrial.rgb)
    if thisTest4afctTrial != None:
        for paramName in thisTest4afctTrial:
            exec('{} = thisTest4afctTrial[paramName]'.format(paramName))
    
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
    street_text_4afct.setText(Cue)
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
    updating_cue = cues[current_index]
    thisExp.addData('updating_cue', updating_cue)
    thisExp.addData('reinstated', reinstate_success)
    # keep track of which components have finished
    test_trial_4afctComponents = [street_text_4afct, test_image1, test_image2, test_image3, test_image4, button_d, button_f, button_j, button_k, key_resp_4afct, clock0]
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
        
        # *street_text_4afct* updates
        if street_text_4afct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            street_text_4afct.frameNStart = frameN  # exact frame index
            street_text_4afct.tStart = t  # local t and not account for scr refresh
            street_text_4afct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(street_text_4afct, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'street_text_4afct.started')
            street_text_4afct.setAutoDraw(True)
        if street_text_4afct.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > street_text_4afct.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                street_text_4afct.tStop = t  # not accounting for scr refresh
                street_text_4afct.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'street_text_4afct.stopped')
                street_text_4afct.setAutoDraw(False)
        
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
    Test4afctTrials.addData('key_resp_4afct.keys',key_resp_4afct.keys)
    if key_resp_4afct.keys != None:  # we had a response
        Test4afctTrials.addData('key_resp_4afct.rt', key_resp_4afct.rt)
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
    short_break_4afct_key.keys = []
    short_break_4afct_key.rt = []
    _short_break_4afct_key_allKeys = []
    # Run 'Begin Routine' code from need_a_break_4afct
    trial_count += 1
    
    if trial_count < 45:
        continueRoutine = False
    else:
        trial_count = 0
        
    # keep track of which components have finished
    short_break_4afctComponents = [short_break_4afct_text, short_break_4afct_key]
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
        
        # *short_break_4afct_text* updates
        if short_break_4afct_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            short_break_4afct_text.frameNStart = frameN  # exact frame index
            short_break_4afct_text.tStart = t  # local t and not account for scr refresh
            short_break_4afct_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(short_break_4afct_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'short_break_4afct_text.started')
            short_break_4afct_text.setAutoDraw(True)
        
        # *short_break_4afct_key* updates
        waitOnFlip = False
        if short_break_4afct_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            short_break_4afct_key.frameNStart = frameN  # exact frame index
            short_break_4afct_key.tStart = t  # local t and not account for scr refresh
            short_break_4afct_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(short_break_4afct_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'short_break_4afct_key.started')
            short_break_4afct_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(short_break_4afct_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(short_break_4afct_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if short_break_4afct_key.status == STARTED and not waitOnFlip:
            theseKeys = short_break_4afct_key.getKeys(keyList=['space'], waitRelease=False)
            _short_break_4afct_key_allKeys.extend(theseKeys)
            if len(_short_break_4afct_key_allKeys):
                short_break_4afct_key.keys = _short_break_4afct_key_allKeys[-1].name  # just the last key pressed
                short_break_4afct_key.rt = _short_break_4afct_key_allKeys[-1].rt
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
    if short_break_4afct_key.keys in ['', [], None]:  # No response was made
        short_break_4afct_key.keys = None
    Test4afctTrials.addData('short_break_4afct_key.keys',short_break_4afct_key.keys)
    if short_break_4afct_key.keys != None:  # we had a response
        Test4afctTrials.addData('short_break_4afct_key.rt', short_break_4afct_key.rt)
    # the Routine "short_break_4afct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Test4afctTrials'


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
end_taskComponents = [end_experiment_text]
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
while continueRoutine and routineTimer.getTime() < 30.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_experiment_text* updates
    if end_experiment_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_experiment_text.frameNStart = frameN  # exact frame index
        end_experiment_text.tStart = t  # local t and not account for scr refresh
        end_experiment_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_experiment_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_experiment_text.started')
        end_experiment_text.setAutoDraw(True)
    if end_experiment_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_experiment_text.tStartRefresh + 30.0-frameTolerance:
            # keep track of stop time/frame for later
            end_experiment_text.tStop = t  # not accounting for scr refresh
            end_experiment_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_experiment_text.stopped')
            end_experiment_text.setAutoDraw(False)
    
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
    routineTimer.addTime(-30.000000)

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

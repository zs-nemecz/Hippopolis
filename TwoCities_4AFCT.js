/************************ 
 * Twocities_4Afct Test *
 ************************/

import { PsychoJS } from './lib/core-2021.1.4.js';
import * as core from './lib/core-2021.1.4.js';
import { TrialHandler } from './lib/data-2021.1.4.js';
import { Scheduler } from './lib/util-2021.1.4.js';
import * as visual from './lib/visual-2021.1.4.js';
import * as sound from './lib/sound-2021.1.4.js';
import * as util from './lib/util-2021.1.4.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1.0, 1.0, 1.0]),
  units: 'pix',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'TwoCities_4AFCT';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(setupRoutineBegin());
flowScheduler.add(setupRoutineEachFrame());
flowScheduler.add(setupRoutineEnd());
const CityBlockLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(CityBlockLoopBegin, CityBlockLoopScheduler);
flowScheduler.add(CityBlockLoopScheduler);
flowScheduler.add(CityBlockLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'stimuli/test_4afc_k.png', 'path': 'stimuli/test_4afc_k.png'},
    {'name': 'stimuli/test_4afc_d.png', 'path': 'stimuli/test_4afc_d.png'},
    {'name': 'stimuli/test_4afc_f.png', 'path': 'stimuli/test_4afc_f.png'},
    {'name': 'stimuli/test_4afc_j.png', 'path': 'stimuli/test_4afc_j.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var setupClock;
var ID;
var city_list;
var city_nameClock;
var cityname_text;
var city_image;
var test_trialClock;
var plate_updating;
var city_text_updating;
var street_text_updating;
var test_image1;
var test_image2;
var test_image3;
var test_image4;
var button_d;
var button_f;
var button_j;
var button_k;
var key_resp;
var fixation_crossClock;
var fx_cross;
var t;
var l;
var d1;
var d2;
var take_a_breakClock;
var break_text;
var break_key_resp;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "setup"
  setupClock = new util.Clock();
  ID = expInfo["participant"];
  city_list = (("./stimuli/subj_files/" + ID) + "_city_list.csv");
  
  // Initialize components for Routine "city_name"
  city_nameClock = new util.Clock();
  cityname_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'cityname_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 400], height: 48.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  city_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'city_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, (- 100)], size : [1200, 630],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "test_trial"
  test_trialClock = new util.Clock();
  plate_updating = new visual.ImageStim({
    win : psychoJS.window,
    name : 'plate_updating', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 350], size : [513, 215],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  city_text_updating = new visual.TextStim({
    win: psychoJS.window,
    name: 'city_text_updating',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 400], height: 36.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  street_text_updating = new visual.TextStim({
    win: psychoJS.window,
    name: 'street_text_updating',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 320], height: 48.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  test_image1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test_image1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 512), 0], size : [256, 256],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  test_image2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test_image2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 192), 0], size : [256, 256],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  test_image3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test_image3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [192, 0], size : [256, 256],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  test_image4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test_image4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [512, 0], size : [256, 256],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  button_d = new visual.ImageStim({
    win : psychoJS.window,
    name : 'button_d', units : undefined, 
    image : 'stimuli\\\\test_4afc_d.png', mask : undefined,
    ori : 0.0, pos : [(- 512), (- 350)], size : [99, 94],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  button_f = new visual.ImageStim({
    win : psychoJS.window,
    name : 'button_f', units : undefined, 
    image : 'stimuli\\\\test_4afc_f.png', mask : undefined,
    ori : 0.0, pos : [(- 192), (- 350)], size : [99, 94],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  button_j = new visual.ImageStim({
    win : psychoJS.window,
    name : 'button_j', units : undefined, 
    image : 'stimuli\\\\test_4afc_j.png', mask : undefined,
    ori : 0.0, pos : [192, (- 350)], size : [99, 94],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  button_k = new visual.ImageStim({
    win : psychoJS.window,
    name : 'button_k', units : undefined, 
    image : 'stimuli\\\\test_4afc_k.png', mask : undefined,
    ori : 0.0, pos : [512, (- 350)], size : [99, 94],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -10.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation_cross"
  fixation_crossClock = new util.Clock();
  fx_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fx_cross',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 48.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  t = 0;
  l = 0;
  d1 = 0;
  d2 = 0;
  
  // Initialize components for Routine "take_a_break"
  take_a_breakClock = new util.Clock();
  break_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'break_text',
    text: 'Szünet....\n\nA folytatáshoz nyomja le a SZÓKÖZ billentyűt.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 48.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  break_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var frameN;
var continueRoutine;
var setupComponents;
function setupRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'setup'-------
    t = 0;
    setupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    setupComponents = [];
    
    for (const thisComponent of setupComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function setupRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'setup'-------
    // get current time
    t = setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of setupComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function setupRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'setup'-------
    for (const thisComponent of setupComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var CityBlock;
var currentLoop;
function CityBlockLoopBegin(CityBlockLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  CityBlock = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: city_list,
    seed: undefined, name: 'CityBlock'
  });
  psychoJS.experiment.addLoop(CityBlock); // add the loop to the experiment
  currentLoop = CityBlock;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisCityBlock of CityBlock) {
    const snapshot = CityBlock.getSnapshot();
    CityBlockLoopScheduler.add(importConditions(snapshot));
    CityBlockLoopScheduler.add(city_nameRoutineBegin(snapshot));
    CityBlockLoopScheduler.add(city_nameRoutineEachFrame(snapshot));
    CityBlockLoopScheduler.add(city_nameRoutineEnd(snapshot));
    const LearningTrialsLoopScheduler = new Scheduler(psychoJS);
    CityBlockLoopScheduler.add(LearningTrialsLoopBegin, LearningTrialsLoopScheduler);
    CityBlockLoopScheduler.add(LearningTrialsLoopScheduler);
    CityBlockLoopScheduler.add(LearningTrialsLoopEnd);
    CityBlockLoopScheduler.add(take_a_breakRoutineBegin(snapshot));
    CityBlockLoopScheduler.add(take_a_breakRoutineEachFrame(snapshot));
    CityBlockLoopScheduler.add(take_a_breakRoutineEnd(snapshot));
    CityBlockLoopScheduler.add(endLoopIteration(CityBlockLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var LearningTrials;
function LearningTrialsLoopBegin(LearningTrialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  LearningTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: StimuliFile,
    seed: undefined, name: 'LearningTrials'
  });
  psychoJS.experiment.addLoop(LearningTrials); // add the loop to the experiment
  currentLoop = LearningTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLearningTrial of LearningTrials) {
    const snapshot = LearningTrials.getSnapshot();
    LearningTrialsLoopScheduler.add(importConditions(snapshot));
    LearningTrialsLoopScheduler.add(test_trialRoutineBegin(snapshot));
    LearningTrialsLoopScheduler.add(test_trialRoutineEachFrame(snapshot));
    LearningTrialsLoopScheduler.add(test_trialRoutineEnd(snapshot));
    LearningTrialsLoopScheduler.add(fixation_crossRoutineBegin(snapshot));
    LearningTrialsLoopScheduler.add(fixation_crossRoutineEachFrame(snapshot));
    LearningTrialsLoopScheduler.add(fixation_crossRoutineEnd(snapshot));
    LearningTrialsLoopScheduler.add(endLoopIteration(LearningTrialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function LearningTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(LearningTrials);

  return Scheduler.Event.NEXT;
}


function CityBlockLoopEnd() {
  psychoJS.experiment.removeLoop(CityBlock);

  return Scheduler.Event.NEXT;
}


var city_nameComponents;
function city_nameRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'city_name'-------
    t = 0;
    city_nameClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    cityname_text.setText(CityName);
    city_image.setImage(CityImage);
    // keep track of which components have finished
    city_nameComponents = [];
    city_nameComponents.push(cityname_text);
    city_nameComponents.push(city_image);
    
    for (const thisComponent of city_nameComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function city_nameRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'city_name'-------
    // get current time
    t = city_nameClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cityname_text* updates
    if (t >= 0.0 && cityname_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cityname_text.tStart = t;  // (not accounting for frame time here)
      cityname_text.frameNStart = frameN;  // exact frame index
      
      cityname_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cityname_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cityname_text.setAutoDraw(false);
    }
    
    // *city_image* updates
    if (t >= 0.0 && city_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      city_image.tStart = t;  // (not accounting for frame time here)
      city_image.frameNStart = frameN;  // exact frame index
      
      city_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (city_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      city_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of city_nameComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function city_nameRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'city_name'-------
    for (const thisComponent of city_nameComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var test_trialComponents;
function test_trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'test_trial'-------
    t = 0;
    test_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    plate_updating.setImage(StreetSign);
    city_text_updating.setText(CityName);
    street_text_updating.setText(Cue);
    test_image1.setImage(TestImage1);
    test_image2.setImage(TestImage2);
    test_image3.setImage(TestImage3);
    test_image4.setImage(TestImage4);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    test_trialComponents = [];
    test_trialComponents.push(plate_updating);
    test_trialComponents.push(city_text_updating);
    test_trialComponents.push(street_text_updating);
    test_trialComponents.push(test_image1);
    test_trialComponents.push(test_image2);
    test_trialComponents.push(test_image3);
    test_trialComponents.push(test_image4);
    test_trialComponents.push(button_d);
    test_trialComponents.push(button_f);
    test_trialComponents.push(button_j);
    test_trialComponents.push(button_k);
    test_trialComponents.push(key_resp);
    
    for (const thisComponent of test_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function test_trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'test_trial'-------
    // get current time
    t = test_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *plate_updating* updates
    if (t >= 0.0 && plate_updating.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      plate_updating.tStart = t;  // (not accounting for frame time here)
      plate_updating.frameNStart = frameN;  // exact frame index
      
      plate_updating.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (plate_updating.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      plate_updating.setAutoDraw(false);
    }
    
    // *city_text_updating* updates
    if (t >= 0.0 && city_text_updating.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      city_text_updating.tStart = t;  // (not accounting for frame time here)
      city_text_updating.frameNStart = frameN;  // exact frame index
      
      city_text_updating.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (city_text_updating.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      city_text_updating.setAutoDraw(false);
    }
    
    // *street_text_updating* updates
    if (t >= 0.0 && street_text_updating.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      street_text_updating.tStart = t;  // (not accounting for frame time here)
      street_text_updating.frameNStart = frameN;  // exact frame index
      
      street_text_updating.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (street_text_updating.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      street_text_updating.setAutoDraw(false);
    }
    
    // *test_image1* updates
    if (t >= 0.0 && test_image1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test_image1.tStart = t;  // (not accounting for frame time here)
      test_image1.frameNStart = frameN;  // exact frame index
      
      test_image1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test_image1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test_image1.setAutoDraw(false);
    }
    
    // *test_image2* updates
    if (t >= 0.0 && test_image2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test_image2.tStart = t;  // (not accounting for frame time here)
      test_image2.frameNStart = frameN;  // exact frame index
      
      test_image2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test_image2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test_image2.setAutoDraw(false);
    }
    
    // *test_image3* updates
    if (t >= 0.0 && test_image3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test_image3.tStart = t;  // (not accounting for frame time here)
      test_image3.frameNStart = frameN;  // exact frame index
      
      test_image3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test_image3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test_image3.setAutoDraw(false);
    }
    
    // *test_image4* updates
    if (t >= 0.0 && test_image4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test_image4.tStart = t;  // (not accounting for frame time here)
      test_image4.frameNStart = frameN;  // exact frame index
      
      test_image4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test_image4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test_image4.setAutoDraw(false);
    }
    
    // *button_d* updates
    if (t >= 0.0 && button_d.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_d.tStart = t;  // (not accounting for frame time here)
      button_d.frameNStart = frameN;  // exact frame index
      
      button_d.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (button_d.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      button_d.setAutoDraw(false);
    }
    
    // *button_f* updates
    if (t >= 0.0 && button_f.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_f.tStart = t;  // (not accounting for frame time here)
      button_f.frameNStart = frameN;  // exact frame index
      
      button_f.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (button_f.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      button_f.setAutoDraw(false);
    }
    
    // *button_j* updates
    if (t >= 0.0 && button_j.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_j.tStart = t;  // (not accounting for frame time here)
      button_j.frameNStart = frameN;  // exact frame index
      
      button_j.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (button_j.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      button_j.setAutoDraw(false);
    }
    
    // *button_k* updates
    if (t >= 0.0 && button_k.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_k.tStart = t;  // (not accounting for frame time here)
      button_k.frameNStart = frameN;  // exact frame index
      
      button_k.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (button_k.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      button_k.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['d', 'f', 'j', 'k'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test_trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'test_trial'-------
    for (const thisComponent of test_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    return Scheduler.Event.NEXT;
  };
}


var key;
var response;
var fixation_crossComponents;
function fixation_crossRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fixation_cross'-------
    t = 0;
    fixation_crossClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    key = test_trial_keys.keys;
    response = "invalid";
    if ((key === "d")) {
        response = TestImage1Type;
    } else {
        if ((key === "f")) {
            response = TestImage2Type;
        } else {
            if ((key === "j")) {
                response = TestImage3Type;
            } else {
                if ((key === "k")) {
                    response = TestImage4Type;
                }
            }
        }
    }
    console.log(response);
    thisExp.addData("test_resp", response);
    if ((response === "target")) {
        t += 1;
    }
    if ((response === "lure")) {
        l += 1;
    }
    if ((response === "dist1")) {
        d1 += 1;
    }
    if ((response === "dist2")) {
        d2 += 1;
    }
    
    // keep track of which components have finished
    fixation_crossComponents = [];
    fixation_crossComponents.push(fx_cross);
    
    for (const thisComponent of fixation_crossComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fixation_crossRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fixation_cross'-------
    // get current time
    t = fixation_crossClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fx_cross* updates
    if (t >= 0.0 && fx_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fx_cross.tStart = t;  // (not accounting for frame time here)
      fx_cross.frameNStart = frameN;  // exact frame index
      
      fx_cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fx_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fx_cross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixation_crossComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation_crossRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fixation_cross'-------
    for (const thisComponent of fixation_crossComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _break_key_resp_allKeys;
var take_a_breakComponents;
function take_a_breakRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'take_a_break'-------
    t = 0;
    take_a_breakClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    break_key_resp.keys = undefined;
    break_key_resp.rt = undefined;
    _break_key_resp_allKeys = [];
    // keep track of which components have finished
    take_a_breakComponents = [];
    take_a_breakComponents.push(break_text);
    take_a_breakComponents.push(break_key_resp);
    
    for (const thisComponent of take_a_breakComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function take_a_breakRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'take_a_break'-------
    // get current time
    t = take_a_breakClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *break_text* updates
    if (t >= 0.0 && break_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      break_text.tStart = t;  // (not accounting for frame time here)
      break_text.frameNStart = frameN;  // exact frame index
      
      break_text.setAutoDraw(true);
    }

    
    // *break_key_resp* updates
    if (t >= 0.0 && break_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      break_key_resp.tStart = t;  // (not accounting for frame time here)
      break_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { break_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { break_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { break_key_resp.clearEvents(); });
    }

    if (break_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = break_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _break_key_resp_allKeys = _break_key_resp_allKeys.concat(theseKeys);
      if (_break_key_resp_allKeys.length > 0) {
        break_key_resp.keys = _break_key_resp_allKeys[_break_key_resp_allKeys.length - 1].name;  // just the last key pressed
        break_key_resp.rt = _break_key_resp_allKeys[_break_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of take_a_breakComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function take_a_breakRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'take_a_break'-------
    for (const thisComponent of take_a_breakComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('break_key_resp.keys', break_key_resp.keys);
    if (typeof break_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('break_key_resp.rt', break_key_resp.rt);
        routineTimer.reset();
        }
    
    break_key_resp.stop();
    // the Routine "take_a_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  thisExp.addData("n_targets", t);
  thisExp.addData("n_lures", l);
  thisExp.addData("n_dist1s", d1);
  thisExp.addData("n_dist2s", d2);
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}

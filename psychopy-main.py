from psychopy import visual, core, event  # import some libraries from PsychoPy
import psychtoolbox as ptb
from psychopy import sound
import random
import os



# create a window
mywin = visual.Window(monitor="testMonitor", units="deg", fullscr=True)

# create some stimuli
polygon = visual.ShapeStim(
    win=mywin, name='polygon', vertices='cross',
    size=(1, 1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=0.0, interpolate=True)
polygon.draw()
mywin.update()

beep = sound.Sound('A')
now = ptb.GetSecs()
beep.play(when=now+0.5)  # play in EXACTLY 0.5s

sound_2 = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='sound_2')
#mywin.flip()
#nextFlip = mywin.getFutureFlipTime(clock='ptb')
now = ptb.GetSecs()
sound_2.play(when=now+2)
core.wait(3.0)


STIMULI_COUNT = 3

materials_dir = '/home/kayhan/Repos/synthoice/materials/'
random_stimuli = random.sample(range(1, STIMULI_COUNT+1), STIMULI_COUNT)

type_of_stimulus = random.choice(['voice', 'voice_image', 'voice_text', 'voice_image_text'])

mywin.flip()
for i in range(STIMULI_COUNT):
    image_stim = visual.ImageStim(mywin, image=os.path.join(materials_dir, ('images/' + (str(random_stimuli[i]) + ".jpg"))))
    f = open(os.path.join(materials_dir, ('texts/' + (str(random_stimuli[i]) + ".txt"))), "r")
    text_stim = visual.TextStim(
        mywin,
        text=f.read(),
        pos=(0.0, -0.8),
        units="norm",
        height=0.05,
        wrapWidth=0.8,
    )
    voice= sound.Sound(os.path.join(materials_dir, ('voices/' + (str(random_stimuli[i]) + ".wav"))), secs=-1, stereo=True, hamming=True,
    name='voice')
    voice.setVolume(1.0)

    image_stim.draw()
    text_stim.draw()
    now = ptb.GetSecs()
    voice.play(when=now + 3)
    mywin.flip()
    core.wait(4)


core.wait(3.0)
'''
#cleanup
mywin.close()
core.quit()
'''

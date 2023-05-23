from psychopy import core, visual, gui, data, event
from time import sleep
import numpy as np
from psychopy import visual, core  # import some libraries from PsychoPy
from psychopy.hardware import keyboard
import random
import csv
import pandas as pd
import random
import math
import sys
def createStim(list_c, list_sf):
    
    x = (-2,2,-2,2)
    y = (2,2,-2,-2)
    
    i = 0
    grating_1 = visual.GratingStim(win=mywin, mask="circle", size=3, pos=[x[i],y[i]],sf = list_sf[0],contrast = list_c[0])
    title_1 = visual.TextStim(win=mywin, text="1", pos=[-2, 4], height=1.0, color="black")
    
    i = 1
    grating_2 = visual.GratingStim(win=mywin, mask="circle", size=3, pos=[x[i],y[i]],sf = list_sf[1],contrast = list_c[1])
    title_2 = visual.TextStim(win=mywin, text="2", pos=[2, 4], height=1.0, color="black")
    
    i = 2
    grating_3 = visual.GratingStim(win=mywin, mask="circle", size=3, pos=[x[i],y[i]],sf = list_sf[2],contrast = list_c[2])
    title_3 = visual.TextStim(win=mywin, text="3", pos=[-2,0], height=1.0, color="black")
    
    i = 3
    grating_4 = visual.GratingStim(win=mywin, mask="circle", size=3, pos=[x[i],y[i]],sf = list_sf[3],contrast = list_c[3])
    title_4 = visual.TextStim(win=mywin, text="4", pos=[2, 0], height=1.0, color="black")
    
    grating_1.draw()
    grating_2.draw()
    grating_3.draw()
    grating_4.draw()
    
    title_1.draw()
    title_2.draw()
    title_3.draw()
    title_4.draw()
    
    return [rnd_sf,rnd_c]
    
mywin = visual.Window([600,600], monitor="testMonitor", units="deg")
log_contrast = np.array([])
log_sf = np.array([])
chosen_gratings = np.array([])
j = 0
keyList=['1','2','3','4','q']
keys = []
N_times = 2
repeated_c = []
repeated_c_copy = []
df_dict = {}
all_sf = np.logspace(-1,2,10)
np.random.shuffle(all_sf)
#all_sf = all_sf.tolist()
#all_sf = np.random.uniform(0.1,math.log(2),10)
#all_sf = np.linspace(0.1,1,5)
index = []
c = np.logspace(-3,0,10)
c = c.tolist()
#c = np.linspace(0.05,1,10)

for i in range(N_times*10):
    np.random.shuffle(c)
    repeated_c = np.append(repeated_c,c)
#np.random.shuffle(repeated_c)
i = 0
ans = []
ctrs = []
r_sf = []

while repeated_c.size:  
    i = i + 1
    
    for rnd_sf in all_sf:
        rnd_sf = float(rnd_sf) + sys.float_info.epsilon
        rnd_c = float(random.choice(repeated_c))
        index_to_remove = np.argwhere(repeated_c == rnd_c)[0][0]
        repeated_c = np.delete(repeated_c, index_to_remove)
       
        
        list_c = [0,0,0,rnd_c]
        list_sf = [1,1,1,rnd_sf]
        
        mapIndexPosition = list(zip(list_c, list_sf))
        random.shuffle(mapIndexPosition)
        list_c, list_sf = zip(*mapIndexPosition)
        non_one_indices = [index for index, element in enumerate(list_sf) if element != int(1)]
        get_key = non_one_indices[0] + 1
        print("Position of the circle: " +str(get_key))
        [sf,cont] = createStim(list_c, list_sf)
        print("Remaining test: " + str(len(repeated_c)))
        msg_1 = "Repeat: " + str(j)
        msg_2 = "Spatial Freq: " + str(rnd_sf)
        title_msg1 = visual.TextStim(win=mywin, text=msg_1, pos=[-3, 8], height=0.5, color="black")
        title_msg2 = visual.TextStim(win=mywin, text=msg_2, pos=[3, 8], height=0.5, color="black")
        title_msg1.draw()
        title_msg2.draw()
        mywin.flip()
        
        keys = event.waitKeys(keyList=['1','2','3','4','q'])
        check_key = keys[0]
        
        
        if check_key in keyList:
            if int(check_key) == int(get_key):
                y_n = 'y'
            else:
                y_n = 'n'
            j = j + 1
            if check_key == 'q':
                core.quit()
                break
            ans.append(y_n)
            ctrs.append(rnd_c)
            r_sf.append(rnd_sf)
            index.append(j)
            check_key = []
        df = pd.DataFrame ({'user_answer': ans, 'contrast_value': ctrs,'spatial_freq': r_sf},index)
        mywin.update()
df.to_csv('my_data_df_2.csv', index=False)

  

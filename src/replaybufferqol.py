import obspython as obs
from playsound import playsound
import os

#get current directory of this file
current_directory = os.path.dirname(os.path.realpath(__file__))
#make a buffer that holds that, plus the "rsound.mp3" file
replaysound_buffer = "{}\\rsound.mp3".format(current_directory)
#change all the "\" to "/" so our playsound function actually works
replaysound = replaysound_buffer.replace("\\", "/")

#can be used to manually set replaysound if my janky dynamic directory thing doesn't work
#replaysound = "D:/OBS/obs-studio/data/obs-scripting/64bit/rsound.mp3"

# Description displayed in the Scripts dialog window
def script_description():
  return "simple obs plugin to add replay buffer qol\n\n made by snower"

#used to start replay buffer when obs / plugin is opened
if(obs.obs_frontend_replay_buffer_active() == True):
    print("replay is on")
else:
    print("replay isn't on \n turning replay on")
    obs.obs_frontend_replay_buffer_start()

#the OBS_FRONTEND_EVENT_REPLAY_BUFFERs send a fake, stinky, unwanted callback when the plugin is started
#this is used to stop that from actually saving a replay
how_many_replays_saved = 0 

def replay_buffer_saved(event):

    global how_many_replays_saved

    if event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_STARTED:
        how_many_replays_saved = 1
        return 1

    if event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_STARTING:
        how_many_replays_saved = 1
        return 1

    if event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_SAVED:
        print("how many replays equal: ", how_many_replays_saved)
        if how_many_replays_saved == 1:
            
            print("if")
            print("replay buffer saved")
            print(current_directory, replaysound)
            playsound(replaysound)

            return 0
        else:
            how_many_replays_saved = 1
            print("else", how_many_replays_saved)
            
            return 1



replay_buffer_saved(obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_SAVED)

def script_load(self):
    obs.obs_frontend_add_event_callback(replay_buffer_saved)

def script_unload():
    obs.obs_frontend_remove_event_callback(replay_buffer_saved)
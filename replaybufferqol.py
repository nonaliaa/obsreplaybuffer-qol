import obspython as obs
from playsound import playsound


replaysound = "D:/OBS/obs-studio/data/obs-scripting/64bit/rsound.mp3"

# Description displayed in the Scripts dialog window
def script_description():
  return "simple obs plugin to add replay buffer qol\n\n made by snower"


if(obs.obs_frontend_replay_buffer_active() == True):
    print("replay is on")
else:
    print("replay isn't on \n turning replay on")
    obs.obs_frontend_replay_buffer_start()


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
            playsound(replaysound)

        else:
            how_many_replays_saved = 1
            print("else", how_many_replays_saved)
            
            return 0



replay_buffer_saved(obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_SAVED)

def script_load(self):
    obs.obs_frontend_add_event_callback(replay_buffer_saved)

def script_unload():
    obs.obs_frontend_remove_event_callback(replay_buffer_saved)
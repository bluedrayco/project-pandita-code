from mp3.DFPlayer import DFPlayer
import time 

class PlaylistConfig:
    def __init__(self,repo:str,volume:int,start:int,end:int,exclude:list):
        if repo is "songs":
            self.directory=1
            self.start=start
            self.end=end
        if repo is "shrek":
            self.directory=2
        self.volume = 28 if volume >=28 else volume
        self.exclude=exclude
    
    
class Playlist:
    
    def __init__(self,config:PlaylistConfig):
        self.__df=DFPlayer(uart_id=2)
        #wait some time till the DFPlayer is ready
        time.sleep_ms(200)
        #change the volume (0-30). The DFPlayer doesn't remember these settings
        self.__df.volume(config.volume)
        time.sleep_ms(200)
        self.__config = config
        
    def isPlaying(self)->bool:
        return self.__df.is_playing()
    
    def runFirst(self):
        self.__df.play(self.__config.directory,1)
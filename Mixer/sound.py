from pygame import mixer

class Sound:
    def __init__(self, path:str, volume:float):
        self.sound = mixer.Sound(path)
        self.sound.set_volume(volume)
        

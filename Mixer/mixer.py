from Mixer.mixer_settings import MixerSettings
from Mixer.sound import Sound


class Mixer:
    def __init__(self):
        self.settings = MixerSettings()
        self.ball = Sound(
            path=self.settings.ball_sound,
            volume=self.settings.ball_sound_volume
        )
        self.music = Sound(
            path=self.settings.soundtrack,
            volume=self.settings.sountrack_volume
        )
        self.target = Sound(
            path=self.settings.target,
            volume=self.settings.target_volume
        )

    def play_sf(self, sound:object):
        sound.play()

    def play_music(self, sound:object):
        sound.play(loops=-1)

    
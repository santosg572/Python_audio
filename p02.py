from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_mp3("2025_03_13_08_14_00.mp3")

play(audio)




from pydub import AudioSegment
from pydub.playback import play

musica = AudioSegment.from_mp3('PayPhone.mp3')
play(musica)

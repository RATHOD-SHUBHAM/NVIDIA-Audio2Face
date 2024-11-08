from openai import OpenAI
import os
from dotenv import load_dotenv

HOME = os.getcwd()
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

class STT:
    def __init__(self):
        self.client = OpenAI()
        self.audio_file_path = f'{HOME}/src/voice/audio_file/recorded_audio.wav'

    def transcribe(self):
        audio_file= open(self.audio_file_path, "rb")

        transcription = self.client.audio.transcriptions.create(
          model="whisper-1",
          file=audio_file
        )

        print(transcription.text)

        return transcription.text
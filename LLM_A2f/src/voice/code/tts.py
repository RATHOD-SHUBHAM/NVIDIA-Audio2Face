from openai import OpenAI
import os
from dotenv import load_dotenv

HOME = os.getcwd()
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

class TTS:
    def __init__(self):
        self.client = OpenAI()
        self.speech_file_path = f'{HOME}/src/voice/audio_file/speech.wav'

    def generate(self, llm_response):
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input=llm_response
        )

        response.stream_to_file(self.speech_file_path)

        return True
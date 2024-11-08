from src.voice.code.stt import STT
from src.voice.code.tts import TTS
from src.LLM.llm_agent import Agent

class Solution:
    # Todo: Speech to text
    def run_stt(self):
        speech_obj = STT()
        transcribed_speech = speech_obj.transcribe()
        return transcribed_speech

    # Todo: LLM Code
    def generate_response(self, user_input):
        llm_obj = Agent()
        response = llm_obj.agents_tool(user_input=user_input)
        return response

    # Todo: Text to Speech
    def run_tts(self, llm_response):
        voice_obj = TTS()
        voice_obj.generate(llm_response=llm_response)

    # Todo: A2F

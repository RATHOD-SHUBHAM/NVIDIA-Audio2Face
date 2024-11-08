import streamlit as st
from st_audiorec import st_audiorec
import os
from src.main import Solution


HOME = os.getcwd()
obj = Solution()

# Record Audio
wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    # Save the raw audio data to a .wav file
    wav_file_name = f'{HOME}/src/voice/audio_file/recorded_audio.wav'

    with open(wav_file_name, 'wb') as f:
        f.write(wav_audio_data)  # Write raw bytes directly to the file

    st.write("Audio saved as 'recorded_audio.wav'")

    # STT
    user_input = obj.run_stt()

    # LLM
    response = obj.generate_response(user_input=user_input)

    # TTS
    successful = obj.run_tts(llm_response = response)

    # Audio2Face
    if successful:
        obj.run_a2f(successful=successful)

    
        

    st.write(response)



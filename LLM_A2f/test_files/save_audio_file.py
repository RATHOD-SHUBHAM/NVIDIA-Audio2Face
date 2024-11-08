import streamlit as st
from st_audiorec import st_audiorec

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')

    # Save the raw audio data to a .wav file
    wav_file_name = 'recorded_audio.wav'

    with open(wav_file_name, 'wb') as f:
        f.write(wav_audio_data)  # Write raw bytes directly to the file

    st.write("Audio saved as 'recorded_audio.wav'")
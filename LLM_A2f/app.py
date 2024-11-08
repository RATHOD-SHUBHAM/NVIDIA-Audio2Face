import streamlit as st
from st_audiorec import st_audiorec
import os
from src.main import Solution

# ----------------------------------------------------------------------
# streamlit code for viewing document
st.set_page_config(layout="wide",
                   page_title="OmniAvatar",
                   page_icon="🤖",
                   )

# hide hamburger and customize footer
hide_menu = """
    <style>

    #MainMenu {
        visibility:hidden;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        color: grey;
        text-align: center;
    }

    </style>

    <div class="footer">
        <p>'With 🫶️ from Shubham Shankar.'</p>
    </div>

"""

# Styling ----------------------------------------------------------------------
st.image("icon.jpg", width=85)
st.title("OmniAvatar: Breathing Life into Digital Characters")
st.subheader(" Transforming Frames into Frequencies: AI Breathing Life into Avatars! 🧠.")
st.write("Powered by Nvidia Omniverse, OpenAI and LLM Agents.")
st.markdown(hide_menu, unsafe_allow_html=True)

# Intro ----------------------------------------------------------------------

st.write(
    """
    Hi 👋, I'm **:red[Shubham Shankar]**, and welcome to my **:green[OmniAvatar]**! :rocket:

    We once dreamed of our digital avatars engaging in meaningful conversations just like real people. However, the challenge of creating lifelike interactions often felt daunting, leaving our avatars static and unresponsive.
    
    Introducing **:orange[OmniAvatar]!** Powered by **:green[NVIDIA Omniverse]** and cutting-edge **:violet[LLMs]**, OmniAvatar brings **avatars to life in real time.** ✨ 
    Effortlessly integrate captivating dialogue into virtual characters, transforming every interaction into a natural and immersive experience.
    Say goodbye to lifeless avatars and hello to dynamic, engaging conversations—our digital companions are ready to speak!✨
    """
)

st.markdown('---')

st.write(
    """
    ### App Components and Pipeline.

    1] **:red[ASR (Automatic Speech Recognition)]**: Effortlessly capture human interactions and convert them to text using OpenAI Whisper.

    2] **:blue[LLM Agents]**: Utilize advanced tools to understand and respond to user queries effectively.

    3] **:violet[TTS (Text to Speech)]**: Transform generated text into natural-sounding audio.

    4] **:green[Omniverse Audio2Face]**: Stream audio and convert it into facial blendshapes for real-time lip syncing and facial performances.
    """
)

st.markdown('---')

st.write(
    """
    ### App Interface!!

    :dog: The web app has an easy-to-use interface. 

    1] **:red[Start Recording]**: Capture human interactions effortlessly.
    
    2] **:blue[Stop]**: End the recording with a single click.
    
    3] **:orange[Reset]**: Clear the current recording with ease.
    
    4] **:green[Download]**: Save the audio file directly to your device.

    """
)

st.markdown('---')

st.error(
    """
    Connect with me on [**Github**](https://github.com/RATHOD-SHUBHAM) and [**LinkedIn**](https://www.linkedin.com/in/shubhamshankar/). ✨
    """,
    icon="🧟‍♂️",
)

st.markdown('---')

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
    obj.run_tts(llm_response = response)

    st.write(response)



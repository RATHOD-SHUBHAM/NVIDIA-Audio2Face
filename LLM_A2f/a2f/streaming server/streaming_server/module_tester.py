import subprocess
import wave
#import pyaudio
import tempfile
import os
import threading
import re
# import translate_tester
import soundfile as sf


voice = 'English-US-RadTTS.Female-Happy'

## Capture voice from mic button (On click)
"""
    We pass this to transcribe_audio()
        returns string of audio
    
    Pass string of audio to ollama
        returns string of llm response
    
    pass string of llm response to synthesize_audio()
        returns audio.wav
    
    pass audio.wav to audio2face   
    
"""

def transcribe_audio(audio_file_path):
    asr_auth_token = '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'  

    command = [
        'python3', '/home/azureuser/python-clients/scripts/asr/transcribe_file.py',
        '--server', 'grpc.nvcf.nvidia.com:443', '--use-ssl',
        '--metadata', 'function-id', 'd8dd4e9b-fbf5-4fb0-9dba-8cf436c8d965',
        '--metadata', 'authorization', f'Bearer {asr_auth_token}',
        '--language-code', 'en-US',
        '--input-file', audio_file_path
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    print("Output:", result.stdout)
    if(result.stderr):
        print("Error:", result.stderr)

    # Cleaning up the transcription output
    transcript = result.stdout.strip()
    
    # Removing unwanted characters 
    cleaned_transcript = transcript.replace('##', '').strip()

    return cleaned_transcript


def synthesize_audio(text):
    global voice
    tts_auth_token = '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'

    command = [
        'python3', '/home/azureuser/python-clients/scripts/tts/talk.py',
        '--server', 'grpc.nvcf.nvidia.com:443', '--use-ssl',
        '--metadata', 'function-id', '5e607c81-7aa6-44ce-a11d-9e08f0a3fe49',
        '--metadata', 'authorization', f'Bearer {tts_auth_token}',
        '--text', text,
        '--voice', voice,
        '--output', '/home/azureuser/NIM/audio.wav'
    ]

    audio_result = subprocess.run(command, capture_output=True, text=True)

    print("Output:",audio_result.stdout)
    if(audio_result.stderr):
        print("Error:", audio_result.stderr)

    # sf.write("output.wav",audio_result)
    return audio_result

   



# OLD was used for TESTING
if __name__ == "__main__":
    #wav_file = "/home/azureuser/NIM/pln.wav"
    #new_string = transcribe_audio(wav_file)
    #print(str(new_string))
    #thing = translate_tester.translate_text("Hello, and welcome to the all new way we are doing text to voice.")
    synthesize_audio("Hello, and welcome to the all new way we are doing text to voice.")
    
    

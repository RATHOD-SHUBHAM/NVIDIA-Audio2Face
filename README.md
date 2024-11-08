# NVIDIA-Audio2Face

# OmniAvatar
Welcome to OmniAvatar, a project that brings lifelike virtual avatars to reality by seamlessly integrating Large Language Models (LLMs) with NVIDIA Omniverse’s Audio2Face technology. Imagine avatars that don’t just look real but engage in dynamic, real-time conversations, responding to emotions and context with authenticity and depth. OmniAvatar transforms static digital characters into vivid personalities, revolutionizing how virtual interactions feel and respond.

## Overview
OmniAvatar leverages the power of LLMs and NVIDIA Omniverse Audio2Face to create avatars capable of real-time interaction and expression. NVIDIA Omniverse provides a solid foundation with its APIs, SDKs, and services, enabling developers to build advanced AI-driven systems with sophisticated simulation workflows. Through OmniAvatar, avatars can not only mimic human speech and expression but also respond intelligently and naturally, creating a more engaging and lifelike interaction experience.

## Project Structure
This repository is organized into two main parts, each serving a key role in building OmniAvatar:

### 1] LLM Code
Contains all code related to the LLM that powers the conversation and response generation. This module enables the avatar to understand and process user inputs and generate meaningful, contextually relevant replies.

### 2] Streaming Server
This module connects the LLM to the avatar, acting as the bridge between text-based intelligence and visual, expressive output. It streams data between the LLM and Audio2Face to synchronize audio, text, and facial animation.

## Getting Started
1. Clone the repository.
2. Follow the setup instructions in each module’s README file to install dependencies and configure the environment.
3. Start the Streaming Server to enable real-time communication between the LLM and the avatar in Omniverse Audio2Face.
4. Run the LLM Code to initialize conversation processing.

### Prerequisites
1. NVIDIA Omniverse installed and configured.
2. Access to Audio2Face in the Omniverse environment.
3. Python 3.x for LLM code execution.
4. Streaming server dependencies as outlined in the Streaming Server folder.

## Customizing Avatar Configuration
To make it easier to customize avatars in OmniAvatar, changes needed in the test_client.py file within the Streaming Server folder is provided below:

The Streaming Server module provides flexibility to change the avatar configuration, including setting personalized avatars by adjusting paths in the test_client.py script.

### Steps to Customize
1. Locate test_client.py
Go to the Streaming Server folder and open test_client.py.

2. Set the Audio File Path
Update the path to the WAV audio file that will be streamed to Audio2Face:
```
# Local input WAV file path
audio_fpath = r"C:\Users\SmgHima\Desktop\AvatarAI-oct-14\LLMCode\voiceservice\outputaudio\audio.wav"
Replace this with the desired path for the audio input file.
```

3. Set the Instance Name
Choose the appropriate instance_name for the Audio2Face Streaming Audio Player. This setting directs where to push the audio data on the Omniverse stage:
```
# Prim path of the Audio2Face Streaming Audio Player on the stage (where to push the audio data)
instance_name = "/World/audio2face/PlayerStreaming"
```
By default, instance_name is set to /World/audio2face/PlayerStreaming. To personalize the avatar setup, replace this path with the appropriate instance path for your specific configuration.




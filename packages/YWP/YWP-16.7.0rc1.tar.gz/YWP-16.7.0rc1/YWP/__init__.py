r"""
Created By Your Wanted Products (YWP)

Email: pbstzidr@ywp.freewebhostmost.com

Phone Number: +201096730619

WhatsApp Number: +201096730619

website: https://ywp.freewebhostmost.com
























"""

from flask import Flask
import platform
import subprocess
import sys
from googletrans import Translator
from moviepy.editor import ImageClip, concatenate_videoclips
from moviepy.video.fx import all as vfx
import os
import subprocess
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish
import binascii
import base64
import webbrowser
import nltk
import pygame
import sounddevice as sd
import wave
import speech_recognition as sr
import pyaudio
from gtts import gTTS
from typing import Any
import numpy as np
import json
import pickle
import nltk
from nltk.stem.lancaster import LancasterStemmer
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sys import stdout
import pyttsx3
from vosk import Model, KaldiRecognizer
import random
from time import sleep
import nmap
from cryptography.fernet import Fernet as CryptographyFernet
import hashlib
import logging
import yara
import itertools
import string
import socket
import requests
from scapy.all import sniff, IP

class Server:
    """
    A simple class to create and run a Flask server.

    Methods:
    - __init__: Initializes the server instance with None.
    - route_flask: Adds a route to the Flask application.
    - run: Starts the Flask server with specified configurations.

    Attributes:
    - app: Holds the Flask application instance.
    """

    def __init__(self):
        """
        Initializes the server with None for the app attribute.
        """
        self.app = None

    def route_flask(self, location="", returnValue=""):
        """
        Adds a route to the Flask application.

        Args:
        - location: URL endpoint for the route.
        - returnValue: Value returned by the route function.

        Returns:
        - 'done' if route addition is successful.
        """
        app = self.app
        try:
            if app is None:
                app = Flask(__name__)

            def make_route(return_value):
                def route():
                    return return_value
                return route

            endpoint = location.strip('/')
            if endpoint == '':
                endpoint = 'index'

            app.add_url_rule(location, endpoint, make_route(returnValue))
            self.app = app
            return 'done'
        except Exception as error:
            raise error
        
    def run(self, check=False, debug=True, host="0.0.0.0", port="8000"):
        """
        Starts the Flask server.

        Args:
        - check: If True, runs only if __name__ == "__main__".
        - debug: Enables debug mode if True.
        - host: Host IP address to run the server on.
        - port: Port number to run the server on.

        Returns:
        - 'done' if server starts successfully.
        """
        app = self.app
        try:
            if app is None:
                raise Exception("App not initialized")
            
            if check:
                if __name__ == "__main__":
                    app.run(debug=debug, host=host, port=port)
            else:
                app.run(debug=debug, host=host, port=port)
            return 'done'
        except Exception as error:
            raise error
        
class VideosCreator:
    """
    A class for creating videos from images using MoviePy.

    Nested Class:
    - Basic: Provides basic functionalities for video creation.

    Methods:
    - basic_video_creator: Creates a video from images with basic effects and options.

    Attributes:
    - VIDEO_DURATIONS: Dictionary mapping video platforms to their maximum durations.
    """

    class Basic:
        """
        Provides basic functionalities for creating videos from images.
        """

        def basic_video_creator(image_folder="images/", animation_choice="None", frame_rate=25, video_name="output", video_type="mp4", video_platform="Youtube", image_time=5):
            """
            Creates a video from images with specified parameters.

            Args:
            - image_folder: Folder containing images.
            - animation_choice: Animation effect between images (FadeIn, FadeOut, Rotate, FlipHorizontal, FlipVertical).
            - frame_rate: Frames per second for the video.
            - video_name: Name of the output video file.
            - video_type: Type of the output video file (e.g., mp4).
            - video_platform: Platform for which the video is optimized (Youtube, Facebook, Instagram, Tiktok).
            - image_time: Duration each image appears in seconds.

            Returns:
            - 'done' if video creation is successful.
            """

            VIDEO_DURATIONS = {
                'Youtube': 60,
                'Facebook': 20,
                'Instagram': 15,
                'Tiktok': 60
            }

            try:
                files = os.listdir(image_folder)
                image_files = [os.path.join(image_folder, f) for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                image_files.sort()
            except Exception as error:
                raise error

            if video_platform in VIDEO_DURATIONS:
                video_duration = VIDEO_DURATIONS[video_platform]
            else:
                raise ValueError(f"Unsupported video platform: {video_platform}. Choose from Youtube, Facebook, Instagram, or Tiktok.")

            video_clips = []
            for i, image_file in enumerate(image_files):
                clip = ImageClip(image_file).set_duration(image_time)
                video_clips.append(clip)
                
                if i < len(image_files) - 1 and animation_choice:
                    next_clip = ImageClip(image_files[i + 1]).set_duration(image_time)
                    if animation_choice == 'FadeIn':
                        fade_duration = min(1, image_time / 2)
                        video_clips.append(next_clip.crossfadein(fade_duration).set_start(clip.end))
                    elif animation_choice == 'FadeOut':
                        video_clips.append(clip.crossfadeout(1).set_end(clip.end))
                    elif animation_choice == 'Rotate':
                        rotate_clip = next_clip.rotate(lambda t: 360*t).set_start(clip.end)
                        video_clips.append(rotate_clip)
                    elif animation_choice == 'FlipHorizontal':
                        video_clips.append(next_clip.fx(vfx.mirror_x).set_start(clip.end))
                    elif animation_choice == 'FlipVertical':
                        video_clips.append(next_clip.fx(vfx.mirror_y).set_start(clip.end))
            
            final_video = concatenate_videoclips(video_clips, method="compose")
            
            output_file = f"{video_name}.{video_type}"
            final_video.write_videofile(output_file, fps=frame_rate)
            return 'done'

class Files:
    """
    A class for handling file operations.

    Methods:
    - delete_file: Deletes a file if it exists.
    - open_file: Opens a file if it exists using subprocess.
    - create_file: Creates a new file and writes user input into it.
    - delete_all_files: Deletes files in a directory based on specified types.

    Attributes:
    - None
    """

    def delete_file(filepath):
        """
        Deletes a file if it exists.

        Args:
        - filepath: Path to the file to delete.

        Returns:
        - "Deleted" if file is successfully deleted.
        - Raises an exception if deletion fails.
        """
        if os.path.exists(filepath):
            try:
                os.remove(filepath)
                return "Deleted"
            except Exception as error:
                raise error
    
    def open_file(filepath=""):
        """
        Opens a file if it exists using subprocess.

        Args:
        - filepath: Path to the file to open.

        Returns:
        - "open" if file is successfully opened.
        - "Not Found Path" if file path does not exist.
        - "An error occurred" with the error message if an exception occurs.
        """
        try:
            if os.path.exists(filepath):
                subprocess.Popen([str(filepath)])
                return "open"
            else:
                return "Not Found Path"
        except Exception as e:
            print("An error occurred:", e)
            return "An error occurred:", e
   
    def create_file(name=""):
        """
        Creates a new file and writes user input into it.

        Args:
        - name: Name of the file to create.

        Returns:
        - "created" if file is successfully created and written to.
        - Raises an exception if creation fails.
        """
        print("Please enter the text or code (press Ctrl + D on Unix or Ctrl + Z then Enter on Windows to finish):")

        user_input_lines = []
        try:
            while True:
                line = input()
                user_input_lines.append(line)
        except EOFError:
            pass

        user_input = '\n'.join(user_input_lines)
        
        filename = name

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(user_input)
            return "created"
        except Exception as error:
            raise error

    def delete_all_files(directory=".", type={}):
        """
        Deletes files in a directory based on specified types.

        Args:
        - directory: Directory path where files are located.
        - type: Dictionary mapping index to file types to delete.

        Returns:
        - "Deleted" if files are successfully deleted.
        - Raises an exception if deletion fails.
        """
        
        for filename in os.listdir(directory):
            for index, filetype in type.items():
                if filename.endswith(filetype):
                    filepath = os.path.join(directory, filename)
                    try:
                        os.remove(filepath)
                    except Exception as error:
                        raise error
        return "Deleted"
                
class endecrypt:
    """
    A class for handling encryption and decryption operations.

    Methods:
    - aes.encrypt: Encrypts a file using AES encryption.
    - aes.decrypt: Decrypts a file encrypted using AES encryption.
    - BlowFish.encrypt: Encrypts a file using Blowfish encryption.
    - BlowFish.decrypt: Decrypts a file encrypted using Blowfish encryption.
    - Base64.encrypt: Encrypts a file using Base64 encoding.
    - Base64.decrypt: Decrypts a file encoded using Base64 encoding.
    - Hex.encrypt: Encrypts a file by converting it to hexadecimal format.
    - Hex.decrypt: Decrypts a file from hexadecimal format.

    Attributes:
    - None
    """

    class aes:
        """
        AES encryption and decryption operations.

        Methods:
        - encrypt: Encrypts a file using AES encryption.
        - decrypt: Decrypts a file encrypted using AES encryption.

        Attributes:
        - None
        """

        def encrypt(file_path="", password=""):
            """
            Encrypts a file using AES encryption.

            Args:
            - file_path: Path to the file to encrypt.
            - password: Password used for encryption.

            Returns:
            - 'done' if encryption is successful.
            - Raises an exception if encryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                cipher = AES.new(key, AES.MODE_CBC)
                ct_bytes = cipher.encrypt(pad(data, AES.block_size))
                result = cipher.iv + ct_bytes
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                raise e

        def decrypt(file_path="", password=""):
            """
            Decrypts a file encrypted using AES encryption.

            Args:
            - file_path: Path to the file to decrypt.
            - password: Password used for decryption.

            Returns:
            - 'done' if decryption is successful.
            - Raises an exception if decryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                iv = data[:16]
                ct = data[16:]
                cipher = AES.new(key, AES.MODE_CBC, iv)
                result = unpad(cipher.decrypt(ct), AES.block_size)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                raise e

    class BlowFish:
        """
        Blowfish encryption and decryption operations.

        Methods:
        - encrypt: Encrypts a file using Blowfish encryption.
        - decrypt: Decrypts a file encrypted using Blowfish encryption.

        Attributes:
        - None
        """

        def encrypt(file_path="", password=""):
            """
            Encrypts a file using Blowfish encryption.

            Args:
            - file_path: Path to the file to encrypt.
            - password: Password used for encryption.

            Returns:
            - 'done' if encryption is successful.
            - Returns error message as string if encryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                cipher = Blowfish.new(key, Blowfish.MODE_CBC)
                ct_bytes = cipher.encrypt(pad(data, Blowfish.block_size))
                result = cipher.iv + ct_bytes
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)

        def decrypt(file_path="", password=""):
            """
            Decrypts a file encrypted using Blowfish encryption.

            Args:
            - file_path: Path to the file to decrypt.
            - password: Password used for decryption.

            Returns:
            - 'done' if decryption is successful.
            - Returns error message as string if decryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                iv = data[:8]
                ct = data[8:]
                cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
                result = unpad(cipher.decrypt(ct), Blowfish.block_size)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)

    class Base64:
        """
        Base64 encoding and decoding operations.

        Methods:
        - encrypt: Encrypts a file using Base64 encoding.
        - decrypt: Decrypts a file encoded using Base64 encoding.

        Attributes:
        - None
        """

        def encrypt(file_path=""):
            """
            Encrypts a file using Base64 encoding.

            Args:
            - file_path: Path to the file to encrypt.

            Returns:
            - 'done' if encryption is successful.
            - Returns error message as string if encryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = base64.b64encode(data)
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
            
        def decrypt(file_path=""):
            """
            Decrypts a file encoded using Base64 encoding.

            Args:
            - file_path: Path to the file to decrypt.

            Returns:
            - 'done' if decryption is successful.
            - Returns error message as string if decryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = base64.b64decode(data)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
            
    class Hex:
        """
        Hexadecimal encoding and decoding operations.

        Methods:
        - encrypt: Encrypts a file by converting it to hexadecimal format.
        - decrypt: Decrypts a file from hexadecimal format.

        Attributes:
        - None
        """

        def encrypt(file_path=""):
            """
            Encrypts a file by converting it to hexadecimal format.

            Args:
            - file_path: Path to the file to encrypt.

            Returns:
            - 'done' if encryption is successful.
            - Returns error message as string if encryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = binascii.hexlify(data)
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
            
        def decrypt(file_path=""):
            """
            Decrypts a file from hexadecimal format.

            Args:
            - file_path: Path to the file to decrypt.

            Returns:
            - 'done' if decryption is successful.
            - Returns error message as string if decryption fails.
            """
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = binascii.unhexlify(data)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
        


class Libraries:
    """
    A class for creating and managing libraries and setup files.

    Methods:
    - init_creator: Initializes a Python file with import statements.
    - basic_setup_file_creator: Creates a basic setup.py file for a Python library.
    - upload_file_creator: Creates upload scripts for distributing a Python library.

    Attributes:
    - None
    """

    class Basic:
        @staticmethod
        def init_creator(filesave="__init__.py", filename="", function_class=""):
            """
            Initializes a Python file with import statements.

            Args:
            - filesave: File path to save the initialization.
            - filename: Name of the Python file to import from.
            - function_class: Name of the function or class to import.

            Returns:
            - 'done' if successful.
            - Error message if unsuccessful.
            """
            if filename == "" or function_class == "" or filesave == "":
                return "FileSave or FileName or Function/Class Name is Not Found"
            
            try:
                if os.path.exists(filesave):
                    with open(filesave, "r") as f:
                        text = f.read()
                else:
                    text = ""

                text += f"\nfrom .{filename} import {function_class}"
                
                with open(filesave, "w") as f:
                    f.write(text)
                
                return 'done'
            except Exception as e:
                return str(e)

        @staticmethod
        def basic_setup_file_creator(filename="setup.py", folder_name="", readme_name="README.md", library_name="", library_version="", libraries_required=[], description="", creator_name="", creator_email="", License="MIT"):
            """
            Creates a basic setup.py file for a Python library.

            Args:
            - filename: Name of the setup file to create.
            - folder_name: Folder name (not used in function logic).
            - readme_name: Name of the README file.
            - library_name: Name of the Python library.
            - library_version: Version of the Python library.
            - libraries_required: List of required libraries.
            - description: Description of the Python library.
            - creator_name: Name of the library creator.
            - creator_email: Email of the library creator.
            - License: License type (default: MIT).

            Returns:
            - 'done' if successful.
            - 'FileName Found' if filename already exists.
            - Error message if unsuccessful.
            """
            if License == "MIT":
                libraries_required.append("YWP")
                file_data = (
                    "from setuptools import setup, find_packages\n\n"
                    f"setup(\nname='{library_name}',\nversion='{library_version}',\n"
                    f"packages=find_packages(),\ninstall_requires={str(libraries_required)},\n"
                    "classifiers=[\n'Programming Language :: Python :: 3',\n],\n"
                    "python_requires='>=3.6',\ndescription='" + description + "',\n"
                    f"long_description=open('{readme_name}').read(),\n"
                    "long_description_content_type='text/markdown',\n"
                    f"author='{creator_name}',\nauthor_email='{creator_email}',\n"
                    ")"
                )
                
                if os.path.exists(filename):
                    return 'FileName Found'
                
                try:
                    with open(filename, "w") as f:
                        f.write(file_data)
                    return 'done'
                except Exception as e:
                    return str(e)
            else:
                return 'Not From Licenses'

        @staticmethod
        def upload_file_creator(filename="upload_library", pypi_api="", platform="windows"):
            """
            Creates upload scripts for distributing a Python library.

            Args:
            - filename: Name of the upload script file.
            - pypi_api: PyPI API key or token.
            - platform: Platform to generate script for (windows or linux).

            Returns:
            - 'done' if successful.
            - 'FileName Found' if filename already exists.
            - 'Platform Not Supported' if platform is not windows or linux.
            - Error message if unsuccessful.
            """
            platforms = ["windows", "linux"]
            
            if platform in platforms:
                if platform == "windows":
                    filename += ".bat"
                    file_data = (
                        "set TWINE_USERNAME=__token__\n"
                        f"set TWINE_PASSWORD={pypi_api} /n"
                        "python setup.py sdist bdist_wheel\n"
                        "set TWINE_USERNAME=%TWINE_USERNAME% "
                        "set TWINE_PASSWORD=%TWINE_PASSWORD% "
                        "twine upload dist/*"
                    )
                elif platform == "linux":
                    filename += ".sh"
                    file_data = (
                        'export TWINE_USERNAME="__token__"\n'
                        f'export TWINE_PASSWORD="{pypi_api}"\n'
                        'python setup.py sdist bdist_wheel\n'
                        'TWINE_USERNAME="$TWINE_USERNAME" '
                        'TWINE_PASSWORD="$TWINE_PASSWORD" '
                        'twine upload dist/*'
                    )
                
                if os.path.exists(filename):
                    return 'FileName Found'
                
                try:
                    with open(filename, "w") as f:
                        f.write(file_data)
                    return 'done'
                except Exception as e:
                    return str(e)
            else:
                return 'Platform Not Supported'



class Websites:
       
    @staticmethod
    def open_website(url=""):
        """
        Opens a website in the default web browser.

        Args:
        - url: The URL of the website to open.

        Returns:
        - 'opened' if successful.
        - Error message if unsuccessful.
        """
        try:
            webbrowser.open(url)
            return "opened"
        except Exception as e:
            print("An error occurred:", e)
            return "An error occurred:", e

class Audios:
    
    @staticmethod
    def play_audio(pro_path="", mp3_file_path=""):
        """
        Plays an audio file using a specified program.

        Args:
        - pro_path: Path to the program to use for playing the audio.
        - mp3_file_path: Path to the MP3 file to play.

        Returns:
        - 'opened' if successful.
        - 'Not Found File' if the file does not exist.
        """
        if os.path.exists(mp3_file_path):
            subprocess.Popen([pro_path, mp3_file_path])
            return "opened"
        else:
            return "Not Found File"
        
    @staticmethod
    def play_sound(filename="tts.mp3"):
        """
        Plays a sound file using pygame.

        Args:
        - filename: Path to the sound file (MP3).

        Returns:
        - 'played' if successful.
        """
        pygame.mixer.init()
        sound = pygame.mixer.Sound(filename)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)
        sound.stop()
        return "played"

    @staticmethod
    def play_audio_online(pro_path="", mp3_file_link=""):
        """
        Plays an online audio file using a specified program.

        Args:
        - pro_path: Path to the program to use for playing the audio.
        - mp3_file_link: URL or link to the MP3 file to play.

        Returns:
        - 'opened' if successful.
        """
        subprocess.Popen([pro_path, mp3_file_link])
        return "opened"
        
    @staticmethod
    def record_audio(filename="recorder.wav", duration=5, fs=44100, device_number=None):
        """
        Records audio using the default or specified audio device.

        Args:
        - filename: Name of the WAV file to save the recorded audio.
        - duration: Duration of the recording in seconds.
        - fs: Sampling frequency (default: 44100).
        - device_number: Optional device number to record from.

        Returns:
        - 'saved' if successful.
        - Error message if unsuccessful.
        """
        if device_number is not None:
            sd.default.device = device_number
        try:
            audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
            sd.wait()
            with wave.open(filename, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(fs)
                wf.writeframes(audio_data.tobytes())
            return "saved"
        except Exception as e:
            print("An error occurred:", e)
            return "An error occurred:", e
        
    @staticmethod
    def transcribe_audio(filename="recorder.wav", language_="en-US"):
        """
        Transcribes audio from a WAV file using Google Speech Recognition.

        Args:
        - filename: Path to the WAV file to transcribe.
        - language_: Language code for the language spoken (default: 'en-US').

        Returns:
        - Transcribed text if successful.
        - Empty string if no speech detected or unrecognized.
        - Error message if unsuccessful.
        """
        recognizer = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)
            try:
                query = recognizer.recognize_google(audio, language=language_)
                return query
            except sr.UnknownValueError:
                return ""
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return f"Could not request results; {e}"
            
    @staticmethod
    def stop_recording():
        """
        Stops recording audio by terminating PyAudio instances.
        """
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            p.terminate()
            
    @staticmethod
    def text_to_speech(text="", filename="tts.mp3", language='en'):
        """
        Converts text to speech and saves it as an MP3 file using gTTS.

        Args:
        - text: Text to convert to speech.
        - filename: Name of the output MP3 file.
        - language: Language code for the language spoken (default: 'en').

        Returns:
        - 'saved' if successful.
        """
        tts = gTTS(text, lang=language)
        tts.save(filename)
        return "saved"

class System:
        
    @staticmethod
    def hibernate():
        """
        Hibernate the system.

        Raises:
        - NotImplementedError: If the OS is not supported (only Windows is supported).
        """
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /h")
        else:
            raise NotImplementedError("Unsupported OS")

    @staticmethod
    def restart():
        """
        Restart the system.

        Raises:
        - NotImplementedError: If the OS is not supported (only Windows is supported).
        """
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /r /t 1")
        else:
            raise NotImplementedError("Unsupported OS")

    @staticmethod
    def shutdown():
        """
        Shutdown the system.

        Raises:
        - NotImplementedError: If the OS is not supported (Windows, Linux, and macOS are supported).
        """
        system = platform.system()
        if system == "Windows":
            subprocess.run(["shutdown", "/s", "/t", "1"])
        elif system == "Linux" or system == "Darwin":
            subprocess.run(["sudo", "shutdown", "-h", "now"])
        else:
            raise NotImplementedError("Unsupported OS")
        
    @staticmethod
    def log_off():
        """
        Log off the current user.

        Raises:
        - NotImplementedError: If the OS is not supported (only Windows is supported).
        """
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /l")
        else:
            raise NotImplementedError("Unsupported OS")

class Crypto:

    @staticmethod
    def token_information(data: Any = "", type: str = 'binance') -> str:
        """
        Opens a web browser with token information based on the type.

        Args:
        - data (Any): Token identifier or data.
        - type (str): Type of token platform ('binance', 'etherum', 'geckoterminal').

        Returns:
        - str: Message indicating if the operation was successful or unsupported type.
        """
        if type == 'binance':
            link = "https://bscscan.com/token/" + str(data)
            Websites.open_website(link)
            return "opened"
        elif type == 'etherum':
            link = "https://etherscan.io/token/" + str(data)
            Websites.open_website(link)
            return "opened"
        elif type == 'geckoterminal':
            link = 'https://ywp.freewebhostmost.com/really/token.php?pool=' + str(data)
            Websites.open_website(link)
            return "opened"
        else:
            return "Unsupported type"

class AI:

    class Builder:

        def __init__(self):
            self.intents = []

        def json_creator(self, jsonfile: str = "intents.json", tag: str = "", patterns: list = [], responses: list = []) -> None:
            """
            Creates or appends intents to a JSON file.

            Args:
            - jsonfile (str): Path to the JSON file.
            - tag (str): Tag name for the intent.
            - patterns (list): List of patterns or queries.
            - responses (list): List of responses corresponding to the patterns.

            Returns:
            - None
            """
            intents = self.intents

            intents.append({
                "tag": tag,
                "patterns": patterns,
                "responses": responses
            })

            with open(jsonfile, 'w', encoding='utf-8') as f:
                json.dump({"intents": intents}, f, indent=4, ensure_ascii=False)

        def train(self, jsonfile: str = "intents.json", picklefile: str = "data.pickle", h5file: str = "model.h5") -> str:
            """
            Trains an AI model using intents JSON file and saves the model.

            Args:
            - jsonfile (str): Path to the intents JSON file.
            - picklefile (str): Path to save/load the pickle data.
            - h5file (str): Path to save/load the trained model weights.

            Returns:
            - str: Message indicating the training status.
            """
            nltk.download('punkt')
            stemmer = LancasterStemmer()

            try:
                with open(jsonfile, encoding='utf-8') as file:
                    data = json.load(file)
            except:
                return 'error:jsonnotfound'

            try:
                with open(picklefile, "rb") as f:
                    words, labels, training, output = pickle.load(f)
            except:
                words = []
                labels = []
                docs_x = []
                docs_y = []
                for intent in data["intents"]:
                    for pattern in intent["patterns"]:
                        wrds = nltk.word_tokenize(pattern)
                        words.extend(wrds)
                        docs_x.append(wrds)
                        docs_y.append(intent["tag"])

                    if intent["tag"] not in labels:
                        labels.append(intent["tag"])

                words = [stemmer.stem(w.lower()) for w in words if w != "?"]
                words = sorted(list(set(words)))

                labels = sorted(labels)

                training = []
                output = []

                out_empty = [0 for _ in range(len(labels))]

                for x, doc in enumerate(docs_x):
                    bag = []

                    wrds = [stemmer.stem(w) for w in doc]

                    for w in words:
                        if w in wrds:
                            bag.append(1)
                        else:
                            bag.append(0)

                    output_row = out_empty[:]
                    output_row[labels.index(docs_y[x])] = 1

                    training.append(bag)
                    output.append(output_row)

                training = np.array(training)
                output = np.array(output)

                with open(picklefile, "wb") as f:
                    pickle.dump((words, labels, training, output), f)

            model = Sequential()
            model.add(Dense(8, input_shape=(len(training[0]),), activation='relu'))
            model.add(Dense(8, activation='relu'))
            model.add(Dense(len(output[0]), activation='softmax'))

            model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

            try:
                model.load_weights(h5file)
            except:
                model.fit(training, output, epochs=1000, batch_size=8, verbose=1)
                model.save(h5file)

            return 'done'

        @staticmethod
        def bag_of_words(s: str, words: list) -> np.ndarray:
            """
            Converts a sentence into a bag of words format.

            Args:
            - s (str): Sentence or message to convert.
            - words (list): List of words to match against.

            Returns:
            - np.ndarray: Bag of words representation of the sentence.
            """
            stemmer = LancasterStemmer()

            bag = [0 for _ in range(len(words))]

            s_words = nltk.word_tokenize(s)
            s_words = [stemmer.stem(word.lower()) for word in s_words]

            for se in s_words:
                for i, w in enumerate(words):
                    if w == se:
                        bag[i] = 1

            return np.array(bag)

        def process(self, message: str = "", picklefile: str = "data.pickle", h5file: str = "model.h5", jsonfile: str = "intents.json", sleeptime: int = 0) -> str:
            """
            Processes a message using the trained AI model and returns a response.

            Args:
            - message (str): Input message to process.
            - picklefile (str): Path to the pickle file containing training data.
            - h5file (str): Path to the trained model weights.
            - jsonfile (str): Path to the intents JSON file.
            - sleeptime (int): Optional sleep time before returning a response.

            Returns:
            - str: AI response based on the input message.
            """
            nltk.download('punkt')
            stemmer = LancasterStemmer()

            try:
                with open(jsonfile, encoding='utf-8') as file:
                    data = json.load(file)
            except:
                return 'error:jsonnotfound'

            try:
                with open(picklefile, "rb") as f:
                    words, labels, training, output = pickle.load(f)
            except:
                return 'error:picklenotfound'

            model = Sequential()
            model.add(Dense(8, input_shape=(len(training[0]),), activation='relu'))
            model.add(Dense(8, activation='relu'))
            model.add(Dense(len(output[0]), activation='softmax'))

            model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

            try:
                model.load_weights(h5file)
            except:
                return 'h5notfound'

            bag = self.bag_of_words(message, words)
            results = model.predict(np.array([bag]))[0]
            results_index = np.argmax(results)
            tag = labels[results_index]
            if results[results_index] > 0.8:
                for tg in data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']
                sleep(sleeptime)
                Bot = random.choice(responses)
                return Bot
            else:
                return "I don't understand!"

class inuser:
    class Audios:
        def play_sound_inuser():
            filename = input("Enter FileName: ")
            return Audios.play_sound(filename)
        
        def play_audio_inuser():
            pro_path = input("Enter Program Path: ")
            mp3_file_path = input("Enter MP3 File Path: ")
            return Audios.play_audio(pro_path, mp3_file_path)
            
        def record_audio_inuser():
            filename = input("Enter FileName [recorder.wav]: ")
            if filename == "":
                filename = "recorder.wav"
            return Audios.record_audio(filename)
        
        def transcribe_audio_inuser():
            filename = input("Enter FileName [recorder.wav]: ")
            if filename == "":
                filename = "recorder.wav"
            return Audios.transcribe_audio(filename)
                
        def text_to_speech_inuser():
            text = input("Enter Text: ")
            filename = input("Enter FileName [tts.mp3]: ")
            if filename == "":
                filename = "tts.mp3"
            return Audios.text_to_speech(text, filename)
        
        def text_to_speech_offline_inuser():
            text = input("Enter Text: ")
            filename = input("Enter FileName [tts.mp3]: ")
            if filename == "":
                filename = "tts.mp3"
            engine = pyttsx3.init()
            engine.save_to_file(text, filename)
            engine.runAndWait()
            return "saved"
        
        def play_audio_online_inuser():
            pro_path = input("Enter Program Path: ")
            mp3_file_link = input("Enter MP3 File Link: ")
            subprocess.Popen([pro_path, mp3_file_link])
            return "opened"
        
    class Files:
        def create_file_inuser():
            name = input("Enter FileName: ")
            return Files.create_file(name)
            
        def open_file_inuser():
            filepath = input("Enter FilePath: ")
            return Files.open_file(filepath)
            
        def delete_all_files_inuser():
            directory = input("Enter Directory/Folder [.]: ")
            if directory == "":
                directory = "."
            type = input("Enter Type: ")
            return Files.delete_all_files(directory, type)
                        
        def delete_file_inuser():
            filepath = input("Enter FilePath: ")
            return Files.delete_file(filepath)
                        
    class Websites:
       
        def open_website_inuser():
            url = input("Enter URL: ")
            return Websites.open_website(url)
            
    class Crypto:

        def token_information_inuser():
            data = input("Enter Data: ")
            type = input("Enter Type [binance]: ")
            if type == "":
                type = "binance"
            return Crypto.token_information(data, type)
            
    class server:

        def __init__(self):
            self.app = None

        def route_flask_inuser(self):
            location = input("Enter Location [.]: ")
            if location == "":
                location = "."
            returnValue = input("Enter returnValue: ")

            app = self.app
            try:
                if app is None:
                    app = Flask(__name__)

                def make_route(return_value):
                    def route():
                        return return_value
                    return route

                endpoint = location.strip('/')
                if endpoint == '':
                    endpoint = 'index'

                app.add_url_rule(location, endpoint, make_route(returnValue))
                self.app = app
                return 'done'
            except Exception as error:
                raise error
            
        def run_inuser(self):
            check = input("Enter check [False]: ")
            if check == "":
                check = False
            else:
                check = bool(check)
            debug = input("Enter Debug [True]: ")
            if debug == "":
                debug = True
            else:
                debug = bool(debug)
            host = input("Enter Host [0.0.0.0]: ")
            if host == "":
                host = "0.0.0.0"
            port = input("Enter Port [8000]: ")
            if port == "":
                port = "8000"
            
            app = self.app
            try:
                if app is None:
                    raise Exception("App not initialized")
                
                if check:
                    if __name__ == "__main__":
                        app.run(debug=debug, host=host, port=port)
                else:
                    app.run(debug=debug, host=host, port=port)
                return 'done'
            except Exception as error:
                raise error
            
    class AI:
        class Builder:
            def __init__(self):
                self.intents = []
                
            def json_creator_inuser(self):
                jsonfile = input("Enter JsonFile Name/Path [intents.json]: ")
                if jsonfile == "":
                    jsonfile = "intents.json"
                tag = input("Enter tag: ")
                patterns = input("Enter Patterns (,): ").split(",")
                responses = input("Enter Responses (,): ").split(",")
                intents = self.intents

                intents.append({
                    "tag": tag,
                    "patterns": patterns,
                    "responses": responses
                })

                with open(jsonfile, 'w', encoding='utf-8') as f:
                    json.dump({"intents": intents}, f, indent=4, ensure_ascii=False)

            def train_inuser(self):
                jsonfile = input("Enter JsonFile Name/Path [intents.json]: ")
                if jsonfile == "":
                    jsonfile = "intents.json"
                picklefile = input("Enter PickleFile Name/Path [data.pickle]: ")
                if picklefile == "":
                    picklefile = "data.pickle"
                h5file = input("Enter H5File Name/Path [model.h5]: ")
                if h5file == "":
                    h5file = "model.h5"

                nltk.download('punkt')
                stemmer = LancasterStemmer()

                try:
                    with open(jsonfile, encoding='utf-8') as file:
                        data = json.load(file)
                except:
                    return 'error:jsonnotfound'

                try:
                    with open(picklefile, "rb") as f:
                        words, labels, training, output = pickle.load(f)
                except:
                    words = []
                    labels = []
                    docs_x = []
                    docs_y = []
                    for intent in data["intents"]:
                        for pattern in intent["patterns"]:
                            wrds = nltk.word_tokenize(pattern)
                            words.extend(wrds)
                            docs_x.append(wrds)
                            docs_y.append(intent["tag"])

                        if intent["tag"] not in labels:
                            labels.append(intent["tag"])

                    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
                    words = sorted(list(set(words)))

                    labels = sorted(labels)

                    training = []
                    output = []

                    out_empty = [0 for _ in range(len(labels))]

                    for x, doc in enumerate(docs_x):
                        bag = []

                        wrds = [stemmer.stem(w) for w in doc]

                        for w in words:
                            if w in wrds:
                                bag.append(1)
                            else:
                                bag.append(0)

                        output_row = out_empty[:]
                        output_row[labels.index(docs_y[x])] = 1

                        training.append(bag)
                        output.append(output_row)

                    training = np.array(training)
                    output = np.array(output)

                    with open(picklefile, "wb") as f:
                        pickle.dump((words, labels, training, output), f)

                model = Sequential()
                model.add(Dense(8, input_shape=(len(training[0]),), activation='relu'))
                model.add(Dense(8, activation='relu'))
                model.add(Dense(len(output[0]), activation='softmax'))

                model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

                try:
                    model.load_weights(h5file)
                except:
                    model.fit(training, output, epochs=1000, batch_size=8, verbose=1)
                    model.save(h5file)

                return 'done'

            def process_inuser(self):
                message = input("Enter Message: ")
                picklefile = input("Enter PickleFile Name/Path [data.pickle]: ")
                if picklefile == "":
                    picklefile = "data.pickle"
                h5file = input("Enter H5File Name/Path [model.h5]: ")
                if h5file == "":
                    h5file = "model.h5"
                jsonfile = input("Enter JsonFile Name/Path [intents.json]: ")
                if jsonfile == "":
                    jsonfile = "intents.json"
                sleeptime = input("Enter Sleep Time [0]: ")
                if sleeptime == "":
                    sleeptime = 0
                else:
                    sleeptime = int(sleeptime)
                    
                nltk.download('punkt')
                stemmer = LancasterStemmer()

                try:
                    with open(jsonfile, encoding='utf-8') as file:
                        data = json.load(file)
                except:
                    return 'error:jsonnotfound'

                try:
                    with open(picklefile, "rb") as f:
                        words, labels, training, output = pickle.load(f)
                except:
                    return 'error:picklenotfound'

                model = Sequential()
                model.add(Dense(8, input_shape=(len(training[0]),), activation='relu'))
                model.add(Dense(8, activation='relu'))
                model.add(Dense(len(output[0]), activation='softmax'))

                model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

                try:
                    model.load_weights(h5file)
                except:
                    return 'h5notfound'

                ai = AI.Builder()
                bag = ai.bag_of_words(message, words)
                results = model.predict(np.array([bag]))[0]
                results_index = np.argmax(results)
                tag = labels[results_index]
                if results[results_index] > 0.8:
                    for tg in data["intents"]:
                        if tg['tag'] == tag:
                            responses = tg['responses']
                    sleep(sleeptime)
                    Bot = random.choice(responses)
                    return Bot
                else:
                    return "I don't understand!"
    
    class VideosCreator:
    
        class Basic:
            
            def basic_video_creator_inuser():
                image_folder = input("Enter Image Folder Name/Path [images]: ")
                if image_folder == "":
                    image_folder = "images"
                animation_choice = input("Enter Animation [None]: ")
                if animation_choice == "":
                    animation_choice = "None"
                frame_rate = input("Enter Frame Rate [25]: ")
                if frame_rate == "":
                    frame_rate = 25
                else:
                    frame_rate = int(frame_rate)
                video_name = input("Enter Video Name: ")
                video_type = input("Enter Video Type [mp4]: ")
                if video_type == "":
                    video_type = "mp4"
                video_platform = input("Enter Video Platform [Youtube]: ")
                if video_platform == "":
                    video_platform = "Youtube"
                image_time = input("Enter Image Time [5]: ")
                if image_time == "":
                    image_time = 5
                else:
                    image_time = int(image_time)
                return VideosCreator.Basic.basic_video_creator(image_folder, animation_choice, frame_rate, video_name, video_type, video_platform, image_time)
            
    class endecrypt:

        class aes:
            def encrypt_inuser():
                file_path = input("Enter File Path: ")
                password = input("Enter Password: ")
                
                return endecrypt.aes.encrypt(file_path, password)

            def decrypt_inuser():
                file_path = input("Enter File Path: ")
                password = input("Enter Password: ")
                
                return endecrypt.aes.decrypt(file_path, password)

        class BlowFish:
            def encrypt_inuser():
                file_path = input("Enter File Path: ")
                password = input("Enter Password: ")
                
                return endecrypt.BlowFish.encrypt(file_path, password)

            def decrypt_inuser():
                file_path = input("Enter File Path: ")
                password = input("Enter Password: ")
                
                return endecrypt.BlowFish.decrypt(file_path, password)

        class Base64:
            def encrypt_inuser():
                file_path = input("Enter File Path: ")
                
                return endecrypt.Base64.encrypt(file_path)
                
            def decrypt_inuser():
                file_path = input("Enter File Path: ")
                
                return endecrypt.Base64.decrypt(file_path)
                
        class Hex:
            def encrypt_inuser():
                file_path = input("Enter File Path: ")
                
                return endecrypt.Hex.encrypt(file_path)
                
            def decrypt_inuser():
                file_path = input("Enter File Path: ")
                
                return endecrypt.Hex.decrypt(file_path)
                
    class Libraries:
    
        class Basic:
            def init_creator_inuser():
                filesave = input("Enter File Save [__init__.py]: ")
                if filesave == "":
                    filesave = "__init__.py"
                filename = input("Enter File Name: ")
                function_class = input("Enter Function/Class Name: ")
                
                return Libraries.Basic.init_creator(filesave, filename, function_class)
                    
            def basic_setup_file_creator_inuser():
                filename = input("Enter File Name [setup.py]: ")
                if filename == "":
                    filename = "setup.py"
                folder_name = input("Enter Folder Name: ")
                readme_name = input("Enter Read Me File Name [README.md]: ")
                if readme_name == "":
                    readme_name = "README.md"
                library_name = input("Enter Library Name: ")
                library_version = input("Enter Library Version: ")
                libraries_required = input("Enter Libraries Required (,): ").split(",")
                description = input("Enter Description: ")
                creator_name = input("Enter Creator Name: ")
                creator_email = input("Enter Creator Email: ")
                License = input("Enter License [MIT]: ")
                if License == "":
                    License = "MIT"
                else:
                    return 'Not From Licenses'
                
                return Libraries.Basic.basic_setup_file_creator(filename, folder_name, readme_name, library_name, library_version, libraries_required, description, creator_name, creator_email, License)
                        
            def upload_file_creator_inuser():
                filename = input("Enter File Name [upload_library]: ")
                if filename == "":
                    filename = "upload_library"
                pypi_api = input("Enter PyPi API: ")
                platform = input("Enter Platform: ")
                
                return Libraries.Basic.upload_file_creator(filename, pypi_api, platform)
    
    def install_system_packages():
        system = platform.system()
        
        if system == 'Linux':
            command = 'sudo apt-get update && sudo apt-get install -y portaudio19-dev python3-pyaudio libasound2-dev libportaudio2 libportaudiocpp0'
        elif system == 'Darwin':
            command = 'brew install portaudio'
        elif system == 'Windows':
            command = f'{sys.executable} -m pip install pipwin && {sys.executable} -m pipwin install pyaudio'
        else:
            return "Unsupported OS"
        
        inuser.run_command(command)
        return "Done"

    def install_library_packages():
        libraries=[
            "dill==0.3.8",
            "flask==3.0.3",
            "flask-cors==4.0.1",
            "gtts==2.5.1",
            "joblib==1.4.2",
            "moviepy==1.0.3",
            "nltk==3.8.1",
            "pyaudio==0.2.14",
            "pygame==2.5.2",
            "selenium==4.22.0",
            "setuptools==68.1.2",
            "sounddevice==0.4.7",
            "SpeechRecognition==3.10.4",
            "tensorflow==2.16.1",
            "tflearn==0.5.0",
            "twine==5.1.0",
            "wheel==0.43.0",
            "pycryptodome==3.20.0",
            "vosk==0.3.45",
            "tqdm==4.66.4",
            "pyttsx3==2.90",
            "requests==2.31.0",
            "googletrans==4.0.0rc1",
            "cryptography==42.0.5",
            "scapy==2.5.0+git20240324.2b58b51",
            "python-nmap==0.7.1",
            "yara-python==4.5.1",
        ]

        command = "pip install "
        for library in libraries:
            command += str(library) + " "
        inuser.run_command(command)
        
        return 'Done'

    def upgrade_required_libraries():
        libraries=[
            "dill",
            "flask",
            "flask-cors",
            "gtts",
            "joblib",
            "moviepy",
            "nltk",
            "pyaudio",
            "pygame",
            "selenium",
            "setuptools",
            "sounddevice",
            "SpeechRecognition",
            "tensorflow",
            "tflearn",
            "twine",
            "wheel",
            "pycryptodome",
            "vosk",
            "tqdm",
            "pyttsx3",
            "requests",
            "googletrans",
            "cryptography",
            "scapy",
            "python-nmap",
            "yara-python",
        ]
        
        command = "pip install --upgrade "
        for library in libraries:
            command += library + " "
        inuser.run_command(command)
        
        return 'Done'

    def upgrade_library():
        command = "pip install --upgrade YWP"
        inuser.run_command(command)
        
        return 'Done'

    def get_terminal_command():
        if sys.platform.startswith('win'):
            return "cmd.exe"
        elif sys.platform.startswith('linux'):
            terminals = ["gnome-terminal", "xterm", "konsole", "xfce4-terminal", "lxterminal", "terminator", "tilix", "mate-terminal"]
            available_terminals = [term for term in terminals if os.system(f"which {term} > /dev/null 2>&1") == 0]
            if available_terminals:
                return available_terminals[0]
            else:
                return None
        elif sys.platform.startswith('darwin'):
            return "Terminal"
        else:
            return None

    def run_command(command):
        terminal = inuser.get_terminal_command()
        if terminal:
            if terminal == "cmd.exe":
                os.system(f'start cmd /c "{command}"')
            elif terminal in ["gnome-terminal", "terminator", "tilix"]:
                os.system(f"{terminal} -- bash -c '{command}; read -p \"Press Enter to close...\"'")
            elif terminal == "konsole":
                os.system(f"{terminal} -e 'bash -c \"{command}; read -p \\\"Press Enter to close...\\\"\"'")
            elif terminal == "Terminal":
                os.system(f"open -a {terminal} '{command}'")
            else:
                os.system(f"{terminal} -hold -e 'bash -c \"{command}; read -p \\\"Press Enter to close...\\\"\"'")
        else:
            return "No supported terminal found."

    def install_packages_linux_inuser():
        system = platform.system()
        
        if system == 'Linux':
            command = 'sudo apt-get update && sudo apt-get install -y portaudio19-dev python3-pyaudio libasound2-dev libportaudio2 libportaudiocpp0'
        elif system == 'Darwin':
            command = 'brew install portaudio'
        elif system == 'Windows':
            command = f'{sys.executable} -m pip install pipwin && {sys.executable} -m pipwin install pyaudio'
        else:
            return "Unsupported OS"
        
        inuser.run_command(command)
        return "Done"

    def install_libraries_inuser():
        libraries=[
            "dill==0.3.8",
            "flask==3.0.3",
            "flask-cors==4.0.1",
            "gtts==2.5.1",
            "joblib==1.4.2",
            "moviepy==1.0.3",
            "nltk==3.8.1",
            "pyaudio==0.2.14",
            "pygame==2.5.2",
            "selenium==4.22.0",
            "setuptools==68.1.2",
            "sounddevice==0.4.7",
            "SpeechRecognition==3.10.4",
            "tensorflow==2.16.1",
            "tflearn==0.5.0",
            "twine==5.1.0",
            "wheel==0.43.0",
            "pycryptodome==3.20.0",
            "vosk==0.3.45",
            "tqdm==4.66.4",
            "pyttsx3==2.90",
            "requests==2.31.0",
            "googletrans==4.0.0rc1",
            "cryptography==42.0.5",
            "scapy==2.5.0+git20240324.2b58b51",
            "python-nmap==0.7.1",
            "yara-python==4.5.1",
        ]

        command = "pip install --upgrade "
        for library in libraries:
            command += str(library) + " "
        inuser.run_command(command)
        
        return 'Done'

    def upgrade_libraries_inuser():
        libraries=[
            "dill",
            "flask",
            "flask-cors",
            "gtts",
            "joblib",
            "moviepy",
            "nltk",
            "pyaudio",
            "pygame",
            "selenium",
            "setuptools",
            "sounddevice",
            "SpeechRecognition",
            "tensorflow",
            "tflearn",
            "twine",
            "wheel",
            "pycryptodome",
            "vosk",
            "tqdm",
            "pyttsx3",
            "requests",
            "googletrans",
            "cryptography",
            "scapy",
            "python-nmap",
            "yara-python",
        ]
        
        command = "pip install --upgrade "
        for library in libraries:
            command += library + " "
        inuser.run_command(command)
        
        return 'Done'

    def upgrade_library_inuser():
        command = "pip install --upgrade YWP"
        inuser.run_command(command)
        
        return 'Done'
    
    class printstyle:
        def print_one_inuser():
            
            text = input("Enter Text: ")
            second = input("Enter Second [0.05]: ")
            if second == "":
                second = 0.05
            else:
                second = float(second)
            
            if len(text) == 0:
                raise ZeroDivisionError
            
            for line in text + '\n':
                stdout.write(line)
                stdout.flush()
                sleep(second)
            
        def print_all_inuser():
            
            text = input("Enter Text: ")
            total_time = input("Enter Total Time [5]: ")
            if total_time == "":
                total_time = 5
            else:
                total_time = float(total_time)
            
            # حساب الوقت الفاصل بين كل حرف
            if len(text) == 0:
                raise ZeroDivisionError
            else:
                interval = total_time / len(text)
            
            # طباعة النص حرفًا بحرف
            for char in text:
                stdout.write(char)
                stdout.flush()
                sleep(interval)
            
            # طباعة سطر جديد بعد انتهاء النص
            stdout.write('\n')
            stdout.flush()

class printstyle:
    def print_one(text, second=0.05):
        """This is For Custom Print for Letter

        Args:
            text (str): this is Sentence
            second (float, optional): this is Seconds For Letter. Defaults to 0.05.

        Raises:
            ZeroDivisionError
        """
        
        if len(text) == 0:
            raise ZeroDivisionError
        
        for line in text + '\n':
            stdout.write(line)
            stdout.flush()
            sleep(second)
	    
    def print_all(text, total_time=5):
        """This is For Custom Print for Sentence

        Args:
            text (_type_): This is Sentence
            total_time (float, optional): This is Seconds For Sentence. Defaults to 5.

        Raises:
            ZeroDivisionError
        """
        
        # حساب الوقت الفاصل بين كل حرف
        if len(text) == 0:
            raise ZeroDivisionError
        else:
            interval = total_time / len(text)
        
        # طباعة النص حرفًا بحرف
        for char in text:
            stdout.write(char)
            stdout.flush()
            sleep(interval)
        
        # طباعة سطر جديد بعد انتهاء النص
        stdout.write('\n')
        stdout.flush()
    
    class Translate:
        def translate_text_inuser():
            text = input("Enter Text: ")
            to_lan = input("Enter To Language [en]: ")
            if to_lan == "":
                to_lan = "en"
            from_lan = input("Enter From Language [en]: ")
            if from_lan == "":
                from_lan = "en"
            translator = Translator()
            return translator.translate(text, src=from_lan, dest=to_lan).text

def help():
    """This is YWP.help Command in Command Line"""
    print("""Avalable Commands:
1- YWP.install_packages
2- YWP.install_libraries
3- YWP.upgrade_libraries
4- YWP.upgrade_library
5- YWP
6- YWP.help""")

class Translate:
    def translate_text(text: str, to_lan="en", from_lan="en"):
        """
            This is for Translate text to any language

            Args:
                text (str)
                to_lan (str): To Language. Defaults to "en".
                from_lan (str, optional): From Language. Defaults to "en".

            Returns:
                str: Translated Text
        """
        translator = Translator()
        return translator.translate(text, src=from_lan, dest=to_lan).text

class ScanSec:
    """Class containing various cybersecurity functions."""
    
    class NmapNetwork:
        """Class for network scanning using Nmap."""

        @staticmethod
        def scan_network(ip):
            """
            Scans a network for open ports and services on a given IP address.
            
            Args:
                ip (str): The IP address to scan.
                
            Summary:
                Uses Nmap to scan the given IP address for open ports and displays
                the protocol and state of each port.
            """
            nm = nmap.PortScanner()
            nm.scan(ip, '1-1024')
            for host in nm.all_hosts():
                print(f'Host: {host} ({nm[host].hostname()})')
                for proto in nm[host].all_protocols():
                    print(f'Protocol: {proto}')
                    lport = nm[host][proto].keys()
                    for port in lport:
                        print(f'Port: {port}\tState: {nm[host][proto][port]["state"]}')
                
    class Fernet:
        """Class for encryption and decryption using Fernet symmetric encryption."""

        @staticmethod
        def generate_key():
            """
            Generates a new Fernet key.
            
            Returns:
                bytes: The generated key.
                
            Summary:
                Generates and returns a new key for Fernet encryption.
            """
            return CryptographyFernet.generate_key()

        @staticmethod
        def encrypt_message(key, message):
            """
            Encrypts a message using the provided Fernet key.
            
            Args:
                key (bytes): The Fernet key.
                message (str): The message to encrypt.
                
            Returns:
                bytes: The encrypted message.
                
            Summary:
                Encrypts a given message using the specified Fernet key and returns
                the encrypted message.
            """
            f = CryptographyFernet(key)
            return f.encrypt(message.encode())

        @staticmethod
        def decrypt_message(key, encrypted_message):
            """
            Decrypts an encrypted message using the provided Fernet key.
            
            Args:
                key (bytes): The Fernet key.
                encrypted_message (bytes): The message to decrypt.
                
            Returns:
                str: The decrypted message.
                
            Summary:
                Decrypts a given encrypted message using the specified Fernet key and returns
                the decrypted message.
            """
            f = CryptographyFernet(key)
            return f.decrypt(encrypted_message).decode()
    
    class HashLib:
        """Class for password hashing and verification using SHA-256."""

        @staticmethod
        def hash_password(password):
            """
            Hashes a password using SHA-256.
            
            Args:
                password (str): The password to hash.
                
            Returns:
                str: The hashed password.
                
            Summary:
                Hashes a given password using SHA-256 and returns the hashed password.
            """
            return hashlib.sha256(password.encode()).hexdigest()

        @staticmethod
        def verify_password(stored_password, provided_password):
            """
            Verifies a password against the stored hashed password.
            
            Args:
                stored_password (str): The stored hashed password.
                provided_password (str): The password to verify.
                
            Returns:
                bool: True if the password matches, False otherwise.
                
            Summary:
                Verifies a provided password by hashing it with SHA-256 and comparing
                it to the stored hashed password.
            """
            return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()
        
    class Logging:
        """Class for setting up a logger to create and manage log files."""

        @staticmethod
        def setup_logger(log_file):
            """
            Sets up a logger to log messages to a specified log file.
            
            Args:
                log_file (str): The path to the log file.
                
            Returns:
                logging.Logger: The configured logger.
                
            Summary:
                Configures and returns a logger that logs messages to the specified log file.
            """
            logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
            logger = logging.getLogger()
            return logger
        
    class Yara:
        """Class for scanning files using Yara rules."""

        @staticmethod
        def scan_file(rule_path, file_path):
            """
            Scans a file for matches against Yara rules.
            
            Args:
                rule_path (str): The path to the Yara rule file.
                file_path (str): The path to the file to scan.
                
            Returns:
                list: A list of matches found in the file.
                
            Summary:
                Compiles Yara rules from the specified rule file and scans the given file
                for matches, returning a list of found matches.
            """
            rules = yara.compile(filepath=rule_path)
            matches = rules.match(file_path)
            return matches

    class BruteForce:
        """Class for performing brute force attacks to crack passwords."""

        @staticmethod
        def brute_force_crack(password_set, target_password):
            """
            Attempts to crack a password using brute force.
            
            Args:
                password_set (str): The set of characters to use for brute force.
                target_password (str): The password to crack.
            
            Returns:
                str: The cracked password if found, else None.
            
            Summary:
                Uses brute force to attempt cracking the target password by generating
                all possible combinations from the provided character set.
            """
            for length in range(1, 6):
                for guess in itertools.product(password_set, repeat=length):
                    guess = ''.join(guess)
                    if guess == target_password:
                        return guess
            return None

    class PortScanner:
        """Class for scanning open ports on a host."""

        @staticmethod
        def scan_ports(host, start_port, end_port):
            """
            Scans open ports on a given host.
            
            Args:
                host (str): The host to scan.
                start_port (int): The starting port number.
                end_port (int): The ending port number.
            
            Returns:
                list: List of open ports.
            
            Summary:
                Scans the specified range of ports on the given host and returns a list
                of open ports.
            """
            open_ports = []
            for port in range(start_port, end_port + 1):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            return open_ports

    class SQLInjectionTester:
        """Class for testing SQL injection vulnerabilities."""

        @staticmethod
        def test_sql_injection(url, payload):
            """
            Tests for SQL injection vulnerability.
            
            Args:
                url (str): The URL to test.
                payload (str): The SQL payload to use.
            
            Returns:
                bool: True if vulnerable, else False.
            
            Summary:
                Tests the given URL for SQL injection vulnerability using the provided
                SQL payload and returns whether the site is vulnerable.
            """
            response = requests.get(url + payload)
            return "syntax error" in response.text or "SQL" in response.text

    class XSSTester:
        """Class for testing cross-site scripting (XSS) vulnerabilities."""

        @staticmethod
        def test_xss(url, payload):
            """
            Tests for XSS vulnerability.
            
            Args:
                url (str): The URL to test.
                payload (str): The XSS payload to use.
            
            Returns:
                bool: True if vulnerable, else False.
            
            Summary:
                Tests the given URL for XSS vulnerability using the provided payload
                and returns whether the site is vulnerable.
            """
            response = requests.get(url, params={'q': payload})
            return payload in response.text

    class CSRFTTester:
        """Class for testing cross-site request forgery (CSRF) vulnerabilities."""

        @staticmethod
        def test_csrf(url, csrf_token, session):
            """
            Tests for CSRF vulnerability.
            
            Args:
                url (str): The URL to test.
                csrf_token (str): The CSRF token.
                session (requests.Session): The session object.
            
            Returns:
                bool: True if vulnerable, else False.
            
            Summary:
                Tests the given URL for CSRF vulnerability using the provided CSRF token
                and session object, and returns whether the site is vulnerable.
            """
            payload = {'csrf_token': csrf_token, 'action': 'test'}
            response = session.post(url, data=payload)
            return response.status_code == 200 and "CSRF" not in response.text

    class TrafficSniffer:
        """Class for sniffing network traffic."""

        @staticmethod
        def sniff_packets(interface, packet_count):
            """
            Sniffs network packets on a given interface.
            
            Args:
                interface (str): The network interface to sniff on.
                packet_count (int): The number of packets to capture.
            
            Returns:
                list: List of captured packets.
            
            Summary:
                Sniffs the specified number of packets on the given network interface
                and returns the captured packets.
            """
            return sniff(iface=interface, count=packet_count, filter="ip")

    class PasswordStrengthChecker:
        """Class for checking the strength of a password."""

        @staticmethod
        def check_password_strength(password):
            """
            Checks the strength of a given password.
            
            Args:
                password (str): The password to check.
            
            Returns:
                str: Strength of the password ("Weak", "Moderate", "Strong").
            
            Summary:
                Analyzes the given password and returns its strength based on length
                and character composition.
            """
            if len(password) < 6:
                return "Weak"
            elif len(password) >= 6 and any(char.isdigit() for char in password):
                return "Moderate"
            elif len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
                return "Strong"
            else:
                return "Weak"

    class FirewallRuleChecker:
        """Class for checking firewall rules."""

        @staticmethod
        def check_firewall_rules():
            """
            Checks the current firewall rules.
            
            Returns:
                str: List of current firewall rules.
            
            Summary:
                Retrieves and returns the current firewall rules configured on the system.
            """
            result = subprocess.run(['sudo', 'iptables', '-L'], stdout=subprocess.PIPE)
            return result.stdout.decode()

    class IPGeolocation:
        """Class for getting geolocation of an IP address."""

        @staticmethod
        def get_geolocation(ip):
            """
            Gets the geolocation of a given IP address.
            
            Args:
                ip (str): The IP address to geolocate.
            
            Returns:
                dict: Geolocation information.
            
            Summary:
                Uses an external service to get and return the geolocation information
                for the specified IP address.
            """
            response = requests.get(f'http://ip-api.com/json/{ip}')
            return response.json()

    class DataExfiltrationDetector:
        """Class for detecting data exfiltration."""

        @staticmethod
        def detect_exfiltration(log_file, threshold=1000):
            """
            Detects potential data exfiltration.
            
            Args:
                log_file (str): The path to the log file.
                threshold (int): The threshold for data transfer in bytes.
            
            Returns:
                bool: True if exfiltration is detected, else False.
            
            Summary:
                Analyzes the specified log file for signs of data exfiltration based on
                the provided threshold and returns whether exfiltration is detected.
            """
            with open(log_file, 'r') as file:
                data_transferred = sum(int(line.split()[1]) for line in file)
            return data_transferred > threshold

    class MalwareAnalyzer:
        """Class for analyzing malware samples."""

        @staticmethod
        def analyze_malware(file_path):
            """
            Analyzes a given malware sample.
            
            Args:
                file_path (str): The path to the malware file.
            
            Returns:
                str: Analysis report.
            
            Summary:
                Analyzes the specified malware sample and returns an analysis report.
            """
            result = subprocess.run(['strings', file_path], stdout=subprocess.PIPE)
            return result.stdout.decode()

    class SocialEngineeringDetector:
        """Class for detecting social engineering attacks."""

        @staticmethod
        def detect_social_engineering(email_content):
            """
            Detects potential social engineering attacks.
            
            Args:
                email_content (str): The content of the email to analyze.
            
            Returns:
                bool: True if a social engineering attack is detected, else False.
            
            Summary:
                Analyzes the specified email content for signs of social engineering
                attacks and returns whether an attack is detected.
            """
            suspicious_keywords = ["urgent", "click here", "immediate action", "confidential"]
            return any(keyword in email_content.lower() for keyword in suspicious_keywords)

    class PhishingURLDetector:
        """Class for detecting phishing URLs."""

        @staticmethod
        def detect_phishing(url):
            """
            Detects if a URL is a phishing attempt.
            
            Args:
                url (str): The URL to check.
            
            Returns:
                bool: True if the URL is a phishing attempt, else False.
            
            Summary:
                Analyzes the specified URL to determine if it is a phishing attempt
                and returns the result.
            """
            phishing_keywords = ["login", "verify", "account", "secure"]
            return any(keyword in url.lower() for keyword in phishing_keywords)

    class RansomwareDetector:
        """Class for detecting ransomware."""

        @staticmethod
        def detect_ransomware(file_path):
            """
            Detects if a file is ransomware.
            
            Args:
                file_path (str): The path to the file.
            
            Returns:
                bool: True if the file is ransomware, else False.
            
            Summary:
                Analyzes the specified file to determine if it is ransomware and
                returns the result.
            """
            ransomware_signatures = ["ecbbf1c523f175282d807d073e07d54d"]
            file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            return file_hash in ransomware_signatures

    class WirelessAuditor:
        """Class for auditing wireless networks."""

        @staticmethod
        def audit_wireless(interface):
            """
            Audits wireless networks on a given interface.
            
            Args:
                interface (str): The wireless interface to audit.
            
            Returns:
                str: Audit report.
            
            Summary:
                Performs an audit of wireless networks using the specified interface
                and returns an audit report.
            """
            result = subprocess.run(['sudo', 'airodump-ng', interface], stdout=subprocess.PIPE)
            return result.stdout.decode()

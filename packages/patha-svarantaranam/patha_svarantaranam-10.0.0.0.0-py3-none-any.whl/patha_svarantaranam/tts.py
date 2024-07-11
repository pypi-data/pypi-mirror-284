import requests
import json
import re
from playsound import playsound
from colorama import init, Fore, Style

init(autoreset=True)

class TextToSpeech:
    def __init__(self, api_url):
        self.api_url = api_url
        self.voices = self._get_available_voices()

    def _get_available_voices(self):
        try:
            response = requests.get(f"{self.api_url}/voice-info")
            response.raise_for_status()
            html_content = response.text
            voice_start = html_content.find('<h2>Available Voices</h2>')
            voices_section = html_content[voice_start:]
            voice_names = [line.split('<h3>')[1].split('</h3>')[0] for line in voices_section.split('') if '<h3>' in line]
            
            voice_map = {}
            for name in voice_names:
                simplified_name = re.split(r'\s*\(', name)[0].strip().lower()
                voice_map[simplified_name] = name
            return voice_map
        except requests.RequestException as e:
            print(Fore.RED + f"Failed to fetch available voices: {e}" + Style.RESET_ALL)
            return {}

    def convert(self, text, voice, speed='normal', output_file='output.wav'):
        if voice.lower() not in self.voices:
            print(Fore.RED + f"Voice '{voice}' not found. Available voices: {', '.join(self.voices.keys())}" + Style.RESET_ALL)
            return None

        full_voice_name = self.voices[voice.lower()]
        data = {
            'text': text,
            'voice': full_voice_name,
            'speed': speed
        }
        try:
            response = requests.post(f"{self.api_url}/api/v3", data=data)
            response.raise_for_status()
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(Fore.GREEN + f"Audio saved as {output_file}" + Style.RESET_ALL)
            return output_file
        except requests.RequestException as e:
            print(Fore.RED + f"TTS conversion failed: {e}" + Style.RESET_ALL)
            return None

    def list_voices(self):
        return list(self.voices.keys())

    def get_languages(self):
        languages = set()
        for full_name in self.voices.values():
            language = re.search(r'\((.*?),', full_name)
            if language:
                languages.add(language.group(1))
        return sorted(list(languages))

    def play_audio(self, file_path):
        try:
            playsound(file_path)
            print(Fore.GREEN + f"Played audio: {file_path}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to play audio: {e}" + Style.RESET_ALL)

def list_available_voices(api_url):
    tts = TextToSpeech(api_url)
    return tts.list_voices()
# Open TTS

A Python module for easy text-to-speech conversion using an open API.

## Installation

```bash
pip install open-tts
```

## Usage

```python
from open_tts import TextToSpeech

# Initialize TextToSpeech with your API URL
tts = TextToSpeech("http://your-api-url:port")

# List available voices
print(tts.list_voices())

# Get available languages
print(tts.get_languages())

# Convert text to speech
output_file = tts.convert("Hello, world!", "emma", speed="normal", output_file="hello.wav")

# Play the generated audio
if output_file:
    tts.play_audio(output_file)

# Display languages and models
tts.display_languages_and_models("terminal")  # Display in terminal
tts.display_languages_and_models("web")  # Display in web browser
```

## Features

- Easy-to-use Python interface for text-to-speech conversion
- Support for multiple voices and languages
- Adjustable speech speed
- Audio playback functionality
- Display of available languages and models in terminal or web browser

## API Configuration

When initializing the TextToSpeech class, provide your API URL:

```python
tts = TextToSpeech("http://your-api-url:port")
```

For more information, please refer to the [GitHub repository](https://github.com/sandeshaiplus/open-tts).
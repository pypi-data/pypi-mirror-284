import os
import re
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from colorama import init, Fore, Style
import webbrowser



init(autoreset=True)
VERSION = "2.0.0 Version 2.O newly patched to get more dteails of this project kindly visit sandeshai https://sandeshai.in/projects/open-tts"
class TextToSpeech:
    def __init__(self, api_url):
        self.api_url = api_url
        self.voices = self._get_available_voices()
    def _get_available_voices(self):
        try:
            response = requests.get(f"{self.api_url}/voice-info")
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            voice_elements = soup.find_all('h3')
            
            voice_map = {}
            for element in voice_elements:
                name = element.text.strip()
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

   

    def display_languages_and_models(self, output_type="terminal"):
        if output_type == "terminal":
            print(Fore.CYAN + "Available Languages:" + Style.RESET_ALL)
            for lang in self.get_languages():
                print(f"- {lang}")
            
            print(Fore.CYAN + "\nAvailable Voices:" + Style.RESET_ALL)
            for voice, full_name in self.voices.items():
                gender = "Female" if "female" in full_name.lower() else "Male"
                print(f"- {voice} ({gender}): {full_name}")
        
        elif output_type == "web":
            language_voices = {}
            for voice, full_name in self.voices.items():
                lang = re.search(r'\((.*?),', full_name)
                if lang:
                    lang = lang.group(1)
                    if lang not in language_voices:
                        language_voices[lang] = []
                    language_voices[lang].append((voice, full_name))

            html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Open TTS - Languages and Models</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

            :root {{
                --bg-primary: #121212;
                --bg-secondary: #1e1e1e;
                --text-primary: #ffffff;
                --text-secondary: #b3b3b3;
                --accent-primary: #bb86fc;
                --accent-secondary: #03dac6;
                --male-skin: #e0ac69;
                --female-skin: #f1c27d;
                --male-hair: #3d3d3d;
                --female-hair: #8c4b00;
            }}

            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}

            body {{
                font-family: 'Roboto', sans-serif;
                line-height: 1.6;
                color: var(--text-primary);
                background-color: var(--bg-primary);
                transition: background-color 0.3s ease;
            }}

            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}

            header {{
                background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
                color: var(--bg-primary);
                text-align: center;
                padding: 2rem 0;
                margin-bottom: 2rem;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}

            h1 {{
                font-size: 2.5rem;
                text-transform: uppercase;
                letter-spacing: 2px;
                margin: 0;
            }}

            h2 {{
                color: var(--accent-primary);
                border-bottom: 2px solid var(--accent-secondary);
                padding-bottom: 10px;
                margin-top: 2rem;
            }}

            .content-wrapper {{
                display: flex;
                justify-content: space-between;
                flex-wrap: wrap;
            }}

            .languages, .voices {{
                background-color: var(--bg-secondary);
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                width: calc(50% - 20px);
                margin-bottom: 2rem;
            }}

            @media (max-width: 768px) {{
                .languages, .voices {{
                    width: 100%;
                }}
            }}

            ul {{
                list-style-type: none;
                padding: 0;
            }}

            li {{
                background-color: rgba(255,255,255,0.05);
                margin-bottom: 10px;
                padding: 15px;
                border-radius: 5px;
                transition: all 0.3s ease;
            }}

            li:hover {{
                transform: translateX(5px);
                background-color: rgba(255,255,255,0.1);
            }}

            .voice-item {{
                display: flex;
                align-items: center;
            }}

            .avatar {{
                width: 80px;
                height: 80px;
                margin-right: 15px;
                position: relative;
                border-radius: 50%;
                overflow: hidden;
                background-color: var(--bg-secondary);
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            }}

            .avatar::before {{
                content: '';
                position: absolute;
                width: 100%;
                height: 100%;
                background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.2), transparent 40%);
            }}

            .face {{
                position: absolute;
                width: 70%;
                height: 80%;
                bottom: 0;
                left: 15%;
                border-radius: 50% 50% 40% 40% / 60% 60% 40% 40%;
            }}

            .male .face {{
                background-color: var(--male-skin);
            }}

            .female .face {{
                background-color: var(--female-skin);
            }}

            .eyes {{
                position: absolute;
                width: 100%;
                top: 25%;
                display: flex;
                justify-content: space-around;
            }}

            .eye {{
                width: 22%;
                height: 22%;
                background-color: white;
                border-radius: 50%;
                position: relative;
                overflow: hidden;
            }}

            .eye::after {{
                content: '';
                position: absolute;
                width: 50%;
                height: 50%;
                background-color: #3d3d3d;
                border-radius: 50%;
                top: 25%;
                left: 25%;
            }}

            .eye::before {{
                content: '';
                position: absolute;
                width: 100%;
                height: 30%;
                background-color: rgba(0,0,0,0.1);
                top: 0;
                left: 0;
                border-radius: 50% 50% 0 0;
            }}

            .eyebrows {{
                position: absolute;
                width: 100%;
                top: 20%;
                display: flex;
                justify-content: space-around;
            }}

            .eyebrow {{
                width: 25%;
                height: 6%;
                background-color: var(--male-hair);
                border-radius: 50%;
            }}

            .male .eyebrow {{
                transform: rotate(-10deg);
            }}

            .female .eyebrow {{
                transform: rotate(-5deg);
                height: 4%;
            }}

            .nose {{
                position: absolute;
                width: 12%;
                height: 20%;
                background-color: rgba(0,0,0,0.1);
                bottom: 30%;
                left: 44%;
                border-radius: 50% 50% 50% 50% / 30% 30% 70% 70%;
            }}

            .mouth {{
                position: absolute;
                width: 30%;
                height: 10%;
                background-color: #c0392b;
                bottom: 15%;
                left: 35%;
                border-radius: 0 0 100px 100px;
                overflow: hidden;
            }}

            .mouth::after {{
                content: '';
                position: absolute;
                width: 100%;
                height: 30%;
                background-color: rgba(255,255,255,0.3);
                bottom: 0;
            }}

            .hair {{
                position: absolute;
                width: 100%;
                top: -15%;
            }}

            .male .hair {{
                height: 45%;
                background-color: var(--male-hair);
                clip-path: polygon(0 30%, 20% 0, 50% 15%, 80% 0, 100% 30%, 100% 100%, 0 100%);
            }}

            .female .hair {{
                height: 75%;
                background-color: var(--female-hair);
                clip-path: polygon(0 60%, 20% 40%, 50% 20%, 80% 40%, 100% 60%, 100% 100%, 0 100%);
            }}

            .female .hair::after {{
                content: '';
                position: absolute;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.2) 50%, transparent 100%);
                animation: hairShine 5s infinite linear;
            }}

            @keyframes hairShine {{
                0% {{ transform: translateX(-100%); }}
                100% {{ transform: translateX(100%); }}
            }}

            .male .face::after {{
                content: '';
                position: absolute;
                width: 70%;
                height: 20%;
                background-color: rgba(0,0,0,0.1);
                bottom: 15%;
                left: 15%;
                border-radius: 50%;
                filter: blur(3px);
            }}

            .female .face::after {{
                content: '';
                position: absolute;
                width: 30%;
                height: 10%;
                background-color: #e74c3c;
                bottom: 15%;
                left: 35%;
                border-radius: 50%;
                filter: blur(2px);
            }}

            .accessories {{
                position: absolute;
                width: 100%;
                height: 100%;
            }}

            .male .accessories::before {{
                content: '';
                position: absolute;
                width: 20%;
                height: 5%;
                background-color: #2c3e50;
                top: 22%;
                left: 5%;
                transform: rotate(-20deg);
            }}

            .female .accessories::before {{
                content: '';
                position: absolute;
                width: 30%;
                height: 30%;
                border: 2px solid #f39c12;
                border-radius: 50%;
                top: 60%;
                left: -15%;
            }}

            .voice-details {{
                flex-grow: 1;
            }}

            .voice-name {{
                font-weight: bold;
                color: var(--accent-primary);
            }}

            .voice-full-name {{
                color: var(--text-secondary);
                font-size: 0.9rem;
            }}

            #searchInput {{
                width: 100%;
                padding: 10px;
                border: 2px solid var(--accent-secondary);
                border-radius: 5px;
                font-size: 1rem;
                margin-bottom: 20px;
                background-color: var(--bg-secondary);
                color: var(--text-primary);
            }}

            #searchInput:focus {{
                outline: none;
                border-color: var(--accent-primary);
                box-shadow: 0 0 5px var(--accent-primary);
            }}

            .language-item {{
                cursor: pointer;
                transition: background-color 0.3s ease;
            }}

            .language-item:hover {{
                background-color: rgba(255,255,255,0.1);
            }}

            .models-list {{
                display: none;
                margin-top: 10px;
                padding-left: 20px;
                border-left: 2px solid var(--accent-secondary);
            }}

            .models-list li {{
                font-size: 0.9em;
                padding: 5px 0;
            }}

            .active {{
                background-color: rgba(255,255,255,0.1);
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Open TTS - Languages and Models</h1>
        </header>
        
        <div class="container">
            <div class="content-wrapper">
                <div class="languages">
                    <h2>Available Languages</h2>
                    <ul id="languageList">
                        {''.join(f"""
                        <li class="language-item" data-language="{lang}">
                            {lang}
                            <ul class="models-list">
                                {''.join(f"<li>{voice}: {full_name}</li>" for voice, full_name in voices)}
                            </ul>
                        </li>
                        """ for lang, voices in language_voices.items())}
                    </ul>
                </div>
                
                <div class="voices">
                    <h2>Available Voices</h2>
                    <input type="text" id="searchInput" placeholder="Search voices...">
                    <ul id="voiceList">
                        {''.join(f"""
                        <li class="voice-item {'male' if 'male' in full_name.lower() else 'female'}">
                            <div class="avatar">
                                <div class="face">
                                    <div class="eyebrows">
                                        <div class="eyebrow"></div>
                                        <div class="eyebrow"></div>
                                    </div>
                                    <div class="eyes">
                                        <div class="eye"></div>
                                        <div class="eye"></div>
                                    </div>
                                    <div class="nose"></div>
                                    <div class="mouth"></div>
                                </div>
                                <div class="hair"></div>
                                <div class="accessories"></div>
                            </div>
                            <div class="voice-details">
                                <div class="voice-name">{voice}</div>
                                <div class="voice-full-name">{full_name}</div>
                            </div>
                        </li>
                        """ for voice, full_name in self.voices.items())}
                    </ul>
                </div>
            </div>
        </div>

        <script>
            document.getElementById('searchInput').addEventListener('input', function() {{
                const searchTerm = this.value.toLowerCase();
                const voiceItems = document.querySelectorAll('#voiceList li');
                
                voiceItems.forEach(item => {{
                    const voiceName = item.textContent.toLowerCase();
                    if (voiceName.includes(searchTerm)) {{
                        item.style.display = 'flex';
                    }} else {{
                        item.style.display = 'none';
                    }}
                }});
            }});

            document.getElementById('languageList').addEventListener('click', function(event) {{
                const languageItem = event.target.closest('.language-item');
                if (languageItem) {{
                    const modelsList = languageItem.querySelector('.models-list');
                    const allModelsLists = document.querySelectorAll('.models-list');
                    const allLanguageItems = document.querySelectorAll('.language-item');

                    allModelsLists.forEach(list => {{
                    if (list !== modelsList) {{
                        list.style.display = 'none';
                    }}
                }});

                allLanguageItems.forEach(item => {{
                    item.classList.remove('active');
                }});

                if (modelsList.style.display === 'block') {{
                    modelsList.style.display = 'none';
                    languageItem.classList.remove('active');
                }} else {{
                    modelsList.style.display = 'block';
                    languageItem.classList.add('active');
                }}
            }}
        }});
    </script>
</body>
</html>
        """
            html_file = 'open_tts_voices.html'
            with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(html_content)
            webbrowser.open('file://' + os.path.realpath(html_file))
        
        else:
            print(f"Invalid output type: {output_type}. Use 'terminal' or 'web'.")
def usage():
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Open TTS - Help Guide</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

        :root {
            --bg-primary: #121212;
            --bg-secondary: #1e1e1e;
            --text-primary: #ffffff;
            --text-secondary: #b3b3b3;
            --accent-primary: #bb86fc;
            --accent-secondary: #03dac6;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Roboto', sans-serif;
            line-height: 1.6;
            color: var(--text-primary);
            background-color: var(--bg-primary);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            color: var(--bg-primary);
            text-align: center;
            padding: 2rem 0;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        h2 {
            color: var(--accent-primary);
            margin-top: 2rem;
            margin-bottom: 1rem;
        }

        p {
            margin-bottom: 1rem;
        }

        .section {
            background-color: var(--bg-secondary);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .feature {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }

        .feature-icon {
            font-size: 2rem;
            margin-right: 1rem;
        }

        .code-block {
            background-color: rgba(255,255,255,0.05);
            color: var(--text-primary);
            padding: 1rem;
            border-radius: 4px;
            font-family: monospace;
            margin-bottom: 1rem;
        }

        .btn {
            display: inline-block;
            background-color: var(--accent-primary);
            color: var(--bg-primary);
            padding: 0.5rem 1rem;
            text-decoration: none;
            border-radius: 4px;
            transition: background-color 0.3s ease;
        }

        .btn:hover {
            background-color: var(--accent-secondary);
        }

        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }

        .floating {
            animation: float 3s ease-in-out infinite;
        }
    </style>
</head>
<body>
    <header>
        <h1>🎙️ Open TTS Help Guide</h1>
        <p>Your comprehensive guide to using the Open Text-to-Speech System</p>
    </header>

    <div class="container">
        <section class="section">
            <h2>🚀 Getting Started</h2>
            <p>Welcome to Open TTS! This powerful tool allows you to convert text to speech with ease. Here's how to get started:</p>
            <div class="feature">
                <span class="feature-icon floating">📥</span>
                <div>
                    <h3>Installation</h3>
                    <p>Install Open TTS using pip:</p>
                    <div class="code-block">
                        pip install open-tts
                    </div>
                </div>
            </div>
            <div class="feature">
                <span class="feature-icon floating">🔧</span>
                <div>
                    <h3>Basic Usage</h3>
                    <p>Here's a simple example to get you started:</p>
                    <div class="code-block">
                        from open_tts import TextToSpeech<br>
                        <br>
                        tts = TextToSpeech("http://your-api-url:port")<br>
                        tts.convert("Hello, world!", "emma", output_file="hello.wav")
                    </div>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>🔑 Key Features</h2>
            <div class="feature">
                <span class="feature-icon floating">🗣️</span>
                <div>
                    <h3>Multiple Voices</h3>
                    <p>Choose from a wide range of voices across different languages and accents.</p>
                </div>
            </div>
            <div class="feature">
                <span class="feature-icon floating">🎚️</span>
                <div>
                    <h3>Adjustable Speech Speed</h3>
                    <p>Customize the speed of the generated speech to suit your needs.</p>
                </div>
            </div>
            <div class="feature">
                <span class="feature-icon floating">🌐</span>
                <div>
                    <h3>Web Interface</h3>
                    <p>Explore available voices and languages through an interactive web interface.</p>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>📚 Advanced Usage</h2>
            <div class="feature">
                <span class="feature-icon floating">🔍</span>
                <div>
                    <h3>Listing Available Voices</h3>
                    <div class="code-block">
                        voices = tts.list_voices()<br>
                        print(voices)
                    </div>
                </div>
            </div>
            <div class="feature">
                <span class="feature-icon floating">🌍</span>
                <div>
                    <h3>Getting Available Languages</h3>
                    <div class="code-block">
                        languages = tts.get_languages()<br>
                        print(languages)
                    </div>
                </div>
            </div>
            <div class="feature">
                <span class="feature-icon floating">🖥️</span>
                <div>
                    <h3>Displaying Languages and Models</h3>
                    <div class="code-block">
                        tts.display_languages_and_models("web")  # Opens in web browser<br>
                        tts.display_languages_and_models("terminal")  # Displays in console
                    </div>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>🆘 Need More Help?</h2>
            <p>If you need further assistance, check out our documentation or reach out to our support team.</p>
            <a href="https://sandeshai.in/projects/open-tts" target = "blank" class="btn">View Documentation</a>
        </section>
    </div>

    <script>
        // You can add any JavaScript for additional interactivity here
    </script>
</body>
</html>
    """

    # Write the HTML content to a file
    help_file = 'open_tts_help.html'
    with open(help_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Open the help file in the default web browser
    webbrowser.open('file://' + os.path.realpath(help_file))
def version():
    return VERSION
def list_available_voices(api_url):
    tts = TextToSpeech(api_url)
    return tts.list_voices()


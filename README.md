# AI Text Corrector using OpenAI's API

This AI Typing assistant is powered by OpenAI's GPT-3.5-turbo, and functions in similar fashion as the auto-correct feature in Gboard or Grammarly. Should be used in text editors, word processors, or any other text input fields. Text language should be English.

## Functionality
Fixes all typographical, grammatical, punctuation or spelling errors, or any irregularities that may override the intended message of the user.

## How it works
When run, the Python script listens to the user-defined hotkeys, while still running in the background.
For this project, function keys - `f8` and `f9` has been defined as default key bindings to trigger fixes on text.

- `f8` - Calls a function that first triggers the select all (ctrl+a) command highlighting the entire text in the active editor window, before then calling on the same function as `f9` to fix the highlighted text.

- `f9` - Calls a function that first triggers the copy-to-clipboard (ctrl+c) command copying the highlighted text in the active editor window. The text from clipboard is sent, along with a prompt, to GPT-3.5-turbo via an API call. The LLM performs the fixes, where its needed, and returns the fixed text back to the clipboard. Afterwards, a paste (ctrl+v) command is triggered to display fixed text to window.

## Getting Started

1. Clone this repository to your local machine:
    ```
    git clone https://github.com/Xelvise/AI-Text-Corrector.git
    ```
2. Navigate to the project directory:
    ```
    cd AI-Text-Corrector
    ```
3. Create and activate a Virtual Environment: (Optional, but recommended)
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```
    ```
     conda activate <Environment_Name>/
    ```
4. In the same directory, create a `.env` file containing **'your-api-key'** assigned to an environment variable:
    ```
    OPENAI_API_KEY = 'your-api-key'
    ```
5. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
    For Linux OS, you may need to install `xclip` and/or `PyQt5` to enable clipboard functionality, as required by **pyperclip**:
        
        pip install PyQt5
        sudo apt-get install xclip

6. Run the script:
    ```
    python main.py
    ```
**PS:** Due to differences in key bindings across platforms, this script may only run fixes on Windows and Linux OS. 
For MacOS, kindly modify the key bindings in the `main.py` file, as shown below:

Change `Key.ctrl` -> `Key.cmd`

## Usage

- Open a text editor or word processor, and start typing.
- If errors are present, hit `f8` or `f9` to fix the text.
- If errors are still present after the first fix, hit `f8` or `f9` repeatedly to implement more fixes.
- To stop/end the script, close the terminal or hit `ctrl+c` while in the terminal window.

## Customize

Hotkeys and prompts can be easily customized in the `main.py` file to suit the User's preference.
Shown below is the default prompt template being used by the LLM, and can be modified:

```python
from langchain.prompts import PromptTemplate

template = '''For every text given, you should fix all typographical, grammatical, 
punctuation or spelling errors, or any irregularities that may override the intended message. 
However, you should preserve all the text's formattings and retain its original meaning.\n
Text: {input}'''

prompt = PromptTemplate(template=template, input_variables=['input'])
```

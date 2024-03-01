from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pynput.keyboard import Key, Controller, GlobalHotKeys
import pyperclip
import time
load_dotenv()

controller = Controller()
llm = ChatOpenAI(temperature=0.2)

# define keys
f8 = str(Key.f8.value)
f9 = str(Key.f9.value)


def fix_text(text: str):
    '''Calls on OpenAI's GPT-3 to fix the text.'''

    template = '''For every text given, you should fix all typographical, grammatical, 
    punctuation or spelling errors, or any irregularities that may override the intended message. 
    However, you should preserve all the text's formattings and retain its original meaning.\n
    Text: {input}'''
    prompt = PromptTemplate(template=template, input_variables=['input'])
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({'input':text})
    return response.replace('Text: ','',1)

def fix_selection():
    '''Copies highlighted text to clipboard. Retrieves text from clipboard, initiate a fix and pushes the fixed text back to clipboard. Finally pastes text to display.'''

    with controller.pressed(Key.ctrl):
        controller.tap('c')     # implement a copy (ctrl+c) command that copies selected text to clipboard
    time.sleep(0.1)     # to implement a delay of 0.1 seconds

    text = pyperclip.paste()    # to retrieve text from clipboard
    if type(text) == str:
        fixed_text = fix_text(text)     # fixes the text
    else:
        fixed_text = text   # if text is not a string, it is left unchanged
    
    pyperclip.copy(fixed_text)   # pushes the fixed text back to clipboard
    time.sleep(0.1)     # to implement additional delay of 0.1 seconds
    with controller.pressed(Key.ctrl):
        controller.tap('v')     # implement a paste (ctrl+v) command
    
    print('fixed current selection')

def fix_entire_lines():
    with controller.pressed(Key.ctrl):
        controller.tap('a')     # implement a select all (ctrl+a) command
    fix_selection()     # calls the fix_selection function


# define a hotkey listener
        
with GlobalHotKeys({
    f8: fix_entire_lines, 
    f9: fix_selection}) as h:
    h.join()

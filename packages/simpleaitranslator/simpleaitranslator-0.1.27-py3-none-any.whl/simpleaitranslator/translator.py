import os
from openai import OpenAI
import json
from simpleaitranslator.utils.function_tools import tools_get_text_language, tools_translate

CHATGPT_MODEL = "gpt-4o"
OPENAI_API_KEY=None


def get_text_language(text):
    global OPENAI_API_KEY
    client = OpenAI(api_key=OPENAI_API_KEY)
    messages = [
        {"role": "system", "content": "You are a language detector. You should return the ISO 639-3 code to the get_from_language function of user text."},
        {"role": "user", "content": text}
    ]

    response = client.chat.completions.create(
        model=CHATGPT_MODEL,
        messages=messages,
        tools=tools_get_text_language,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    if tool_calls:
        #print(tool_calls)
        tool_call = tool_calls[0]
        function_args = json.loads(tool_call.function.arguments)
        return function_args.get("iso639_3")

    return None


def translate(text, to_language):
    global OPENAI_API_KEY
    client = OpenAI(api_key=OPENAI_API_KEY)
    messages = [
        {"role": "system", "content": f"You are a language translator. You should translate the text to the {to_language} language and then put result of the translation to the translate_to_language function"},
        {"role": "user", "content": text}
    ]
    response = client.chat.completions.create(
        model=CHATGPT_MODEL,
        messages=messages,
        tools=tools_translate,
        tool_choice="auto",
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    #print(tool_calls)
    #print(response_message)
    if tool_calls:
        #print(tool_calls)
        tool_call = tool_calls[0]
        function_args = json.loads(tool_call.function.arguments)
        return function_args.get("translated_text")
    return None









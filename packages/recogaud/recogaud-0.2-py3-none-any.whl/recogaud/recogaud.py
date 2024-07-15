import speech_recognition as sr
from g4f.client import Client
import asyncio
import sys

# Устанавливаем правильную политику цикла событий для Windows
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def recog(audio_file_path):
    """
    Распознает речь из аудиофайла и корректирует полученный текст.
    
    :param audio_file_path: путь к аудиофайлу
    :return: распознанный и исправленный текст
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)
        
        text = recognizer.recognize_google(audio_data, language="ru-RU")
        return _correct_text(text)
    except sr.UnknownValueError:
        return "Не удалось распознать речь в аудиофайле"
    except sr.RequestError as e:
        return f"Ошибка сервиса распознавания речи: {e}"
    except Exception as e:
        return f"Произошла ошибка при обработке аудиофайла: {e}"

def _correct_text(text):
    """
    Корректирует текст с помощью GPT модели.
    
    :param text: исходный текст
    :return: исправленный текст
    """
    client = Client()
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": f"Исправь ошибки в тексте и улучши грамматику, но не добавляй никаких пояснений и не включай URL: {text}"
            }]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка при коррекции текста: {e}"
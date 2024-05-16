import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QComboBox
import speech_recognition as sr
from openai import OpenAI
from gtts import gTTS
import threading
import os
from dotenv import load_dotenv
from playsound import playsound
import io
import pygame
# .env dosyasından ortam değişkenlerini yükle
load_dotenv()
OpenAI_API_KEY = os.getenv('OPENAI_API_KEY')
OpenAI.api_key = OpenAI_API_KEY






def listen_and_respond(mic, label):
    recognizer = sr.Recognizer()

    try:
        # Mikrofondan sesi dinle
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            label.setText("Dinleniyor...")
            audio = recognizer.listen(source, timeout=3.0, phrase_time_limit=3)
        
        # Google Web Speech API kullanarak sesi metne çevir
        text = recognizer.recognize_google(audio, language='tr-TR')
        print(f"Algılanan metin: {text}")
        
        client = OpenAI(api_key=OpenAI_API_KEY)
        # GPT-4 chat modelini kullanarak metne cevap oluştur
        chat_completion = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": text}],
        )


        answer = chat_completion.choices[0].message.content
        print(f"Cevap: {answer}")
        
        

        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=answer,
            response_format="wav"
        )

        # BytesIO nesnesi oluşturun ve yanıt verilerini içine yazın
        soundIO = io.BytesIO(response.read())

        # pygame'i başlatın
        pygame.mixer.init()

        # BytesIO nesnesini pygame ile oynatın
        pygame.mixer.music.load(soundIO, 'wav')
        pygame.mixer.music.play()

        # Sesin bitmesini bekleyin
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


        # # Cevabı sesli olarak oku (Türkçe destekli)
        # tts = gTTS(answer, lang='tr')
        # tts.save("response.mp3")
        # playsound("response.mp3")
        # os.remove("response.mp3")  # Dosyayı çaldıktan sonra sil
    except sr.WaitTimeoutError:
        print("Dinleme zaman aşımına uğradı, yeniden deneyin...")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    
    label.setText("Dinlemeyi Başlat")

def on_button_click(mic, label):
    threading.Thread(target=listen_and_respond, args=(mic, label)).start()

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Sesli Asistan')

layout = QVBoxLayout()
label = QLabel("Dinlemeyi Başlat")
layout.addWidget(label)

mic_list = QComboBox()
recognizer = sr.Recognizer()
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    mic_list.addItem(name, index)
layout.addWidget(mic_list)

button = QPushButton('Dinlemeye Başla')
button.clicked.connect(lambda: on_button_click(sr.Microphone(device_index=mic_list.currentData()), label))
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())

# Türkçe-sesli-asistan
türkçe sesli asistan chat gpt yardımıyla yapılmıştır


## Burulum
kullanmaya başlamadan önce gerekli kütüphaneleri kuralım
bunu yapmak için requirements.txt içindeki kütüphaneleri sürümleriyle birlikte kurmamız gerek
bu işlemi kısa yoldan hedef dosya dizinin içinde python terminali içerisine
```python
pip install -r requirements.txt
```
bu adımı tamamladıktan sonra hedef klasörün içine bir adet .env dosyası oluşturun 
.env dosyasının içini şunlarla doldurun:
```python
TTS_LANGUAGE=tr
TTS_RATE=150
OPENAI_API_KEY=openai-api-key
```
koddaki "openai-api-key" kısmını kendi api keyiniz ile değiştirin.

## Başlatma
kütüphaneleri başarılı birşekilde kurduktan sonra kodu çalıştırma adımına geçelim
main.py dosyasını çalıştırdıktan sonra karşınıza resimdekine benzer bir gui çıkıcak
bu guide sesli asistan ile konuşmak istediğiniz mikrofonunuzu seçin

<img src="https://i.hizliresim.com/9q9hhmn.png" width="320" height="180">


mikrofonunuzu seçtikten sonra dinlemeye başla butonuna tıklayın
guide resimdeki gibi dinleniyor yazısı varken konuşabilirsiniz

<img src="https://i.hizliresim.com/3c4of1u.png" width="320" height="180">

sesli asistan konuşmanız bittikten 3 saniye sonra dinlemeyi keser ve api yardımıyla chat gpt 4 chatbotunun yanıtını sesli bir şekilde size okur
tekrar konuşmak için dinlemeye başla butonuna tıklayabilirsiniz

eğer kod çalışmıyorsa tokeninizi kontrol ediniz, tükenmiş olabilir

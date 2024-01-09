import urllib3
import json

BOT_TOKEN = "6810883359:AAGHeiTe0L9pjyvLQOusxAjym4SKH7_hZus" #bongkook_bot 텔레그램 봇

#메시지 읽어오기
def get_updates():
    http = urllib3.PoolManager()
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = http.request('GET', url)
    return json.loads(response.data.decode('utf-8'))

updates = get_updates()
print(updates)

#메시지 보내기
def sendMessage(chat_id, text) :
    data = {
        'chat_id': chat_id,
        'text': text
    }
    http = urllib3.PoolManager()
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = http.request('POST', url, fields=data)
    return json.loads(response.data.decode('utf-8'))

result = sendMessage(724604760,"반갑습니다. 저는 텔레그램 봉국 봇 입니다.")
print(result)

#사진 보내기
def sendPhoto(chat_id, image_url):
    data = {
        'chat_id':chat_id,
        'photo':image_url,
    }
    http = urllib3.PoolManager()
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    response = http.request('POST', url,fields=data)
    return json.loads(response.data.decode('utf-8'))

result1 = sendPhoto(724604760, "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcclXjp%2Fbtq6mBVIBsW%2FMiBiEx0vu3xOhNhxQvzAJ1%2Fimg.jpg")
result2 = sendPhoto(724604760, "https://talkimg.imbc.com/TVianUpload/tvian/TViews/image/2022/10/08/b0bb64c1-989a-4ff6-abeb-fd92e81eda16.jpg")
print(result1)
print(result2)
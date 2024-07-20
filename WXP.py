import requests,json
def send(bt,xx):
    url = "https://wxpusher.zjiecode.com/api/send/message"
    headers = {
        'Content-Type':'application/json',
    }
    data = {
      "appToken":"AT_vFc4PrvLlS3Ufj4DD5Ljcp9Tsappp6ab",
      "content":f"{xx}",
      "summary":f"{bt}",
      "contentType":2,
      "topicIds":[ 
          123
      ],
      "uids":[
          "UID_IgMqGRXD3p0HJgvUmxqRbD9VxAox"
      ],
      "url":"https://wxpusher.zjiecode.com", 
      "verifyPay":False, 
      "verifyPayType":0 
    }
    #print(data)
    ad = requests.post(url,headers=headers,json=data).json()
    if ad['code'] == 1000:
        print(ad['msg'])
        aa = ad['msg']
        return aa
    else:
        ss ="发送消息失败"
        #print(ss)
        return ss
def send1(bt,xx,aa):
    url = "https://wxpusher.zjiecode.com/api/send/message"
    headers = {
        'Content-Type':'application/json',
    }
    data = {
      "appToken":"AT_vFc4PrvLlS3Ufj4DD5Ljcp9Tsappp6ab",
      "content":f"{xx}",
      "summary":f"{bt}",
      "contentType":2,
      "topicIds":[ 
          123
      ],
      "uids":[
          "UID_IgMqGRXD3p0HJgvUmxqRbD9VxAox"
      ],
      "url":f"{aa}", 
      "verifyPay":False, 
      "verifyPayType":0 
    }
    #print(data)
    ad = requests.post(url,headers=headers,json=data).json()
    if ad['code'] == 1000:
        print(ad['msg'])
        aa = ad['msg']
        return aa
    else:
        ss ="发送消息失败"
        #print(ss)
        return ss
if __name__ == "__main__":
    b = "标题"
    a = "内容11"
    send(a,b)

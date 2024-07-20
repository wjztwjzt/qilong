import requests,json,os

uid = os.getenv("wxuid")
wxtoken = os.getenv("wxtoken")
def send(bt,xx,uid,wxtoken):
    url = "https://wxpusher.zjiecode.com/api/send/message"
    headers = {
        'Content-Type':'application/json',
    }
    data = {
      "appToken":f"{wxtoken}",
      "content":f"{xx}",
      "summary":f"{bt}",
      "contentType":2,
      "topicIds":[ 
          123
      ],
      "uids":[
          f"uid"
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
def send1(bt,xx,aa,uid,wxtoken):
    url = "https://wxpusher.zjiecode.com/api/send/message"
    headers = {
        'Content-Type':'application/json',
    }
    data = {
      "appToken":f"{wxtoken}",
      "content":f"{xx}",
      "summary":f"{bt}",
      "contentType":2,
      "topicIds":[ 
          123
      ],
      "uids":[
          f"uid"
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

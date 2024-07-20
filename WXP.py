import requests,json,os

uid = os.getenv("wxuid")
wxtoken = os.getenv("wxtoken")
PUSH_PLUS_TOKEN = os.getenv("plus_a")
def send(bt,xx):
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
def send1(bt,xx,aa):
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

def push(title: str, content: str) -> None:
        """
        通过 push+ 推送消息。
        """
    if not PUSH_PLUS_TOKEN:
        print("PUSHPLUS 服务的 PUSH_PLUS_TOKEN 未设置!!\n取消推送")
        return
    print("PUSHPLUS 服务启动")
    
    url = "http://www.pushplus.plus/send"
    data = {
            "token": PUSH_PLUS_TOKEN,
            "title": title,
            "content": content,
            #"topic": push_config.get("PUSH_PLUS_USER"),
        }
    body = json.dumps(data).encode(encoding="utf-8")
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, data=body, headers=headers).json()
    
    if response["code"] == 200:
        print("PUSHPLUS 推送成功！")
    
    else:
    
        url_old = "http://pushplus.hxtrip.com/send"
        headers["Accept"] = "application/json"
        response = requests.post(url=url_old, data=body, headers=headers).json()
    
        if response["code"] == 200:
            print("PUSHPLUS(hxtrip) 推送成功！")
    
        else:
            print("PUSHPLUS 推送失败！")
if __name__ == "__main__":
    b = "标题"
    a = "内容11"
    send(a,b)

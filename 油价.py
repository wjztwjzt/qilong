import raw_main_WXP
import requests,os,time,json,re
date = time.strftime(f"%Y年%m月%d日",time.localtime(time.time()))

url = "https://www.autohome.com.cn/oil/130500.html"
headers = {
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
}
res = requests.post(url,headers=headers,json=None)
text = str(res.text)
pattern = r'汽油、柴油每升最新价格为：(.+?)，(.+?)，(.+?)，(.+?)。'
result = re.search(pattern, text, re.S)

if result:
    #print("价格信息为:")
    #print("92号汽油为：" + result.group(1))
    #print("95号汽油为：" + result.group(2))
    #print("98号汽油为：" + result.group(3))
    #print("0号柴油为：" + result.group(4))
    print(f"{date},今日价格为:\n92号汽油为：{result.group(1)}\n95号汽油为：{result.group(2)}\n98号汽油为：{result.group(3)}\n0号柴油为：{result.group(4)}")
    raw_main_WXP.send(f"{date}汽油价格"， f"今日价格为:\n92号汽油为：{result.group(1)}\n95号汽油为：{result.group(2)}\n98号汽油为：{result.group(3)}\n0号柴油为：{result.group(4)}")
else:
    print("未匹配到价格信息")

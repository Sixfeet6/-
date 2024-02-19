# 导入requests库
import requests

# 定义请求的url
url = "https://www.zukongguan.com/forum.php?mod"

# 定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.zukongguan.com/forum.php?mod",
    "Cookie": "4Svp_2132_saltkey=nv7cHhHZ; 4Svp_2132_lastvisit=1708338699; 4Svp_2132_sid=HuTSZ7; 4Svp_2132_lastact=1708342541%09member.php%09logging; SourcePage=; FirstBrowsePage=https%3A%2F%2Fwww.zukongguan.com%2Fforum.php%3Fmod%3D; 4Svp_2132_sendmail=1; 4Svp_2132_ulastactivity=9e87t2MIrvAcnQjNkwcf0wfQczNX6fGfmpIxVGWG5iBS7XPe9Day; 4Svp_2132_auth=756e2UV1ILcLYeIcGiyxI2z%2FB3sZjpzorTJGJJu4u9WJbRI5ZzBuiophWZQ%2FBUqVEty6HNH%2BEagz6%2FLy9d%2BCbNE7; 4Svp_2132_creditnotice=0D30D0D0D0D0D0D0D0D3107; 4Svp_2132_creditbase=0D780D201D0D0D0D0D0D0; 4Svp_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; 4Svp_2132_lastcheckfeed=3107%7C1708342541; 4Svp_2132_checkfollow=1; 4Svp_2132_lip=113.128.75.65%2C1707287805",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}

# 发送get请求
response = requests.get(url, headers=headers)

# 打印响应状态码和内容
print(response.status_code)
print(response.text)


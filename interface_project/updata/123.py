import requests

url = "http://api.app.inno72.com/push/pushMsg"

payload = "{\"alias\":\"18047652\",\"machineCode\":\"18047652\",\"title\":\"这是标题\",\"text\":\"这是简介\",\"pushType\":1,\"msgInfo\":{\n \"apps\":[{\n    \"url\": \"http://inno72.oss.72solo.com/apk/prod/prod_monitor.apk \", \n    \"startStatus\": 1, \n    \"appPackageName\": \"com.inno72.monitorapp\", \n    \"versionCode\": 9\n }]\n  }\n \n}"
headers = {
    'Content-Type': "application/json",
    'lf-None-Matoh': "7e91454ec997430fb9b2a29c85982aba",
    'Cache-Control': "no-cache",
    'Postman-Token': "8e399c62-d6f9-435f-a9bd-d144fd4dbf7d"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
import requests
import json


def get_response(msg):
    api = 'http://openapi.tuling123.com/openapi/api/v2'
    dat = {
            "reqType":0,
            "perception": {
                "inputText": {
                    "text": msg
                }
            },
            "userInfo": {
                "apiKey": "683fc09c862e49a4b70b8abdaa274d87",
                "userId": "123456"
            }
        }
    dat = json.dumps(dat)
    r = requests.post(api, data=dat).json()

    # 以下为r的内容
    # {'emotion': {'userEmotion': {'emotionId': 10300, 'd': 0, 'p': 0, 'a': 0},
    #              'robotEmotion': {'emotionId': 0, 'd': 0, 'p': 0, 'a': 0}},
    #  'intent': {'code': 10004, 'actionName': '', 'intentName': ''},
    # 'results': [{'resultType': 'text', 'values': {'text': '别兴奋别兴奋，很高兴认识你！'}, 'groupType': 1}]}

    print(r)
    mesage = r['results'][0]['values'][r['results'][0]['resultType']]
    print("调用图灵机器人")
    print(mesage)
    return mesage
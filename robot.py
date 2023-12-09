# -*- coding: UTF-8 -*-
from qg_botsdk import BOT, Model   # 导入SDK核心类（BOT）、所有数据模型（Model）
import requests
import json

def ask_openai(task,question):

    url = "https://api.openai-hk.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer hk-gljj8h100000934043cccd7f710c1770032ac7b4d76ac420"
    }

    #user_ask=input()

    data = {
        "max_tokens": 1200,
        "model": "gpt-3.5-turbo",
        "temperature": 0.8,
        "top_p": 1,
        "presence_penalty": 1,
        "messages": [
            {
                "role": "system",
                "content": task
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data).encode('utf-8') )
    result = response.content.decode("utf-8")

    #print(result)

    # 解析JSON字符串
    data = json.loads(result)

    # 定位到我们想要的信息
    content = data["choices"][0]["message"]["content"]

    #print(content)
    return content

def get_task(taskname):
    # 打开文件
    with open(taskname, 'r',encoding='utf-8') as file:
        # 读取多行内容
        lines = file.readlines()

        # 拼接为一行，并保留换行符和制表符
        merged_line = ''.join(lines)

        # 打印结果
        return merged_line

bot = BOT(bot_id='102070552', bot_token='qHAvc3v8Me2XvIdspk4MgWPcEcAsN2A3', is_private=True, is_sandbox=True)   # 实例化SDK核心类




@bot.bind_msg()   # 绑定接收消息事件的函数
def deliver(data: Model.MESSAGE):   # 创建接收消息事件的函数
    #if '你好' in data.treated_msg:   # 判断消息是否存在特定内容
    #    data.reply('你好，世界')   # 发送被动回复（带message_id直接reply回复）
        # 如需使用如 Embed 等消息模板，可传入相应结构体， 如：
        # data.reply(ApiModel.MessageEmbed(title="你好", content="世界"))
    #task=get_task('readme.txt')
    task=get_task('reply.txt')
    data.reply(ask_openai(task,data.treated_msg))

if __name__ == '__main__':
    bot.start()   # 开始运行机器人


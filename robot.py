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
        "max_tokens": 2000,
        "model": "gpt-3.5-turbo-1106",
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
    #print(data)
    # 定位到我们想要的信息
    content = data["choices"][0]["message"]["content"]

    print(content+'\n')
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

def is_at(users):
    x=bot.api.get_bot_info().data.id
    for i in users:
        if (x==i.id):
            return True
    return False

def is_question(msg):
    que=get_task('question.txt')
    ans=ask_openai(que,msg)
    #print(ans)
    #print(ans=='是')
    if ('是' in ans):
        #print('是问句')
        return True
    #print('不是是问句')
    return False

bot = BOT(bot_id='102070552', bot_token='qHAvc3v8Me2XvIdspk4MgWPcEcAsN2A3', is_private=True, is_sandbox=False)   # 实例化SDK核心类

@bot.bind_msg()   # 绑定接收消息事件的函数
def deliver(data: Model.MESSAGE):   # 创建接收消息事件的函数
    #task=get_task('readme.txt')
    if ('深渊使用率' in data.treated_msg):
        #print('A\n')
        return
    if ('角色持有' in data.treated_msg):
        #print('B\n')
        return
    print(data.treated_msg+'\n')
    if ('mentions' in data.__dict__):
        if (is_at(data.mentions)):
            task=get_task('reply.txt')
            ans='<@'+data.author.id+'>'
            ans=ans+ask_openai(task,data.treated_msg)
            data.reply(ans,message_reference_id=data.id) 
    '''
    else:
        if (is_question(data.treated_msg)):
            ans='<@'+data.author.id+'>'+'我是频道管理员，如果你有频道相关问题。可以@我并附上问题，我会尽力为你解答。'
            data.reply(ans,message_reference_id=data.id)
    '''

'''
@bot.bind_audit()
def msg_function(data: Model.MESSAGE_AUDIT):
    if (data.t=='MESSAGE_AUDIT_REJECT'):
        print('你没过审核\n')
    else:
        print('你过审核了\n')
'''


if __name__ == '__main__':
    bot.start()   # 开始运行机器人


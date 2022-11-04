# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 22:55:28 2022

@author: User
"""
"""
import gspread
from Mahjong import *
"""


#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)
import datetime



from linebot.models import MessageEvent,TextSendMessage,TextSendMessage,ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton, MessageAction

 




# 必須放上自己的Channel Access Token          #medbotma
line_bot_api = LineBotApi('8+3WhZhpi6DtH9ngI04I9+APY+Lh/QovOIZr1iuqHtfUoq9p/fsTkeXqKQ6eDR/nTJVfeJCT0h1XTCUkiCvwLC+dOU5+ZSTilI8Qn8H8r9Z2lW9cLF71aDcqMnhH36uVrRqc+F5LliNPYyHht4QoQwdB04t89/1O/w1cDnyilFU=')

# 必須放上自己的Channel Secret
handler = WebhookHandler('c8a14092281cef72ea0ca7fb76c3c122')  #medbot 03

line_bot_api.push_message('U01d75620e9f2ce94285be32cce03989c', TextSendMessage(text='你可以開始了'))
                         
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'







#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
             
    if mtext == '@傳送文字':
        try:
            message=TextSendMessage(#文字傳送格式---------------
                text="我是 衰歌 \n 您好"
            )#文字傳送格式---------------
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,
                                       TextSendMessage(text='發生錯誤!'))
         
 
     


        
        
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

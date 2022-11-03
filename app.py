# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 22:55:28 2022

@author: User
"""

import gspread

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

 
from Mahjong import *



# 必須放上自己的Channel Access Token          #medbot 03
line_bot_api = LineBotApi('/Hpu1Xs7VljOdUqGPbJ+fCqQoI7RVNMI33Q7PSOjavguWxXhDbWKDxZ8UVbso0K9TJVfeJCT0h1XTCUkiCvwLC+dOU5+ZSTilI8Qn8H8r9YkLCaaSO8lWk770XS0RJ6JAF8x+0NInAaRhNM/w7ztAQdB04t89/1O/w1cDnyilFU=')

# 必須放上自己的Channel Secret
handler = WebhookHandler('20c392f5eb85cd603d21ad94c05ec894')  #medbot 03

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
             
    if mtext == '#查詢#':  
        try:
            message=TextSendMessage(#文字傳送格式---------------
                text= ff()
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

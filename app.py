# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 22:55:28 2022

@author: User
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

 
from strwork import *



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
             
    if mtext == '@預約':  
        buttons_template_message = TemplateSendMessage(
        alt_text='麻將預約系統',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/4LljfMm.png',
            title='麻將預約系統',
            text='選單功能',
            actions=[
                PostbackAction(
                    label='預約系統',
                    display_text='@我要預約',
                    data='sendDatetime(event)'
                ),
                PostbackAction(
                    label='預約查詢',
                    display_text='我要預約',
                    data='q2'
                ),
                PostbackAction(
                    label='場次',
                    display_text='我要預約',
                    data='q3'
                ),
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message) 
      
    
    elif mtext == '預約資料':  
            try:
                message=TextSendMessage(#文字傳送格式---------------
                    text=strto()
                )#文字傳送格式---------------
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,
      
                                           TextSendMessage(text='發生錯誤!'))
    elif mtext == '@我要預約':
         sendDatetime(event)            
            
def sendDatetime(event):
    try:
        carousel_template_message = TemplateSendMessage(
                alt_text='功能選單',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/3SvSaue.png',
                    title='麻將預約',
                    text='請點擊',
                    actions=[
                        DatetimePickerTemplateAction(
                            label="選取日期",
                            data="q1",#觸發 postback 事件
                            #data="action=sell&mode=date",#觸發 postback 事件
                            mode="date",
                            #initial="new Date",
                            #initial="2022-10-19",
                            min="2022-10-01",
                            max="2023-10-10"
                        )     
                              
                    ]
                )
                  
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    except:
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text='發生錯誤!'))      
     
@handler.add(PostbackEvent)  
def handle_postback(event):
    postback= event.postback.data
    try:
        if postback == "q1":
            #if backdata.get('mode') == 'date':
            dt ='日期為:'+ event.postback.params.get('date')#抓取輸入 日期
            message = dt
               
            line_bot_api.reply_message(event.reply_token,TextSendMessage(message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage('發生錯誤')) 
        




        
        
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

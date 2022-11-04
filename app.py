# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 22:55:28 2022

@author: User
"""


import gspread
from seett  import *



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

 
 



# 必須放上自己的Channel Access Token  #  medbot 02
line_bot_api = LineBotApi('3By8v6Y6J286AHBSC+yZBZnmQPk++dNcx7m0zw6ihE6b1yIwEMDWXmBrXrLBFPmcSVAR4fWbeK/F0fqD9YWqF77qbCk8WjsIwhpTjYiY+i4B8c2toRi/HwvJiD3AXR0FfnPPBhPlHVwNczVbQ+ZA3AdB04t89/1O/w1cDnyilFU=')

# 必須放上自己的Channel Secret
handler = WebhookHandler('d53c1e419d3e95f3211926807d541fe3')#  medbot 02

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


"""

@handler.add(PostbackEvent)  
def handle_postback(event):
    postback= event.postback.data
    try:
        if postback == "q1":
            
            carousel_template_message = TemplateSendMessage(
                    alt_text='功能選單',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/3SvSaue.png',
                        title='集元果菜單',
                        text='請選擇',
                        actions=[
                            DatetimePickerTemplateAction(
                                label="選取日期",
                                data="q2",#觸發 postback 事件
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
        line_bot_api.reply_message(event.reply_token,TextSendMessage('發生錯誤'))
    if postback == "q2":
        #if backdata.get('mode') == 'date':
        dt ='日期為:'+ event.postback.params.get('date')+ss#抓取輸入 日期
        message = dt
           
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))                              

"""

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '#背闊肌訓練#':  
        carousel_template_message = TemplateSendMessage(
            alt_text='功能選單',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/VCTeGLb.jpg',
                        title='上下運動',
                        text='背闊肌訓練',
                        actions=[
                            URIAction(
                                label='動作影片',
                                uri='https://liff.line.me/1657584801-YVvzvWOx'
                            ),                       
                            MessageAction(
                                label='訓練',
                                text="@背闊肌-上下運動@"
                                
                            )
                        ]
                    ),
                   
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/VCTeGLb.jpg',
                        title='前後運動',
                        text='背闊肌訓練',
                       actions=[
                           URIAction(
                               label='動作影片',
                               uri='https://liff.line.me/1657584801-YVvzvWOx'
                           ),                       
                           MessageAction(
                               label='訓練',
                               text="@背闊肌-前後運動@"
                               
                           )
          
                        ]
                    ),
                    
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/VCTeGLb.jpg',
                        title='背闊肌訓練',
                        text='運動',
                        actions=[
                            MessageAction(
                                label='影片',
                                text="@..."
                            ),                      
                            MessageAction(
                                label='訓練',
                                text="@@"
                                
                            )
                        ]
                    ),
                    
                    
                    
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    
       
      
    elif mtext == '@背闊肌-上下運動@':  
            buttons_template_message = TemplateSendMessage(
                    alt_text='背部',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/VCTeGLb.jpg',
                        title='背闊肌-上下運動',
                        text='健身紀錄',
                        actions=[
                            MessageAction(
                                label='歷史紀錄',
                                text=g1g1()+"\n"+g1g2()+"\n"+g1g3()
                               ),
                            URIAction(
                                label='訓練紀錄',
                                uri='https://liff.line.me/1657584801-3LMWM0Pd'
                            ), 
                        ]
                    )
        )
            line_bot_api.reply_message(event.reply_token,buttons_template_message)        
        
    elif mtext == '@背闊肌-前後運動@':  
            buttons_template_message = TemplateSendMessage(
                    alt_text='背部',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/VCTeGLb.jpg',
                        title='背闊肌-前後運動',
                        text='健身紀錄',
                        actions=[
                            MessageAction(
                                label='歷史紀錄',
                                text=gg1()+"\n"+gg2()+"\n"+gg3()
                               ),
                            URIAction(
                                label='訓練紀錄',
                                uri='https://liff.line.me/1657584801-3LMWM0Pd'
                            ), 
                        ]
                    )
        )
            line_bot_api.reply_message(event.reply_token,buttons_template_message)      
        
        
        
        
    elif mtext == '@背部訓練':  
            buttons_template_message = TemplateSendMessage(
                    alt_text='背部',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/VCTeGLb.jpg',
                        title='背部訓練',
                        text='健身紀錄',
                        actions=[
                            MessageAction(
                                label='背闊肌訓練',
                                text='#背闊肌訓練#'
                               ),
                            MessageAction(
                                label='菱形肌訓練',
                                text='#菱形肌訓練#'
                            )
                        ]
                    )
        )
            line_bot_api.reply_message(event.reply_token,buttons_template_message)
     
        
     
        
     
        
     
        
     
        
     
    elif mtext == '@腿部訓練':  
            buttons_template_message = TemplateSendMessage(
                    alt_text='腿部',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/8YYODdF.jpg',
                        title='腿部訓練',
                        text='健身紀錄',
                        actions=[
                            URIAction(
                                   label='紀錄訓練',
                                   uri='https://liff.line.me/1657584801-Nr8D8J2m'
                               ),
                            MessageAction(
                                label='訓練日誌',
                                text='^腿部訓練日誌'
                            )
                        ]
                    )
        )
            line_bot_api.reply_message(event.reply_token,buttons_template_message)    
    elif mtext == '@肩部訓練':  
            buttons_template_message = TemplateSendMessage(
                    alt_text='肩部',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/yk4O9pH.png',
                        title='肩部訓練',
                        text='健身紀錄',
                        actions=[
                            URIAction(
                                   label='紀錄訓練',
                                   uri='https://liff.line.me/1657584801-8v6W65X4'
                               ),
                            MessageAction(
                                label='訓練日誌',
                                text='^肩部訓練日誌'
                            )
                        ]
                    )
        )
            line_bot_api.reply_message(event.reply_token,buttons_template_message)  
    elif mtext == '@二頭&三頭':  
            buttons_template_message = TemplateSendMessage(
                    alt_text='二頭&三頭',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/e5Dr9A9.jpg',
                        title='二頭&三頭訓練',
                        text='健身紀錄',
                        actions=[
                            URIAction(
                                   label='紀錄訓練',
                                   uri='https://liff.line.me/1657584801-MAj6j53G'
                               ),
                            MessageAction(
                                label='訓練日誌',
                                text='^二頭&三頭訓練日誌'
                            )
                        ]
                    )
        )
            line_bot_api.reply_message(event.reply_token,buttons_template_message)  
    elif mtext == '@胸部訓練':  
        buttons_template_message = TemplateSendMessage(
                alt_text='胸部',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/iglkQnd.jpg',
                    title='胸部訓練',
                    text='健身紀錄',
                    actions=[
                        URIAction(
                               label='紀錄訓練',
                               uri='https://liff.line.me/1657584801-4wm6mgPN'
                           ),
                        MessageAction(
                            label='訓練日誌',
                            text='^胸部訓練日誌'
                        )
                    ]
                )
    )
        line_bot_api.reply_message(event.reply_token,buttons_template_message)      
            
            
    elif mtext == '@腹肌訓練':  
            buttons_template_message = TemplateSendMessage(
                    alt_text='腹部訓練',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/PuRLsrN.jpg',
                        title='腹部訓練',
                        text='健身紀錄',
                        actions=[
                            URIAction(
                                   label='紀錄訓練',
                                   uri='https://liff.line.me/1657584801-VZ2Z21m7'
                               ),
                            MessageAction(
                                label='訓練日誌',
                                text='^腹部訓練日誌'
                            )
                        ]
                    )
        )
            line_bot_api.reply_message(event.reply_token,buttons_template_message)             
    
      
     
 
        




        
        
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

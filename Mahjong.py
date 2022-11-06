# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 22:55:08 2022

@author: User
"""
##使用API  一定要 開啟  Seet 跟雲端硬碟 的 API


import gspread

def ff():
    
    credentials = {
         "type": "service_account",
         "project_id": "my-project-workhard",
         "private_key_id": "8dd65185815c8395a91f67f4441a017f44f00042",
         "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDzx/q4A2x1M0Ou\ndAWpwqO9hudYxuYIqJxKAhIc70slksujspHdL2zMMI7nWodX+VG3fYe3le6GZJD3\nuar95uWwp5t8S5KopMpj7i4AzSn+NbvApOx9/OAZD0yUfZ0JjSdcXDXSq7jJvQsG\nc3cRkrXvLorP6Stpbz/eh9XBmJ3eVVp8zzgNFj2yhrnXfsMVrPZ7TgKqy7rMR3XS\n04wHVd1qJGjbg6w0RkS2CP1RgGw32PuGlR0xEJ4fzwY/xCO/RyCE+tFJa5KOpkut\n0ySBoIpMvnkYlYU5a819uNEItn3vTza7yZwXz5YN8su0zKXmHKIEMra+TZoGDaTH\nucNnEmsBAgMBAAECggEABngtORY2vo5ZOWUMaJGNj5TVki00h74m6DeakL0C+bw4\nNR/Zr9XubpNdUcgGCedIIxmszG6pPwumUzuHhDoog+H/87Ig3+K3GSSGE0xei9oB\noZ6DaZjPUWHKV9YwIMOw2YEgqxs7HBya2l6d72I9IDdUMnK8u2ikLzPcEABoD4y8\nD/dJDKsVkH/EPjOSpDiwH4NXIwO8PB6LSwID90GlClqjxo8uvLOM6XXV23DuqyRE\nBaJznuAr4CFNxQ3zpQB6sBSIev/+Yt2FT1AklF4Xk/JIwpgQsF6lTUcU7kXChJd3\nW0qHRENKJOG4nIcjLKCbrN53vn7+GHRfuttXd3W2iQKBgQD/huIyYjt0qpmGUIrb\nkboKNRiL9RfEr+W+un/cS3s0rPfY7ibrLEOdjXIomniAwTfL8sP2o+mfD608C3sx\nR53NUqwgYbJjhXEIFDDp54anaValYHbB0bZK8FTx0YaV4GyHocTrpDQVQCE+kGCz\nC/K6KyJE0iPZi6Xg/Wm2ZcZj7QKBgQD0O4dJ3dkJirC2H55wn9XlcTcv25T42vdJ\nYEekO9fW/UADv80/+ICUsdzbyBVvU6uk3N7gJR4YpAYh4ON7HH/PSCogLZoMVGfi\nFpjQWSHabfdHNcEF2exrUU98kLHFoFiPw6S+Fk91zWhHIuxzJ6lHEGXyivsey2XA\nI7t8TTYo5QKBgEYQhCFwkgDxbltH5mtCUBLQcESgFb5WxNZBaSHMiKHu857F3mIJ\npxiiWjUL9hLH6DbCAD22wC5fLA8Uzti6XGiaTJwsba+gPVgLwUXBuEhbN+jsxGNs\nz2FI+OG9o/ugp+Gg19ANHELfbL4s9HbjxdCKV0ErpazW/8rrcXsT+QwZAoGAajOg\nhrxTblTCts9VBEBcsKLkjoj7ZKNCuMOHI6FqH/CL75Vt2Q1kTERzd5avy3MkxlHN\nEMbTKX/Zss2p3ZTs9uO4fbmWrRne+m89EAxSLjt3NZ3oS3UR2zDGUbJRu1AYcptu\nfcIR13X0jEpha0mp0F8PFcLdo+xqWHyxQEIK9QkCgYBe8bOUZFs98d8f85GQki7S\nFdLUrkmtJxBXC5LReVOxf2a45P+7RV2jLyB9/HtsMdtKS74Aqyu2kNhdar8M1mEf\n45dDfuwgsSTGp4NSbA4S6TNemS9Cb/31D5DGH06iYv4ERO627UvUOO0f8zx2pUKx\nkUrjtH4a1WQF7MjR4aG28g==\n-----END PRIVATE KEY-----\n",
         "client_email": "wuwu-264@my-project-workhard.iam.gserviceaccount.com",
         "client_id": "110694500794745845144",
         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
         "token_uri": "https://oauth2.googleapis.com/token",
         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/wuwu-264%40my-project-workhard.iam.gserviceaccount.com"
    }
    gc = gspread.service_account_from_dict(credentials)
    sh =gc .open("麻將預約後台")
    worksheet_list = sh.worksheets()  #抓取 所有工作表名稱
    worksheet = sh.worksheet("麻將") #選擇工作表
    data3= (worksheet.get_all_values() ) #抓取工作表內的資料 **需先指定開啟 工作表 worksheet = sh.worksheet("背部") #選擇文件
    data4=data3[len(data3)-1]#取最後一筆   #data4=data3[len(data3)] #抓取最後三筆資料
    
    
    data5_1="預約者:"
    data5_2="    日期:"
    data5_3="    時間:"
    data5=data5_1+data4[1]+"\n"+data5_2+data4[2]+"\n"+data5_3+data4[3]
    return  data5



def dd():    
    credentials = {
         "type": "service_account",
         "project_id": "my-project-workhard",
         "private_key_id": "8dd65185815c8395a91f67f4441a017f44f00042",
         "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDzx/q4A2x1M0Ou\ndAWpwqO9hudYxuYIqJxKAhIc70slksujspHdL2zMMI7nWodX+VG3fYe3le6GZJD3\nuar95uWwp5t8S5KopMpj7i4AzSn+NbvApOx9/OAZD0yUfZ0JjSdcXDXSq7jJvQsG\nc3cRkrXvLorP6Stpbz/eh9XBmJ3eVVp8zzgNFj2yhrnXfsMVrPZ7TgKqy7rMR3XS\n04wHVd1qJGjbg6w0RkS2CP1RgGw32PuGlR0xEJ4fzwY/xCO/RyCE+tFJa5KOpkut\n0ySBoIpMvnkYlYU5a819uNEItn3vTza7yZwXz5YN8su0zKXmHKIEMra+TZoGDaTH\nucNnEmsBAgMBAAECggEABngtORY2vo5ZOWUMaJGNj5TVki00h74m6DeakL0C+bw4\nNR/Zr9XubpNdUcgGCedIIxmszG6pPwumUzuHhDoog+H/87Ig3+K3GSSGE0xei9oB\noZ6DaZjPUWHKV9YwIMOw2YEgqxs7HBya2l6d72I9IDdUMnK8u2ikLzPcEABoD4y8\nD/dJDKsVkH/EPjOSpDiwH4NXIwO8PB6LSwID90GlClqjxo8uvLOM6XXV23DuqyRE\nBaJznuAr4CFNxQ3zpQB6sBSIev/+Yt2FT1AklF4Xk/JIwpgQsF6lTUcU7kXChJd3\nW0qHRENKJOG4nIcjLKCbrN53vn7+GHRfuttXd3W2iQKBgQD/huIyYjt0qpmGUIrb\nkboKNRiL9RfEr+W+un/cS3s0rPfY7ibrLEOdjXIomniAwTfL8sP2o+mfD608C3sx\nR53NUqwgYbJjhXEIFDDp54anaValYHbB0bZK8FTx0YaV4GyHocTrpDQVQCE+kGCz\nC/K6KyJE0iPZi6Xg/Wm2ZcZj7QKBgQD0O4dJ3dkJirC2H55wn9XlcTcv25T42vdJ\nYEekO9fW/UADv80/+ICUsdzbyBVvU6uk3N7gJR4YpAYh4ON7HH/PSCogLZoMVGfi\nFpjQWSHabfdHNcEF2exrUU98kLHFoFiPw6S+Fk91zWhHIuxzJ6lHEGXyivsey2XA\nI7t8TTYo5QKBgEYQhCFwkgDxbltH5mtCUBLQcESgFb5WxNZBaSHMiKHu857F3mIJ\npxiiWjUL9hLH6DbCAD22wC5fLA8Uzti6XGiaTJwsba+gPVgLwUXBuEhbN+jsxGNs\nz2FI+OG9o/ugp+Gg19ANHELfbL4s9HbjxdCKV0ErpazW/8rrcXsT+QwZAoGAajOg\nhrxTblTCts9VBEBcsKLkjoj7ZKNCuMOHI6FqH/CL75Vt2Q1kTERzd5avy3MkxlHN\nEMbTKX/Zss2p3ZTs9uO4fbmWrRne+m89EAxSLjt3NZ3oS3UR2zDGUbJRu1AYcptu\nfcIR13X0jEpha0mp0F8PFcLdo+xqWHyxQEIK9QkCgYBe8bOUZFs98d8f85GQki7S\nFdLUrkmtJxBXC5LReVOxf2a45P+7RV2jLyB9/HtsMdtKS74Aqyu2kNhdar8M1mEf\n45dDfuwgsSTGp4NSbA4S6TNemS9Cb/31D5DGH06iYv4ERO627UvUOO0f8zx2pUKx\nkUrjtH4a1WQF7MjR4aG28g==\n-----END PRIVATE KEY-----\n",
         "client_email": "wuwu-264@my-project-workhard.iam.gserviceaccount.com",
         "client_id": "110694500794745845144",
         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
         "token_uri": "https://oauth2.googleapis.com/token",
         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/wuwu-264%40my-project-workhard.iam.gserviceaccount.com"
    }
    gc = gspread.service_account_from_dict(credentials)
    sh =gc .open("麻將預約後台")
    worksheet_list = sh.worksheets()  #抓取 所有工作表名稱
    worksheet = sh.worksheet("麻將") #選擇工作表
    data3= (worksheet.get_all_values() ) #抓取工作表內的資料 **需先指定開啟 工作表 worksheet = sh.worksheet("背部") #選擇文件
    data4=  data3[len(data3)-3:len(data3)+1] #抓取最後三筆資料
    
    data5_1="預約者:"
    data5_2="    日期:"
    data5_3="\n"
    data5_4="    時間:"
    data5=[ data5_1+i[1]+"\n"+data5_2+i[2]+ data5_3+ data5_4+i[4]  for i in data4 ]
    
    data6=data5[0]+data5_3+data5[1]+data5_3+data5[2]
    return  data6


    
credentials = {
     "type": "service_account",
     "project_id": "my-project-workhard",
     "private_key_id": "8dd65185815c8395a91f67f4441a017f44f00042",
     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDzx/q4A2x1M0Ou\ndAWpwqO9hudYxuYIqJxKAhIc70slksujspHdL2zMMI7nWodX+VG3fYe3le6GZJD3\nuar95uWwp5t8S5KopMpj7i4AzSn+NbvApOx9/OAZD0yUfZ0JjSdcXDXSq7jJvQsG\nc3cRkrXvLorP6Stpbz/eh9XBmJ3eVVp8zzgNFj2yhrnXfsMVrPZ7TgKqy7rMR3XS\n04wHVd1qJGjbg6w0RkS2CP1RgGw32PuGlR0xEJ4fzwY/xCO/RyCE+tFJa5KOpkut\n0ySBoIpMvnkYlYU5a819uNEItn3vTza7yZwXz5YN8su0zKXmHKIEMra+TZoGDaTH\nucNnEmsBAgMBAAECggEABngtORY2vo5ZOWUMaJGNj5TVki00h74m6DeakL0C+bw4\nNR/Zr9XubpNdUcgGCedIIxmszG6pPwumUzuHhDoog+H/87Ig3+K3GSSGE0xei9oB\noZ6DaZjPUWHKV9YwIMOw2YEgqxs7HBya2l6d72I9IDdUMnK8u2ikLzPcEABoD4y8\nD/dJDKsVkH/EPjOSpDiwH4NXIwO8PB6LSwID90GlClqjxo8uvLOM6XXV23DuqyRE\nBaJznuAr4CFNxQ3zpQB6sBSIev/+Yt2FT1AklF4Xk/JIwpgQsF6lTUcU7kXChJd3\nW0qHRENKJOG4nIcjLKCbrN53vn7+GHRfuttXd3W2iQKBgQD/huIyYjt0qpmGUIrb\nkboKNRiL9RfEr+W+un/cS3s0rPfY7ibrLEOdjXIomniAwTfL8sP2o+mfD608C3sx\nR53NUqwgYbJjhXEIFDDp54anaValYHbB0bZK8FTx0YaV4GyHocTrpDQVQCE+kGCz\nC/K6KyJE0iPZi6Xg/Wm2ZcZj7QKBgQD0O4dJ3dkJirC2H55wn9XlcTcv25T42vdJ\nYEekO9fW/UADv80/+ICUsdzbyBVvU6uk3N7gJR4YpAYh4ON7HH/PSCogLZoMVGfi\nFpjQWSHabfdHNcEF2exrUU98kLHFoFiPw6S+Fk91zWhHIuxzJ6lHEGXyivsey2XA\nI7t8TTYo5QKBgEYQhCFwkgDxbltH5mtCUBLQcESgFb5WxNZBaSHMiKHu857F3mIJ\npxiiWjUL9hLH6DbCAD22wC5fLA8Uzti6XGiaTJwsba+gPVgLwUXBuEhbN+jsxGNs\nz2FI+OG9o/ugp+Gg19ANHELfbL4s9HbjxdCKV0ErpazW/8rrcXsT+QwZAoGAajOg\nhrxTblTCts9VBEBcsKLkjoj7ZKNCuMOHI6FqH/CL75Vt2Q1kTERzd5avy3MkxlHN\nEMbTKX/Zss2p3ZTs9uO4fbmWrRne+m89EAxSLjt3NZ3oS3UR2zDGUbJRu1AYcptu\nfcIR13X0jEpha0mp0F8PFcLdo+xqWHyxQEIK9QkCgYBe8bOUZFs98d8f85GQki7S\nFdLUrkmtJxBXC5LReVOxf2a45P+7RV2jLyB9/HtsMdtKS74Aqyu2kNhdar8M1mEf\n45dDfuwgsSTGp4NSbA4S6TNemS9Cb/31D5DGH06iYv4ERO627UvUOO0f8zx2pUKx\nkUrjtH4a1WQF7MjR4aG28g==\n-----END PRIVATE KEY-----\n",
     "client_email": "wuwu-264@my-project-workhard.iam.gserviceaccount.com",
     "client_id": "110694500794745845144",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/wuwu-264%40my-project-workhard.iam.gserviceaccount.com"
}
gc = gspread.service_account_from_dict(credentials)
sh =gc .open("麻將預約資料庫")
worksheet_list = sh.worksheets()  #抓取 所有工作表名稱
worksheet = sh.worksheet("麻將") #選擇工作表
data3= (worksheet.get_all_values() ) #抓取工作表內的資料 **需先指定開啟 工作表 worksheet = sh.worksheet("背部") #選擇文件
data4=  data3[len(data3)-3:len(data3)+1] #抓取最後三筆資料

data5_1="預約者:"
data5_2="    日期:"
data5_3="\n"
data5_4="時間:"
data5=[ data5_1+i[1]+"\n"+data5_2+i[2]+ data5_4+i[4]  for i in data4 ]

data6=data5[0]+data5_3+data5[1]+data5_3+data5[2]
    


  
"""
for i in 
data5_1="預約者:"
data5_2="    時間:"
data5=data5_1+data4[1]+"\n"+data5_2+data4[2]

"""


#指令懶人包
"""
worksheet = sh.worksheet("背部") #選擇工作表

list_of_lists = str(worksheet.get_all_values())  #抓取工作表內的資料 **需先指定開啟 工作表 worksheet = sh.worksheet("背部") #選擇文件

list_of_dicts = worksheet.get_all_records() #變字典 清單
#worksheet_list = sh.worksheets()  #抓取 所有工作表名稱
#ss=str(sh.sheet1.get('A1:C1'))#範圍 橫向
#ss=str(sh.sheet1.get('A1:A4'))#範圍 直向

#data6="\n".join([str(_) for _ in data5]) #將清單 變成一串字串
"""


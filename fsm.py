from transitions.extensions import GraphMachine
import sys
import random
from io import BytesIO

import telegram
import youtube_dl

from flask import Flask, request, send_file

import urllib.request

from urllib.request import urlopen

class TocMachine(GraphMachine):
    global x
    global y
    global z
    global w
    global v
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
#**********************************************************1000
    def is_going_to_state1000(self, update):
        print('state1000 inging******************************')
        text = update.message.text
        return text.lower() == 'hi' or text.lower() == 'hello'
    def on_enter_state1000(self, update):
        update.message.reply_text("hi")
        update.message.reply_text("what do you want to do? food , music or chat")
        #photo=urllib.request.urlopen('http://img05.tooopen.com/images/20150925/tooopen_sy_143684733881.jpg')
        #print(photo.read())
        #bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
        #update.message.reply_photo("https://upload.wikimedia.org/wikipedia/zh-yue/a/ab/Apple-logo.png")
        #update.message.reply_vedio('https://www.youtube.com/results?search_query=%E8%96%9B%E4%B9%8B%E8%AC%99')
        #self.go_back(update)
    def on_exit_state1000(self, update):
        print('Leaving state1000')
#**********************************************************      
#**********************************************************1
    def is_going_to_state1(self, update):
        print('state1 inging******************************')
        text = update.message.text
        return text.lower() == 'food'
    def on_enter_state1(self, update):
        update.message.reply_text("what do you want to eat? breakfast, lunch , dinner or late-night supper")
        #photo=urllib.request.urlopen('http://img05.tooopen.com/images/20150925/tooopen_sy_143684733881.jpg')
        #print(photo.read())
        #bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
        #update.message.reply_photo("https://upload.wikimedia.org/wikipedia/zh-yue/a/ab/Apple-logo.png")
        #update.message.reply_vedio('https://www.youtube.com/results?search_query=%E8%96%9B%E4%B9%8B%E8%AC%99')
        #self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')
#**********************************************************5,9,19,13
#breakfast
    def is_going_to_state5(self, update):
        print('state5 inging******************************')
        text = update.message.text
        return text.lower() == 'breakfast'
#breakfast
    def on_enter_state5(self, update):
        a1="https://farm8.staticflickr.com/7409/16383770940_8624a1e5c1_c.jpg"
        a2="http://img.foodieteller.com/20170217135950_76.jpg"
        a3="http://img.foodieteller.com/20170217142229_68.jpg"
        a4="http://img.foodieteller.com/20170217002803_97.jpg"
        a5="http://img.foodieteller.com/20170217133557_72.jpg"
        a6="http://img.foodieteller.com/20170217134644_44.jpg"
        a7="http://img.foodieteller.com/20170217143536_41.jpg"
        a8="http://img.foodieteller.com/20170217144814_6.jpg"
        a9="http://img.foodieteller.com/20170217145652_88.jpg"
        a10="http://img.foodieteller.com/20170217150253_45.jpg"
        a11="http://img.foodieteller.com/20170217151226_12.jpg"
        a12="http://img.foodieteller.com/20170217151713_25.jpg"
        a13="http://img.foodieteller.com/20170217152818_10.jpg"
        a14="http://img.foodieteller.com/20170217153524_95.jpg"
        a15="http://img.foodieteller.com/20170217154245_51.jpg"
        i=random.choice([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15])
        #i=random.choice ( ["https://farm8.staticflickr.com/7409/16383770940_8624a1e5c1_c.jpg","http://img.foodieteller.com/20170217135950_76.jpg","http://img.foodieteller.com/20170217142229_68.jpg","http://img.foodieteller.com/20170217002803_97.jpg","http://img.foodieteller.com/20170217133557_72.jpg","http://img.foodieteller.com/20170217134644_44.jpg","http://img.foodieteller.com/20170217143536_41.jpg","http://img.foodieteller.com/20170217144814_6.jpg","http://img.foodieteller.com/20170217145652_88.jpg","http://img.foodieteller.com/20170217150253_45.jpg","http://img.foodieteller.com/20170217151226_12.jpg","http://img.foodieteller.com/20170217151713_25.jpg","http://img.foodieteller.com/20170217152818_10.jpg","http://img.foodieteller.com/20170217153524_95.jpg","http://img.foodieteller.com/20170217154245_51.jpg"])
        update.message.reply_photo(i)
        if i==a13:
            update.message.reply_text("無名早餐")
        update.message.reply_text("Do you want to get more information about this breakfast? yes(to get the menu) , no(to get other breakfast) or back(back to the previous state) ")
        global x
        if i==a1:
            x=1
            print('****************1**********************')
        elif i==a2:
            x=2
            print('****************2**********************')
        elif i==a3:
            x=3
            print('****************3**********************')
        elif i==a4:
            x=4
            print('****************4**********************')
        elif i==a5:
            x=5
            print('****************5*********************')
        elif i==a6:
            x=6
            print('****************6**********************')
        elif i==a7:
            x=7
            print('****************7**********************')
        elif i==a8:
            x=8
            print('****************8**********************')
        elif i==a9:
            x=9
            print('****************9**********************')
        elif i==a10:
            x=10
            print('****************10**********************')
        elif i==a11:
            x=11
            print('****************11**********************')
        elif i==a12:
            x=12
            print('****************12**********************')
        elif i==a13:
            x=13
            print('****************13**********************')
        elif i==a14:
            x=14
            print('****************14**********************')
        else:
            x=15
            print('****************15**********************')
#breakfast           
    def on_exit_state5(self, update):
        print('Leaving state5')
#**********************************************************
#breakfast_menu
    def is_going_to_state9(self, update):
        print('state9 inging******************************')
        text = update.message.text
        return text.lower() == 'yes'
#breakfast_menu
    def on_enter_state9(self, update):
        update.message.reply_text("It's the menu")
        global x
        print(x)
        print('********************')
        if x==1:
            update.message.reply_photo("http://img.foodieteller.com/20170217132442_57.jpg") 
        elif x==2:
            update.message.reply_photo("http://img.foodieteller.com/20170217140255_55.jpg")
        elif x==3:
            update.message.reply_photo("http://img.foodieteller.com/20170217142355_47.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20170217142620_6.jpg")
        elif x==4:
            update.message.reply_photo("http://img.foodieteller.com/20170221211117_94.jpg")
        elif x==5:
            update.message.reply_photo("http://img.foodieteller.com/20170411225325_99.jpg")
        elif x==6:
            update.message.reply_photo("http://img.foodieteller.com/20170217134836_16.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20170217134839_46.jpg")
        elif x==7:
            update.message.reply_photo("http://img.foodieteller.com/20170217143702_52.jpg")
        elif x==8:
            update.message.reply_photo("http://img.foodieteller.com/20170217145117_22.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20170217145136_44.jpg")
        elif x==9:
            update.message.reply_photo("http://img.foodieteller.com/20170217145916_94.jpg")
        elif x==10:
            update.message.reply_photo("http://img.foodieteller.com/20170217150340_20.jpg")
        elif x==11:
            update.message.reply_photo("http://img.foodieteller.com/20170217151420_29.jpg")
        elif x==12:
            update.message.reply_photo("http://img.foodieteller.com/20170224230917_66.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20170224230939_6.jpg")
        elif x==13:
            update.message.reply_photo("http://img.foodieteller.com/20170217153150_71.jpg")
        elif x==14:
            update.message.reply_photo("http://img.foodieteller.com/20170217153639_20.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20170217153652_52.jpg")
        else:
            update.message.reply_photo("http://img.foodieteller.com/20170217154643_73.jpg") 
        update.message.reply_text("Do you want to get more information about this breakfast? yes(to get the information) , back(back to the previous state) or food(back to the food state) ")
        #self.go_back(update)
#breakfast_menu
    def on_exit_state9(self, update):
        print('Leaving state9')
#**********************************************************
#breakfast_not_menu
    def is_going_to_state19(self, update):
        print('state19 inging******************************')
        text = update.message.text
        return text.lower() == 'no' 
#breakfast_not_menu
    def on_enter_state19(self, update):
        update.message.reply_text("I'm entering state19")
        #self.go_back(update)
#breakfast_not_menu
    def on_exit_state19(self, update):
        print('Leaving state19')
#**********************************************************  
#breakfast_information
    def is_going_to_state13(self, update):
        print('state13 inging******************************')
        text = update.message.text
        return text.lower() == 'information'
#breakfast_information
    def on_enter_state13(self, update):
        update.message.reply_text("It's the information")
        global x
        print(x)
        print('********************')
        if x==1:
            update.message.reply_text("勝利早點")
            update.message.reply_text("地址：台南市東區勝利路119號")
            update.message.reply_text("電話：06-2386043")
            update.message.reply_text("營業時間：16:30-10:30(宵夜、早餐都賣)")
        elif x==2:
            update.message.reply_text("老丘早餐")
            update.message.reply_text("地址：台南市東區勝利路135號")
            update.message.reply_text("電話：0920268523")
            update.message.reply_text("營業時間：06:00-12:00（週日公休)")
        elif x==3:
            update.message.reply_text("大成美食")
            update.message.reply_text("地址：台南市東區大學路西段47號")
            update.message.reply_text("電話：06-2368457")
            update.message.reply_text("營業時間：06:00-12:00（週日公休）")
        elif x==4:
            update.message.reply_text("緹克廚房")
            update.message.reply_text("地址：台南市北區勝利路407號")
            update.message.reply_text("電話：06-2341872")
            update.message.reply_text("營業時間：06:00-13:30")
        elif x==5:
            update.message.reply_text("良辰吉食")
            update.message.reply_text("地址：台南市北區勝利路210號")
            update.message.reply_text("電話：06-2373996")
            update.message.reply_text("營業時間：05:00-13:30")
        elif x==6:
            update.message.reply_text("A-bao")
            update.message.reply_text("地址：台南市北區勝利路204號")
            update.message.reply_text("電話：06-2066620")
            update.message.reply_text("營業時間：05:00-13:30")
        elif x==7:
            update.message.reply_text("海鷗牌餐飲城")
            update.message.reply_text("地址：台南市東區勝利路54號")
            update.message.reply_text("電話：06-2092598")
            update.message.reply_text("營業時間：早餐時段")
        elif x==8:
            update.message.reply_text("元之氣早午餐輕食")
            update.message.reply_text("地址：台南市東區勝利路50-4號")
            update.message.reply_text("電話：06-2007096 ")
            update.message.reply_text("營業時間：05:30-12:30")
        elif x==9:
            update.message.reply_text("少爺手作蛋餅")
            update.message.reply_text("地址：台南市民族路一段20號")
            update.message.reply_text("電話：06-2085077")
            update.message.reply_text("營業時間：06:00-12:00")
        elif x==10:
            update.message.reply_text("阿公阿婆蛋餅")
            update.message.reply_text("地址：台南市東區小東路198巷10號")
            update.message.reply_text("電話：06-2747580")
            update.message.reply_text("營業時間：06:30-12:00 (周一公休)")
        elif x==11:
            update.message.reply_text("黑色香蕉(庭園早餐)")
            update.message.reply_text("地址：台南市長榮路三段27號")
            update.message.reply_text("電話：06-2081281")
            update.message.reply_text("營業時間：06:00-12:00")
        elif x==12:
            update.message.reply_text("彩虹城堡")
            update.message.reply_text("地址：台南市東區大學路22巷19號")
            update.message.reply_text("電話：06-2091152")
            update.message.reply_text("營業時間：07:00-20:30")
        elif x==13:
            update.message.reply_text("長榮路無名早餐")
            update.message.reply_text("地址：台南市長榮路三段3號")
            update.message.reply_text("營業時間：06:00-11:00(週日公休)")
        elif x==14:
            update.message.reply_text("弘爺漢堡")
            update.message.reply_text("地址：台南市東區東和路125號")
            update.message.reply_text("電話：06-2388250")
            update.message.reply_text("營業時間：05:00-13:00")
        else:
            update.message.reply_text("水工坊早午餐")
            update.message.reply_text("地址：台南市東區怡東路91號")
            update.message.reply_text("電話：06-2357371")
            update.message.reply_text("營業時間：07:10-14:00、17:00-20:00")
        update.message.reply_text("Do you want to turn to the food state? yes(back to the food state) , no(to go to the initial state) or back(back to the previous state) ")
        #self.go_back(update)
#breakfast_information
    def on_exit_state13(self, update):
        print('Leaving state13')
#**********************************************************25,29,39,23
#lunch
    def is_going_to_state25(self, update):
        print('state25 inging******************************')
        text = update.message.text
        return text.lower() == 'lunch'
#lunch
    def on_enter_state25(self, update):
        a1="http://img.foodieteller.com/20170502140109_60.jpg"
        a2="http://img.foodieteller.com/20160910174827_91.jpg"
        a3="http://img.foodieteller.com/20160910174834_18.jpg"
        a4="http://img.foodieteller.com/20160910174821_86.jpg"
        a5="http://img.foodieteller.com/20170401113818_45.jpg"
        a6="http://img.foodieteller.com/20160910174800_84.jpg"
        a7="http://img.foodieteller.com/20160910174754_85.jpg"
        a8="http://img.foodieteller.com/20160910174747_22.jpg"
        a9="http://img.foodieteller.com/20170125170448_65.jpg"
        a10="http://img.foodieteller.com/20161129193515_1.jpg"
        i=random.choice([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10])
        update.message.reply_photo(i)
        update.message.reply_text("Do you want to get more information about this lunch? yes(to get the menu) , no(to get other lunch) or back(back to the previous state)  ")
        global y
        if i==a1:
            y=1
            print('****************1**********************')
        elif i==a2:
            y=2
            print('****************2**********************')
        elif i==a3:
            y=3
            print('****************3**********************')
        elif i==a4:
            y=4
            print('****************4**********************')
        elif i==a5:
            y=5
            print('****************5*********************')
        elif i==a6:
            y=6
            print('****************6**********************')
        elif i==a7:
            y=7
            print('****************7**********************')
        elif i==a8:
            y=8
            print('****************8**********************')
        elif i==a9:
            y=9
            print('****************9**********************')
        else:
            y=10
            print('****************10**********************')
#lunch
    def on_exit_state25(self, update):
        print('Leaving state25')
#**********************************************************
#lunch_menu
    def is_going_to_state29(self, update):
        print('state29 inging******************************')
        text = update.message.text
        return text.lower() == 'yes'
#lunch_menu
    def on_enter_state29(self, update):
        update.message.reply_text("It's the menu")
        global y
        print(y)
        print('********************')
        if y==1:
            update.message.reply_photo("http://img.foodieteller.com/20170502135753_54.jpg") 
        elif y==2:
            update.message.reply_photo("http://img.foodieteller.com/20160817010511_99.jpg")
        elif y==3:
            update.message.reply_photo("http://www.hibabino.com/wp-content/uploads/2015/11/P1010161.jpg")
            update.message.reply_photo("http://www.hibabino.com/wp-content/uploads/2015/11/P1010162.jpg")
        elif y==4:
            update.message.reply_photo("http://img.foodieteller.com/20161005012739_62.jpg")
        elif y==5:
            update.message.reply_photo("http://img.foodieteller.com/20170401113823_12.jpg")
        elif y==6:
            update.message.reply_photo("http://img.foodieteller.com/20160924022112_100.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022116_74.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022136_11.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022131_53.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022126_6.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022121_2.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022146_11.jpg")
        elif y==7:
            update.message.reply_photo("http://img.foodieteller.com/20160914063047_52.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160914063054_2.jpg")
        elif y==8:
            update.message.reply_photo("http://img.foodieteller.com/20160814171048_62.jpg")
        elif y==9:
            update.message.reply_photo("http://img.foodieteller.com/20170125170504_29.jpg")
        else:
            update.message.reply_photo("http://img.foodieteller.com/20161129193107_89.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20161129193109_6.jpg")
        update.message.reply_text("Do you want to get more information about this lunch? yes(to get the information) , back(back to the previous state) or food(back to the food state) ")
#lunch_menu       
    def on_exit_state29(self, update):
        print('Leaving state29')
#**********************************************************
#lunch_not_menu
    def is_going_to_state39(self, update):
        print('state39 inging******************************')
        text = update.message.text
        return text.lower() == 'no'
#lunch_not_menu
    def on_enter_state39(self, update):
        update.message.reply_text("I'm entering state39")
        #self.go_back(update)
#lunch_not_menu
    def on_exit_state39(self, update):
        print('Leaving state39')
#**********************************************************
#lunch_information    
    def is_going_to_state23(self, update):
        print('state23 inging******************************')
        text = update.message.text
        return text.lower() == 'information'
#lunch_information
    def on_enter_state23(self, update):
        update.message.reply_text("It's the information")
        global y
        print(y)
        print('********************')
        if y==1:
            update.message.reply_text("大豆豆嫩骨餐飲")
            update.message.reply_text("地址：臺南市東區長榮路3段36號")
            update.message.reply_text("電話：06-2008327")
            update.message.reply_text("營業時間：11:00–14:00, 17:00–21:00")
        elif y==2:
            update.message.reply_text("日喜蒸蛋飯")
            update.message.reply_text("地址：台南市育樂街238號")
            update.message.reply_text("電話：06-2089081")
            update.message.reply_text("營業時間：11:00-14:00/17:00-21:00(週六公休)")
        elif y==3:
            update.message.reply_text("老友小吃")
            update.message.reply_text("地址：台南市北區勝利路268號")
            update.message.reply_text("電話：06-2357564")
            update.message.reply_text("營業時間：10:00~21:30(休三節：端午、中秋、過年)")
        elif y==4:
            update.message.reply_text("元味屋")
            update.message.reply_text("地址：台南市東區育樂街160號")
            update.message.reply_text("電話：06-2368830")
            update.message.reply_text("營業時間：11:00-14:00/17:00-20:00 (周日公休)")
        elif y==5:
            update.message.reply_text("添福麵館")
            update.message.reply_text("地址：台南市北區長榮路四段73號")
            update.message.reply_text("電話：0977120112")
            update.message.reply_text("營業時間：10:00-22:00")
        elif y==6:
            update.message.reply_text("Cocina Quesadilla")
            update.message.reply_text("地址：台南市東豐路137號")
            update.message.reply_text("電話：0973230819")
            update.message.reply_text("營業時間：週一至六 11:30 – 2:30、17:00 – 21:00(週三、日公休)")
        elif y==7:
            update.message.reply_text("廣越美食店")
            update.message.reply_text("地址：台南市長榮路四段108號")
            update.message.reply_text("電話：06-2087799")
            update.message.reply_text("營業時間：11:00 – 3:00；16:30 – 20:00(週日公休)")
        elif y==8:
            update.message.reply_text("開元紅燒土魠魚羹")
            update.message.reply_text("地址：台南市北區開元路307號")
            update.message.reply_text("電話：06-2373195 ")
            update.message.reply_text("營業時間：08:00-19:00")
        elif y==9:
            update.message.reply_text("萬伯鹹粥")
            update.message.reply_text("地址：台南市北區長榮路四段156號")
            update.message.reply_text("電話：06-2352643")
            update.message.reply_text("營業時間：9:00–1:30")
        else:
            update.message.reply_text("上海好味道小籠湯包")
            update.message.reply_text("地址：台南市東區東安路26號")
            update.message.reply_text("電話：06-2081601")
            update.message.reply_text("營業時間：10:30–23:00")
        update.message.reply_text("Do you want to turn to the food state? yes(back to the food state) , no(to go to the initial state) or back(back to the previous state) ")
#lunch_information
    def on_exit_state23(self, update):
        print('Leaving state23')
#**********************************************************
#dinner
    def is_going_to_state45(self, update):
        print('state45 inging******************************')
        text = update.message.text
        return text.lower() == 'dinner'
#dinner
    def on_enter_state45(self, update):
        a1="http://img.foodieteller.com/20170502140109_60.jpg"
        a2="http://img.foodieteller.com/20160910174827_91.jpg"
        a3="http://img.foodieteller.com/20160910174834_18.jpg"
        a4="http://img.foodieteller.com/20160910174821_86.jpg"
        a5="http://img.foodieteller.com/20170401113818_45.jpg"
        a6="http://img.foodieteller.com/20160910174800_84.jpg"
        a7="http://img.foodieteller.com/20160910174754_85.jpg"
        a8="http://img.foodieteller.com/20160910174747_22.jpg"
        a9="http://img.foodieteller.com/20170125170448_65.jpg"
        a10="http://img.foodieteller.com/20161129193515_1.jpg"
        i=random.choice([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10])
        update.message.reply_photo(i)
        update.message.reply_text("Do you want to get more information about this dinner? yes(to get the menu) or no(to get other dinner) ")
        global z
        if i==a1:
            z=1
            print('****************1**********************')
        elif i==a2:
            z=2
            print('****************2**********************')
        elif i==a3:
            z=3
            print('****************3**********************')
        elif i==a4:
            z=4
            print('****************4**********************')
        elif i==a5:
            z=5
            print('****************5*********************')
        elif i==a6:
            z=6
            print('****************6**********************')
        elif i==a7:
            z=7
            print('****************7**********************')
        elif i==a8:
            z=8
            print('****************8**********************')
        elif i==a9:
            z=9
            print('****************9**********************')
        else:
            z=10
            print('****************10**********************')
#dinner
    def on_exit_state45(self, update):
        print('Leaving state45')
#**********************************************************
#dinner_menu
    def is_going_to_state49(self, update):
        print('state49 inging******************************')
        text = update.message.text
        return text.lower() == 'yes'
#dinner_menu
    def on_enter_state49(self, update):
        update.message.reply_text("It's the menu")
        global z
        print(z)
        print('********************')
        if z==1:
            update.message.reply_photo("http://img.foodieteller.com/20170502135753_54.jpg") 
        elif z==2:
            update.message.reply_photo("http://img.foodieteller.com/20160817010511_99.jpg")
        elif z==3:
            update.message.reply_photo("http://www.hibabino.com/wp-content/uploads/2015/11/P1010161.jpg")
            update.message.reply_photo("http://www.hibabino.com/wp-content/uploads/2015/11/P1010162.jpg")
        elif z==4:
            update.message.reply_photo("http://img.foodieteller.com/20161005012739_62.jpg")
        elif z==5:
            update.message.reply_photo("http://img.foodieteller.com/20170401113823_12.jpg")
        elif z==6:
            update.message.reply_photo("http://img.foodieteller.com/20160924022112_100.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022116_74.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022136_11.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022131_53.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022126_6.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022121_2.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160924022146_11.jpg")
        elif z==7:
            update.message.reply_photo("http://img.foodieteller.com/20160914063047_52.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20160914063054_2.jpg")
        elif z==8:
            update.message.reply_photo("http://img.foodieteller.com/20160814171048_62.jpg")
        elif z==9:
            update.message.reply_photo("http://img.foodieteller.com/20170125170504_29.jpg")
        else:
            update.message.reply_photo("http://img.foodieteller.com/20161129193107_89.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20161129193109_6.jpg")
        update.message.reply_text("Do you want to get more information about this dinner? yes(to get the information) , back(back to the previous state) or food(back to the food state) ")
#dinner_menu       
    def on_exit_state49(self, update):
        print('Leaving state49')
#**********************************************************
#dinner_not_menu
    def is_going_to_state59(self, update):
        print('state59 inging******************************')
        text = update.message.text
        return text.lower() == 'no'
#dinner_not_menu
    def on_enter_state59(self, update):
        update.message.reply_text("I'm entering state59")
        #self.go_back(update)
#dinner_not_menu
    def on_exit_state59(self, update):
        print('Leaving state59')
#**********************************************************
#dinner_information    
    def is_going_to_state33(self, update):
        print('state33 inging******************************')
        text = update.message.text
        return text.lower() == 'information'
#dinner_information
    def on_enter_state33(self, update):
        update.message.reply_text("It's the information")
        global z
        print(z)
        print('********************')
        if z==1:
            update.message.reply_text("大豆豆嫩骨餐飲")
            update.message.reply_text("地址：臺南市東區長榮路3段36號")
            update.message.reply_text("電話：06-2008327")
            update.message.reply_text("營業時間：11:00–14:00, 17:00–21:00")
        elif z==2:
            update.message.reply_text("日喜蒸蛋飯")
            update.message.reply_text("地址：台南市育樂街238號")
            update.message.reply_text("電話：06-2089081")
            update.message.reply_text("營業時間：11:00-14:00/17:00-21:00(週六公休)")
        elif z==3:
            update.message.reply_text("老友小吃")
            update.message.reply_text("地址：台南市北區勝利路268號")
            update.message.reply_text("電話：06-2357564")
            update.message.reply_text("營業時間：10:00~21:30(休三節：端午、中秋、過年)")
        elif z==4:
            update.message.reply_text("元味屋")
            update.message.reply_text("地址：台南市東區育樂街160號")
            update.message.reply_text("電話：06-2368830")
            update.message.reply_text("營業時間：11:00-14:00/17:00-20:00 (周日公休)")
        elif z==5:
            update.message.reply_text("添福麵館")
            update.message.reply_text("地址：台南市北區長榮路四段73號")
            update.message.reply_text("電話：0977120112")
            update.message.reply_text("營業時間：10:00-22:00")
        elif z==6:
            update.message.reply_text("Cocina Quesadilla")
            update.message.reply_text("地址：台南市東豐路137號")
            update.message.reply_text("電話：0973230819")
            update.message.reply_text("營業時間：週一至六 11:30 – 2:30、17:00 – 21:00(週三、日公休)")
        elif z==7:
            update.message.reply_text("廣越美食店")
            update.message.reply_text("地址：台南市長榮路四段108號")
            update.message.reply_text("電話：06-2087799")
            update.message.reply_text("營業時間：11:00 – 3:00；16:30 – 20:00(週日公休)")
        elif z==8:
            update.message.reply_text("開元紅燒土魠魚羹")
            update.message.reply_text("地址：台南市北區開元路307號")
            update.message.reply_text("電話：06-2373195 ")
            update.message.reply_text("營業時間：08:00-19:00")
        elif z==9:
            update.message.reply_text("萬伯鹹粥")
            update.message.reply_text("地址：台南市北區長榮路四段156號")
            update.message.reply_text("電話：06-2352643")
            update.message.reply_text("營業時間：9:00–1:30")
        else:
            update.message.reply_text("上海好味道小籠湯包")
            update.message.reply_text("地址：台南市東區東安路26號")
            update.message.reply_text("電話：06-2081601")
            update.message.reply_text("營業時間：10:30–23:00")
        update.message.reply_text("Do you want to turn to the food state? yes(back to the food state) , no(to go to the initial state) or back(back to the previous state) ")
#dinner_information
    def on_exit_state33(self, update):
        print('Leaving state33')
#**********************************************************
#late-night supper
    def is_going_to_state65(self, update):
        print('state65 inging******************************')
        text = update.message.text
        return text.lower() == 'late-night supper'
#late-night supper
    def on_enter_state65(self, update):
        a1="http://iphoto.ipeen.com.tw/photo/comment/697890/610492/cgmf76ab97b693845cfe029f1d0d58136db528.jpg"
        a2="http://img.foodieteller.com/20161114062851_74.jpg"
        a3="https://farm4.staticflickr.com/3915/14495583752_2ed7d3da10_c.jpg"
        a4="https://pic.pimg.tw/kammy12/1431617458-2064705445_n.jpg"
        a5="https://farm9.staticflickr.com/8113/29596137360_1509db8e40_c.jpg"
        a6="http://iphoto.ipeen.com.tw/photo/comment/697890/610492/cgmf76ab97b693845cfe029f1d0d58136db528.jpg"
        a7="https://farm8.staticflickr.com/7409/16383770940_8624a1e5c1_c.jpg"
        a8="https://pic.pimg.tw/ku5553221/1470068259-3043085363.jpg"
        a9="http://img.foodieteller.com/20170125170448_65.jpg"
        a10="http://img.foodieteller.com/20161129193515_1.jpg"
        i=random.choice([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10])
        update.message.reply_photo(i)
        update.message.reply_text("Do you want to get more information about this late-night supper? yes(to get the menu) or no(to get other late-night supper) ")
        global w
        if i==a1:
            w=1
            print('****************1**********************')
        elif i==a2:
            w=2
            print('****************2**********************')
        elif i==a3:
            w=3
            print('****************3**********************')
        elif i==a4:
            w=4
            print('****************4**********************')
        elif i==a5:
            w=5
            print('****************5*********************')
        elif i==a6:
            w=6
            print('****************6**********************')
        elif i==a7:
            w=7
            print('****************7**********************')
        elif i==a8:
            w=8
            print('****************8**********************')
        elif i==a9:
            w=9
            print('****************9**********************')
        else:
            w=10
            print('****************10**********************')
#late-night supper
    def on_exit_state65(self, update):
        print('Leaving state65')
#**********************************************************
#late-night supper_menu
    def is_going_to_state69(self, update):
        print('state69 inging******************************')
        text = update.message.text
        return text.lower() == 'yes'
#late-night supper_menu
    def on_enter_state69(self, update):
        update.message.reply_text("It's the menu")
        global w
        print(w)
        print('********************')
        if w==1:
            update.message.reply_photo("http://pic.pimg.tw/imsean/1401966859-1181315599.jpg") 
        elif w==2:
            update.message.reply_photo("http://img.foodieteller.com/20161114062026_41.jpg")
        elif w==3:
            update.message.reply_text("店閱")
        elif w==4:
            update.message.reply_photo("https://pic.pimg.tw/kammy12/1431617450-3880989613_n.jpg")            
            update.message.reply_photo("https://pic.pimg.tw/kammy12/1431617451-1240382858_n.jpg")
            update.message.reply_photo("https://pic.pimg.tw/kammy12/1431617452-1712807384_n.jpg")
            update.message.reply_photo("https://pic.pimg.tw/kammy12/1431617454-2464507463_n.jpg")
        elif w==5:
            update.message.reply_photo("http://www.possession-tea.com/upload/products/20170318171117.jpg")
        elif w==6:
            update.message.reply_photo("http://pic.pimg.tw/imsean/1401966859-1181315599.jpg") 
        elif w==7:
            update.message.reply_photo("http://img.foodieteller.com/20170217132442_57.jpg")
        elif w==8:
            update.message.reply_photo("https://pic.pimg.tw/ku5553221/1469001946-3501870136_l.jpg")
            update.message.reply_photo("https://pic.pimg.tw/ku5553221/1469001945-266930609_l.jpg")
        elif w==9:
            update.message.reply_photo("http://img.foodieteller.com/20170125170504_29.jpg")
        else:
            update.message.reply_photo("http://img.foodieteller.com/20161129193107_89.jpg")
            update.message.reply_photo("http://img.foodieteller.com/20161129193109_6.jpg")
        update.message.reply_text("Do you want to get more information about this late-night supper? yes(to get the information) , back(back to the previous state) or food(back to the food state) ")
#late-night supper_menu       
    def on_exit_state69(self, update):
        print('Leaving state69')
#**********************************************************
#late-night supper_menu
    def is_going_to_state79(self, update):
        print('state79 inging******************************')
        text = update.message.text
        return text.lower() == 'no'
#late-night supper_not_menu
    def on_enter_state79(self, update):
        update.message.reply_text("I'm entering state79")
        #self.go_back(update)
#late-night supper_not_menu
    def on_exit_state79(self, update):
        print('Leaving state79')
#**********************************************************
#late-night supper_information    
    def is_going_to_state43(self, update):
        print('state43 inging******************************')
        text = update.message.text
        return text.lower() == 'information'
#late-night supper_information
    def on_enter_state43(self, update):
        update.message.reply_text("It's the information")
        global w
        print(w)
        print('********************')
        if w==1:
            update.message.reply_text("天蠍座燒烤")
            update.message.reply_text("地址：台南市東區東寧路340號(東寧郵局正對面，紅太陽飲料店旁)")
            update.message.reply_text("電話：0919137979")
            update.message.reply_text("營業時間：PM 17:00~AM 01:30 (每周一 二公休)")
        elif w==2:
            update.message.reply_text("小茂屋")
            update.message.reply_text("地址：台南市東區長榮路三段40號")
            update.message.reply_text("電話：06-2358162")
            update.message.reply_text("營業時間：11:00-00:00")
        elif w==3:
            update.message.reply_text("小東路麻辣關東煮")
            update.message.reply_text("地址：台南市東區小東路上，約在132巷巷口附近")
            update.message.reply_text("電話：06-2363299")
            update.message.reply_text("營業時間：07：30Pm-02:00Am")
        elif w==4:
            update.message.reply_text("夏沐綠野 鮮果汁冰沙茶飲")
            update.message.reply_text("地址：台南市東區育樂街35號")
            update.message.reply_text("電話：0975622262")
            update.message.reply_text("營業時間：11:00–23:00")
        elif w==5:
            update.message.reply_text("御私藏鮮奶茶")
            update.message.reply_text("地址：台南市東區育樂街17號")
            update.message.reply_text("電話：06-2092929")
            update.message.reply_text("營業時間：09:00–23:00")
        elif w==6:
            update.message.reply_text("天蠍座燒烤")
            update.message.reply_text("地址：台南市東區東寧路340號(東寧郵局正對面，紅太陽飲料店旁)")
            update.message.reply_text("電話：0919137979")
            update.message.reply_text("營業時間：PM 17:00~AM 01:30 (每周一 二公休)")
        elif w==7:
            update.message.reply_text("勝利早點")
            update.message.reply_text("地址：台南市東區勝利路119號")
            update.message.reply_text("電話：06-2386043")
            update.message.reply_text("營業時間：16:30-10:30(宵夜、早餐都賣)")
        elif w==8:
            update.message.reply_text("阿強冰店")
            update.message.reply_text("地址：台南市東區長榮路三段39號")
            update.message.reply_text("電話：06-2355768")
            update.message.reply_text("營業時間：10:00-00:30")
        elif w==9:
            update.message.reply_text("萬伯鹹粥")
            update.message.reply_text("地址：台南市北區長榮路四段156號")
            update.message.reply_text("電話：06-2352643")
            update.message.reply_text("營業時間：9:00–1:30")
        else:
            update.message.reply_text("上海好味道小籠湯包")
            update.message.reply_text("地址：台南市東區東安路26號")
            update.message.reply_text("電話：06-2081601")
            update.message.reply_text("營業時間：10:30–23:00")
        update.message.reply_text("Do you want to turn to the food state? yes(back to the food state) , no(to go to the initial state) or back(back to the previous state) ")
#late-night supper_information
    def on_exit_state43(self, update):
        print('Leaving state43')
#**********************************************************
#breakfast,lunch,dinner,late-night supper back to food
    def is_going_to_state101(self, update):
        print('state101 inging******************************')
        text = update.message.text
        return text.lower() == 'food'
    def on_enter_state101(self, update):
        update.message.reply_text("I'm entering state101")
        #self.go_back(update)
    def on_exit_state101(self, update):
        print('Leaving state101')
#**********************************************************
#breakfast,lunch,dinner,late-night supper back to finish
    def is_going_to_state100(self, update):
        print('state100 inging******************************')
        text = update.message.text
        return text.lower() == 'no'
    def on_enter_state100(self, update):
        update.message.reply_text("It's finish")
        update.message.reply_text("You can reselect food , music or chat")
        self.go_back(update)
    def on_exit_state100(self, update):
        print('Leaving state100')
#**********************************************************
#back 
    def is_going_to_state102(self, update):
        print('state102 inging******************************')
        text = update.message.text
        return text.lower() == 'back'
    def on_enter_state102(self, update):
        update.message.reply_text("I'm entering state102")
        #self.go_back(update)
    def on_exit_state102(self, update):
        print('Leaving state102')
#**********************************************************
#music
    def is_going_to_state2(self, update):
        print('state2 inging******************************')
        text = update.message.text
        return text.lower() == 'music'

    def on_enter_state2(self, update):
        update.message.reply_text("Do you want to listen to music ? yes(to get the music) or no(back to the initial state)")
        #self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
#********************************************************** 
#music_information
    def is_going_to_state6(self, update):
        print('state6 inging******************************')
        text = update.message.text
        return text.lower() == 'go to state6'
   
    def on_enter_state6(self, update):
        update.message.reply_text("It's the information of music")
        global v        
        i=random.randint(1,10)
        v=i
        if i==1:
            update.message.reply_text("黃明志&王力宏【飄向北方】 文慧如版")
        elif i==2:
            update.message.reply_text("周杰倫【告白氣球】")
        elif i==3:
            update.message.reply_text("魏如昀【聽見下雨的聲音】")
        elif i==4:
            update.message.reply_text("鄧紫棋【光年之外】")
        elif i==5:
            update.message.reply_text("張信哲【太想愛你】")
        elif i==6:
            update.message.reply_text("動力火車【外套】")
        elif i==7:
            update.message.reply_text("信【我選擇笑】")
        elif i==8:
            update.message.reply_text("林凡【歲月這把刀】")
        elif i==9:
            update.message.reply_text("品冠【隨時都在】")
        else:
            update.message.reply_text("蕭閎仁【因為我愛你】")
        update.message.reply_text("Do you want to listen to this music ? yes(to play music) or no(to get other music)")
        #self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')
#**********************************************************
#music_play
    def is_going_to_state10(self, update):
        print('state10 inging******************************')
        text = update.message.text
        return text.lower() == 'go to state10'

    def on_enter_state10(self, update):
        update.message.reply_text("It's the music")
        global v 
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
        with ydl:
            if v==1:
                result = ydl.extract_info('https://www.youtube.com/watch?v=oc5kSed3u44',download=False )
            elif v==2:
                result = ydl.extract_info('https://www.youtube.com/watch?v=MIFaBOLnoik',download=False )
            elif v==3:
                result = ydl.extract_info('https://www.youtube.com/watch?v=rGyon4SF8VM',download=False )
            elif v==4:
                result = ydl.extract_info('https://www.youtube.com/watch?v=tcNonA-VZ3E',download=False )
            elif v==5:
                result = ydl.extract_info('https://www.youtube.com/watch?v=Pv3t5XsbNV0',download=False )
            elif v==6:
                result = ydl.extract_info('https://www.youtube.com/watch?v=0eAoaB9-470',download=False )
            elif v==7:
                result = ydl.extract_info('https://www.youtube.com/watch?v=Mk1kDq_T8q8',download=False )
            elif v==8:
                result = ydl.extract_info('https://www.youtube.com/watch?v=pnkW5tzur2E',download=False )
            elif v==9:
                result = ydl.extract_info('https://www.youtube.com/watch?v=pWpHinO9i78',download=False )
            else:
                result = ydl.extract_info('https://www.youtube.com/watch?v=mr2cBsMgNqQ',download=False )

        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result

        print(video)
        video_url = video['url']
        print(video_url)
        update.message.reply_audio(video_url)
        update.message.reply_text("Do you want to listen to other music ? yes(to get other music) or no(to go to the initial state)")
        #self.go_back(update)

    def on_exit_state10(self, update):
        print('Leaving state10')
#**********************************************************
#chat
    def is_going_to_state3(self, update):
        print('state3 inging******************************')
        text = update.message.text
        return text.lower() == 'chat'
    
    def on_enter_state3(self, update):
        update.message.reply_text("你想要說些什麼？ hw , friend or other")
        update.message.reply_text("hw (計算理論作業的死線在後天喔，要記得交)")
        update.message.reply_text("friend (你是不是有上計算理論阿？)")
        update.message.reply_text("other (自由發揮)")
        #self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
#**********************************************************
#chat hw
    def is_going_to_state7(self, update):
        print('state7 inging******************************')
        text = update.message.text
        return text.lower() == 'hw'

    def on_enter_state7(self, update):
        update.message.reply_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNh6994Q2CYyM7YSgCXBp3RR46b2ACPkhzAFlMHa0nJPGs0Aq2")
        update.message.reply_text("你還想要說些什麼呢？ hw , friend or other")
        update.message.reply_text("hw (計算理論作業的死線在明天喔，要趕快交)")
        update.message.reply_text("friend (我記得沒錯你有上計算理論阿？)")
        update.message.reply_text("other (自由發揮)")
        #self.go_back(update)

    def on_exit_state7(self, update):
        print('Leaving state7')
#**********************************************************
#chat hw-1
    def is_going_to_state11(self, update):
        print('state11 inging******************************')
        text = update.message.text
        return text.lower() == 'go to state11'

    def on_enter_state11(self, update):
        update.message.reply_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtoslG-jCyE_88xJiZVDDt0azCI2QF_iZ6w-lAnwklFX8awITlbw")
        update.message.reply_text("別拖拖拉拉的～你還有什麼話要說？ hw , friend or other")
        update.message.reply_text("hw (計算理論作業的死線在今天喔，你交的出來嗎？)")
        update.message.reply_text("friend (我確定你有上計算理論阿？)")
        update.message.reply_text("other (自由發揮)")
        #self.go_back(update)

    def on_exit_state11(self, update):
        print('Leaving state11')
#**********************************************************
#chat hw-2
    def is_going_to_state15(self, update):
        print('state15 inging******************************')
        text = update.message.text
        return text.lower() == 'go to state15'

    def on_enter_state15(self, update):
        update.message.reply_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXvA6wJ_1Mh2eESAYj9UVRVDDFOHZ9l0Sm5-LTpFiY83FQh0xH")
        update.message.reply_text("再不說～我要走囉？ hw , friend or other")
        update.message.reply_text("hw (計算理論作業的死線只剩兩小時，你...交不出來)")
        update.message.reply_text("friend (難道我記錯了嗎？)")
        update.message.reply_text("other (自由發揮)")
        #self.go_back(update)

    def on_exit_state15(self, update):
        print('Leaving state15')
#**********************************************************
#chat other
    def is_going_to_state17(self, update):
        print('state17 inging******************************')
        text = update.message.text
        if text.lower() == 'friend' or text.lower() == 'hw':
            return 0
        else:
            return 1

    def on_enter_state17(self, update):
        update.message.reply_photo("http://scontent.cdninstagram.com/t51.2885-15/s480x480/e15/13636045_607919839367667_158110428_n.jpg?ig_cache_key=MTI5NTAzNTMwNTg3MTM4MzUwNQ%3D%3D.2")
        update.message.reply_text("你還想要說些什麼呢？ hw , friend or other")
        update.message.reply_text("hw (計算理論作業的死線在明天喔，要趕快交)")
        update.message.reply_text("friend (我記得沒錯你有上計算理論阿？)")
        update.message.reply_text("other (自由發揮)")
        #self.go_back(update)

    def on_exit_state17(self, update):
        print('Leaving state17')
#**********************************************************
#chat other_1
    def is_going_to_state171(self, update):
        print('state171 inging******************************')
        text = update.message.text
        return text.lower() == 'other'

    def on_enter_state171(self, update):
        update.message.reply_photo("http://scontent.cdninstagram.com/t51.2885-15/s480x480/e15/13636045_607919839367667_158110428_n.jpg?ig_cache_key=MTI5NTAzNTMwNTg3MTM4MzUwNQ%3D%3D.2")
        update.message.reply_text("別拖拖拉拉的～你還有什麼話要說？ hw , friend or other")
        update.message.reply_text("hw (計算理論作業的死線在今天喔，你交的出來嗎？)")
        update.message.reply_text("friend (我確定你有上計算理論阿？)")
        update.message.reply_text("other (自由發揮)")
        #self.go_back(update)

    def on_exit_state171(self, update):
        print('Leaving state171')
#**********************************************************
#chat other_2
    def is_going_to_state172(self, update):
        print('state172 inging******************************')
        text = update.message.text
        return text.lower() == 'other'

    def on_enter_state172(self, update):
        update.message.reply_photo("http://www.niusnews.com/upload/posts/po2_41288_1450254487.jpg")
        update.message.reply_text("再不說～我要走囉？ hw , friend or other")
        update.message.reply_text("hw (計算理論作業的死線只剩兩小時，你...交不出來)")
        update.message.reply_text("friend (難道我記錯了嗎？)")
        update.message.reply_text("other (自由發揮)")
        #self.go_back(update)

    def on_exit_state172(self, update):
        print('Leaving state172')
#**********************************************************
#chat friend
    def is_going_to_state27(self, update):
        print('state27 inging******************************')
        text = update.message.text
        return text.lower() == 'friend'

    def on_enter_state27(self, update):
        update.message.reply_photo("https://fsp.youthwant.com/images/580_1184348714942331.jpg")
        update.message.reply_text("你還想要說些什麼呢？ hw , friend or other")
        update.message.reply_text("hw (計算理論作業的死線在明天喔，要趕快交)")
        update.message.reply_text("friend (我記得沒錯你有上計算理論阿？)")
        update.message.reply_text("other (自由發揮)")
        #self.go_back(update)

    def on_exit_state27(self, update):
        print('Leaving state27')
#**********************************************************
#chat friend_1
    def is_going_to_state271(self, update):
        print('state271 inging******************************')
        text = update.message.text
        return text.lower() == 'friend'

    def on_enter_state271(self, update):
        update.message.reply_photo("https://s3-us-west-1.amazonaws.com/niusnews-imgs/377202_1.png")
        update.message.reply_text("別拖拖拉拉的～你還有什麼話要說？ hw , friend or other")
        update.message.reply_text("hw (計算理論作業的死線在今天喔，你交的出來嗎？)")
        update.message.reply_text("friend (我確定你有上計算理論阿？)")
        update.message.reply_text("other (自由發揮)")
        #self.go_back(update)

    def on_exit_state271(self, update):
        print('Leaving state271')
#**********************************************************
#chat friend_2
    def is_going_to_state272(self, update):
        print('state272 inging******************************')
        text = update.message.text
        return text.lower() == 'friend'

    def on_enter_state272(self, update):
        update.message.reply_photo("https://scontent-ams3-1.cdninstagram.com/t51.2885-15/s750x750/sh0.08/e35/15043859_698787033631691_6513644562416664576_n.jpg")
        update.message.reply_text("再不說～我要走囉？ hw , friend or other")
        update.message.reply_text("hw (計算理論作業的死線只剩兩小時，你...交不出來)")
        update.message.reply_text("friend (難道我記錯了嗎？)")
        update.message.reply_text("other (自由發揮)")
        #self.go_back(update)

    def on_exit_state272(self, update):
        print('Leaving state272')
#**********************************************************
#**********************************************************
#chat last
    def is_going_to_state77(self, update):
        print('state77 inging******************************')
        text = update.message.text
        return text.lower() == 'friend'

    def on_enter_state77(self, update):
        update.message.reply_photo("https://68.media.tumblr.com/b1502fcbc3e0e76d546397f702059e9e/tumblr_oarwo0UVeM1umk6azo1_1280.jpg")
        update.message.reply_text("還有話要說嗎？(自由發揮)")
        #self.go_back(update)
    
    def on_exit_state77(self, update):
        print('Leaving state77')
#**********************************************************
#chat last last
    def is_going_to_state78(self, update):
        print('state78 inging******************************')
        text = update.message.text
        if text.lower() == 'friend' or text.lower() == 'hw':
            return 1
        else:
            return 1

    def on_enter_state78(self, update):
        update.message.reply_photo("http://dl.stickershop.line.naver.jp/products/0/0/1/1218851/android/stickers/8886095.png")
        update.message.reply_text("要我別走？ yes（再聊一次）or no (to go to the initial state)")
        #self.go_back(update)

    def on_exit_state78(self, update):
        print('Leaving state78')
#**********************************************************


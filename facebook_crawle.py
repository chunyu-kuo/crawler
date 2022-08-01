import requests
import re
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from requests import post,Session
import time
import datetime
import dateparser 
import pandas as pd

def crawler_private_group(Email, Password, groupurl, post_number):
	
	# 瀏覽器設定
	options = webdriver.ChromeOptions()
	options.add_argument('blink-settings=imagesEnabled=false')
	options.add_argument('--headless')
	options.add_argument('--log-level=3')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(chrome_options=options)
	
	# facebook登入
	driver.get('https://www.facebook.com/')
	input_1 = driver.find_element_by_css_selector("input[name='email']")
	input_2 = driver.find_element_by_css_selector("input[type='password']")
	input_1.send_keys(Email)
	input_2.send_keys(Password)
	driver.find_element_by_css_selector("button[name='login']").click()
	time.sleep(1)

	# # 取得登入fb後的cookie
	# cookies = driver.get_cookies()
	# s = requests.Session()
	# for cookie in cookies:
	#     s.cookies.set(cookie['name'], cookie['value'])

	# 前往要爬取的網站，並分析網頁原始碼
	driver.get(groupurl)
	htmltext = driver.page_source
	soup = BeautifulSoup(htmltext,"lxml")
	postList = soup.find('article','_55wo _5rgr _5gh8 async_like')

	postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
	postN = len(postList)
	
	# # 滾動頁面操作，此為控制想要爬取的文章數
	# js = 'window.scrollTo(0, document.body.scrollHeight)'
	# while postN < post_number :
	#     driver.execute_script(js)
	#     time.sleep(0.5)
	#     htmltext = driver.page_source
	#     soup = BeautifulSoup(htmltext,"lxml")
	#     postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
	#     postN = len(postList)
	    

	# # 設定完篇數時要爬資料
	# df = []
	# df = pd.DataFrame(columns=['發文者id','發文者','更新時間','發文時間','文章id','發文內容','分享次數','總心情數','讚','愛心','哇','哈哈','加油','怒','嗚','留言數','連結'])
	# for post in postList:
	#     utime = post.find('abbr')
	#     utime = utime.text
	#     date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	#     if '剛剛' in utime:
	#     	utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#     else:
	#     	if '下午' in utime:
	#     		if '年'in utime:
	#         			utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	#         	else:
	#         		utime = dateparser.parse(utime,date_formats=date_formats)
	#         		utime = utime + datetime.timedelta(hours=12)

	#     	else:
	#     		if '上週' in utime:
	#     			utime = utime.strip('上')
	#     			utime = dateparser.parse(utime,date_formats=date_formats)
	#     			if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
	#     				utime = utime - datetime.timedelta(days=7)
	#     			else:
	#     				pass
	#     		else:
	#     			utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

	#     update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#     name = post.find('h3').text
	#     idd = "'"+re.findall('content_owner_id_new.([0-9]{1,})',str(post))[0]
	#     url = post.find('div','_52jc _5qc4 _78cz _24u0 _36xo').find('a').get('href')  
	#     content = post.find('div','_5rgt _5nk5 _5msi')
	#     if(content.text == ''):
	#         content = '圖檔'
	#     else:
	#         content = content.text
	#     like = post.find('div','_1g06')
	#     if(like == None):
	#         like = '0'
	#     else:
	#         like = like.text
	#     messages = post.find('span','_1j-c')
	#     if(messages == None):
	#         messages = '0'
	#     else:
	#         messages = messages.text.strip('則留言')
	    

	#     headers = {
 #    		'referer': 'https://m.facebook.com/',
 #    		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
	# 		}

	#     post_id = re.findall('"feedback_target":([0-9]{1,})',str(post))[0]
	#     url_1 ='https://m.facebook.com/ufi/reaction/profile/browser/'
	#     params = {'ft_ent_identifier': post_id}
	#     resp = s.get(url_1, headers =headers,params=params)
	#     data = resp.text
	#     soup = BeautifulSoup(data, 'lxml')
	#     like_1 = soup.find('span',{'data-store':'{"reactionType":1}'})
	#     if(like_1 == None):
	#         like_1 = '0'
	#     else:
	#         like_1 = like_1.text
	#     love = soup.find('span',{'data-store':'{"reactionType":2}'})
	#     if(love == None):
	#         love = '0'
	#     else:
	#         love = love.text
	#     haha = soup.find('span',{'data-store':'{"reactionType":4}'})
	#     if(haha == None):
	#         haha = '0'
	#     else:
	#         haha = haha.text
	#     support = soup.find('span',{'data-store':'{"reactionType":16}'})
	#     if(support == None):
	#         support = '0'
	#     else:
	#         support = support.text
	#     wow = soup.find('span',{'data-store':'{"reactionType":3}'})
	#     if(wow == None):
	#         wow = '0'
	#     else:
	#         wow = wow.text
	#     sorry = soup.find('span',{'data-store':'{"reactionType":7}'})
	#     if(sorry == None):
	#         sorry = '0'
	#     else:
	#         sorry = sorry.text
	#     anger = soup.find('span',{'data-store':'{"reactionType":8}'})
	#     if(anger == None):
	#         anger = '0'
	#     else:
	#         anger = anger.text
	        

	#     df = df.append({
	#     '發文者id':idd,  
	#     '發文者':name,
	#     '更新時間':update_time,
	#     '發文時間' :utime ,
	#     '文章id':"'"+post_id ,
	#     '發文內容' : content,
	#     '分享次數' : '0',
	#     '總心情數':like,
	#     '讚':like_1,  
	#     '愛心':love,
	#     '哇':wow,
	#     '哈哈' :haha ,
	#     '加油' : support,
	#     '怒':anger,
	#     '嗚':sorry,
	#     '留言數':messages,
	#     '連結':url,
	# }, ignore_index=True)
	df=[]
	while(True):
	    delay_choice = [5,7,9]
	    delay = random.choice(delay_choice)
	    driver.execute_script(js)
	    time.sleep(delay)
	    htmltext = driver.page_source
	    soup = BeautifulSoup(htmltext,"lxml")
	    postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
	    postN = len(postList)
	    if(postN > 1000):
	        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	        print(postN)
	        df = pd.DataFrame(columns=['發文者id','發文者','更新時間','發文時間','文章id','發文內容','分享次數','總心情數','讚','愛心','哇','哈哈','加油','怒','嗚','留言數','連結'])
	        for post in postList[0:1000]:
	                utime = post.find('abbr')
	                utime = utime.text
	                date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	                if '剛剛' in utime:
	                    utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                else:
	                    if '下午' in utime:
	                        if '年' in utime:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            utime = utime + datetime.timedelta(hours=12)
	                    else:
	                        if '上週' in utime:
	                            utime = utime.strip('上')
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
	                                utime = utime - datetime.timedelta(days=7)
	                            else:
	                                pass
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

	                update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                name = post.find('h3').text
	                idd = "'"+re.findall('content_owner_id_new.([0-9]{1,})',str(post))[0]
	                url = post.find('div','_52jc _5qc4 _78cz _24u0 _36xo').find('a').get('href')  
	                content = post.find('div','_5rgt _5nk5 _5msi')
	                if(content.text == ''):
	                    content = '圖檔'
	                else:
	                    content = content.text
	                like = post.find('div','_1g06')
	                if(like == None):
	                    like = '0'
	                else:
	                    like = like.text
	                messages = post.find('span','_1j-c')
	                if(messages == None):
	                    messages = '0'
	                else:
	                    messages = messages.text.strip('則留言')


	                headers = {
	                    'referer': 'https://m.facebook.com/',
	                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
	                    }

	                post_id = re.findall('"feedback_target":([0-9]{1,})',str(post))[0]
	                url_1 ='https://m.facebook.com/ufi/reaction/profile/browser/'
	                params = {'ft_ent_identifier': post_id}
	                resp = s.get(url_1, headers =headers,params=params)     
	                data = resp.text
	                soup = BeautifulSoup(data, 'lxml')
	                like_1 = soup.find('span',{'data-store':'{"reactionType":1}'})
	                if(like_1 == None):
	                    like_1 = '0'
	                else:
	                    like_1 = like_1.text
	                love = soup.find('span',{'data-store':'{"reactionType":2}'})
	                if(love == None):
	                    love = '0'
	                else:
	                    love = love.text
	                haha = soup.find('span',{'data-store':'{"reactionType":4}'})
	                if(haha == None):
	                    haha = '0'
	                else:
	                    haha = haha.text
	                support = soup.find('span',{'data-store':'{"reactionType":16}'})
	                if(support == None):
	                    support = '0'
	                else:
	                    support = support.text
	                wow = soup.find('span',{'data-store':'{"reactionType":3}'})
	                if(wow == None):
	                    wow = '0'
	                else:
	                    wow = wow.text
	                sorry = soup.find('span',{'data-store':'{"reactionType":7}'})
	                if(sorry == None):
	                    sorry = '0'
	                else:
	                    sorry = sorry.text
	                anger = soup.find('span',{'data-store':'{"reactionType":8}'})
	                if(anger == None):
	                    anger = '0'
	                else:
	                    anger = anger.text


	                df = df.append({
	                '發文者id':idd,  
	                '發文者':name,
	                '更新時間':update_time,
	                '發文時間' :utime ,
	                '文章id':"'"+post_id ,
	                '發文內容' : content,
	                '分享次數' : '0',
	                '總心情數':like,
	                '讚':like_1,  
	                '愛心':love,
	                '哇':wow,
	                '哈哈' :haha ,
	                '加油' : support,
	                '怒':anger,
	                '嗚':sorry,
	                '留言數':messages,
	                '連結':url,
	            }, ignore_index=True)
	        break
	df.to_csv('0_1000.csv',index=False,encoding='utf-8-sig')
	df = []
	del htmltext

	while(True):
	    delay_choice = [5,7,9]
	    delay = random.choice(delay_choice)
	    driver.execute_script(js)
	    time.sleep(delay)
	    htmltext = driver.page_source
	    soup = BeautifulSoup(htmltext,"lxml")
	    postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
	    postN = len(postList)
	    if(postN > 2000):
	        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	        print(postN)
	        df = pd.DataFrame(columns=['發文者id','發文者','更新時間','發文時間','文章id','發文內容','分享次數','總心情數','讚','愛心','哇','哈哈','加油','怒','嗚','留言數','連結'])
	        for post in postList[1000:2000]:
	                utime = post.find('abbr')
	                utime = utime.text
	                date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	                if '剛剛' in utime:
	                    utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                else:
	                    if '下午' in utime:
	                        if '年' in utime:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            utime = utime + datetime.timedelta(hours=12)
	                    else:
	                        if '上週' in utime:
	                            utime = utime.strip('上')
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
	                                utime = utime - datetime.timedelta(days=7)
	                            else:
	                                pass
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

	                update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                name = post.find('h3').text
	                idd = "'"+re.findall('content_owner_id_new.([0-9]{1,})',str(post))[0]
	                url = post.find('div','_52jc _5qc4 _78cz _24u0 _36xo').find('a').get('href')  
	                content = post.find('div','_5rgt _5nk5 _5msi')
	                if(content.text == ''):
	                    content = '圖檔'
	                else:
	                    content = content.text
	                like = post.find('div','_1g06')
	                if(like == None):
	                    like = '0'
	                else:
	                    like = like.text
	                messages = post.find('span','_1j-c')
	                if(messages == None):
	                    messages = '0'
	                else:
	                    messages = messages.text.strip('則留言')


	                headers = {
	                    'referer': 'https://m.facebook.com/',
	                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
	                    }

	                post_id = re.findall('"feedback_target":([0-9]{1,})',str(post))[0]
	                url_1 ='https://m.facebook.com/ufi/reaction/profile/browser/'
	                params = {'ft_ent_identifier': post_id}
	                resp = s.get(url_1, headers =headers,params=params)     
	                data = resp.text
	                soup = BeautifulSoup(data, 'lxml')
	                like_1 = soup.find('span',{'data-store':'{"reactionType":1}'})
	                if(like_1 == None):
	                    like_1 = '0'
	                else:
	                    like_1 = like_1.text
	                love = soup.find('span',{'data-store':'{"reactionType":2}'})
	                if(love == None):
	                    love = '0'
	                else:
	                    love = love.text
	                haha = soup.find('span',{'data-store':'{"reactionType":4}'})
	                if(haha == None):
	                    haha = '0'
	                else:
	                    haha = haha.text
	                support = soup.find('span',{'data-store':'{"reactionType":16}'})
	                if(support == None):
	                    support = '0'
	                else:
	                    support = support.text
	                wow = soup.find('span',{'data-store':'{"reactionType":3}'})
	                if(wow == None):
	                    wow = '0'
	                else:
	                    wow = wow.text
	                sorry = soup.find('span',{'data-store':'{"reactionType":7}'})
	                if(sorry == None):
	                    sorry = '0'
	                else:
	                    sorry = sorry.text
	                anger = soup.find('span',{'data-store':'{"reactionType":8}'})
	                if(anger == None):
	                    anger = '0'
	                else:
	                    anger = anger.text


	                df = df.append({
	                '發文者id':idd,  
	                '發文者':name,
	                '更新時間':update_time,
	                '發文時間' :utime ,
	                '文章id':"'"+post_id ,
	                '發文內容' : content,
	                '分享次數' : '0',
	                '總心情數':like,
	                '讚':like_1,  
	                '愛心':love,
	                '哇':wow,
	                '哈哈' :haha ,
	                '加油' : support,
	                '怒':anger,
	                '嗚':sorry,
	                '留言數':messages,
	                '連結':url,
	            }, ignore_index=True)
	        break
	df.to_csv('1000_2000.csv',index=False,encoding='utf-8-sig')
	df = []
	del htmltext

	while(True):
	    delay_choice = [5,7,9]
	    delay = random.choice(delay_choice)
	    driver.execute_script(js)
	    time.sleep(delay)
	    htmltext = driver.page_source
	    soup = BeautifulSoup(htmltext,"lxml")
	    postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
	    postN = len(postList)
	    if(postN > 3000):
	        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	        print(postN)
	        df = pd.DataFrame(columns=['發文者id','發文者','更新時間','發文時間','文章id','發文內容','分享次數','總心情數','讚','愛心','哇','哈哈','加油','怒','嗚','留言數','連結'])
	        for post in postList[2000:3000]:
	                utime = post.find('abbr')
	                utime = utime.text
	                date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	                if '剛剛' in utime:
	                    utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                else:
	                    if '下午' in utime:
	                        if '年' in utime:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            utime = utime + datetime.timedelta(hours=12)
	                    else:
	                        if '上週' in utime:
	                            utime = utime.strip('上')
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
	                                utime = utime - datetime.timedelta(days=7)
	                            else:
	                                pass
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

	                update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                name = post.find('h3').text
	                idd = "'"+re.findall('content_owner_id_new.([0-9]{1,})',str(post))[0]
	                url = post.find('div','_52jc _5qc4 _78cz _24u0 _36xo').find('a').get('href')  
	                content = post.find('div','_5rgt _5nk5 _5msi')
	                if(content.text == ''):
	                    content = '圖檔'
	                else:
	                    content = content.text
	                like = post.find('div','_1g06')
	                if(like == None):
	                    like = '0'
	                else:
	                    like = like.text
	                messages = post.find('span','_1j-c')
	                if(messages == None):
	                    messages = '0'
	                else:
	                    messages = messages.text.strip('則留言')


	                headers = {
	                    'referer': 'https://m.facebook.com/',
	                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
	                    }

	                post_id = re.findall('"feedback_target":([0-9]{1,})',str(post))[0]
	                url_1 ='https://m.facebook.com/ufi/reaction/profile/browser/'
	                params = {'ft_ent_identifier': post_id}
	                resp = s.get(url_1, headers =headers,params=params)     
	                data = resp.text
	                soup = BeautifulSoup(data, 'lxml')
	                like_1 = soup.find('span',{'data-store':'{"reactionType":1}'})
	                if(like_1 == None):
	                    like_1 = '0'
	                else:
	                    like_1 = like_1.text
	                love = soup.find('span',{'data-store':'{"reactionType":2}'})
	                if(love == None):
	                    love = '0'
	                else:
	                    love = love.text
	                haha = soup.find('span',{'data-store':'{"reactionType":4}'})
	                if(haha == None):
	                    haha = '0'
	                else:
	                    haha = haha.text
	                support = soup.find('span',{'data-store':'{"reactionType":16}'})
	                if(support == None):
	                    support = '0'
	                else:
	                    support = support.text
	                wow = soup.find('span',{'data-store':'{"reactionType":3}'})
	                if(wow == None):
	                    wow = '0'
	                else:
	                    wow = wow.text
	                sorry = soup.find('span',{'data-store':'{"reactionType":7}'})
	                if(sorry == None):
	                    sorry = '0'
	                else:
	                    sorry = sorry.text
	                anger = soup.find('span',{'data-store':'{"reactionType":8}'})
	                if(anger == None):
	                    anger = '0'
	                else:
	                    anger = anger.text


	                df = df.append({
	                '發文者id':idd,  
	                '發文者':name,
	                '更新時間':update_time,
	                '發文時間' :utime ,
	                '文章id':"'"+post_id ,
	                '發文內容' : content,
	                '分享次數' : '0',
	                '總心情數':like,
	                '讚':like_1,  
	                '愛心':love,
	                '哇':wow,
	                '哈哈' :haha ,
	                '加油' : support,
	                '怒':anger,
	                '嗚':sorry,
	                '留言數':messages,
	                '連結':url,
	            }, ignore_index=True)
	        break
	df.to_csv('2000_3000.csv',index=False,encoding='utf-8-sig')
	df = []
	del htmltext

	while(True):
	    delay_choice = [5,7,9]
	    delay = random.choice(delay_choice)
	    driver.execute_script(js)
	    time.sleep(delay)
	    htmltext = driver.page_source
	    soup = BeautifulSoup(htmltext,"lxml")
	    postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
	    postN = len(postList)
	    if(postN > 4000):
	        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	        print(postN)
	        df = pd.DataFrame(columns=['發文者id','發文者','更新時間','發文時間','文章id','發文內容','分享次數','總心情數','讚','愛心','哇','哈哈','加油','怒','嗚','留言數','連結'])
	        for post in postList[3000:4000]:
	                utime = post.find('abbr')
	                utime = utime.text
	                date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	                if '剛剛' in utime:
	                    utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                else:
	                    if '下午' in utime:
	                        if '年' in utime:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            utime = utime + datetime.timedelta(hours=12)
	                    else:
	                        if '上週' in utime:
	                            utime = utime.strip('上')
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
	                                utime = utime - datetime.timedelta(days=7)
	                            else:
	                                pass
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

	                update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                name = post.find('h3').text
	                idd = "'"+re.findall('content_owner_id_new.([0-9]{1,})',str(post))[0]
	                url = post.find('div','_52jc _5qc4 _78cz _24u0 _36xo').find('a').get('href')  
	                content = post.find('div','_5rgt _5nk5 _5msi')
	                if(content.text == ''):
	                    content = '圖檔'
	                else:
	                    content = content.text
	                like = post.find('div','_1g06')
	                if(like == None):
	                    like = '0'
	                else:
	                    like = like.text
	                messages = post.find('span','_1j-c')
	                if(messages == None):
	                    messages = '0'
	                else:
	                    messages = messages.text.strip('則留言')


	                headers = {
	                    'referer': 'https://m.facebook.com/',
	                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
	                    }

	                post_id = re.findall('"feedback_target":([0-9]{1,})',str(post))[0]
	                url_1 ='https://m.facebook.com/ufi/reaction/profile/browser/'
	                params = {'ft_ent_identifier': post_id}
	                resp = s.get(url_1, headers =headers,params=params)     
	                data = resp.text
	                soup = BeautifulSoup(data, 'lxml')
	                like_1 = soup.find('span',{'data-store':'{"reactionType":1}'})
	                if(like_1 == None):
	                    like_1 = '0'
	                else:
	                    like_1 = like_1.text
	                love = soup.find('span',{'data-store':'{"reactionType":2}'})
	                if(love == None):
	                    love = '0'
	                else:
	                    love = love.text
	                haha = soup.find('span',{'data-store':'{"reactionType":4}'})
	                if(haha == None):
	                    haha = '0'
	                else:
	                    haha = haha.text
	                support = soup.find('span',{'data-store':'{"reactionType":16}'})
	                if(support == None):
	                    support = '0'
	                else:
	                    support = support.text
	                wow = soup.find('span',{'data-store':'{"reactionType":3}'})
	                if(wow == None):
	                    wow = '0'
	                else:
	                    wow = wow.text
	                sorry = soup.find('span',{'data-store':'{"reactionType":7}'})
	                if(sorry == None):
	                    sorry = '0'
	                else:
	                    sorry = sorry.text
	                anger = soup.find('span',{'data-store':'{"reactionType":8}'})
	                if(anger == None):
	                    anger = '0'
	                else:
	                    anger = anger.text


	                df = df.append({
	                '發文者id':idd,  
	                '發文者':name,
	                '更新時間':update_time,
	                '發文時間' :utime ,
	                '文章id':"'"+post_id ,
	                '發文內容' : content,
	                '分享次數' : '0',
	                '總心情數':like,
	                '讚':like_1,  
	                '愛心':love,
	                '哇':wow,
	                '哈哈' :haha ,
	                '加油' : support,
	                '怒':anger,
	                '嗚':sorry,
	                '留言數':messages,
	                '連結':url,
	            }, ignore_index=True)
	        break
	df.to_csv('3000_4000.csv',index=False,encoding='utf-8-sig')
	df = []
	del htmltext

	while(True):
	    delay_choice = [5,7,9]
	    delay = random.choice(delay_choice)
	    driver.execute_script(js)
	    time.sleep(delay)
	    htmltext = driver.page_source
	    soup = BeautifulSoup(htmltext,"lxml")
	    postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
	    postN = len(postList)
	    if(postN > 5000):
	        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	        print(postN)
	        df = pd.DataFrame(columns=['發文者id','發文者','更新時間','發文時間','文章id','發文內容','分享次數','總心情數','讚','愛心','哇','哈哈','加油','怒','嗚','留言數','連結'])
	        for post in postList[4000:5000]:
	                utime = post.find('abbr')
	                utime = utime.text
	                date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	                if '剛剛' in utime:
	                    utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                else:
	                    if '下午' in utime:
	                        if '年' in utime:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            utime = utime + datetime.timedelta(hours=12)
	                    else:
	                        if '上週' in utime:
	                            utime = utime.strip('上')
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
	                                utime = utime - datetime.timedelta(days=7)
	                            else:
	                                pass
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

	                update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                name = post.find('h3').text
	                idd = "'"+re.findall('content_owner_id_new.([0-9]{1,})',str(post))[0]
	                url = post.find('div','_52jc _5qc4 _78cz _24u0 _36xo').find('a').get('href')  
	                content = post.find('div','_5rgt _5nk5 _5msi')
	                if(content.text == ''):
	                    content = '圖檔'
	                else:
	                    content = content.text
	                like = post.find('div','_1g06')
	                if(like == None):
	                    like = '0'
	                else:
	                    like = like.text
	                messages = post.find('span','_1j-c')
	                if(messages == None):
	                    messages = '0'
	                else:
	                    messages = messages.text.strip('則留言')


	                headers = {
	                    'referer': 'https://m.facebook.com/',
	                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
	                    }

	                post_id = re.findall('"feedback_target":([0-9]{1,})',str(post))[0]
	                url_1 ='https://m.facebook.com/ufi/reaction/profile/browser/'
	                params = {'ft_ent_identifier': post_id}
	                resp = s.get(url_1, headers =headers,params=params)     
	                data = resp.text
	                soup = BeautifulSoup(data, 'lxml')
	                like_1 = soup.find('span',{'data-store':'{"reactionType":1}'})
	                if(like_1 == None):
	                    like_1 = '0'
	                else:
	                    like_1 = like_1.text
	                love = soup.find('span',{'data-store':'{"reactionType":2}'})
	                if(love == None):
	                    love = '0'
	                else:
	                    love = love.text
	                haha = soup.find('span',{'data-store':'{"reactionType":4}'})
	                if(haha == None):
	                    haha = '0'
	                else:
	                    haha = haha.text
	                support = soup.find('span',{'data-store':'{"reactionType":16}'})
	                if(support == None):
	                    support = '0'
	                else:
	                    support = support.text
	                wow = soup.find('span',{'data-store':'{"reactionType":3}'})
	                if(wow == None):
	                    wow = '0'
	                else:
	                    wow = wow.text
	                sorry = soup.find('span',{'data-store':'{"reactionType":7}'})
	                if(sorry == None):
	                    sorry = '0'
	                else:
	                    sorry = sorry.text
	                anger = soup.find('span',{'data-store':'{"reactionType":8}'})
	                if(anger == None):
	                    anger = '0'
	                else:
	                    anger = anger.text


	                df = df.append({
	                '發文者id':idd,  
	                '發文者':name,
	                '更新時間':update_time,
	                '發文時間' :utime ,
	                '文章id':"'"+post_id ,
	                '發文內容' : content,
	                '分享次數' : '0',
	                '總心情數':like,
	                '讚':like_1,  
	                '愛心':love,
	                '哇':wow,
	                '哈哈' :haha ,
	                '加油' : support,
	                '怒':anger,
	                '嗚':sorry,
	                '留言數':messages,
	                '連結':url,
	            }, ignore_index=True)
	        break
	df.to_csv('4000_5000.csv',index=False,encoding='utf-8-sig')
	df = []
	del htmltext

	while(True):
	    delay_choice = [5,7,9]
	    delay = random.choice(delay_choice)
	    driver.execute_script(js)
	    time.sleep(delay)
	    htmltext = driver.page_source
	    soup = BeautifulSoup(htmltext,"lxml")
	    postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
	    postN = len(postList)
	    if(postN > 6000):
	        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	        print(postN)
	        df = pd.DataFrame(columns=['發文者id','發文者','更新時間','發文時間','文章id','發文內容','分享次數','總心情數','讚','愛心','哇','哈哈','加油','怒','嗚','留言數','連結'])
	        for post in postList[5000:6000]:
	                utime = post.find('abbr')
	                utime = utime.text
	                date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	                if '剛剛' in utime:
	                    utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                else:
	                    if '下午' in utime:
	                        if '年' in utime:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            utime = utime + datetime.timedelta(hours=12)
	                    else:
	                        if '上週' in utime:
	                            utime = utime.strip('上')
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
	                                utime = utime - datetime.timedelta(days=7)
	                            else:
	                                pass
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

	                update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                name = post.find('h3').text
	                idd = "'"+re.findall('content_owner_id_new.([0-9]{1,})',str(post))[0]
	                url = post.find('div','_52jc _5qc4 _78cz _24u0 _36xo').find('a').get('href')  
	                content = post.find('div','_5rgt _5nk5 _5msi')
	                if(content.text == ''):
	                    content = '圖檔'
	                else:
	                    content = content.text
	                like = post.find('div','_1g06')
	                if(like == None):
	                    like = '0'
	                else:
	                    like = like.text
	                messages = post.find('span','_1j-c')
	                if(messages == None):
	                    messages = '0'
	                else:
	                    messages = messages.text.strip('則留言')


	                headers = {
	                    'referer': 'https://m.facebook.com/',
	                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
	                    }

	                post_id = re.findall('"feedback_target":([0-9]{1,})',str(post))[0]
	                url_1 ='https://m.facebook.com/ufi/reaction/profile/browser/'
	                params = {'ft_ent_identifier': post_id}
	                resp = s.get(url_1, headers =headers,params=params)     
	                data = resp.text
	                soup = BeautifulSoup(data, 'lxml')
	                like_1 = soup.find('span',{'data-store':'{"reactionType":1}'})
	                if(like_1 == None):
	                    like_1 = '0'
	                else:
	                    like_1 = like_1.text
	                love = soup.find('span',{'data-store':'{"reactionType":2}'})
	                if(love == None):
	                    love = '0'
	                else:
	                    love = love.text
	                haha = soup.find('span',{'data-store':'{"reactionType":4}'})
	                if(haha == None):
	                    haha = '0'
	                else:
	                    haha = haha.text
	                support = soup.find('span',{'data-store':'{"reactionType":16}'})
	                if(support == None):
	                    support = '0'
	                else:
	                    support = support.text
	                wow = soup.find('span',{'data-store':'{"reactionType":3}'})
	                if(wow == None):
	                    wow = '0'
	                else:
	                    wow = wow.text
	                sorry = soup.find('span',{'data-store':'{"reactionType":7}'})
	                if(sorry == None):
	                    sorry = '0'
	                else:
	                    sorry = sorry.text
	                anger = soup.find('span',{'data-store':'{"reactionType":8}'})
	                if(anger == None):
	                    anger = '0'
	                else:
	                    anger = anger.text


	                df = df.append({
	                '發文者id':idd,  
	                '發文者':name,
	                '更新時間':update_time,
	                '發文時間' :utime ,
	                '文章id':"'"+post_id ,
	                '發文內容' : content,
	                '分享次數' : '0',
	                '總心情數':like,
	                '讚':like_1,  
	                '愛心':love,
	                '哇':wow,
	                '哈哈' :haha ,
	                '加油' : support,
	                '怒':anger,
	                '嗚':sorry,
	                '留言數':messages,
	                '連結':url,
	            }, ignore_index=True)
	        break
	df.to_csv('5000_6000.csv',index=False,encoding='utf-8-sig')
	df = []
	del htmltext

	while(True):
	    delay_choice = [5,7,9]
	    delay = random.choice(delay_choice)
	    driver.execute_script(js)
	    time.sleep(delay)
	    htmltext = driver.page_source
	    soup = BeautifulSoup(htmltext,"lxml")
	    postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
	    postN = len(postList)
	    if(postN > 7000):
	        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	        print(postN)
	        df = pd.DataFrame(columns=['發文者id','發文者','更新時間','發文時間','文章id','發文內容','分享次數','總心情數','讚','愛心','哇','哈哈','加油','怒','嗚','留言數','連結'])
	        for post in postList[6000:7000]:
	                utime = post.find('abbr')
	                utime = utime.text
	                date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	                if '剛剛' in utime:
	                    utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                else:
	                    if '下午' in utime:
	                        if '年' in utime:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            utime = utime + datetime.timedelta(hours=12)
	                    else:
	                        if '上週' in utime:
	                            utime = utime.strip('上')
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
	                                utime = utime - datetime.timedelta(days=7)
	                            else:
	                                pass
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

	                update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                name = post.find('h3').text
	                idd = "'"+re.findall('content_owner_id_new.([0-9]{1,})',str(post))[0]
	                url = post.find('div','_52jc _5qc4 _78cz _24u0 _36xo').find('a').get('href')  
	                content = post.find('div','_5rgt _5nk5 _5msi')
	                if(content.text == ''):
	                    content = '圖檔'
	                else:
	                    content = content.text
	                like = post.find('div','_1g06')
	                if(like == None):
	                    like = '0'
	                else:
	                    like = like.text
	                messages = post.find('span','_1j-c')
	                if(messages == None):
	                    messages = '0'
	                else:
	                    messages = messages.text.strip('則留言')


	                headers = {
	                    'referer': 'https://m.facebook.com/',
	                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
	                    }

	                post_id = re.findall('"feedback_target":([0-9]{1,})',str(post))[0]
	                url_1 ='https://m.facebook.com/ufi/reaction/profile/browser/'
	                params = {'ft_ent_identifier': post_id}
	                resp = s.get(url_1, headers =headers,params=params)     
	                data = resp.text
	                soup = BeautifulSoup(data, 'lxml')
	                like_1 = soup.find('span',{'data-store':'{"reactionType":1}'})
	                if(like_1 == None):
	                    like_1 = '0'
	                else:
	                    like_1 = like_1.text
	                love = soup.find('span',{'data-store':'{"reactionType":2}'})
	                if(love == None):
	                    love = '0'
	                else:
	                    love = love.text
	                haha = soup.find('span',{'data-store':'{"reactionType":4}'})
	                if(haha == None):
	                    haha = '0'
	                else:
	                    haha = haha.text
	                support = soup.find('span',{'data-store':'{"reactionType":16}'})
	                if(support == None):
	                    support = '0'
	                else:
	                    support = support.text
	                wow = soup.find('span',{'data-store':'{"reactionType":3}'})
	                if(wow == None):
	                    wow = '0'
	                else:
	                    wow = wow.text
	                sorry = soup.find('span',{'data-store':'{"reactionType":7}'})
	                if(sorry == None):
	                    sorry = '0'
	                else:
	                    sorry = sorry.text
	                anger = soup.find('span',{'data-store':'{"reactionType":8}'})
	                if(anger == None):
	                    anger = '0'
	                else:
	                    anger = anger.text


	                df = df.append({
	                '發文者id':idd,  
	                '發文者':name,
	                '更新時間':update_time,
	                '發文時間' :utime ,
	                '文章id':"'"+post_id ,
	                '發文內容' : content,
	                '分享次數' : '0',
	                '總心情數':like,
	                '讚':like_1,  
	                '愛心':love,
	                '哇':wow,
	                '哈哈' :haha ,
	                '加油' : support,
	                '怒':anger,
	                '嗚':sorry,
	                '留言數':messages,
	                '連結':url,
	            }, ignore_index=True)
	        break
	df.to_csv('6000_7000.csv',index=False,encoding='utf-8-sig')
	df = []
	del htmltext

	while(True):
	    delay_choice = [5,7,9]
	    delay = random.choice(delay_choice)
	    driver.execute_script(js)
	    time.sleep(delay)
	    htmltext = driver.page_source
	    soup = BeautifulSoup(htmltext,"lxml")
	    postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
	    postN = len(postList)
	    if(postN > 8000):
	        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	        print(postN)
	        df = pd.DataFrame(columns=['發文者id','發文者','更新時間','發文時間','文章id','發文內容','分享次數','總心情數','讚','愛心','哇','哈哈','加油','怒','嗚','留言數','連結'])
	        for post in postList[7000:8000]:
	                utime = post.find('abbr')
	                utime = utime.text
	                date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	                if '剛剛' in utime:
	                    utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                else:
	                    if '下午' in utime:
	                        if '年' in utime:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            utime = utime + datetime.timedelta(hours=12)
	                    else:
	                        if '上週' in utime:
	                            utime = utime.strip('上')
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
	                                utime = utime - datetime.timedelta(days=7)
	                            else:
	                                pass
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

	                update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                name = post.find('h3').text
	                idd = "'"+re.findall('content_owner_id_new.([0-9]{1,})',str(post))[0]
	                url = post.find('div','_52jc _5qc4 _78cz _24u0 _36xo').find('a').get('href')  
	                content = post.find('div','_5rgt _5nk5 _5msi')
	                if(content.text == ''):
	                    content = '圖檔'
	                else:
	                    content = content.text
	                like = post.find('div','_1g06')
	                if(like == None):
	                    like = '0'
	                else:
	                    like = like.text
	                messages = post.find('span','_1j-c')
	                if(messages == None):
	                    messages = '0'
	                else:
	                    messages = messages.text.strip('則留言')


	                headers = {
	                    'referer': 'https://m.facebook.com/',
	                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
	                    }

	                post_id = re.findall('"feedback_target":([0-9]{1,})',str(post))[0]
	                url_1 ='https://m.facebook.com/ufi/reaction/profile/browser/'
	                params = {'ft_ent_identifier': post_id}
	                resp = s.get(url_1, headers =headers,params=params)     
	                data = resp.text
	                soup = BeautifulSoup(data, 'lxml')
	                like_1 = soup.find('span',{'data-store':'{"reactionType":1}'})
	                if(like_1 == None):
	                    like_1 = '0'
	                else:
	                    like_1 = like_1.text
	                love = soup.find('span',{'data-store':'{"reactionType":2}'})
	                if(love == None):
	                    love = '0'
	                else:
	                    love = love.text
	                haha = soup.find('span',{'data-store':'{"reactionType":4}'})
	                if(haha == None):
	                    haha = '0'
	                else:
	                    haha = haha.text
	                support = soup.find('span',{'data-store':'{"reactionType":16}'})
	                if(support == None):
	                    support = '0'
	                else:
	                    support = support.text
	                wow = soup.find('span',{'data-store':'{"reactionType":3}'})
	                if(wow == None):
	                    wow = '0'
	                else:
	                    wow = wow.text
	                sorry = soup.find('span',{'data-store':'{"reactionType":7}'})
	                if(sorry == None):
	                    sorry = '0'
	                else:
	                    sorry = sorry.text
	                anger = soup.find('span',{'data-store':'{"reactionType":8}'})
	                if(anger == None):
	                    anger = '0'
	                else:
	                    anger = anger.text


	                df = df.append({
	                '發文者id':idd,  
	                '發文者':name,
	                '更新時間':update_time,
	                '發文時間' :utime ,
	                '文章id':"'"+post_id ,
	                '發文內容' : content,
	                '分享次數' : '0',
	                '總心情數':like,
	                '讚':like_1,  
	                '愛心':love,
	                '哇':wow,
	                '哈哈' :haha ,
	                '加油' : support,
	                '怒':anger,
	                '嗚':sorry,
	                '留言數':messages,
	                '連結':url,
	            }, ignore_index=True)
	        break
	df.to_csv('7000_8000.csv',index=False,encoding='utf-8-sig')
	df = []
	del htmltext

	while(True):
	    delay_choice = [5,7,9]
	    delay = random.choice(delay_choice)
	    driver.execute_script(js)
	    time.sleep(delay)
	    htmltext = driver.page_source
	    soup = BeautifulSoup(htmltext,"lxml")
	    postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
	    postN = len(postList)
	    if(postN > 9000):
	        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	        print(postN)
	        df = pd.DataFrame(columns=['發文者id','發文者','更新時間','發文時間','文章id','發文內容','分享次數','總心情數','讚','愛心','哇','哈哈','加油','怒','嗚','留言數','連結'])
	        for post in postList[8000:9000]:
	                utime = post.find('abbr')
	                utime = utime.text
	                date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	                if '剛剛' in utime:
	                    utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                else:
	                    if '下午' in utime:
	                        if '年' in utime:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            utime = utime + datetime.timedelta(hours=12)
	                    else:
	                        if '上週' in utime:
	                            utime = utime.strip('上')
	                            utime = dateparser.parse(utime,date_formats=date_formats)
	                            if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
	                                utime = utime - datetime.timedelta(days=7)
	                            else:
	                                pass
	                        else:
	                            utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

	                update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                name = post.find('h3').text
	                idd = "'"+re.findall('content_owner_id_new.([0-9]{1,})',str(post))[0]
	                url = post.find('div','_52jc _5qc4 _78cz _24u0 _36xo').find('a').get('href')  
	                content = post.find('div','_5rgt _5nk5 _5msi')
	                if(content.text == ''):
	                    content = '圖檔'
	                else:
	                    content = content.text
	                like = post.find('div','_1g06')
	                if(like == None):
	                    like = '0'
	                else:
	                    like = like.text
	                messages = post.find('span','_1j-c')
	                if(messages == None):
	                    messages = '0'
	                else:
	                    messages = messages.text.strip('則留言')


	                headers = {
	                    'referer': 'https://m.facebook.com/',
	                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
	                    }

	                post_id = re.findall('"feedback_target":([0-9]{1,})',str(post))[0]
	                url_1 ='https://m.facebook.com/ufi/reaction/profile/browser/'
	                params = {'ft_ent_identifier': post_id}
	                resp = s.get(url_1, headers =headers,params=params)     
	                data = resp.text
	                soup = BeautifulSoup(data, 'lxml')
	                like_1 = soup.find('span',{'data-store':'{"reactionType":1}'})
	                if(like_1 == None):
	                    like_1 = '0'
	                else:
	                    like_1 = like_1.text
	                love = soup.find('span',{'data-store':'{"reactionType":2}'})
	                if(love == None):
	                    love = '0'
	                else:
	                    love = love.text
	                haha = soup.find('span',{'data-store':'{"reactionType":4}'})
	                if(haha == None):
	                    haha = '0'
	                else:
	                    haha = haha.text
	                support = soup.find('span',{'data-store':'{"reactionType":16}'})
	                if(support == None):
	                    support = '0'
	                else:
	                    support = support.text
	                wow = soup.find('span',{'data-store':'{"reactionType":3}'})
	                if(wow == None):
	                    wow = '0'
	                else:
	                    wow = wow.text
	                sorry = soup.find('span',{'data-store':'{"reactionType":7}'})
	                if(sorry == None):
	                    sorry = '0'
	                else:
	                    sorry = sorry.text
	                anger = soup.find('span',{'data-store':'{"reactionType":8}'})
	                if(anger == None):
	                    anger = '0'
	                else:
	                    anger = anger.text


	                df = df.append({
	                '發文者id':idd,  
	                '發文者':name,
	                '更新時間':update_time,
	                '發文時間' :utime ,
	                '文章id':"'"+post_id ,
	                '發文內容' : content,
	                '分享次數' : '0',
	                '總心情數':like,
	                '讚':like_1,  
	                '愛心':love,
	                '哇':wow,
	                '哈哈' :haha ,
	                '加油' : support,
	                '怒':anger,
	                '嗚':sorry,
	                '留言數':messages,
	                '連結':url,
	            }, ignore_index=True)
	        break
	df.to_csv('8000_9000.csv',index=False,encoding='utf-8-sig')
	df = []
	del htmltext
	driver.close()

	# 透過 合併後excel 留言爬取
	options = webdriver.ChromeOptions()
	options.add_argument('blink-settings=imagesEnabled=false')
	options.add_argument('--headless')
	options.add_argument('--log-level=3')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(chrome_options=options)
	
	# facebook登入
	driver.get('https://www.facebook.com/')
	input_1 = driver.find_element_by_css_selector("input[name='email']")
	input_2 = driver.find_element_by_css_selector("input[type='password']")
	input_1.send_keys(Email)
	input_2.send_keys(Password)
	driver.find_element_by_css_selector("button[name='login']").click()
	time.sleep(1)

	daf = pd.DataFrame(columns=['留言者id','留言者','更新時間','留言時間','文章id','留言內容','留言網址'])
	for x in df.values[0:9000]:
	    url = x[0]
	    driver.get(url)
	    num.append(x)
	    print(len(num))
	    while(True):
	        delay_choices = [3, 4, 5]
	        delay = random.choice(delay_choices)
	        htmltext = driver.page_source
	        soup = BeautifulSoup(htmltext,"lxml")
	        postList = soup.find_all('div','_2a_i')
	        postN = len(postList)
	        try:
	            driver.find_element_by_css_selector('a._108_').click()
	        except:
	            pass
	        time.sleep(delay)
	        htmltext = driver.page_source
	        soup = BeautifulSoup(htmltext,"lxml")
	        postList_1 = soup.find_all('div','_2a_i')
	        postN_1 = len(postList_1)

	        if(postN == postN_1):
	            break
	            
	    while(True):
	        delay_choices_1 = [3, 4]
	        delay_1 = random.choice(delay_choices_1)
	        htmltext = driver.page_source
	        soup = BeautifulSoup(htmltext,"lxml")
	        postList = soup.find_all('div','_2a_i')
	        postN = len(postList)
	        try:
	            driver.find_element_by_css_selector('div._2b1h.async_elem').click()
	        except:
	            pass
	        time.sleep(delay_1)
	        htmltext = driver.page_source
	        soup = BeautifulSoup(htmltext,"lxml")
	        postList_1 = soup.find_all('div','_2a_i')
	        postN_1 = len(postList_1)

	        if(postN == postN_1):
	            break
	            
	    for post in postList:
	        idd = "'"+re.findall('feed_story_ring([0-9]{1,})',str(post))[0]
	        name = post.find('div','_2b05').text
	        update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	        utime = post.find('abbr').text
	        date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	        if '剛剛' in utime:
	        	utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	        else:
	        	if '下午' in utime:
	        		if '年'in utime:
	        			utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	        		else:
	        			utime = dateparser.parse(utime,date_formats=date_formats)
	        			utime = utime+datetime.timedelta(hours=12)
	        	else:
                    if '上週' or '上星' in utime:
                        utime = utime.strip('上')
                        utime = dateparser.parse(utime,date_formats=date_formats)
                        if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
                            utime = utime - datetime.timedelta(days=7)
                        else:
                            pass
                    else:
                        utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")


	        post_idd = "'"+re.findall('permalink/([0-9]{0,})',str(url))[0]
	        message = post.find('div', {'data-sigil':'comment-body'})
	        if(message.text == name):
	            message = '圖檔'
	        else:
	            message = message.text
	        daf = daf.append({
	        '留言者id':idd,
	        '留言者': name,
	        '更新時間':update_time,
	        '留言時間':utime,
	        '文章id':post_idd,
	        '留言內容':message,
	        '留言網址':url
	    }, ignore_index=True)
	daf.to_csv('0_9000.csv',index=False,encoding='utf-8-sig')
	print('Finish')



	# # 設定完篇數時要爬留言資料
	# daf = pd.DataFrame(columns=['留言者id','留言者','更新時間','留言時間','文章id','留言內容','留言網址'])
	# delay_choices = [3, 4, 5]
	# delay_choices_1 = [3, 4]
	# delay = random.choice(delay_choices)
	# delay_1 = random.choice(delay_choices_1)
	# for x in range(postN):
	#     url = df['連結'][x]
	#     driver.get(url)

	#     while(True):
	#         htmltext = driver.page_source
	#         soup = BeautifulSoup(htmltext,"lxml")
	#         postList = soup.find_all('div','_2a_i')
	#         postN = len(postList)
	#         try:
	#             driver.find_element_by_css_selector('a._108_').click()
	#         except:
	#             pass
	#         time.sleep(delay)
	#         htmltext = driver.page_source
	#         soup = BeautifulSoup(htmltext,"lxml")
	#         postList_1 = soup.find_all('div','_2a_i')
	#         postN_1 = len(postList_1)

	#         if(postN == postN_1):
	#             break
	            
	#     while(True):
	#         htmltext = driver.page_source
	#         soup = BeautifulSoup(htmltext,"lxml")
	#         postList = soup.find_all('div','_2a_i')
	#         postN = len(postList)
	#         try:
	#             driver.find_element_by_css_selector('div._2b1h.async_elem').click()
	#         except:
	#             pass
	#         time.sleep(delay_1)
	#         htmltext = driver.page_source
	#         soup = BeautifulSoup(htmltext,"lxml")
	#         postList_1 = soup.find_all('div','_2a_i')
	#         postN_1 = len(postList_1)

	#         if(postN == postN_1):
	#             break
	            
	#     for post in postList:
	#         idd = "'"+re.findall('feed_story_ring([0-9]{1,})',str(post))[0]
	#         name = post.find('div','_2b05').text
	#         update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#         utime = post.find('abbr').text
	#         date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
	#         if '剛剛' in utime:
	#         	utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#         else:
	#         	if '下午' in utime:
	#         		if '年'in utime:
	#         			utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
	#         		else:
	#         			utime = dateparser.parse(utime,date_formats=date_formats)
	#         			utime = utime+datetime.timedelta(hours=12)
	#         	else:
	# 	    		if '上週' in utime:
	# 	    			utime = utime.strip('上')
	# 	    			utime = dateparser.parse(utime,date_formats=date_formats)
	# 	    			if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
	# 	    				utime = utime - datetime.timedelta(days=7)
	# 	    			else:
	# 	    				pass
	# 	    		else:
	# 	    			utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

	#         post_idd = "'"+re.findall('permalink/([0-9]{0,})',str(url))[0]
	#         message = post.find('div', {'data-sigil':'comment-body'})
	#         if(message.text == name):
	#             message = '圖檔'
	#         else:
	#             message = message.text
	#         daf = daf.append({
	#         '留言者id':idd,
	#         '留言者': name,
	#         '更新時間':update_time,
	#         '留言時間':utime,
	#         '文章id':post_idd,
	#         '留言內容':message,
	#         '留言網址':url
	#     }, ignore_index=True)
	        
	# daf.to_csv('留言內容.csv',index=False,encoding='utf-8-sig')
	# print('Finish')
	


# def crawler_group(Email, Password, groupurl, post_number):
# 	driver = webdriver.Chrome()
# 	driver.get('https://www.facebook.com/')
# 	input_1 = driver.find_element_by_css_selector("input[name='email']")
# 	input_2 = driver.find_element_by_css_selector("input[type='password']")
# 	input_1.send_keys(Email)
# 	input_2.send_keys(Password)
# 	driver.find_element_by_css_selector("button[name='login']").click()
# 	time.sleep(1)

# 	cookies = driver.get_cookies()
# 	s = requests.Session()
# 	for cookie in cookies:
# 	    s.cookies.set(cookie['name'], cookie['value'])

# 	driver.get(groupurl)
# 	htmltext = driver.page_source
# 	soup = BeautifulSoup(htmltext,"lxml")
# 	postList = soup.find('article','_55wo _5rgr _5gh8 async_like')

# 	postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
# 	postN = len(postList)
	
# 	js = 'window.scrollTo(0, document.body.scrollHeight)'

# 	while postN < 30 :
# 	    driver.execute_script(js)
# 	    htmltext = driver.page_source
# 	    soup = BeautifulSoup(htmltext,"lxml")
# 	    postList = soup.find_all('article','_55wo _5rgr _5gh8 async_like')
# 	    postN = len(postList)


# 	df = []
# 	df = pd.DataFrame(columns=['發文者id','發文者','更新時間','發文時間','發文內容','分享數','總心情數','讚','愛心','哇','哈哈','加油','怒','嗚','留言數','連結'])
# 	for post in postList:
# 	    utime = post.find('abbr')
# 	    utime = utime.text
# 	    date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
# 	    if '剛剛' in utime:
# 	    	utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# 	    else:
# 	    	if '下午' in utime:
# 	    		if '年'in utime:
# 	        			utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")
# 	        		else:
# 	        			utime = dateparser.parse(utime,date_formats=date_formats)
# 	        			utime = utime+datetime.timedelta(hours=12)
# 	    	else:
# 	    		if '上週' in utime:
# 	    			utime = utime.strip('上')
# 	    			utime = dateparser.parse(utime,date_formats=date_formats)
# 	    			if str(utime) == str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")):
# 	    				utime = utime - datetime.timedelta(days=7)
# 	    			else:
# 	    				pass
# 	    		else:
# 	    			utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

# 	    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# 	    name = post.find('h3').text
# 	    idd = re.findall('content_owner_id_new.([0-9]{1,})',str(post))[0]
# 	    url = post.find('div','_52jc _5qc4 _78cz _24u0 _36xo').find('a').get('href')  
# 	    content = post.find('div','_5rgt _5nk5 _5msi')
# 	    if(content.text == ''):
# 	        content = '圖檔'
# 	    else:
# 	        content = content.text
# 	    try:
# 	        share  = post.find_all('span','_1j-c')[0-1]
# 	        if re.search('分',share.text):
# 	            share =  share.text.strip('次分享')
# 	        else:
# 	            share = '0'
# 	    except:
# 	        share = '0'
	        
# 	    like = post.find('div','_1g06')
# 	    if(like == None):
# 	        like = '0'
# 	    else:
# 	        like = like.text
	        
# 	    messages  = post.find('span',{'data-sigil':'comments-token'})
# 	    if(messages == None):
# 	        messages = '0'
# 	    else:
# 	        messages = messages.text.strip('則留言')
	    
# 	    headers = {
#     		'referer': 'https://m.facebook.com/',
#     		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
# 			}

# 	    post_id = re.findall('"feedback_target":([0-9]{1,})',str(post))[0]
# 	    url_1 ='https://m.facebook.com/ufi/reaction/profile/browser/'
# 	    params = {'ft_ent_identifier': post_id}
# 	    resp = s.get(url_1, headers =headers,params=params)
# 	    data = resp.text
# 	    soup = BeautifulSoup(data, 'lxml')
# 	    like_1 = soup.find('span',{'data-store':'{"reactionType":1}'})
# 	    if(like_1 == None):
# 	        like_1 = '0'
# 	    else:
# 	        like_1 = like_1.text
# 	    love = soup.find('span',{'data-store':'{"reactionType":2}'})
# 	    if(love == None):
# 	        love = '0'
# 	    else:
# 	        love = love.text
# 	    haha = soup.find('span',{'data-store':'{"reactionType":4}'})
# 	    if(haha == None):
# 	        haha = '0'
# 	    else:
# 	        haha = haha.text
# 	    support = soup.find('span',{'data-store':'{"reactionType":16}'})
# 	    if(support == None):
# 	        support = '0'
# 	    else:
# 	        support = support.text
# 	    wow = soup.find('span',{'data-store':'{"reactionType":3}'})
# 	    if(wow == None):
# 	        wow = '0'
# 	    else:
# 	        wow = wow.text
# 	    sorry = soup.find('span',{'data-store':'{"reactionType":7}'})
# 	    if(sorry == None):
# 	        sorry = '0'
# 	    else:
# 	        sorry = sorry.text
# 	    anger = soup.find('span',{'data-store':'{"reactionType":8}'})
# 	    if(anger == None):
# 	        anger = '0'
# 	    else:
# 	        anger = anger.text
	        

# 	    df = df.append({
# 	    '發文者id':idd,  
# 	    '發文者':name,
# 	    '更新時間':update_time,
# 	    '發文時間' :utime ,
# 	    '發文內容' : content,
# 	    '分享數':share,
# 	    '總心情數':like,
# 	    '讚':like_1,  
# 	    '愛心':love,
# 	    '哇':wow,
# 	    '哈哈' :haha ,
# 	    '加油' : support,
# 	    '怒':anger,
# 	    '嗚':sorry,
# 	    '留言數':messages,
# 	    '連結':url,
# 	}, ignore_index=True)

# 	df.to_csv('公開社團.csv',index=False,encoding='utf-8-sig')
	
# 	daf = pd.DataFrame(columns=['留言者id','留言者','更新時間','留言時間','留言內容','留言網址'])
# 	delay_choices = [3, 4, 5]
# 	delay = random.choice(delay_choices)
# 	for x in range(postN):
# 	    url = df['連結'][x]
# 	    driver.get(url)

# 	    while(True):
# 	        htmltext = driver.page_source
# 	        soup = BeautifulSoup(htmltext,"lxml")
# 	        postList = soup.find_all('div','_2a_i')
# 	        postN = len(postList)
# 	        try:
# 	            driver.find_element_by_css_selector('a._108_').click()
# 	        except:
# 	            pass
# 	        time.sleep(delay)
# 	        htmltext = driver.page_source
# 	        soup = BeautifulSoup(htmltext,"lxml")
# 	        postList_1 = soup.find_all('div','_2a_i')
# 	        postN_1 = len(postList_1)

# 	        if(postN == postN_1):
# 	            break
	            
# 	    while(True):
# 	        htmltext = driver.page_source
# 	        soup = BeautifulSoup(htmltext,"lxml")
# 	        postList = soup.find_all('div','_2a_i')
# 	        postN = len(postList)
# 	        try:
# 	            driver.find_element_by_css_selector('div._2b1h.async_elem').click()
# 	        except:
# 	            pass
# 	        time.sleep(delay)
# 	        htmltext = driver.page_source
# 	        soup = BeautifulSoup(htmltext,"lxml")
# 	        postList_1 = soup.find_all('div','_2a_i')
# 	        postN_1 = len(postList_1)

# 	        if(postN == postN_1):
# 	            break
	            
# 	    for post in postList:
# 	        idd = re.findall('feed_story_ring([0-9]{1,})',str(post))[0]
# 	        name = post.find('div','_2b05').text
# 	        date_formats = ["%m月%d日下午%H:%M","%m月%d日上午%H:%M"]
# 	        if '剛剛' in utime:
# 	        	utime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# 	        else:
# 	        	if '下午' in utime:
# 	        		utime = dateparser.parse(utime,date_formats=date_formats)
# 	        		utime = utime+datetime.timedelta(hours=12)
# 	        	else:
# 	        		utime = dateparser.parse(utime,date_formats=date_formats).strftime("%Y-%m-%d %H:%M:%S")

# 	        update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# 	        utime = post.find('abbr').text
# 	        message = post.find('div', {'data-sigil':'comment-body'})
# 	        if(message.text == name):
# 	            message = '圖檔'
# 	        else:
# 	            message = message.text
# 	        daf = daf.append({
# 	        '留言者id':idd,
# 	        '留言者': name,
# 	        '更新時間':update_time,
# 	        '留言時間':utime,
# 	        '留言內容':message,
# 	        '留言網址':url
# 	    }, ignore_index=True)
	        
# 	daf.to_csv('留言內容.csv',index=False,encoding='utf-8-sig')
# 	print('Finish')
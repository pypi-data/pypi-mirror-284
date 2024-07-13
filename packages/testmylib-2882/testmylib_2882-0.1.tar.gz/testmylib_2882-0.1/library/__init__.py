import re
import os
import json
import random
import requests
import urllib.request
class TikTok:
	@staticmethod
	def Info(user):
		url = 'https://www.tiktok.com/@'+user
		page = urllib.request.urlopen(url)
		content = (page.read()).decode('utf-8')
		user_id_match = re.search(r'"id":"(\d+)"', content)
		user_id = user_id_match.group(1) if user_id_match else None
		
		unique_id_match = re.search(r'"uniqueId":"([^"]+)"', content)
		unique_id = unique_id_match.group(1) if unique_id_match else None
		
		nickname_match = re.search(r'"nickname":"([^"]+)"', content)
		nickname = nickname_match.group(1) if nickname_match else None
		
		follower_count_match = re.search(r'"followerCount":(\d+)', content)
		follower_count = follower_count_match.group(1) if follower_count_match else None
		
		following_count_match = re.search(r'"followingCount":(\d+)', content)
		following_count = following_count_match.group(1) if following_count_match else None
		
		heart_count_match = re.search(r'"heartCount":(\d+)', content)
		heart_count = heart_count_match.group(1) if heart_count_match else None
		
		avatar_url_match = re.search(r'"avatarLarger":"([^"]+)"', content)
		avatar_url = avatar_url_match.group(1).replace(r'\u002F', '/') if avatar_url_match else None
		
		video_count_match = re.search(r'"videoCount":(\d+)', content)
		video_count = video_count_match.group(1) if video_count_match else None
		
		bio_match = re.search(r'"signature":"([^"]+)"', content)
		bio = bio_match.group(1) if bio_match else None
		
		verified_match = re.search(r'"verified":(\w+)', content)
		verified = verified_match.group(1) if verified_match else None
		data = {"status_code": 200, "info": {"user_id": user_id, "unique_id": unique_id, "nickname": nickname, "follower": follower_count, "following": following_count, "hearts": heart_count, "avatar": avatar_url, "video": video_count, "verified": verified, "bio": bio}}
		json_string = json.dumps(data)
		return json_string
		
	def VID(url):
		if "https://vt.tiktok.com/" in url:
			headers = {
			    'authority': 'ytshorts.savetube.me',
			    'accept': 'application/json, text/plain, */*',
			    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'content-type': 'application/json',
			    'origin': 'https://ytshorts.savetube.me',
			    'referer': 'https://ytshorts.savetube.me/ar/tiktok-downloader-online?id=521909177',
			    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-origin',
			    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
			}
			json_data = {
			    'url': url,
			}
			try:
				res = requests.post('https://ytshorts.savetube.me/api/v1/tiktok-downloader', headers=headers, json=json_data).json()
				video = res["response"]["resolutions"]["HD Video"]
				thumbnail = res["response"]["thumbnail"]
				data = {"status_code": 200, "data": {"video": video, "thumbnail": thumbnail}}
				json_string = json.dumps(data)
				return json_string
			except:
				data = {"status_code": 404}
				json_string = json.dumps(data)
				return json_string
		else:
			data = {"status_code": 404}
			json_string = json.dumps(data)
			return json_string
		
	def IMG(url):
		if "https://vt.tiktok.com/" in url:
			headers = {
			    'authority': 'ytshorts.savetube.me',
			    'accept': 'application/json, text/plain, */*',
			    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'content-type': 'application/json',
			    'origin': 'https://ytshorts.savetube.me',
			    'referer': 'https://ytshorts.savetube.me/ar/tiktok-photo-downloader',
			    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-origin',
			    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
			}
			
			json_data = {
			    'url': url,
			    'apiUrl': '/tiktok-picture-downloader',
			}
			try:
				res = requests.post('https://ytshorts.savetube.me/api/v1/downloader-api', headers=headers, json=json_data).json()
				images = res["response"]["images"]
				thumbnail = res["response"]["thumbnail"]
				title = res["response"]["title"]
				data = {"status_code": 200, "data": {"images": images, "thumbnail": thumbnail, "title": title}}
				json_string = json.dumps(data)
				return json_string
			except:
				data = {"status_code": 404}
				json_string = json.dumps(data)
				return json_string
		else:
			data = {"status_code": 404}
			json_string = json.dumps(data)
			return json_string
def Telegram_Support(text):
	if "str" in str(type(text)):
		rand = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		email = str(''.join(random.choice(rand) for i in range(int(random.randint(6,9)))))+random.choice(["@gmail.com","@hotmail.com","@yahoo.com","@live.com"])
		rand = ["1","2","3","4","5","6","7","8","9","0"]
		rand_num = str(''.join(random.choice(rand) for i in range(int((10)))))
		phone_1 = "+1"+rand_num
		phone_2 = "+7"+rand_num
		phone_3 = "+44"+rand_num
		phonse = phone_1,phone_2,phone_3
		phone = random.choice(phonse)
		Countries = "English","Español","Français","Italiano","Українська"
		country = random.choice(Countries)
		
		cookies = {
			'cookie': 'stel_ssid=e903cc958eed67339f_11355632487222066292'
		}
		headers = {
		    'authority': 'telegram.org',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'cache-control': 'max-age=0',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://telegram.org',
		    'referer': 'https://telegram.org/support',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'same-origin',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		data = {
		    'message': text,
		    'email': email,
		    'phone': phone,
		    'setln': country,
		}
		try:
			response = requests.post('https://telegram.org/support', headers=headers, cookies=cookies, data=data).text
		except requests.exceptions.ConnectionError:
			Telegram_Support(text)
		res_get = re.compile(r'<div class="alert alert-success"><b>(.*?)</b><br/>(.*?)</div>', re.DOTALL)
		match = res_get.search(response)
		if match:
			responses = match.group(1) + " " + match.group(2)
			rand = ["1","2","3","4","5","6","7","8","9","0"]
			rand_num = str(''.join(random.choice(rand) for i in range(int((10)))))
			if "شكرًا على بلاغك&#33; سنحاول الرّد بأسرع ما يمكن." in responses:
				data = {"status_code": 200, "data": {"message": "Success"}}
				json_string = json.dumps(data)
				return json_string
			else:
				data = {"status_code": 200, "data": {"message": "unSuccess"}}
				json_string = json.dumps(data)
				return json_string
		else:
			data = {"status_code": 200, "data": {"message": "try again later ."}}
			json_string = json.dumps(data)
	else:
		data = {"status_code": 404}
		json_string = json.dumps(data)
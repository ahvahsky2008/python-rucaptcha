import requests
import time
import urllib3
#site_key = "6Lf77CsUAAAAALLFD1wIhbfQRD07VxhvPbyQFaQJ"

class ReCaptcha:
	def __init__(self, recaptcha_api, sleep_time=5):
		self.url_request = "http://2captcha.com/in.php"
		self.url_response = "http://2captcha.com/res.php"
		self.RECAPTCHA_KEY = recaptcha_api
		self.sleep_time = sleep_time

	#Работа с капчей
	#тестовый ключ сайта
	def captcha_handler(self, site_key="6Lf77CsUAAAAALLFD1wIhbfQRD07VxhvPbyQFaQJ", page_url='http://127.0.0.1:5000/'):
		
		captcha_download = 'http://rucaptcha.com/in.php?key={0}&method=userrecaptcha&googlekey={1}&pageurl={2}&json=1'\
			.format(self.RECAPTCHA_KEY, site_key, page_url)
		
		answer = requests.request('GET', captcha_download)
		print(answer.json())
		#пейлоад с ключем сайта, методом, и ответом в json формате
		payload = {"key": self.RECAPTCHA_KEY,
					"method": "post",
					"json": 1}

		#получаем ID капчи
		captcha_id = {(requests.request('POST',
										"http://rucaptcha.com/in.php",
										data=payload).json())['request']}
		print(captcha_id)
		answer = 'http://rucaptcha.com/res.php?key={0}&action=get&id={1}&json=1'.format(self.RECAPTCHA_KEY, captcha_id)
		
		# Ожидаем решения капчи
		time.sleep(self.sleep_time * 4)
		
		while True:
			captcha_response = requests.request('GET', answer)
			if captcha_response.json()["request"] == 'CAPCHA_NOT_READY':
				time.sleep(self.sleep_time)
			else:
				return captcha_response.json()["request"]




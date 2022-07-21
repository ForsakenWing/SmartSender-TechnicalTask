"""
Хотел попробовать регистрацию проверить с статичной рекапчей
(Немного абсурдно, конечно, пытаться таким банальным способом гугловскую рекапчу обходить,
но все же.) Попробуйте этот файлик позапускакть и посмотреть, есть ли запись в бдшке
(Сомневаюсь, конечно, что она есть, тк 302 статус код с редиректом должен идти, но все же)

Курл, если что,  прямо в терминале будет
"""


import requests
from faker import Faker

fake = Faker()
fake.name()

cookies = {
    'first_time_referrer': 'google.com',
    '_ga': 'GA1.1.1933669828.1658314912',
    'hubspotutk': '2f4f5661975b62ade0fb89b52dcd45ac',
    '__hssrc': '1',
    '_ga_3B9NJEWQ3W': 'GS1.1.1658409351.4.0.1658409351.60',
    '__hstc': '41880957.2f4f5661975b62ade0fb89b52dcd45ac.1658314912524.1658395231942.1658409352600.3',
    '__hssc': '41880957.1.1658409352600',
    'PHPSESSID': '7ee4698e9faef4109be0e96755dd1383',
}

headers = {
    'authority': 'partner.smartsender.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'first_time_referrer=google.com; _ga=GA1.1.1933669828.1658314912; hubspotutk=2f4f5661975b62ade0fb89b52dcd45ac; __hssrc=1; _ga_3B9NJEWQ3W=GS1.1.1658409351.4.0.1658409351.60; __hstc=41880957.2f4f5661975b62ade0fb89b52dcd45ac.1658314912524.1658395231942.1658409352600.3; __hssc=41880957.1.1658409352600; PHPSESSID=7ee4698e9faef4109be0e96755dd1383',
    'dnt': '1',
    'origin': 'https://partner.smartsender.io',
    'referer': 'https://partner.smartsender.io/registration',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}


class Data:

    first_name, last_name, *_ = fake.name().split(' ')
    email = fake.email()
    password = fake.password()


random_data = Data()


data = {
    'registration[firstName]': random_data.first_name,
    'registration[lastName]': random_data.last_name,
    'registration[email]': random_data.email,
    'registration[plainPassword]': random_data.password,
    'g-recaptcha-response': '03ANYolqvOnZOkr5e21irYt5PmwUufZ8nERDpNpopJIIt_NbjOVkpmsIMf5Aamcf3YpO7kCcIEWkDR6vs8J6feHBnXr_f9ruedg2tbXLzykxyOZaVQZqxMpFf9U8hNSv9dtPFilxJbLYvgmXtH-5gCHNMJ8Y8izJqhNP_8N-cupZ9v0o4tvjFV2P211Xi8KndKSsrdhtcl7NbL2CiEA_EK2f8NgNREEoKFbPA_5R831oOTn0fctmBp0AG6ODhifLhE4efvscAoPXgwAUTmUuCsFvKHeLJmoAKg51Ap4gCWJ2H6HLYbBcwHxsGzcLfpwEZBgdXMgtq6bbtalS7LSkOzVgwl-KXmTVnkhhiuzqU_Sp04rqDV8zzscPfI-xNFI3M6e4M59XpFeZmxPMp302cLrThV50HF56fsuI3uUACZoWuWEWV1wIhZQwnw7-E_ZfSB5-ORbYpAvVJAnwjOzNctsxaQViyqmxol5Q',
    'registration[privacyConfirm]': '1',
    'registration_recaptcha': '',
    'registration[_token]': 'KqySCkbLSUd39REEHH4aFjhqz48x_GdcFZy4VEuV4ck',
}
with requests.Session() as session:
    session.max_redirects = 0
    response = session.post('https://partner.smartsender.io/registration', cookies=cookies, headers=headers, data=data)
    from curlify import to_curl
    print(to_curl(response.request), '\n')
    print(response.text, response.content, response.cookies, response.status_code)

import time
import requests
from anticaptchaofficial.recaptchav3proxyless import *
solver = recaptchaV3Proxyless()

solver.set_verbose(1)
solver.set_key("f3a44e66302c61ffec07c80f4732baf3")
solver.set_website_url("https://ebanking.vietabank.com.vn/")
solver.set_page_action("home_page")
solver.set_min_score(0.3)
solver.set_soft_id(0)

solver.set_website_key('6LeOhmAjAAAAAAE4tUjHQ5jPpr_XNAeaYREy9fDw')
reCaptcha_response = solver.solve_and_return_solution()
print(reCaptcha_response)

# api_key = "CAP-6C2884061D70C08F10D6257F2CA9518C"  # your api key of capsolver
# site_url = "https://ebanking.vietabank.com.vn/"  # page url of your target site


# def capsolver(site_key):
#     payload = {
#         "clientKey": api_key,
#         "task": {
#             "type": 'ReCaptchaV3TaskProxyLess',
#             "websiteKey": site_key,
#             "websiteURL": site_url,
#             "minScore": 0.7
#         }
#     }
#     res = requests.post("https://api.capsolver.com/createTask", json=payload)
#     resp = res.json()
#     task_id = resp.get("taskId")
#     if not task_id:
#         print("Failed to create task:", res.text)
#         return
#     print(f"Got taskId: {task_id} / Getting result...")

#     while True:
#         time.sleep(1)  # delay
#         payload = {"clientKey": api_key, "taskId": task_id}
#         res = requests.post("https://api.capsolver.com/getTaskResult", json=payload)
#         resp = res.json()
#         status = resp.get("status")
#         if status == "ready":
#             return resp.get("solution", {}).get('gRecaptchaResponse')
#         if status == "failed" or resp.get("errorId"):
#             print("Solve failed! response:", res.text)
#             return
# reCaptcha_response = capsolver('6LeOhmAjAAAAAAE4tUjHQ5jPpr_XNAeaYREy9fDw')
# print(reCaptcha_response)
# url = "https://onlinebanking.eximbank.com.vn/api/IB/KHDN/login/siteVerify"

# payload = json.dumps({
#   "captcha": "03AFcWeA5GOucXMwEYOcO52ehQ5OuBD5B_bLdARG4wCKKU4YHkvCdo-fIb5_TE80HoyMZn6AxXhSzLC_QPaNPv3CJklK5wxmBJlxCIiLV0EiMfAdAsXTU9_fxkhwDHie0O_ndLIiGj2NUBMMRrKD3nULaoXraD_p4cyzMXs5Gv5SUI3CvcXyZVtj9NMJZKa_IkZ_TuWNl8U3mpDg9kNggyL_9TktR2EaqRrV_qj9rkUGf2-rA4l8T7fmCQOsusAUgxYGsg_FPPhvNYOsaEhWznjHCQoHeupPCsOlO6vp-1vtfp1fg4PAUoPItW4VqHnxTAMXGjpHzNc97ZjJEQPhA0YeMsgB6E52k1EKO817-ZL91eP6SDe4Q6b45O4BLsP72BueUS8QgkqAmRtRwBorQn6xSuz9UzxBYq6i8OOxl081z7oEl8b5vBddR0_UConB9G4lfx9ibUQjQa3sYfMEEZZDWiWUAw2V2pLnFi6fR9AyCV1O1PD0NLVpYntROq_EC5Yf6rhdLqSuNvr9knTrNTTGeAsF8OvercmEIB5eyTOrVJX2FfViKGHmOiHeTT8xlgsPBFnZwsIn5vfFSrrEp7WBiA3mbQwBVzXXTZPepirsK3SRmZJjhPBiNKNBZAUFfBZMqsQuH2JFDfD6mZ-liDa6VKoxywdm8QU1Ik_HKXzpYMEYXZA0ctql5Fyyk43w7bJazrr6KUs2wYr83Tv4vJ6y0p5x3xHUpHnKxEtbckAz42uSv8sWdZR2OG_YSLogVBVm1aizS6GhEadOHZzl6aKqOiS7LOYzXgFXADkfapH-Ip7LybG_T-TfZMPzrmSoPBxTeixLIEMt8LKpxavK6IMOoRrU6baUUzkR4GX8aGS5DqXBZWdREdkdrvN9xdvCm9-5QaWp2wsCIS",
#   "userId": "121650448"
# })
# headers = {
#   'Accept': 'application/json, text/plain, */*',
#   'Accept-Language': 'en-US,en;q=0.9',
#   'Connection': 'keep-alive',
#   'Content-Type': 'application/json',
#   'Cookie': '_ga=GA1.1.1323823239.1720630752; _ga_FB2E07LDSY=GS1.1.1730754080.9.0.1730754080.0.0.0; TS01686812=01210e54f6526bfbff76ce2bd30fb0c66ae8b7fd22523030c42c51885c08388795b8712f51739683e01fe6c464e3c75f960e348d79; TS01686812=01210e54f6abbe559188268489e16062edc1069b63f0cdeb9fc835afc327bde61c5eba595d5533df9f6e6ee32ad4b737d4c4149f37',
#   'Origin': 'https://onlinebanking.eximbank.com.vn',
#   'Referer': 'https://onlinebanking.eximbank.com.vn/KHDN/account/login-corp?returnUrl=%2Fhome',
#   'Sec-Fetch-Dest': 'empty',
#   'Sec-Fetch-Mode': 'cors',
#   'Sec-Fetch-Site': 'same-origin',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
#   'X-Token': '',
#   'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

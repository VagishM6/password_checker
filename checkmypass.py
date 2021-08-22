import requests
import hashlib
import sys

def url_request(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Detected: {res.status_code} Check and Try again!')
    return res

def get_password_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_password_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, last_char = sha1password[:5], sha1password[5:]
    # response contains all the hashes start with the 5 chars we gave
    url_response = url_request(first5_char)

    return get_password_count(url_response, last_char)


def main(args):
    for password in args:
        count = pwned_password_check(password)
        if count:
            print(f'{password} was found {count} many times...you should probably change the password.')
        else:
            print(f'{password} was NOT found carry on!')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
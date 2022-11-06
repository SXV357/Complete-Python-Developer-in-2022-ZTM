import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + \
        query_char  # represents 1st 5 digits of hash
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, Check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    # to get hashes that match the one passed and how many times they've been hacked
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:  # hashes stores a tuple of multiple arrays with 2 items each
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # needs to be encoded before being hashed and to agree with API, needs to be in upper case
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    # sending first 5 digits to the API
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times... You should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')

# taking inputs through terminal
# if __name__ == '__main__':
#     sys.exit(main(sys.argv[1:]))

# taking inputs through file
with open(r'C:/Users/14058/OneDrive/Desktop/Programming/Python Stuff/Projects/PwChecker/passwords.txt', 'r') as file:
    try:
        passwords = file.read().splitlines()
    except FileNotFoundError as err:
        print(f'{err}. Check the file path and try again')

if __name__ == '__main__':
    main(passwords)

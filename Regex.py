import re

# 999 999-9999


def extract_phone(ip):
    # r mean cek the pattern
    phone_reg = re.compile(r'\d{3} \d{3}-\d{4}')
    # search dalam sring (ke dalam all sentence)
    m = phone_reg.search(ip)

    if m:
        return True
    else:
        return False


# match must in depan
def extract_phone_match(ip):
    phone_reg = re.compile(r'\d{3} \d{3}-\d{4}')
    # search dalam sring (ke dalam all sentence)
    m = phone_reg.match(ip)

    if m:
        return True
    else:
        return False


print(extract_phone("my phone number is 423 231-2314 and 423-234-9999"))
print(extract_phone_match("423 231-2314 is my phone number"))

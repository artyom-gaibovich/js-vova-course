def generate_id(length=16):
    timestamp = str(int(time.time() * 1000000))
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits,k=length-len(timestamp)))
    id_str = timestamp + random_chars



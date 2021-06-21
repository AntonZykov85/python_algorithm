import hashlib, uuid

my_str = 'azazaz'
hashed_set = set()
substriings = set()
salt = uuid.uuid4().hex

for i in range(len(my_str)):
    for j in range(i + 1, len(my_str) + 1):
        if my_str[i:j] != my_str:
            substriings.add(my_str[i:j])
            hashed_set.add(hashlib.sha256(salt.encode() + my_str[i:j].encode()).hexdigest())

for i in substriings:
    print(f'substring id: "{i}".')

print(f'total: {len(hashed_set)} unique substrings')
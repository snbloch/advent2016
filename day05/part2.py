import md5
from operator import itemgetter

door_id = 'ffykfhsq'
password = {}

found_hashes = 0
counter = 0
while found_hashes < 8:
    md5sum = md5.md5(door_id + str(counter))
    md5sum = md5sum.hexdigest()
    if md5sum[0:5] == '0' * 5 and int(md5sum[5], 16) >= 0 and int(md5sum[5], 16) < 8:
        if password.get(int(md5sum[5], 16)) == None:
            password[int(md5sum[5], 16)] = md5sum[6]
            found_hashes += 1
    counter += 1

password_string = ''
for char in sorted(password.items(), key=itemgetter(0)):
    password_string += char[1]

print password_string

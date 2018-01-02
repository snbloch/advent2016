import md5

door_id = 'ffykfhsq'
password = ''

found_hashes = 0
counter = 0
while found_hashes < 8:
    md5sum = md5.md5(door_id + str(counter))
    if md5sum.hexdigest()[0:5] == '0' * 5:
        password += md5sum.hexdigest()[5]
        found_hashes += 1
    counter += 1

print password

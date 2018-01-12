import hashlib

salt = 'jlmsuwbz'
index = 0
indexes_found = []
num_found = 0

while num_found < 64:
    repeated_char = None
    md5sum = hashlib.md5(salt + str(index)).hexdigest()
    string_position = 0
    while string_position < len(md5sum) - 2:
        if md5sum[string_position] == md5sum[string_position + 1] and md5sum[string_position + 1] == md5sum[string_position + 2]:
            repeated_char = md5sum[string_position]
            break
        string_position += 1
    if repeated_char != None:
        iterator = index + 1
        while iterator < index + 1000:
            md5sum = hashlib.md5(salt + str(iterator)).hexdigest()
            string_position = 0
            while string_position < len(md5sum) - 4:
                if md5sum[string_position] == repeated_char and md5sum[string_position] == md5sum[string_position + 1] and md5sum[string_position + 1] == md5sum[string_position + 2] and md5sum[string_position + 2] == md5sum[string_position + 3] and md5sum[string_position + 3] == md5sum[string_position + 4] and index not in indexes_found:
                    indexes_found.append(index)
                    num_found += 1
                    break
                string_position += 1
            iterator += 1
    index += 1

print indexes_found

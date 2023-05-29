def transform_string(s):
    transformed = list(s)
    prev_char = ''
    prev_changed = False

    for i in range(len(s)):
        ascii_value = ord(transformed[i])

        if ascii_value % 2 == 0:
            if not prev_changed:
                new_char = chr((ascii_value + (ascii_value % 7)) % 128)
                transformed[i] = new_char
                prev_char = new_char
                prev_changed = True
        else:
            if i > 0 and not prev_changed:
                new_char = chr((ascii_value - (ascii_value % 5)) % 128)
                transformed[i - 1] = new_char
                prev_char = new_char
                prev_changed = True

    return ''.join(transformed)


s = 'sHQen}'
transformed_string = transform_string(s)
print(transformed_string)

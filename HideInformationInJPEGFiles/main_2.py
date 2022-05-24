with open('photo.jpg', 'ab') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 9)

    with open() as e:
        e.write(f.read())
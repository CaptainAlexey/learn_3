with open('referat.txt', 'r', encoding='utf-8') as refer:
    content = refer.read()
    content_2 = content
    content = content.replace('\n','')
    print(f'Количество символов: {len(content)}')
    content = content.replace(',','')
    content = content.replace('.','')
    content = content.split()
    print(f'Количество слов: {len(content)}')
    content_2 = content_2.replace('.', '!')
    with open('referat2.txt', 'a', encoding='utf-8') as refer_2:
        refer_2.write(content_2)
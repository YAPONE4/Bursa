"""
1) Создать текстовый txt-файл.
2) Вставить туда англоязычную статью из Википедии.
3) Написать функцию со следующим функционалом:
3.1) Прочитать файл построчно, вывести на печать.
3.2) Создать список и добавить туда непустые строки.
3.3) В строках оставить только латинские буквы и пробелы. Прочие символы удалить.
3.4) Объединить список в единую строку. вывести на печать.
3.5) Подсчитать количество вхождений различных слов в тескте. Подсчет вести в словаре.
3.6) Вывести на печать 10 наиболее популярных и наименее популярных слов (“ 1) -- hello -- 15”).
3.7) Заменить наименее популярные слова на “PYTHON”.
3.8) Создать новый txt-файл.
3.9) Записать текст в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов и не делить слова.
"""

def wiki_function():
    f = open("white.txt", "r")
    lines = f.readlines()

    nslines = []
    for i in lines:
        if i != '\n':
            nslines.append(i)
    for i in nslines:
        print(i)

    onetext = ''
    for i in nslines:
        line = ''
        for j in range (0, len(i)):
            if i[j].isalpha() or i[j] == ' ':
                line += i[j]
            elif i[j] == "\n":
                    line += ' '
        f = line
        onetext += f
    print(onetext)

    words = onetext.split(' ')
    dictionary = {}
    for word in words:
        if word != '':
            count = dictionary.setdefault(word, 0)
            dictionary[word] = count + 1
    
    list_dictionary = list(dictionary.items())
    list_dictionary.sort(key=lambda i: i[1])
    print('\n\nLeast popular words:\n')
    least = []
    for i in range(0, 10):
        top = list_dictionary[i]
        least.append(top[0])
        print('(“ {}) -- {} -- {}”)'.format(i + 1, top[0], top[1]))
    print('\n\nMost popular words:\n')
    for i in range(0, 10):
        top = list_dictionary[len(list_dictionary) - i - 1]
        print('(“ {}) -- {} -- {}”)'.format(i + 1, top[0], top[1]))

    for i in words:
        if i in least:
            for j in range(len(words)):
                if words[j] == i:
                    words[j] = 'PYTHON'
    
    of = open("whiteredacted.txt", "w")
    max = 0
    for i in words:
        write_text = i + ' '
        max += len(write_text)
        if max > 100 :
            max = len(write_text)
            of.write('\n')
        of.write(write_text)
    return 1

wiki_function() 

# Создать список (библиотека книг), состоящий из словарей (книги). Словари должны содержать как минимум 5 полей
# (например, номер, название, год издания...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# library = [{"id" : 123456, "title" : "Война и мир", "author" : "Толстой",...} , {...}, {...}, ...]
# Реализовать функции:
# – вывода информации о всех книгах;
# – вывода информации о книге по введенному с клавиатуры номеру;
# – вывода количества книг, старше введённого года;
# – обновлении всей информации о книге по введенному номеру;
# – удалении книги по номеру.
# Провести тестирование функций.



library = [{"id" : 87, "title" : "Война и мир", "author" : "Толстой", "year" : 1867}, {"id" : 2, "title" : "Отцы и дети", "author" : "Тургенев", "year" : 1862}, {"id" : 3, "title" : "Герой нашего времени", "author" : "Лермонтов", "year" : 1840}, {"id" : 4, "title" : "Когда плачут цикады", "author" : "Рюкиши07", "year" : 2002}, {"id" : 5, "title" : "Когда плачут чайки", "author" : "Рюкиши07", "year" : 2007}, {"id" : 6, "title" : "Идиот", "author" : "Достоевский", "year" : 1868}, {"id" : 7, "title" : "Преступление и наказание", "author" : "Достоевский", "year" : 1866}, {"id" : 8, "title" : "Бледный огонь", "author" : "Набоков", "year" : 1962}, {"id" : 9, "title" : "Божественная Комедия", "author" : "Алигьери", "year" : 1472}, {"id" : 10, "title" : "1984", "author" : "Оруэлл", "year" : 1949}]
def info() :
    for i in library :
        print(i)

def outp(k) :
    for i in library :
        if i ["id"] == k :
            print(library[k - 1])

def year(k) : 
    for i in library :
        if i ["year"] > k :
            print(i)
def refresh(k) :
    for i in library :
        if i ["id"] == k :
            i["id"] = int(input())
            i["title"] = str(input())
            i["author"] = str(input())
            l = int(input())
            i["year"] = l
            print(i)

def dele(k) :
    for i in library :
        if i ["id"] == k :
            library.remove(i)

c = input()
if c == 'I' :
    info()
if c == 'O' :
    f = int(input())
    outp(f)
if c == 'Y' :
    f = int(input())
    year(f)
if c == "R" :
    f = int(input())
    refresh(f)
    info()
if c == "D" :
    f = int(input())
    dele(f)
    info()

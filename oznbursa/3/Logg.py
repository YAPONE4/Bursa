import datetime

def logg(comm, obj):
    wf = open('log.txt', 'a')
    wf.write('{} --- {} --- {}\n'.format(comm, datetime.datetime.now(), obj))
    wf.close()
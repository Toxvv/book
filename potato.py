from pythonds import Queue
def hotPotato(namelist,num):
    simqueue=Queue.Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()
    return simqueue.dequeue()

namelist=['1','2','3','4','5','6']
number=7

final=hotPotato(namelist,number)
print(final)
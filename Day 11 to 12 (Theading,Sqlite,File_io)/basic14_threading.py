import threading
import random
import time
import  concurrent.futures

def run_func(i):
    print('{} :No thread stared : {}'.format(i,time.strftime('%H:%M:%S')))
    time.sleep(random.randint(1,5))
    print(i,':No thread stoped')

for i in range(10):
    thread=threading.Thread(target=run_func(i),args=(i,))
    thread.start()
print(threading.activeCount())
print(threading.enumerate())

start_time=time.perf_counter()

def do_something(t):
    print('This function started working')
    time.sleep(1)
    print('functon has stoped after 1 sec')


threads=[]
for _ in range(10):
   t1=threading.Thread(target=do_something,args=(1,))
   t1.start()
   threads.append(t1)

for thread in threads:
    thread.join()

end_time=time.perf_counter()

print('Total time {}'.format(round(end_time-start_time,2)))


def func1(t):
    print("started func at:",t)
    time.sleep(t)
    print('func 1 is done at: ',t)


with concurrent.futures.ThreadPoolExecutor() as executor:
    sleep_times=[2,3,4,1]
    results=[executor.submit(func1,st) for st in sleep_times]
    for f in concurrent.futures.as_completed(results):
        print(f.result())


start=time.perf_counter()
def func2(t):
    print("func sleep for: ",t)
    time.sleep(t)
    print('func done sleeping at: ',t)
    return t

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[2,3,4,3]
    results=executor.map(func2,secs)
    for result in results:
        print(result)


end=time.perf_counter()

print('Time takes to complete :{}'.format(round(end-start,2)))

import threading
counter = 0
def upCounter():
    global counter
    for i in range(100000):
        counter += 1
def downCounter():
    global counter
    for i in range(100000):
        counter -= 1
thread1 = threading.Thread(target=upCounter)
thread1.start()
thread1.join()
thread2 = threading.Thread(target=downCounter)
thread2.start()
thread2.join()
print("Thread has finished execution ")
print(counter)

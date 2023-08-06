from datetime import datetime
import pandas as pd


# คำนวน fibonacci แบบไม่มี i/o
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# คำนวน fibonacci แบบมี i/o
def fibonacciWithIo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacciWithIo(n-1) + fibonacciWithIo(n-2)

if __name__ == "__main__":
    # กำหนดตัวแปร
    ns = [5, 10, 15, 20, 25, 30]
    withIoTime = []
    withOutIoTime =[]

    # วนลูป
    for n in ns:
        # มี i/o
        startTime = datetime.now()
        fibonacciWithIo(n)
        endTime = datetime.now()
        time = (endTime - startTime).total_seconds()
        withIoTime.append(time)

        # ไม่มี i/o
        startTime = datetime.now()
        fibonacci(n)
        endTime = datetime.now()
        time = (endTime - startTime).total_seconds()
        withOutIoTime.append(time)

    # จัดการข้อมูล
    data = {
        'มี I/O': withIoTime,
        'ไม่มี I/O': withOutIoTime
    }
    df = pd.DataFrame(data)
    # แสดงผล
    print("\n", df)



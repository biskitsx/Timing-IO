from datetime import datetime
import pandas as pd

# ฟังก์ชันจับเวลาที่ไม่ใช้ IO
def measureLoopTime(n):
    startTime = datetime.now()
    sum = 0
    for i in range (n):
        sum += i

    endTime = datetime.now()
    return (endTime-startTime).total_seconds()

# ฟังก์ชันจับเวลาที่ใช้ IO
def measureLoopTimeWithIO(n):
    startTime = datetime.now()
    sum = 0
    for i in range (n):
        sum += i
        print(i)

    endTime = datetime.now()
    return (endTime-startTime).total_seconds()


if __name__ == "__main__":
    # กำหนด input size และอาเรย์ที่ไว้เก็บเวลา
    size = [1000, 10000, 100000, 1000000, 10000000]
    withIoTime = []
    withOutIoTime =[]

    for n in size:
        # จับเวลาที่ไม่ใช้ I/O 
        timeWithOutIO = measureLoopTime(n)        
        withOutIoTime.append(timeWithOutIO)
        
        # จับเวลาที่ใช้ I/O
        timeWithIO = measureLoopTimeWithIO(n)
        withIoTime.append(timeWithIO)

    # แสดงผล
    df = pd.DataFrame({
        "Input Size (n)": size,
        "without IO": withOutIoTime,
        "with IO": withIoTime,
    })

    print(df)
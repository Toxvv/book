# 导入所需的模块
import random

# 创建任务类
class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randint(1, 20)  # 随机生成任务的页数

    def getTimestamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, current_time):
        return current_time - self.timestamp

# 创建打印机类
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度（每分钟打印的页数）
        self.currentTask = None  # 当前正在执行的任务
        self.timeRemaining = 0  # 任务剩余时间

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

# 创建任务队列类
class TaskQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# 创建任务模拟类
class TaskSimulator:
    def __init__(self, duration, ppm):
        self.printer = Printer(ppm)
        self.taskQueue = TaskQueue()
        self.duration = duration  # 模拟运行的时间（分钟）
        self.waitingTimes = []

    def simulation(self):
        for currentSecond in range(self.duration):
            if self.newPrintTask():
                task = Task(currentSecond)
                self.taskQueue.enqueue(task)
            if (not self.printer.busy()) and (not self.taskQueue.isEmpty()):
                task = self.taskQueue.dequeue()
                self.waitingTimes.append(task.waitTime(currentSecond))
                self.printer.startNext(task)
            self.printer.tick()
        averageWait = sum(self.waitingTimes) / len(self.waitingTimes)
        print("平均等待时间：%.2f秒，还剩 %d 个任务待处理。" % (averageWait, self.taskQueue.size()))

    def newPrintTask(self):
        num = random.randrange(1, 181)
        if num == 180:
            return True
        else:
            return False

# 创建任务模拟对象并运行模拟
simulator = TaskSimulator(3600, 5)  # 模拟运行1小时，打印机速度为每分钟5页
simulator.simulation()
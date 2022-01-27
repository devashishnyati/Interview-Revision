"""
There is an infinite stream of daily temperatures, design a data structure which allows to perform operations such as:

addTemperature(Date date, int temperature) // adds new temperature value at given day to the stream
updateTemperature(Date date, int newTemperature) // updates the temperature value at given day
removeTemperature (Date date) // removes the temperature for the given date from the stream
getLatestTemperature() // returns the latest temperature value from the stream
getMaxTemperature() // returns the max temperature seen so far
"""

cache = []
addTemp(date, temp) -> 
update(date, temp) -> 
remove(date)
getLatest() ->


class Node:
    def __init__(self, date, temp):
        self.date = date
        self.temp = temp
        self.next = None
        self.prev = None

class TemperatureStream:
    def __init__(self):
        # self.head = Node(0, 0)
        # self.tail = Node(0, 0)
        # self.head.next = self.tail
        # self.tail.prev = self.head
        # mm/dd/yyyy

        self.latest_date = [0]
        self.max_temp = [float('-inf')]

        self.cache = {}

    def add_temp(self, date, temp):
        # node = Node(date, temp)
        if date in self.cache:
            self.update_temp(date, temp)

        # self.cache[date] = node

        # # doubly linked list
        # temp = self.tail.prev
        # temp.next = node
        # node.prev = temp
        # node.next = self.tail
        # self.tail.prev = node
        self.cache[date] = temp
        if temp > self.max_temp[0]:
            self.max_temp.append(temp)
        
        if date > self.latest_date[0]:
            self.latest_date.append(date)




    def update_temp(self, date, temp):
        if date not in self.cache:
            return -1

        self.cache[date] = temp
        if temp > self.max_temp[0]:
            self.max_temp.append(temp)
        
        if date > self.latest_date[0]:
            self.latest_date.append(date)
        
    def remove_temp(self, date):
        # remove node from doubly linked list
        if date not in self.cache:
            return -1
        # node = self.cache[date]

        # node.prev.next = node.next
        # node.next.prev = node.prev
        # node.prev = None
        # node.next = None

        # # remove date from cache
        # del self.cache[date]

        temp = self.cache[date]

        if temp == self.max_temp[0]:
            self.max_temp.pop()

    def get_latest(self):
        pass

    def get_max_temp(self):
        pass






from datetime import datetime
from datetime import timedelta
import json
now = datetime.now()
table_list = []


#---------------------------------------------------------------
class PoolTable:
    def __init__(self, number):
        self.number = number
        self.isOccupied = False
        self.startTime = datetime.now()
        self.endTime =  datetime.now()
        self.duration = 0
        self.cost = 0

    def __repr__(self):
        return 'Table {0}, is occupied: {1}, start time : {2}, end time : {3}, duration : {4},cost :{5}'.format(self.number,self.isOccupied,self.startTime ,self.endTime, self.duration, self.cost)


    def table_checkin(self):
        self.isOccupied = True
        start_time = datetime.now()
        self.startTime = start_time


        print(table)
        # print(table_list)
    def table_checkout(self):
         end_time = datetime.now()
         self.endTime = end_time
         duration = end_time - self.startTime
         self.endTime = end_time
         self.duration = duration
         minutes = (duration.seconds / 60)
         hours = minutes /60
         cost = hours * 30
         self.cost = cost
         print(duration.seconds)
         self.isOccupied = False
         if (duration.seconds / 60) >= 60:
             in_terms_of_hour = float(duration.seconds) / 3600
             self.duration = in_terms_of_hour
         print(table_to_checkout)



    # def admin_table_list(self):


#-------------------------------------------
for i in range(1,13):
    pool_table = PoolTable(str(i))
    table_list.append(pool_table)

while True:
    assign_table = input('Enter the table number to assign or enter to quit: ')

    if assign_table == 'q':
        break


    table = table_list[int(assign_table) - 1]
    if table.isOccupied == True:
        print('Pool Table {0} is occupied, you cannot reassign it'.format(table.number))
    else :
        table.table_checkin()



while True:
    ask_to_checkout = input('Enter table number to checkout or q to quit: ')

    if ask_to_checkout == 'q':
        break

    table_to_checkout = table_list[int(ask_to_checkout) - 1]
    if(ask_to_checkout == table_to_checkout.number and table_to_checkout.isOccupied == True):
        table_to_checkout.table_checkout()
    else:
        print('Please enter a valid number')

print(table_list)
for each in table_list:
    print('***************')
    print('Table {0} \n is occupied : {1}, \n start time : {2} \n end time: {3}'.format(each.number, each.isOccupied, each.startTime, each.endTime ))
#---------------------------------------------
pool_table_json_array = []

class PoolTableJSON:
    def __init__(self):
        self.number = ""
        self.startTime = ""
        self.endTime = ""
        self.duration = ""
        self.cost = ""
    def asDictionary(self):
        return self.__dict__

for table in table_list:
    pt = PoolTableJSON()
    pt.number = table.number
    pt.startTime = table.startTime.isoformat()
    pt.endTime = table.endTime.isoformat()
    pt.duration = str(table.duration)
    pt.cost =table.cost
    pool_table_json_array.append(pt.asDictionary())



with open ('pool_table.json', 'w') as object_file:
    json.dump(pool_table_json_array, object_file)

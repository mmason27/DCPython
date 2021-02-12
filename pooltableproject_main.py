from pooltableproject import PoolTable
import datetime 
import json

pool_tables = []

for index in range(1, 13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

def time_format(td):
    return "%d:%d" % (td.seconds/3600, td.seconds%3600/60)

def display_tables():
    for table in pool_tables:
        if table.is_occupied == False:
            print(f"Pool Table - {table.table_number} | Status - Unoccupied")
        else: 
            print(f"Pool Table - {table.table_number} | Status - Occupied | Start Time - {table.start_time.strftime('%I:%M %p')} | Time Played - {time_format(table.time_played())}") 

def display_unoccupied_tables():
    print("The following tables are unoccupied: ")
    for table in pool_tables:
        if table.is_occupied == False:
            print(f"Pool Table - {table.table_number}")
    
def display_occupied_tables():
    for table in pool_tables:
        if table.is_occupied == True:
            print(f"Pool Table - {table.table_number} | Start Time - {table.start_time.strftime('%I:%M %p')} | Time Played - {time_format(table.time_played())}")

while True:
    try:
        print("Enter [1] to display all tables")
        print("Enter [2] to check-out a pool table")
        print("Enter [3] to check-in a pool table")
        print("Enter [q] to quit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_tables()
        elif choice == "2":
            display_unoccupied_tables()
            table_choice = int(input("Choose a table to check-out: "))
            table = pool_tables[table_choice - 1]
            table.checkout()
        elif choice == "3":
            display_occupied_tables()
            table_choice = int(input("Choose a table to check-in: "))
            table = pool_tables[table_choice -1]
            table.checkin()   
            print(f"End Time - {table.end_time.strftime('%I:%M %p')}")
            print(f"Total Time - {time_format(table.total_time())}")
        elif choice == "q":
            break
    except:
        print("Error! Invalid input. Please try again.")
        continue    

def convert_dt(time):
    if time == None:
        return "Unoccupied"
    else:
        return time.strftime('%I:%M %p')

dictionary_array = []
with open("02-12-2021.json", "w") as file_object:
    for table in pool_tables:
        p_dict = {"PoolTableNumber" : table.table_number, "StartTime" : convert_dt(table.start_time), "EndTime" : convert_dt(table.end_time)}
        dictionary_array.append(p_dict)
    json.dump(dictionary_array, file_object)







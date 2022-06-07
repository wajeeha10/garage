# Define all connection functions.
# import connection , execute, read query, and date function fron their  respective libraries.


from sql import execute_read_query
from sql import create_connection
from sql import execute_query
import datetime
from datetime import date

#creating connection to mysql database.
# provide  compleate database address to connection function. 
conn = create_connection('test1.cukicjxpnl1a.us-east-2.rds.amazonaws.com', 'admin', '12345free', 'test1db')
  
     
# Business functions.

# define a function to display main manu.
def display_menu():
    print("a - Add car\nd - Remove car\nu - Update car details\nr1 - Output all cars sorted by year (ascending)\nr2- Output all cars of a certain color\nq - Quit")


#create a table on mysql database with name garage having column Id, Make,Model,Year,color make id auto_increment.
def createtable():   #create table.

    create_table = """
    create table if not exists garage  (
    Id INT (6) unsigned auto_increment,  
    Make varchar(30) not null,
    Model varchar(30) not null,
    Year INT(6) unsigned,
    color varchar(30) not null,
    PRIMARY KEY (id)
    )
    """
    execute_query(conn, create_table ) # Call function to execute query.
 

#Define a function to add new record on garage table.
def addcar():    
    #Ask for new  record.
    car_make = input('Insert new_car make ')
    car_model = input('Insert new_car model ')
    car_year = input('Insert new_car built year')
    car_color = input('Insert new_car color')
    # add new car record to garage table.
    add_query = "INSERT INTO garage(make, model, year, color)VALUES('%s','%s','%s', '%s')" % (car_make, car_model, car_year, car_color)
    execute_query(conn, add_query) # Call function to add rercord.
    print('data recorded  in table garage')  # message to show record added successfully.


#Define a function to remove a car record from garage table.
def remove_car():
    #ask Id to delete.
    users_id_to_delete = input("what id you want to delete?")    
    # delete car record from users table.
    delete_statement = "DELETE FROM garage WHERE id = '%s'" % (users_id_to_delete)  
    execute_query(conn, delete_statement) #Call function to delete rercord.
    print('data removed from table garage') # message to show record deleted successfully.


#Define a function to update a car record from garage table.
def update():
    #Ask for new  record to update.
    update_id = input("insert id for update")
    new_make = input("insert new car make" )
    new_model = input("insert new car model" )
    new_year = input("insert new car built year" )
    new_color = input("insert new car color" )
    # updating car record.
    update_garage_query = """
    UPDATE garage
    SET Make = '%s' ,Model = '%s' , Year = '%s' , color = '%s' 
    WHERE id = '%s' """ % (new_make, new_model, new_year, new_color, update_id)
    execute_query(conn, update_garage_query) # Call function to update rercord.
    print('data updated in  table garage')   # message to show record has been updated successfully.


#Define a function to sort a car record by year.
def sort():
    # sort garage table data by year ascending(bt default).
    select_users =  "SELECT * FROM garage ORDER BY Year"
    # Call function to run query.
    users = execute_read_query(conn, select_users)
    for user in users:
        # Output all cars sorted by year (ascending).
        print(" Built year:" ,user["Year"], "Car make is : " + user["Make"] + " ,model : " + user["Model"] + "color is  "  + user["color"] )
    print('In table garage all cars sorted by year') # message to show data has been sorted successfully.


#Define a function to sort car record by car_color.
def colored():
    # Ask for a color to sort.
    col = input('Select your desired color ?')
    # sort desir color from garage table data.
    carcolor = "select * from garage where color = ('%s')" %(col)
    user = execute_read_query(conn, carcolor)   # Call function to run query.
    print('colored sorted')  # Message to show desired color data has been sorted successfully.
    print(user) #Output all cars of a certain color


# Define main function.
selection = 1
while selection != 'q' : #Apply loop to again ask for manu option  and quit. 
        display_menu()
        selection = input("Please Select an option:") # Ask for options.
        # Apply conditions to call required function.
        if selection == 'a': 
            addcar() 
        elif selection == 'd': 
            remove_car()
        elif selection == 'u':
            update() 
        elif selection == 'r1': 
            sort()
        elif selection == 'r2':
            colored()
        elif selection == 'q':          
            break
        else: # if user input wrong option.
            print ("Unknown Option Selected!")

     
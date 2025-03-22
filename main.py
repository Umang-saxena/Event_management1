import streamlit as st
import mysql.connector
mydb = mysql.connector.connect(
    host="st.secrets['db_host']",
    user=st.secrets["db_username"],
    password=st.secrets["db_password"], 
    database=st.secrets["db_database"]
)
mycursor = mydb.cursor()


from Events.Select.Select_AllRecords import selectAll 
from Events.Create.CreateClient import createClient
from Events.Create.CreateVenue import createVenue
from Events.Create.CreateEvent import createEvent
from Events.Delete.DeleteVenue import deleteVenue
from Events.Update.EventStatus import updateStatus


# Define the tables and their creation SQL
tables = {
    "Clients": """
        create table Clients
(Client_ID int auto_increment, Name char(50), Phone bigint , email varchar(30), primary key(Client_ID));
    """,
    "Venues": """
        create table Venues 
(Venue_ID int auto_increment, Name char(50) , Owner_Name char(50), Owner_Number bigint , price int , address char(100), primary key(Venue_ID));
    """,
    "Events": """
        create table Events
(Event_ID int auto_increment , Event_Date DATE , Event_Name char(50) , Start_Time time , End_Time time , Client_ID int , Venue_ID int , status bool , primary key(Event_ID) ,  foreign key (Client_ID) references Clients(Client_ID) , foreign key (Venue_ID) references Venues(Venue_ID));
        )
    """
}

# Check and create tables if missing
for table_name, create_sql in tables.items():
    mycursor.execute(f"""
        SELECT COUNT(*) 
        FROM information_schema.tables 
        WHERE table_schema = '{mydb.database}' AND table_name = '{table_name}'
    """)
    if mycursor.fetchone()[0] == 0:
        mycursor.execute(create_sql)
        mydb.commit()

# Create a page dropdown
page = st.selectbox("Choose your page", [
    "Show All Events",
    "Create Client",
    "Create Venue",
    "Create Event",
    "Delete Venue",
    "Update Event Status"
])

# Display the selected page
if page == "Show All Events":
    st.write("Displaying all events...")
    selectAll(mycursor,mydb)
elif page == "Create Client":
    createClient(mycursor,mydb)  
elif page == "Create Venue":
    createVenue(mycursor,mydb)  
elif page == "Create Event":
    createEvent(mycursor,mydb)  
elif page == "Delete Venue":
    deleteVenue(mycursor,mydb)  
elif page == "Update Event Status":
    updateStatus(mycursor,mydb)  

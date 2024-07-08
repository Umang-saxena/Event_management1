import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="umang",
    database="Mini_Project_Event_Management"
)
mycursor = mydb.cursor()


import streamlit as st
from Events.Select.Select_AllRecords import selectAll 
from Events.Create.CreateClient import createClient
from Events.Create.CreateVenue import createVenue
from Events.Create.CreateEvent import createEvent
from Events.Delete.DeleteVenue import deleteVenue
from Events.Update.EventStatus import updateStatus

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

import streamlit as st


def createEvent(mycursor,mydb):
    st.header("Create New Event")
    event_date = st.date_input("Event Date")
    event_name = st.text_input("Event Name")
    start_time = st.time_input("Start Time")
    end_time = st.time_input("End Time")

    # Fetch venue list from database
    mycursor.execute('SELECT * FROM Venues')
    venue_list = mycursor.fetchall()
    venue_id = st.selectbox("Select Venue", [f"{venue[0]}: {venue[1]}" for venue in venue_list])

    # Fetch client list from database
    mycursor.execute('SELECT * FROM Clients')
    client_list = mycursor.fetchall()
    client_id = st.selectbox("Select Client", [f"{client[0]}: {client[1]}" for client in client_list])

    status = st.radio("Event Status", ["On Schedule", "Cancelled"])

    if st.button("Create Event"):
        try:
            query = """
            INSERT INTO Events (Event_Date, Event_Name, Start_Time, End_Time, Client_ID, Venue_ID, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (event_date, event_name, start_time, end_time, int(client_id.split(":")[0]), int(venue_id.split(":")[0]), status == "On Schedule")
            mycursor.execute(query, values)
            mydb.commit()
            st.success("New Event Created Successfully")
        except:
            print("Error Creating the event")



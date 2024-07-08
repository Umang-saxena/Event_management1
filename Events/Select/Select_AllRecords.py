import streamlit as st

def selectAll(mycursor,mydb):
    st.header("All Events")
    mycursor.execute('SELECT * FROM events')
    event_list = mycursor.fetchall()

    for event in event_list:
        status = "Cancelled" if event[7] == 0 else "On Schedule"
        st.write(f"Event ID: {event[0]}, Event Name: {event[2]}, Event Status: {status}")



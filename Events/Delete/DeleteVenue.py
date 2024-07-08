import streamlit as st

def deleteVenue(mycursor, mydb):
    st.title("Venue Management App")
    st.write("Venue List:")
    mycursor.execute('SELECT * FROM Venues')
    myresult = mycursor.fetchall()
    for x in myresult:
        st.write(f"ID: {x[0]}, Name: {x[1]}, Location: {x[5]}, Capacity: {x[4]}")

    venue_id = st.text_input("Enter Venue ID from the list above to delete:")
    if st.button("Delete Venue"):
        try:
            # Check if there are associated events
            mycursor.execute(f"SELECT Event_ID FROM Events WHERE Venue_ID = {venue_id}")
            associated_events = mycursor.fetchall()
            if associated_events:
                st.warning("Cannot delete venue. Associated events exist.")
            else:
                # Delete the venue
                mycursor.execute(f"DELETE FROM Venues WHERE Venue_ID = {venue_id}")
                mydb.commit()
                st.success("Venue Deleted Successfully")
        except Exception as e:
            st.error(str(e))

# Usage example:
# deleteVenue(mycursor, mydb)

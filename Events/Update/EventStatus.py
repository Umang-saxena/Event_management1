import streamlit as st


def updateStatus(mycursor,mydb):
    st.header("Update Event Status")
    event_id = st.text_input("Enter Event ID To Update")
    status = st.radio("Select Updated Status", ["On Schedule", "Cancelled"])

    if st.button("Update Status"):
        try:
            # Check if the event ID exists in the database
            mycursor.execute(f'SELECT Event_ID FROM Events WHERE Event_ID = {event_id}')
            existing_event = mycursor.fetchone()
            if existing_event:
                new_status = 1 if status == "On Schedule" else 0
                mycursor.execute(f'UPDATE Events SET status = {new_status} WHERE Event_ID = {event_id}')
                mydb.commit()
                st.success("Event Status Updated Successfully")
            else:
                st.warning(f"Event ID {event_id} does not exist in the database.")
        except:
            st.error(f"Error updating status: ")




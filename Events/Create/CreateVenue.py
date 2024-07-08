import streamlit as st
def createVenue(mycursor,mydb):
    st.header("Create New Venue")
    venue_name = st.text_input("Venue Name").upper()
    owner_name = st.text_input("Owner Name")
    owner_number = st.text_input("Owner Number")
    price = st.number_input("Price Of Venue", min_value=0.0)
    address = st.text_area("Address Of The Venue")

    if st.button("Create Venue"):
        try:
            query = """
            INSERT INTO Venues (Name, Owner_Name, Owner_Number, price, address)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (venue_name, owner_name, owner_number, price, address)
            mycursor.execute(query, values)
            mydb.commit()
            st.success("New Venue Created Successfully")
        except Exception as e:
            st.error(str(e))

# Streamlit app


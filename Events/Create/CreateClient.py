import streamlit as st
import mysql.connector



def createClient(mycursor,mydb):
    st.header("Create New Client")
    client_name = st.text_input("Client Name")
    client_number = st.text_input("Client Phone Number")
    client_email = st.text_input("Client Email ID")

    if st.button("Create Client"):
        try:
            mycursor.execute(
                f'INSERT INTO Clients (Name, Phone, email) VALUES ("{client_name}", "{client_number}", "{client_email}")'
            )
            mydb.commit()
            st.success("New Client Created Successfully")
        except mysql.connector.Error as err:
            st.error(f"Error creating client: {err}")

# Streamlit app
if __name__ == "__main__":
    st.title("Event Management System")
    createClient()

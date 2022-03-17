import qrcode
import streamlit as st
st.title("QR Generator")
st.subheader("Create a QR Code")
url = st.text_input("Enter the url to be converted to QR code")
qr = qrcode.make(url)
qr.save("some_file.png")
if(url==""):
    st.write("Please enter the url")
else:
    st.image("some_file.png")
    with open("some_file.png", "rb") as file:
     btn = st.download_button(
             label="Download image",
             data=file,
             file_name="QR.png",
             mime="image/png"
           )
    st.write("QR Code generated successfully")
st.header("By Deepank Pushpad")
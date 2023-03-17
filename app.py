import streamlit as st
import qrcode

# Set page title
st.set_page_config(page_title='QR Code Generator')

# Define a function to generate QR codes
def generate_qr_code(data, image_size):
    qr = qrcode.QRCode(version=None, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").resize((image_size, image_size))
    return img

# Define Streamlit app
def main():
    # Set app title
    st.title('QR Code Generator')
    
    # Get input from user
    data = st.text_input('Enter the data to encode:')
    image_size = st.slider('Select image size (pixels):', 100, 1000, 400)
    
    # Generate QR code
    if data:
        img = generate_qr_code(data, image_size)
        st.image(img)

if __name__ == '__main__':
    main()

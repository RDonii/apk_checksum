import streamlit as st
import hashlib

st.title('Ayubxon uchun maxsus')
st.subheader("Test qibko'ring")
uploaded_file = st.file_uploader('Flutter mahsulotizi yuklenchi qani:', type=['apk'])
if uploaded_file is not None:
    sha256_hash = hashlib.sha256()
    for byte_block in iter(lambda: uploaded_file.read(4096),b""):
        sha256_hash.update(byte_block)
    st.success(sha256_hash.hexdigest())
import streamlit as st
import string
import random

st.title("Password Checker")
password = st.text_input("Enter your password", type = "password")

count = 0
password_strength = []


def suggested_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
if count < 4:
     suggested = suggested_password()
     st.warning("❌ Your password is weak. Here’s a strong password suggestion:")
     st.text_input("Suggested Strong Password", value=suggested, disabled=True)

     

if st.button("Check"):
    if len(password) >=8:
       count +=1
       st.success("✔️ Password has 8 characters.")
    else:
        st.error("❌ Password must contain 8 characters")   
    if any(char.isupper() for char in password):
        count +=1 
        st.success("✔️ Password contains an uppercase letter.")   
    else:
       st.error("❌ Password must contain an uppercase")    
    if any(char.islower() for char in password):
        count +=1
        st.success("✔️ Password contains a lowercase letter.")
    else:
        st.error("❌ Password must contain a lowercase")    
    if any(char.isdigit() for char in  password):
        count+=1
        st.success("✔️ Password contains a one number.")
    else:
        st.error("❌ Password must contain a digit (0-9)")  
    if any(char in string.punctuation  for char in password):
        count +=1
        st.success("✔️ Password contains a one special character.")
    else:
        st.error("❌ Password must contain atleast one special character!")  
st.header(" Password Strength Meter:")

progress_bar = st.progress(count / 5)

if count == 5:
        st.success("Strong password 💪")
elif count == 4:
        st.warning("Good password, but can be stronger 🤔")
else:
        st.error("Weak password 🐢")

        
st.write(f"Check count: {count}")
   
st.markdown("""
### Tips for creating a strong password:
- Use **at least 12 characters** (the longer, the better).
- Avoid using **common words, names**, or sequences like `1234` or `password`.
- Use a **mixture of uppercase, lowercase, numbers**, and **special characters**.
- Consider using a **password manager** to generate and store secure passwords.
""")


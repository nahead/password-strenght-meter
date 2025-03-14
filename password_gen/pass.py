import streamlit as st
import re
st.set_page_config("password generator", "🔐")
st.title("Password Generator")
st.markdown("""
## wellcome to password generator
use this simple tool to check the strength of your password and get suggestions on how to improve it.
we will give you helpful tips on how to create a strong password that you can remember.

""")
password = st.text_input("Enter your password", type="password")
feedback = []
score= 0
if password :

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Your password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Your password should contain at least one uppercase letter.")
     
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Your password should contain at least one lowercase letter.")
  
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Your password should contain at least one digit.")

    if re.search(r"\W", password):
        score += 1
    else:
        feedback.append("Your password should contain at least one special character.")
    if score == 5:
        st.success("✔ Your password is strong.")
    elif score >= 3:
        st.warning("⚠ Your password is medium.")
    else:
        st.error("❌ Your password is weak.")
    if feedback :
        st.markdown("### improve suggestions")
        for suggestion in feedback:
            st.write(suggestion)
else:
    st.info("Please enter a password.")


    

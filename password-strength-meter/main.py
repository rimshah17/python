import re
import streamlit as st

st.set_page_config(page_title="Password Strength", page_icon="")

def calculate_strength(password):
    score = 0
    details = {}
   
    details['length'] = len(password) >= 12
    if details['length']:
        score += 1
    details['special'] = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    if details['special']:
        score += 1
    details['uppercase'] = bool(re.search(r"[A-Z]", password))
    if details['uppercase']:
        score += 1
    details['lowercase'] = bool(re.search(r"[a-z]", password))
    if details['lowercase']:
        score += 1
    details['number'] = bool(re.search(r"\d", password))
    if details['number']:
        score += 1
    return score, details

def strength_label(score):
    if score <= 2:
        return "Weak 😞"
    elif score <= 4:
        return "Moderate 😐"
    else:
        return "Strong 😃"

st.title("Password Strength Meter") 
password = st.text_input("Enter your password", type="password")
if password:
    score, details = calculate_strength(password)
    label = strength_label(score)
    
    percentage = (score / 5) * 100
    st.write("Password Strength:", label, f"({percentage:.0f}%)")
    st.progress(score / 5)
    st.write("Criteria:")  
    criteria = {
        "Minimum 12 characters": details['length'],
        "At least one special character": details['special'],
        "At least one uppercase letter": details['uppercase'],
        "At least one lowercase letter": details['lowercase'],
        "At least one number": details['number']
    }
    for crit, passed in criteria.items():
        st.write(f"{crit}: {'✔' if passed else '✖'}")

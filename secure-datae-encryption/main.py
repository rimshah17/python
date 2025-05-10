import streamlit as st
from pathlib import Path
from encryption import encrypt_data, decrypt_data, hash_passkey, load_data, save_data, verify_passkey, EncryptionError
from auth import auth_manager
from config import config

# Configure the Streamlit page
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "username" not in st.session_state:
    st.session_state.username = None
if "stored_data" not in st.session_state:
    st.session_state.stored_data = load_data()

def logout():
    st.session_state.username = None
    st.rerun()

# Custom CSS
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
    }
    div.stAlert {
        padding: 1rem;
        border-radius: 0.5rem;
    }
    div[data-baseweb="input"] {
        border-radius: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Navigation")
    if st.session_state.username:
        st.write(f"👤 Logged in as: {st.session_state.username}")
        if st.button("Logout"):
            logout()
    
    # Navigation menu
    menu_options = ["Home"]
    if not st.session_state.username:
        menu_options.extend(["Login", "Sign Up"])
    else:
        menu_options.extend(["Store Data", "Retrieve Data"])
    
    choice = st.selectbox("Menu", menu_options)

# Main content
if choice == "Home":
    st.title("🔒 Secure Data Encryption System")
    st.markdown("""
    ### Welcome to the Secure Data System
    This application provides a secure way to store and retrieve encrypted data.
    
    #### Features:
    - 🔐 Strong encryption using Fernet
    - 👥 User authentication
    - ⏱️ Time-based lockouts for security
    - 💾 Secure data storage
    """)

elif choice == "Login":
    st.title("🔑 Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        
        if submitted:
            if username and password:
                if auth_manager.is_locked(username):
                    lockout_time = auth_manager.get_lockout_remaining(username)
                    st.error(f"Account locked. Try again in {lockout_time} seconds.")
                elif username in st.session_state.stored_data and verify_passkey(
                    st.session_state.stored_data[username]["passkey"], password
                ):
                    st.session_state.username = username
                    auth_manager.reset_attempts(username)
                    st.success("Login successful!")
                    st.rerun()
                else:
                    auth_manager.increment_attempts(username)
                    attempts_left = config.MAX_ATTEMPTS - auth_manager.get_attempts(username)
                    st.error(f"Invalid credentials! Attempts remaining: {attempts_left}")
            else:
                st.warning("Please fill in all fields.")

elif choice == "Sign Up":
    st.title("✍️ Sign Up")
    with st.form("signup_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        password_confirm = st.text_input("Confirm Password", type="password")
        submitted = st.form_submit_button("Sign Up")
        
        if submitted:
            if username and password and password_confirm:
                if password != password_confirm:
                    st.error("Passwords do not match!")
                elif username in st.session_state.stored_data:
                    st.error("Username already exists!")
                else:
                    hashed_passkey = hash_passkey(password)
                    st.session_state.stored_data[username] = {
                        "passkey": hashed_passkey,
                        "data_entries": []
                    }
                    save_data(st.session_state.stored_data)
                    st.success("Account created successfully! Please log in.")
            else:
                st.warning("Please fill in all fields.")

elif choice == "Store Data":
    if not st.session_state.username:
        st.warning("Please log in first.")
    else:
        st.title("📂 Store Data Securely")
        with st.form("store_data_form"):
            data_title = st.text_input("Enter a title for your data")
            user_data = st.text_area("Enter your data")
            passkey = st.text_input("Enter encryption passkey", type="password")
            submitted = st.form_submit_button("Encrypt & Save")
            
            if submitted:
                if user_data and passkey and data_title:
                    try:
                        encrypted_text = encrypt_data(user_data, passkey)
                        if "data_entries" not in st.session_state.stored_data[st.session_state.username]:
                            st.session_state.stored_data[st.session_state.username]["data_entries"] = []
                        
                        st.session_state.stored_data[st.session_state.username]["data_entries"].append({
                            "title": data_title,
                            "encrypted_text": encrypted_text,
                            "timestamp": st.session_state.get("current_time", "")
                        })
                        save_data(st.session_state.stored_data)
                        st.success("Data encrypted and stored successfully!")
                        st.code(encrypted_text, language=None)
                    except EncryptionError as e:
                        st.error(f"Encryption failed: {str(e)}")
                else:
                    st.warning("Please fill in all fields.")

elif choice == "Retrieve Data":
    if not st.session_state.username:
        st.warning("Please log in first.")
    else:
        st.title("🔍 Retrieve Data")
        user_data = st.session_state.stored_data[st.session_state.username]
        
        if not user_data.get("data_entries"):
            st.info("No encrypted data found. Store some data first!")
        else:
            # Create a list of data titles for the dropdown
            data_entries = user_data["data_entries"]
            titles = [entry["title"] for entry in data_entries]
            
            col1, col2 = st.columns([3, 1])
            with col1:
                selected_title = st.selectbox("Select data to decrypt", titles)
            
            # Find the selected entry
            selected_entry = next(entry for entry in data_entries if entry["title"] == selected_title)
            
            with col2:
                if st.button("🗑️ Delete Entry"):
                    # Remove the selected entry
                    data_entries.remove(selected_entry)
                    save_data(st.session_state.stored_data)
                    st.success("Entry deleted successfully!")
                    st.rerun()
            
            with st.form("retrieve_data_form"):
                st.code(selected_entry["encrypted_text"], language=None)
                passkey = st.text_input("Enter decryption passkey", type="password")
                submitted = st.form_submit_button("Decrypt")
                
                if submitted:
                    if passkey:
                        try:
                            decrypted_text = decrypt_data(
                                selected_entry["encrypted_text"],
                                st.session_state.stored_data[st.session_state.username]["passkey"],
                                passkey
                            )
                            if decrypted_text:
                                st.success("Data decrypted successfully!")
                                st.text_area("Decrypted Data", value=decrypted_text, height=200)
                            else:
                                auth_manager.increment_attempts(st.session_state.username)
                                attempts_left = config.MAX_ATTEMPTS - auth_manager.get_attempts(st.session_state.username)
                                st.error(f"Incorrect passkey! Attempts remaining: {attempts_left}")
                                
                                if auth_manager.is_locked(st.session_state.username):
                                    st.warning("Too many failed attempts! Please try again later.")
                                    st.session_state.username = None
                                    st.rerun()
                        except EncryptionError as e:
                            st.error(f"Decryption failed: {str(e)}")
                    else:
                        st.warning("Please enter a passkey.")

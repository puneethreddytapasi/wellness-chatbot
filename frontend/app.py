import streamlit as st
import sys, os

# Import backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))
import auth

st.set_page_config(page_title="Wellness Chatbot", page_icon="💡", layout="centered")

# --- Session State ---
if "page" not in st.session_state:
    st.session_state.page = "login"
if "user_id" not in st.session_state:
    st.session_state.user_id = None

# --- Language Strings ---
LANG = {
    "English": {
        "login": "Login",
        "register": "Register",
        "profile": "Profile Management",
        "name": "Full Name",
        "age": "Age",
        "gender": "Gender",
        "email": "Email",
        "password": "Password",
        "confirm": "Confirm Password",
        "update": "Update Profile",
        "change_pass": "Change Password",
        "logout": "Logout",
        "new_pass": "New Password",
        "confirm_new": "Confirm New Password",
        "success_update": "✅ Profile updated successfully!",
        "success_pass": "🔑 Password updated successfully!",
        "invalid": "❌ Invalid email or password",
        "already_acc": "Already have an account?",
        "no_acc": "Don’t have an account?",
    },
    "Hindi": {
        "login": "लॉगिन करें",
        "register": "रजिस्टर करें",
        "profile": "प्रोफ़ाइल प्रबंधन",
        "name": "पूरा नाम",
        "age": "उम्र",
        "gender": "लिंग",
        "email": "ईमेल",
        "password": "पासवर्ड",
        "confirm": "पासवर्ड की पुष्टि करें",
        "update": "प्रोफ़ाइल अपडेट करें",
        "change_pass": "पासवर्ड बदलें",
        "logout": "लॉगआउट",
        "new_pass": "नया पासवर्ड",
        "confirm_new": "नए पासवर्ड की पुष्टि करें",
        "success_update": "✅ प्रोफ़ाइल सफलतापूर्वक अपडेट हुई!",
        "success_pass": "🔑 पासवर्ड सफलतापूर्वक बदला गया!",
        "invalid": "❌ अमान्य ईमेल या पासवर्ड",
        "already_acc": "पहले से अकाउंट है?",
        "no_acc": "अकाउंट नहीं है?",
    }
}


# --- Styling ---
def card_container():
    st.markdown(
        """
        <style>
        .main {
            background: linear-gradient(135deg, #dbeafe, #e0f2fe);
        }
        .stButton>button {
            background-color: #2563eb;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #1e40af;
        }
        .card {
            background-color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
            max-width: 500px;
            margin: auto;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    return st.container()


# --- Pages ---
def register_page():
    with card_container():
        st.header("📝 Register")
        full_name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm = st.text_input("Confirm Password", type="password")

        if st.button("Register"):
            if password != confirm:
                st.error("Passwords do not match")
            elif not email or not password or not full_name:
                st.error("Please fill all required fields")
            else:
                success = auth.register_user(email, password, full_name, age, gender, "English")
                if success:
                    st.success("✅ Registration successful! Please log in.")
                    st.session_state.page = "login"
                    st.rerun()
                else:
                    st.error("⚠️ Email already registered")

        st.markdown("Already have an account?")
        if st.button("Go to Login"):
            st.session_state.page = "login"
            st.rerun()


def login_page():
    with card_container():
        st.header("🔐 Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user_id = auth.login_user(email, password)
            if user_id:
                st.session_state.user_id = user_id
                st.session_state.page = "profile"
                st.rerun()
            else:
                st.error("❌ Invalid email or password")

        st.markdown("Don’t have an account?")
        if st.button("Go to Register"):
            st.session_state.page = "register"
            st.rerun()


def profile_page():
    user = auth.get_user(st.session_state.user_id)
    if not user:
        st.error("User not found")
        return

    user_id, email, full_name, age, gender, language = user
    text = LANG[language if language else "English"]

    with card_container():
        st.header(f"👤 {text['profile']}")

        st.write(f"**{text['email']}:** {email}")

        new_name = st.text_input(text["name"], full_name)
        new_age = st.number_input(text["age"], min_value=1, max_value=120, value=age)
        new_gender = st.selectbox(text["gender"], ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(gender) if gender else 0)
        new_lang = st.selectbox("Preferred Language", ["English", "Hindi"], index=["English", "Hindi"].index(language) if language else 0)

        if st.button(text["update"]):
            auth.update_user(user_id, new_name, new_age, new_gender, new_lang)
            st.success(text["success_update"])
            st.rerun()

        st.markdown("---")
        st.subheader(text["change_pass"])
        new_pass = st.text_input(text["new_pass"], type="password")
        confirm_pass = st.text_input(text["confirm_new"], type="password")
        if st.button("Change Password"):
            if new_pass != confirm_pass:
                st.error("Passwords do not match")
            elif not new_pass:
                st.error("Password cannot be empty")
            else:
                auth.change_password(user_id, new_pass)
                st.success(text["success_pass"])

        if st.button(text["logout"]):
            st.session_state.user_id = None
            st.session_state.page = "login"
            st.rerun()


# --- Router ---
if st.session_state.page == "register":
    register_page()
elif st.session_state.page == "login":
    login_page()
elif st.session_state.page == "profile":
    profile_page()

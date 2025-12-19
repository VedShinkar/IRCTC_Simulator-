import streamlit as st
import pandas as pd

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Smart IRCTC Simulator",
    page_icon="🚆",
    layout="wide"
)

# ======================================================
# GLOBAL CSS (IRCTC STYLE + FIX SPACING)
# ======================================================
st.markdown("""
<style>

/* Remove Streamlit default top spacing */
.block-container {
    padding-top: 0rem;
    padding-bottom: 2rem;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #0D47A1;
}

[data-testid="stSidebar"] * {
    color: white;
}

/* Hero container */
.hero-container {
    position: relative;
    width: 100%;
}

/* Hero title overlay */
.hero-text {
    position: absolute;
    bottom: 15%;
    left: 6%;
    color: white;
    text-shadow: 0px 4px 10px rgba(0,0,0,0.8);
}

.hero-text h1 {
    font-size: 3rem;
    margin-bottom: 0.2rem;
}

.hero-text h3 {
    font-weight: 400;
    margin-top: 0;
}

/* Buttons */
.stButton > button {
    background-color: #C62828;
    color: white;
    border-radius: 8px;
    font-weight: bold;
    border: none;
}

/* Metric cards */
[data-testid="metric-container"] {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 15px;
    border-left: 6px solid #C62828;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 10px;
}

/* Force images to behave like banners */
img {
    object-fit: cover;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# HERO BANNER (FULL BLEED)
# ======================================================
st.markdown("<div class='hero-container'>", unsafe_allow_html=True)

st.image(
    "irctc_banner.png",
    use_container_width=True
)

st.markdown("""
<div class="hero-text">
    <h1>🚆 Smart IRCTC Simulator</h1>
    <h3>Indian Railways • Fare & Seat Prediction System 🇮🇳</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# DATA
# ======================================================
stations = ["Mumbai", "Delhi", "Chennai", "Kolkata"]

distance_matrix = [
    [0, 1447, 1384, 1690],
    [1447, 0, 1412, 2180],
    [1384, 1412, 0, 2000],
    [1690, 2180, 2000, 0]
]

seats = {"SL": 5, "3A": 3}
waitlist = {"SL": 0, "3A": 0}

# ======================================================
# CORE LOGIC (FROM C PROJECT)
# ======================================================
def calculate_fare(distance, class_type, age):
    rate = 0.5
    fare = distance * rate
    if class_type == "3A":
        fare *= 2
    if age >= 60:
        fare *= 0.7
    return fare

def predict_confirmation(available, waiting):
    if waiting == 0:
        return 100
    return (available / waiting) * 100

# ======================================================
# SIDEBAR MENU
# ======================================================
st.sidebar.markdown("## 🚆 IRCTC MENU")

menu = st.sidebar.radio(
    "",
    [
        "📍 Display Train Routes",
        "🎟️ Book Ticket",
        "📊 Seat Availability & Prediction",
        "⚡ Tatkal Booking Simulation",
        "🚪 Exit"
    ]
)

# ======================================================
# MAIN CONTENT
# ======================================================

# ---- ROUTES ----
if menu == "📍 Display Train Routes":
    st.subheader("📍 Train Route Distance Matrix (km)")
    df = pd.DataFrame(distance_matrix, columns=stations, index=stations)
    st.dataframe(df, use_container_width=True)

# ---- BOOK TICKET ----
elif menu == "🎟️ Book Ticket":
    st.subheader("🎟️ Ticket Booking Portal")

    with st.form("booking_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Passenger Name")
            age = st.number_input("Age", min_value=1, max_value=100)

        with col2:
            src = st.selectbox("Source Station", stations)
            dest = st.selectbox("Destination Station", stations)

        class_type = st.selectbox("Class", ["SL", "3A"])
        submit = st.form_submit_button("Book Ticket")

    if submit:
        if src == dest:
            st.error("❌ Source and destination cannot be the same.")
        else:
            i, j = stations.index(src), stations.index(dest)
            dist = distance_matrix[i][j]
            fare = calculate_fare(dist, class_type, age)

            if seats[class_type] > 0:
                seats[class_type] -= 1
                st.success("✅ Seat Confirmed!")
            else:
                waitlist[class_type] += 1
                st.warning(f"⏳ Waitlisted: WL{waitlist[class_type]}")

            st.markdown("### 🧾 Ticket Details")
            st.write(f"**Passenger:** {name}")
            st.write(f"**Route:** {src} ➜ {dest}")
            st.write(f"**Distance:** {dist} km")
            st.write(f"**Fare:** ₹ {fare:.2f}")

# ---- SEAT STATUS ----
elif menu == "📊 Seat Availability & Prediction":
    st.subheader("📊 Seat Availability & Confirmation Probability")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Sleeper (SL) Seats", seats["SL"])
        st.metric("Confirmation %", f"{predict_confirmation(seats['SL'], waitlist['SL']):.2f}%")

    with col2:
        st.metric("AC 3 Tier (3A) Seats", seats["3A"])
        st.metric("Confirmation %", f"{predict_confirmation(seats['3A'], waitlist['3A']):.2f}%")

# ---- TATKAL ----
elif menu == "⚡ Tatkal Booking Simulation":
    st.subheader("⚡ Tatkal Booking Rush Simulation")

    tatkal_seats = st.slider("Tatkal Seats Available", 0, 5, 2)
    if st.button("Start Tatkal Booking"):
        if tatkal_seats > 0:
            st.success("🎉 Tatkal Seat Booked Successfully!")
        else:
            st.error("❌ Tatkal Booking Failed – No Seats Available")

# ---- EXIT ----
elif menu == "🚪 Exit":
    st.info("Thank you for using Smart IRCTC Simulator 🇮🇳")
    st.markdown("### 🚆 Indian Railways – Lifeline of the Nation")
    st.stop()

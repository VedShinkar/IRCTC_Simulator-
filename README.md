# 🚆 Smart IRCTC Streamlit Simulator

The **Smart IRCTC Streamlit Simulator** is an interactive, menu-driven reservation system inspired by **Indian Railways**.  
It simulates core railway booking operations such as route display, ticket booking, seat availability, waitlist prediction, and Tatkal booking through a modern Streamlit dashboard.

The project is based on a **C-language Programming for Problem Solving (PPS)** mini-project, where the core logic is first implemented using fundamental C concepts and then visualized using a Python Streamlit UI.

---

## 🎯 Project Objective

- To demonstrate how **real-world systems** like railway reservations can be modeled using **basic C programming concepts**
- To integrate multiple PPS topics into a **single meaningful application**
- To visualize the outputs of a C-based simulator using a clean, IRCTC-style web dashboard

---

## 🧠 Core Features

- 📍 Display train route distance matrix  
- 🎟️ Ticket booking simulation  
- 📊 Seat availability & waitlist confirmation prediction  
- ⚡ Tatkal booking rush simulation  
- 🚪 Menu-driven exit and reset flow  
- 🇮🇳 Indian Railways–inspired UI/UX  

---

## 🛠️ Technologies Used

### Programming Languages
- **C** – Core problem-solving and simulation logic  
- **Python** – Streamlit dashboard visualization  

### Libraries & Tools
- **Streamlit** – Interactive web UI  
- **Pandas** – Tabular data display  
- **GitHub** – Version control  
- **Streamlit Community Cloud** – Online deployment  

---

## 🧩 C Language Concepts Used (PPS Mapping)

This project integrates **all major PPS concepts** in a structured manner:

### 1️⃣ Arithmetic Expressions
- Fare calculation based on distance and class
- Percentage-based waitlist confirmation prediction

### 2️⃣ Conditional Statements
- Class-based fare logic (SL / 3A)
- Senior citizen discount
- Seat available vs waitlist decision

### 3️⃣ Iterative Constructs (Loops)
- Menu-driven program flow
- Matrix traversal for route display

### 4️⃣ 2D Arrays
- Route distance matrix between stations

### 5️⃣ String Operations
- Station names
- Passenger names
- Class type comparison

### 6️⃣ Numerical Methods
- Approximation of waitlist confirmation probability

### 7️⃣ Recursion
- Tatkal booking retry / simulation logic

### 8️⃣ Structures
- `Passenger` structure (ID, name, age)
- `Ticket` structure (route, fare, seat, waitlist)

### 9️⃣ Pointers
- Seat allocation using call-by-reference
- Dynamic update of seat and waitlist counters

### 🔟 Call by Value
- Fare calculation function

### 1️⃣1️⃣ Call by Reference
- Seat and Tatkal booking functions

---

## 🧩 Important Functions (C Logic)

| Function Name | Description |
|--------------|-------------|
| `calculateFare()` | Computes fare using distance, class, and age |
| `allocateSeat()` | Allocates seat or assigns waitlist using pointers |
| `predictConfirmation()` | Estimates confirmation probability |
| `tatkalBooking()` | Simulates Tatkal booking using recursion |
| `displayRoutes()` | Displays route distance matrix |

---

## 🎨 Streamlit Dashboard Role

The Streamlit dashboard **does not replace the C program**.  
Instead, it:

- Visually simulates the same menu-driven logic
- Displays outputs in tables, cards, and forms
- Improves user experience with an IRCTC-style interface

This separation ensures **academic correctness** while showcasing **modern visualization skills**.

---

## ▶️ How to Run Locally

```bash
pip install streamlit pandas
streamlit run irctc_streamlit.py

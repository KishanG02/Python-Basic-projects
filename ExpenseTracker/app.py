import streamlit as st
from tracker import ExpenseTracker

# -----------------------------
# Initialize Tracker
# -----------------------------
if "tracker" not in st.session_state:
    tracker = ExpenseTracker()
    tracker.load_transactions()
    st.session_state.tracker = tracker

tracker = st.session_state.tracker

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("💰 Expense Tracker")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Income",
        "Add Expense",
        "Transactions",
        "Reports"
    ]
)

# -----------------------------
# Dashboard
# -----------------------------
if page == "Dashboard":

    st.title("📊 Dashboard")

    success, summary = tracker.overall_summary()

    if success:
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Income",
            f"₹{summary['income']:,.2f}"
        )

        col2.metric(
            "Expense",
            f"₹{summary['expense']:,.2f}"
        )

        col3.metric(
            "Balance",
            f"₹{summary['balance']:,.2f}"
        )

    st.divider()

    success, transactions = tracker.recent_transactions()

    if success:

        st.subheader("Recent Transactions")

        for transaction in transactions:
            st.text(transaction)

# -----------------------------
# Add Income
# -----------------------------
elif page == "Add Income":

    st.title("➕ Add Income")

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    category = st.selectbox(
        "Category",
        [
            "Salary",
            "Investment",
            "Other"
        ]
    )

    description = st.text_input("Description")

    if st.button("Add Income"):

        success, message = tracker.add_transaction(
            "income",
            amount,
            category,
            description
        )

        if success:
            tracker.save_transactions()
            st.success("Income added successfully.")
        else:
            st.error(message)

# -----------------------------
# Add Expense
# -----------------------------
elif page == "Add Expense":

    st.title("➖ Add Expense")

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Entertainment",
            "Healthcare",
            "Education",
            "Other"
        ]
    )

    description = st.text_input("Description")

    if st.button("Add Expense"):

        success, message = tracker.add_transaction(
            "expense",
            amount,
            category,
            description
        )

        if success:
            tracker.save_transactions()
            st.success("Expense added successfully.")
        else:
            st.error(message)

# -----------------------------
# Transactions
# -----------------------------
elif page == "Transactions":

    st.title("📋 Transactions")

    success, transactions = tracker.view_transactions()

    if success:

        for transaction in transactions:

            with st.expander(
                f"Transaction #{transaction.transaction_id}"
            ):
                st.text(transaction)

    else:
        st.info("No transactions found.")

# -----------------------------
# Reports
# -----------------------------
elif page == "Reports":

    st.title("📈 Reports")

    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=1
    )

    year = st.number_input(
        "Year",
        min_value=2000,
        value=2026
    )

    if st.button("Generate Monthly Report"):

        success, summary = tracker.monthly_summary(
            month,
            year
        )

        if success:

            st.metric(
                "Income",
                f"₹{summary['income']:,.2f}"
            )

            st.metric(
                "Expense",
                f"₹{summary['expense']:,.2f}"
            )

            st.metric(
                "Balance",
                f"₹{summary['balance']:,.2f}"
            )

    st.divider()

    success, categories = tracker.category_summary()

    if success:

        st.subheader("Category Summary")

        st.bar_chart(categories)
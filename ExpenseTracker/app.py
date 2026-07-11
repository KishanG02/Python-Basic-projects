import streamlit as st
from tracker import ExpenseTracker

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# --------------------------------------------------
# Initialize Tracker
# --------------------------------------------------

if "tracker" not in st.session_state:
    st.session_state.tracker = ExpenseTracker()

tracker = st.session_state.tracker

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("💰 Expense Tracker")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Income",
        "Add Expense",
        "Transactions",
        "Reports",
        "Delete Transaction",
        "Find Transaction"
    ]
)

# ==================================================
# Dashboard
# ==================================================

if page == "Dashboard":

    st.title("📊 Dashboard")

    success, summary = tracker.overall_summary()

    if success:

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Income",
            f"₹{summary['income']:,.2f}"
        )

        c2.metric(
            "Expense",
            f"₹{summary['expense']:,.2f}"
        )

        c3.metric(
            "Balance",
            f"₹{summary['balance']:,.2f}"
        )

        c4.metric(
            "Transactions",
            summary["transactions"]
        )

    else:
        st.info(summary)

    st.divider()

    st.subheader("Recent Transactions")

    success, transactions = tracker.recent_transactions()

    if success:

        for transaction in transactions:
            st.text(transaction)

    else:
        st.info(transactions)

# ==================================================
# Add Income
# ==================================================

elif page == "Add Income":

    st.title("➕ Add Income")

    with st.form("income_form"):

        amount = st.number_input(
            "Amount",
            min_value=0.01,
            format="%.2f"
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

        submitted = st.form_submit_button("Add Income")

        if submitted:

            success, message = tracker.add_transaction(
                "income",
                amount,
                category,
                description
            )

            if success:
                st.success("Income added successfully.")
            else:
                st.error(message)

# ==================================================
# Add Expense
# ==================================================

elif page == "Add Expense":

    st.title("➖ Add Expense")

    with st.form("expense_form"):

        amount = st.number_input(
            "Amount",
            min_value=0.01,
            format="%.2f"
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

        submitted = st.form_submit_button("Add Expense")

        if submitted:

            success, message = tracker.add_transaction(
                "expense",
                amount,
                category,
                description
            )

            if success:
                st.success("Expense added successfully.")
            else:
                st.error(message)

# ==================================================
# Transactions
# ==================================================

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
        st.info(transactions)

# ==================================================
# Reports
# ==================================================

elif page == "Reports":

    st.title("📈 Reports")

    col1, col2 = st.columns(2)

    month = col1.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=1
    )

    year = col2.number_input(
        "Year",
        min_value=2024,
        max_value=2100,
        value=2026
    )

    if st.button("Generate Report"):

        success, summary = tracker.monthly_summary(month, year)

        if success:

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Income",
                f"₹{summary['income']:,.2f}"
            )

            c2.metric(
                "Expense",
                f"₹{summary['expense']:,.2f}"
            )

            c3.metric(
                "Balance",
                f"₹{summary['balance']:,.2f}"
            )

        else:
            st.error(summary)

    st.divider()

    st.subheader("Category Summary")

    success, categories = tracker.category_summary()

    if success:

        st.bar_chart(categories)

    else:
        st.info(categories)

# ==================================================
# Delete Transaction
# ==================================================

elif page == "Delete Transaction":

    st.title("🗑 Delete Transaction")

    transaction_id = st.number_input(
        "Transaction ID",
        min_value=1,
        step=1
    )

    if st.button("Delete"):

        success, message = tracker.delete_transaction(transaction_id)

        if success:
            st.success(message)
        else:
            st.error(message)

# ==================================================
# Find Transaction
# ==================================================

elif page == "Find Transaction":

    st.title("🔍 Find Transaction")

    transaction_id = st.number_input(
        "Transaction ID",
        min_value=1,
        step=1
    )

    if st.button("Search"):

        success, transaction = tracker.find_transaction(transaction_id)

        if success:
            st.text(transaction)
        else:
            st.error(transaction)
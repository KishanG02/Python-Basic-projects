import streamlit as st
import pandas as pd
import plotly.express as px

from tracker import ExpenseTracker

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Expense Tracker Pro",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main{
    background:#F8F9FA;
}

.block-container{
    padding-top:2rem;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0 2px 10px rgba(0,0,0,0.08);
}

div[data-testid="metric-container"]{
    background:#ffffff;
    border-radius:12px;
    padding:20px;
    border:1px solid #EAEAEA;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SESSION STATE
# ==========================================================

if "tracker" not in st.session_state:
    st.session_state.tracker = ExpenseTracker()

tracker = st.session_state.tracker

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("💰 Expense Tracker Pro")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "➕ Add Transaction",
        "📋 Transactions",
        "📈 Analytics",
        "⚙️ Settings"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "SQLite Database\n\n"
    "Version 2.0"
)

# ==========================================================
# DASHBOARD
# ==========================================================

if page == "🏠 Dashboard":

    st.title("💰 Expense Tracker Dashboard")

    success, summary = tracker.overall_summary()

    if success:

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "💵 Income",
                f"₹ {summary['income']:,.2f}"
            )

        with col2:
            st.metric(
                "💸 Expense",
                f"₹ {summary['expense']:,.2f}"
            )

        with col3:
            st.metric(
                "💰 Balance",
                f"₹ {summary['balance']:,.2f}"
            )

        with col4:
            st.metric(
                "📋 Transactions",
                summary["transactions"]
            )

    else:
        st.info("No transactions available.")

    st.divider()

    st.subheader("🕒 Recent Transactions")

    success, transactions = tracker.recent_transactions()

    if success:

        data = []

        for transaction in transactions:

            data.append(
                {
                    "ID": transaction.transaction_id,
                    "Date": transaction.date.strftime("%d-%m-%Y"),
                    "Type": transaction.transaction_type.title(),
                    "Category": transaction.category,
                    "Amount": transaction.amount,
                    "Description": transaction.description
                }
            )

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No recent transactions.")

# ==========================================================
# ADD TRANSACTION
# ==========================================================

elif page == "➕ Add Transaction":

    st.title("➕ Add Transaction")

    transaction_type = st.radio(
        "Transaction Type",
        ["Income", "Expense"],
        horizontal=True
    )

    if transaction_type == "Income":

        categories = [
            "Salary",
            "Investment",
            "Other"
        ]

    else:

        categories = [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Entertainment",
            "Healthcare",
            "Education",
            "Other"
        ]

    with st.form("transaction_form", clear_on_submit=True):

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            step=1.0,
            format="%.2f"
        )

        category = st.selectbox(
            "Category",
            categories
        )

        description = st.text_area(
            "Description",
            placeholder="Enter transaction description..."
        )

        submitted = st.form_submit_button(
            "💾 Save Transaction",
            use_container_width=True
        )

    if submitted:

        success, result = tracker.add_transaction(
            transaction_type.lower(),
            amount,
            category,
            description
        )

        if success:

            st.success("✅ Transaction added successfully!")

            st.balloons()

            st.info(result)

        else:

            st.error(result)

# ==========================================================
# TRANSACTIONS
# ==========================================================

elif page == "📋 Transactions":

    st.title("📋 Transactions")

    filter_type = st.selectbox(
        "Filter by Type",
        [
            "All",
            "Income",
            "Expense"
        ]
    )

    filter_category = st.text_input(
        "Filter by Category (optional)"
    )

    if filter_type == "All":
        filter_type = None

    if filter_category.strip() == "":
        filter_category = None

    success, transactions = tracker.view_transactions(
        filter_type,
        filter_category
    )

    if success:

        table = []

        for transaction in transactions:

            table.append({

                "ID": transaction.transaction_id,

                "Date": transaction.date.strftime("%d-%m-%Y"),

                "Type": transaction.transaction_type.title(),

                "Category": transaction.category,

                "Amount": f"₹{transaction.amount:,.2f}",

                "Description": transaction.description

            })

        df = pd.DataFrame(table)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning(transactions)

st.divider()

st.subheader("🗑 Delete Transaction")

transaction_id = st.number_input(
    "Transaction ID",
    min_value=1,
    step=1
)

if st.button("Delete Transaction"):

    success, message = tracker.delete_transaction(transaction_id)

    if success:

        st.success(message)

    else:

        st.error(message)

# ==========================================================
# ANALYTICS
# ==========================================================

elif page == "📈 Analytics":

    st.title("📈 Analytics Dashboard")

    # ------------------------------------------------------
    # Overall Summary
    # ------------------------------------------------------

    success, summary = tracker.overall_summary()

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

    st.divider()

    # ------------------------------------------------------
    # Monthly Summary
    # ------------------------------------------------------

    st.subheader("📅 Monthly Summary")

    col1, col2 = st.columns(2)

    with col1:
        month = st.number_input(
            "Month",
            min_value=1,
            max_value=12,
            value=1
        )

    with col2:
        year = st.number_input(
            "Year",
            min_value=2024,
            value=2026
        )

    if st.button("Generate Summary"):

        success, report = tracker.monthly_summary(month, year)

        if success:

            r1, r2, r3 = st.columns(3)

            r1.metric(
                "Income",
                f"₹{report['income']:,.2f}"
            )

            r2.metric(
                "Expense",
                f"₹{report['expense']:,.2f}"
            )

            r3.metric(
                "Balance",
                f"₹{report['balance']:,.2f}"
            )

        else:

            st.error(report)

    st.divider()

    # ------------------------------------------------------
    # Category Summary
    # ------------------------------------------------------

    st.subheader("🥧 Expense Categories")

    success, category_summary = tracker.category_summary()

    if success and category_summary:

        category_df = pd.DataFrame({
            "Category": list(category_summary.keys()),
            "Amount": list(category_summary.values())
        })

        pie_chart = px.pie(
            category_df,
            names="Category",
            values="Amount",
            hole=0.45,
            title="Expense Distribution"
        )

        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

        bar_chart = px.bar(
            category_df,
            x="Category",
            y="Amount",
            title="Category Wise Spending",
            text_auto=True
        )

        st.plotly_chart(
            bar_chart,
            use_container_width=True
        )

    else:

        st.info("No expense data available.")

    st.divider()

    # ------------------------------------------------------
    # Highest Expense
    # ------------------------------------------------------

    st.subheader("💸 Highest Expense")

    success, expense = tracker.highest_expense()

    if success:

        st.success(
            f"""
Category : {expense.category}

Amount : ₹{expense.amount:,.2f}

Description : {expense.description}
"""
        )

    else:

        st.warning(expense)

    st.divider()

    # ------------------------------------------------------
    # Recent Transactions
    # ------------------------------------------------------

    st.subheader("🕒 Last 5 Transactions")

    success, transactions = tracker.recent_transactions()

    if success:

        data = []

        for transaction in transactions:

            data.append({

                "Date": transaction.date.strftime("%d-%m-%Y"),

                "Type": transaction.transaction_type.title(),

                "Category": transaction.category,

                "Amount": transaction.amount

            })

        st.dataframe(
            pd.DataFrame(data),
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(transactions)

    # ==========================================================
# SETTINGS
# ==========================================================

elif page == "⚙️ Settings":

    st.title("⚙️ Settings")

    st.subheader("📤 Export Transactions")

    success, transactions = tracker.view_transactions()

    if success:

        export_data = []

        for transaction in transactions:

            export_data.append({

                "Transaction ID": transaction.transaction_id,
                "Date": transaction.date.strftime("%d-%m-%Y %H:%M"),
                "Type": transaction.transaction_type.title(),
                "Category": transaction.category,
                "Amount": transaction.amount,
                "Description": transaction.description

            })

        export_df = pd.DataFrame(export_data)

        csv = export_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Download CSV",
            csv,
            "transactions.csv",
            "text/csv"
        )

    else:

        st.info("No transactions available.")

    st.divider()

    # ----------------------------------------------------

    st.subheader("🗑 Clear Database")

    warning = st.checkbox(
        "I understand this action cannot be undone."
    )

    if warning:

        if st.button(
            "Delete All Transactions",
            type="primary"
        ):

            tracker.db.cursor.execute(
                "DELETE FROM transactions"
            )

            tracker.db.connection.commit()

            tracker.next_transaction_id = 1

            st.success(
                "All transactions deleted successfully."
            )

            st.rerun()

    st.divider()

    st.subheader("ℹ️ About")

    st.info("""
Expense Tracker Pro

Version : 2.0

Built Using

• Python
• Streamlit
• SQLite
• Plotly

Developer:
Krishna Gupta
""")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    "Expense Tracker Pro • Built with ❤️ using Python, Streamlit and SQLite"
)
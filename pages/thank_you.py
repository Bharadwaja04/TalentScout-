import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    layout="wide",
    page_icon=":sparkles:"
)

# Inject custom CSS with a dynamic gradient background and refined card styling
st.markdown(
    """
    <style>
    /* Apply a dynamic gradient background to the main app container */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #6A5ACD, #8A2BE2, #7B68EE, #9370DB);
        background-size: 400% 400%;
        animation: gradientScroll 10s ease infinite;
    }
    
    @keyframes gradientScroll {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Style the main content area for a card effect */
    .thank-you-container {
        text-align: center;
        padding: 40px;
        margin: 40px auto;
        max-width: 800px;
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    
    /* Style for the success icon */
    .success-icon {
        font-size: 80px;
        color: #4CAF50;
        margin-bottom: 20px;
    }
    
    /* Styling for headings and paragraphs */
    h1 {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        color: #1E1E1E;
        margin: 20px 0;
    }
    p {
        font-size: 20px;
        color: #000000;
        margin: 20px 0;
    }
    
    /* Style the return button */
    .stButton > button {
        background-color: #6A5ACD;
        color: white;
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #8A2BE2;
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
        transform: translateY(-2px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a centered container with custom styling
st.markdown(
    """
    <div class="thank-you-container">
        <div class="success-icon">✅</div>
        <h1>Thank You!</h1>
        <p>
            Your interview has been successfully submitted. We will reach out to you soon.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Add buttons in a centered layout for navigation
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
        
    if st.button("Return to Home", use_container_width=True):
        # Reset session state so that the candidate form is displayed again
        st.session_state["page"] = "form"
        st.session_state["chat_history"] = []
        st.session_state["question_count"] = 0
        st.session_state["candidate_info"] = {}
        st.switch_page("interface.py")  # Adjust the path if your main file is named differently.

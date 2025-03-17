import requests
import streamlit as st
import os

# Set up the page configuration
st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    layout="wide",
    page_icon=":sparkles:"
)

# Inject custom CSS with dark grey/black shades
st.markdown(
    """
    <style>
    /* Set the main background to a dark grey/black shade */
    [data-testid="stAppViewContainer"] {
        background-color: #121212;  /* Dark background */
    }
    
    /* Style the content area (card effect) with dark shades */
    [data-testid="stSidebarContent"], .main {
        background-color: rgba(30, 30, 30, 0.95);  /* Dark card background */
        border-radius: 10px;
        padding: 25px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.5);
        margin: 10px;
    }
    
    /* Headings styled for high contrast on dark backgrounds */
    h1 {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        color: #ffffff;  /* White text */
        margin-top: 20px;
        margin-bottom: 30px;
        letter-spacing: 1px;
    }
    
    /* General text styling for improved readability */
    p, label, span, div {
        color: #e0e0e0;  /* Light grey text */
    }
    
    /* Style buttons with dark tones */
    .stButton > button {
        background-color: #333333;
        color: white;
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.4);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #555555;
        box-shadow: 0 6px 8px rgba(0,0,0,0.5);
        transform: translateY(-2px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
try:
    st.image("C:\\Users\\bhara\\OneDrive\\Desktop\\GPT\\logo.webp", width=150)
except:
    st.write("Logo not found. Please check the path.")
    
st.title("TalentScout Hiring Assistant")

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "form"
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "question_count" not in st.session_state:
    st.session_state["question_count"] = 0

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

# Function to generate questions
def generate_question(tech_stack, prev_responses):
    prompt = f"""
    You are an AI interviewer. Generate a single, theoretical technical question based on this tech stack: {tech_stack}.
    
    **Rules:**
    - Focus on **concepts, principles, and best practices**.
    - Avoid code-heavy or factual recall questions.
    - Ensure uniqueness by avoiding: {prev_responses}.
    
    Provide ONLY the question.
    """
    
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "llama3-8b-8192", "messages": [{"role": "system", "content": prompt}]}
    
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

# **Page 1: Candidate Form**
if st.session_state["page"] == "form":
    st.markdown("""
        <div style="text-align: center; padding: 10px 0 30px 0;">
            <p style="font-size: 18px; color: #e0e0e0; font-weight: 500;">
                Please fill in your details to begin the interview process
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Create columns for a more balanced layout
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        with st.form("candidate_form"):
            # Create two columns for a more compact form
            form_col1, form_col2 = st.columns(2)
            
            with form_col1:
                name = st.text_input("Full Name")
                email = st.text_input("Email Address")
                phone = st.text_input("Phone Number")
                experience = st.number_input("Years of Experience", min_value=0)
            
            with form_col2:
                position = st.text_input("Desired Position")
                location = st.text_input("Current Location")
                tech_stack = st.text_area("Tech Stack (e.g., Python, Django, SQL)")
            
            submit = st.form_submit_button("Start Interview")

    if submit:
        st.session_state["candidate_info"] = {
            "name": name, "email": email, "phone": phone,
            "experience": experience, "position": position,
            "location": location, "tech_stack": tech_stack
        }
        st.session_state["page"] = "ready_page"
        st.rerun()

# **Page 2: Ready Confirmation**
elif st.session_state["page"] == "ready_page":
    # Create a centered card for the ready confirmation
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown(f"""
            <div style="text-align: center; padding: 30px; background-color: rgba(30, 30, 30, 0.95); 
                        border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.5); margin: 30px 0;">
                <h2 style="color: #ffffff; margin-bottom: 20px;">Hello {st.session_state['candidate_info']['name']}!</h2>
                <p style="font-size: 18px; color: #e0e0e0; margin-bottom: 30px;">Are you ready for the interview?</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Yes, Start Interview", use_container_width=True):
            st.session_state["page"] = "interview"
            # Generate the first question immediately
            first_question = generate_question(
                st.session_state["candidate_info"]["tech_stack"], []
            )
            st.session_state["chat_history"].append({"question": first_question})
            st.session_state["question_count"] += 1
            st.rerun()

# **Page 3: Interview Process**
elif st.session_state["page"] == "interview":
    st.subheader("Interview Session")
    
    # Create a chat container
    chat_container = st.container()
    
    with chat_container:
        # Display chat history with improved styling
        for i, entry in enumerate(st.session_state["chat_history"]):
            # Bot question with custom styling
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(f"{entry['question']}")
            
            # User answer if it exists
            if "answer" in entry:
                with st.chat_message("user", avatar="👤"):
                    st.markdown(f"{entry['answer']}")
    
    # Answer input only if the latest question is unanswered
    if st.session_state["chat_history"] and "answer" not in st.session_state["chat_history"][-1]:
        answer = st.chat_input("Your answer...")
        
        if answer:
            # Store the answer
            st.session_state["chat_history"][-1]["answer"] = answer
            
            # Display the answer immediately
            with st.chat_message("user", avatar="👤"):
                st.markdown(answer)
            
            # Generate next question if interview isn't complete
            if st.session_state["question_count"] < 5:
                with st.status("Generating next question...", expanded=True):
                    next_question = generate_question(
                        st.session_state["candidate_info"]["tech_stack"],
                        [q["question"] for q in st.session_state["chat_history"]]
                    )
                
                # Display the new question
                with st.chat_message("assistant", avatar="🤖"):
                    st.markdown(next_question)
                
                # Store the new question
                st.session_state["chat_history"].append({"question": next_question})
                st.session_state["question_count"] += 1
            st.rerun()

# End Interview
if st.session_state["question_count"] == 5 and "answer" in st.session_state["chat_history"][-1]:
    # Create a success message with custom styling
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Finish Interview", use_container_width=True):
            st.switch_page("pages/thank_you.py")

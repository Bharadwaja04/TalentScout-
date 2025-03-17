# TalentScout Hiring Assistant

TalentScout Hiring Assistant is an innovative web application designed to assist in the technical interview process. Built with Streamlit, it provides an interactive, chat-style interface where candidates can submit their details, answer dynamically generated technical questions, and complete an interview session seamlessly.

## Features

- **Interactive Candidate Form:** Collects candidate details such as full name, email, phone, experience, desired position, current location, and tech stack.
- **Dynamic Question Generation:** Uses an external API to generate theoretical technical questions based on the candidate's tech stack. The questions focus on concepts, principles, and best practices.
- **Chat-Style Interview Interface:** Presents questions and candidate answers in a conversational, chat-like interface with custom styling.
- **Themed UI:** Custom CSS provides a polished look with dark mode and gradient backgrounds (configurable via the provided `config.toml` and custom CSS).
- **Navigation & State Management:** Seamlessly navigates between the candidate form, interview session, and a thank-you page. Session state is managed to allow resetting the interview process.
- **Easy Deployment:** Built using Streamlit, making it simple to run locally or deploy on any cloud service supporting Python web apps.

## Prerequisites

- Python 3.7 or later
- [Streamlit](https://streamlit.io/) (install via `pip install streamlit`)
- An API key for the question generation endpoint. Set your API key in your environment variable (`GROQ_API_KEY`).

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/talentscout-hiring-assistant.git
   cd talentscout-hiring-assistant

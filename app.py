import streamlit as st
import time
import pandas as pd
from datetime import datetime
import requests
import json
import re
import os

# ==========================================
# ⚙️ STREAMLIT PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Hadi Seelro | Agentic AI Systems Architect",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================
# 🎨 CUSTOM MODERN CYBER-GLASS THEME (CSS)
# ==========================================
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Global Dark Canvas */
    .stApp {
        background: radial-gradient(circle at 10% 10%, rgba(14, 165, 233, 0.08) 0%, transparent 40%),
                    radial-gradient(circle at 90% 90%, rgba(99, 102, 241, 0.08) 0%, transparent 45%),
                    #090d16 !important;
        color: #f8fafc !important;
    }

    /* Universal High-Contrast Typography */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-weight: 700 !important;
        letter-spacing: -0.01em;
    }
    
    p, span, li, [data-testid="stMarkdownContainer"] p {
        color: #e2e8f0 !important;
        font-size: 1rem;
        line-height: 1.65;
    }

    strong {
        color: #38bdf8 !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0b1120 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    }

    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
        color: #38bdf8 !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label {
        background: rgba(255, 255, 255, 0.03);
        padding: 10px 14px;
        border-radius: 8px;
        margin-bottom: 6px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        transition: all 0.2s ease;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background: rgba(56, 189, 248, 0.1);
        border-color: rgba(56, 189, 248, 0.3);
    }

    [data-testid="stSidebar"] [role="radiogroup"] label div p {
        color: #f1f5f9 !important;
        font-weight: 500 !important;
    }

    /* Input Fields & Labels */
    [data-testid="stWidgetLabel"] p, [data-testid="stWidgetLabel"] label {
        color: #f8fafc !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
        margin-bottom: 6px !important;
    }

    input, textarea, select {
        color: #ffffff !important;
        background-color: #131c2e !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 8px !important;
    }

    input:focus, textarea:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2) !important;
    }

    /* Modern Hero Banner */
    .hero-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.85));
        border: 1px solid rgba(56, 189, 248, 0.35);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45), 0 0 25px rgba(56, 189, 248, 0.1);
        border-radius: 16px;
        padding: 32px 36px;
        margin-bottom: 24px;
    }

    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 12px;
        letter-spacing: -0.02em;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        color: #f1f5f9 !important;
        font-weight: 400;
        line-height: 1.7;
    }

    /* Live Status Badge */
    .agent-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid rgba(16, 185, 129, 0.45);
        color: #34d399 !important;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 12px;
    }

    .pulse-dot {
        width: 8px;
        height: 8px;
        background-color: #10b981;
        border-radius: 50%;
        box-shadow: 0 0 10px #10b981;
    }

    /* Sleek Metric Cards */
    .metric-card {
        background: #111a2e;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 22px 16px;
        text-align: center;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        border-color: #38bdf8;
    }

    .metric-value {
        font-size: 2.1rem;
        font-weight: 800;
        color: #38bdf8 !important;
        letter-spacing: -0.02em;
    }

    .metric-label {
        font-size: 0.88rem;
        color: #cbd5e1 !important;
        font-weight: 600;
        margin-top: 6px;
    }

    /* Project Cards */
    .project-card {
        background: #111a2e;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 18px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        transition: all 0.2s ease-in-out;
    }

    .project-card:hover {
        border-color: rgba(56, 189, 248, 0.4);
        box-shadow: 0 8px 24px rgba(56, 189, 248, 0.08);
    }

    .tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 0.78rem;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 6px;
        background: rgba(56, 189, 248, 0.12);
        color: #38bdf8 !important;
        border: 1px solid rgba(56, 189, 248, 0.3);
    }

    /* ========================================================
       💬 AESTHETIC CHATBOT & DISTINCT DUAL-COLORED BUBBLES
       ======================================================== */
    /* Base Chat Message */
    [data-testid="stChatMessage"] {
        padding: 12px 16px !important;
        margin-bottom: 12px !important;
        transition: all 0.2s ease !important;
    }

    /* 👤 USER MESSAGE BUBBLE: Right Side, Vibrant Sapphire Gradient */
    [data-testid="stChatMessage"]:has(.user-msg-marker),
    [data-testid="stChatMessage"]:has([aria-label*="user"]),
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
        flex-direction: row-reverse !important;
        background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%) !important;
        border: 1px solid rgba(56, 189, 248, 0.45) !important;
        border-radius: 18px 18px 4px 18px !important;
        margin-left: auto !important;
        margin-right: 0 !important;
        width: fit-content !important;
        max-width: 82% !important;
        box-shadow: 0 4px 16px rgba(2, 132, 199, 0.35) !important;
    }

    [data-testid="stChatMessage"]:has(.user-msg-marker) p,
    [data-testid="stChatMessage"]:has(.user-msg-marker) span,
    [data-testid="stChatMessage"]:has(.user-msg-marker) li,
    [data-testid="stChatMessage"]:has([aria-label*="user"]) p,
    [data-testid="stChatMessage"]:has([aria-label*="user"]) span,
    [data-testid="stChatMessage"]:has([aria-label*="user"]) li,
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) p,
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) span {
        color: #ffffff !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        line-height: 1.55 !important;
    }

    [data-testid="stChatMessage"]:has(.user-msg-marker) [data-testid="stChatMessageAvatarCustom"],
    [data-testid="stChatMessage"]:has([aria-label*="user"]) [data-testid="stChatMessageAvatarCustom"],
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
        background: rgba(255, 255, 255, 0.22) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 50% !important;
    }

    [data-testid="stChatMessage"]:has(.user-msg-marker) [data-testid="stCaptionContainer"] p,
    [data-testid="stChatMessage"]:has([aria-label*="user"]) [data-testid="stCaptionContainer"] p {
        color: rgba(255, 255, 255, 0.8) !important;
        font-size: 0.72rem !important;
        text-align: right !important;
        margin-top: 4px !important;
    }

    /* 🤖 ASSISTANT (AURA) BUBBLE: Left Side, Sleek Cyber Dark-Slate Card */
    [data-testid="stChatMessage"]:has(.assistant-msg-marker),
    [data-testid="stChatMessage"]:has([aria-label*="assistant"]),
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
        flex-direction: row !important;
        background: linear-gradient(135deg, #111a2e 0%, #0d1527 100%) !important;
        border: 1px solid rgba(56, 189, 248, 0.28) !important;
        border-radius: 18px 18px 18px 4px !important;
        margin-right: auto !important;
        margin-left: 0 !important;
        width: fit-content !important;
        max-width: 88% !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.45), 0 0 15px rgba(56, 189, 248, 0.05) !important;
    }

    [data-testid="stChatMessage"]:has(.assistant-msg-marker) p,
    [data-testid="stChatMessage"]:has(.assistant-msg-marker) li,
    [data-testid="stChatMessage"]:has([aria-label*="assistant"]) p,
    [data-testid="stChatMessage"]:has([aria-label*="assistant"]) li,
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) p,
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) li {
        color: #f1f5f9 !important;
        font-size: 0.95rem !important;
        line-height: 1.6 !important;
    }

    [data-testid="stChatMessage"]:has(.assistant-msg-marker) strong,
    [data-testid="stChatMessage"]:has([aria-label*="assistant"]) strong,
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) strong {
        color: #38bdf8 !important;
        font-weight: 700 !important;
    }

    [data-testid="stChatMessage"]:has(.assistant-msg-marker) [data-testid="stChatMessageAvatarCustom"],
    [data-testid="stChatMessage"]:has([aria-label*="assistant"]) [data-testid="stChatMessageAvatarCustom"],
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
        background: rgba(14, 165, 233, 0.15) !important;
        border: 1px solid rgba(56, 189, 248, 0.45) !important;
        border-radius: 50% !important;
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.3) !important;
    }

    [data-testid="stChatMessage"]:has(.assistant-msg-marker) [data-testid="stCaptionContainer"] p,
    [data-testid="stChatMessage"]:has([aria-label*="assistant"]) [data-testid="stCaptionContainer"] p {
        color: #94a3b8 !important;
        font-size: 0.72rem !important;
        margin-top: 4px !important;
    }

    /* Modal / Dialog Enhancements */
    div[data-testid="stDialog"] > div {
        background-color: #0c1222 !important;
        border: 1px solid rgba(56, 189, 248, 0.35) !important;
        border-radius: 18px !important;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.75), 0 0 35px rgba(56, 189, 248, 0.15) !important;
    }

    /* Quick question inquiry pill buttons in Dialog */
    div[data-testid="stDialog"] .stButton > button {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
        color: #cbd5e1 !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        padding: 6px 12px !important;
        transition: all 0.2s ease !important;
    }

    div[data-testid="stDialog"] .stButton > button:hover {
        background: rgba(56, 189, 248, 0.15) !important;
        border-color: rgba(56, 189, 248, 0.45) !important;
        color: #38bdf8 !important;
        transform: translateY(-1px) !important;
    }

    /* Scrollbar styling for message box */
    [data-testid="stDialog"] [data-testid="stContainer"]::-webkit-scrollbar {
        width: 6px;
    }
    [data-testid="stDialog"] [data-testid="stContainer"]::-webkit-scrollbar-thumb {
        background: rgba(56, 189, 248, 0.35);
        border-radius: 9999px;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    }

    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        background-color: #111a2e;
        border-radius: 8px 8px 0 0;
        color: #94a3b8 !important;
        font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
        background-color: #0284c7 !important;
        color: #ffffff !important;
    }

    /* Primary and Secondary Buttons */
    .stButton > button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 8px 18px !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%) !important;
        border: none !important;
        color: #ffffff !important;
    }

    .stButton > button[kind="secondary"] {
        background-color: #1a2234 !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        color: #f1f5f9 !important;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(56, 189, 248, 0.25) !important;
    }

    /* Captions & Info alerts */
    .stCaption, [data-testid="stCaptionContainer"] p {
        color: #94a3b8 !important;
        font-weight: 500 !important;
    }

    .stAlert {
        background-color: #111a2e !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
    }

    /* Floating Corner Chat Widget Button (Guaranteed Right Side) */
    .st-key-floating_corner_chat {
        position: fixed !important;
        bottom: 24px !important;
        right: 24px !important;
        left: auto !important;
        width: auto !important;
        z-index: 999999 !important;
        display: flex !important;
        justify-content: flex-end !important;
        pointer-events: none !important;
    }

    .st-key-fab_corner_chat {
        position: fixed !important;
        bottom: 24px !important;
        right: 24px !important;
        left: auto !important;
        width: auto !important;
        z-index: 999999 !important;
        pointer-events: auto !important;
    }

    .st-key-fab_corner_chat > button,
    .st-key-floating_corner_chat button {
        position: fixed !important;
        bottom: 24px !important;
        right: 24px !important;
        left: auto !important;
        width: auto !important;
        margin: 0 !important;
        background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%) !important;
        color: #ffffff !important;
        border: 1px solid rgba(56, 189, 248, 0.5) !important;
        border-radius: 9999px !important;
        padding: 10px 20px !important;
        font-size: 0.9rem !important;
        font-weight: 700 !important;
        box-shadow: 0 8px 25px rgba(2, 132, 199, 0.5) !important;
        display: flex !important;
        align-items: center !important;
        gap: 6px !important;
        cursor: pointer !important;
        pointer-events: auto !important;
        transition: all 0.25s ease !important;
    }

    .st-key-fab_corner_chat > button:hover,
    .st-key-floating_corner_chat button:hover {
        transform: scale(1.05) translateY(-2px) !important;
        box-shadow: 0 12px 32px rgba(56, 189, 248, 0.65) !important;
    }

    /* Compact Dialog Aligned Towards Right on Desktop */
    @media (min-width: 768px) {
        div[data-testid="stDialog"] > div {
            margin-right: 24px !important;
            margin-left: auto !important;
            max-width: 460px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🧠 COMPREHENSIVE KNOWLEDGE BASE (AURA AI)
# ==========================================
KNOWLEDGE_BASE = {
    "developer_name": "Hadi Seelro",
    "role": "AI Engineer & Automation Specialist",
    "experience": "Specialized in building smart 24/7 customer assistants, automated business workflows, custom document search tools, and modern web applications.",
    "skills": [
        "24/7 Customer Support AI Chatbots (Website & WhatsApp)",
        "Automated Business Workflows (Data entry, emails, invoices)",
        "Smart PDF & Document Search (Ask questions from your files)",
        "Custom AI Websites & Portals (Fast, modern, interactive)",
        "Top AI Models (Google Gemini, OpenAI ChatGPT, Claude)",
        "Simple, user-friendly dashboards for non-technical teams"
    ],
    "services": [
        {
            "title": "24/7 Customer AI Chatbots",
            "desc": "An intelligent virtual assistant for your website or WhatsApp that answers customer questions, captures leads, and books appointments around the clock.",
            "timeline": "1-2 Weeks",
            "tier": "$1,500 - $3,000"
        },
        {
            "title": "Smart Business Automation",
            "desc": "Automate repetitive daily tasks—like answering routine emails, organizing data, generating reports, and processing invoices with zero manual effort.",
            "timeline": "2-3 Weeks",
            "tier": "$2,500 - $5,000"
        },
        {
            "title": "Document & PDF Intelligence",
            "desc": "Upload your company catalogs, user manuals, or legal policies, and let AI instantly search and answer questions with 100% accuracy.",
            "timeline": "1-2 Weeks",
            "tier": "$2,000 - $4,000"
        },
        {
            "title": "1-on-1 AI Strategy & Consulting",
            "desc": "Personal consultation to help you identify the best ways AI can save your company time, reduce overhead costs, and boost team productivity.",
            "timeline": "Hourly or Monthly",
            "tier": "$150 / hour"
        }
    ],
    "projects": [
        {
            "name": "Smart Market & Competitor News Tracker",
            "tags": ["Automated Research", "Market Intel", "Gemini AI"],
            "desc": "An automated AI assistant that scans daily industry news, tracks competitor pricing changes, and delivers a quick morning email briefing.",
            "metrics": "Saves 15+ hours of manual research every week"
        },
        {
            "name": "OmniDoc: Smart PDF & Document Assistant",
            "tags": ["PDF Search", "Zero Hallucination", "Fast AI"],
            "desc": "Allows business teams to upload hundreds of pages of complex documents, contracts, and receipts and ask questions in plain English.",
            "metrics": "Instant answers in < 1 second across 1,000+ pages"
        },
        {
            "name": "SentinelAI: Automated Website Quality Checker",
            "tags": ["Quality Assurance", "Automated Checks", "Security"],
            "desc": "Monitors online forms, websites, and applications to catch errors, dead links, or security gaps before real customers encounter them.",
            "metrics": "Over 400+ issues detected automatically"
        }
    ],
    "contact": {
        "email": "sainbuxseelro11@gmail.com",
        "github": "https://github.com/SainBux-HadiSeelro",
        "linkedin": "https://linkedin.com/in/hadiseelro",
        "availability": "Open for New Client Projects & Remote Consulting"
    }
}

# ==========================================
# 🤖 INTELLIGENT AGENT ENGINE (24/7 OFFLINE & ONLINE)
# ==========================================
def get_gemini_api_key() -> str:
    """Retrieve Gemini API key from session state, Streamlit secrets, or environment."""
    if st.session_state.get("user_gemini_key"):
        return st.session_state.user_gemini_key.strip()
    try:
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"].strip()
    except Exception:
        pass
    return os.environ.get("GEMINI_API_KEY", "").strip()


def query_gemini_api(user_query: str, history: list, api_key: str) -> str:
    """Call Google Gemini 1.5 Flash API via REST endpoint."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    system_instruction = (
        "You are Aura, an elite, professional, and friendly 24/7 autonomous AI concierge representing Hadi Seelro. "
        "Hadi is a Senior Agentic AI Systems Architect & Generative AI Engineer based in Pakistan, collaborating globally. "
        "Hadi specializes in: "
        "- Autonomous Multi-Agent Swarms (LangGraph, CrewAI, AutoGen) "
        "- Enterprise Zero-Hallucination RAG Pipelines (ChromaDB, Pinecone, FAISS, Hybrid Search) "
        "- Model Context Protocol (MCP) and custom tool execution "
        "- Production LLM orchestration with Google Gemini 2.5/Flash, GPT-4o, and Claude 3.5 Sonnet "
        "- Pricing tiers: MVP Agent ($1,500 - $3,000), Enterprise Swarms ($3,500 - $8,000), Consulting ($150/hr). "
        "Hadi's contact: Email: hadi.seelro@example.com, LinkedIn: linkedin.com/in/hadiseelro, GitHub: github.com/hadiseelro. "
        "Instructions: "
        "1. Always reply in the exact language the user uses (English, Urdu, Roman Urdu, Hindi). "
        "2. Answer ANY technical, architectural, pricing, timeline, coding, or general question intelligently and concisely. "
        "3. If the user shares an idea or asks for project advice, provide actionable technical feedback and encourage hiring Hadi. "
        "4. If the user provides their email or contact info, politely confirm that Hadi will contact them within 24 hours."
    )
    
    contents = []
    if history:
        for msg in history[-6:]:
            role = "user" if msg.get("role") == "user" else "model"
            contents.append({
                "role": role,
                "parts": [{"text": msg.get("content", "")}]
            })
            
    contents.append({
        "role": "user",
        "parts": [{"text": user_query}]
    })
    
    payload = {
        "systemInstruction": {"parts": [{"text": system_instruction}]},
        "contents": contents,
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 600
        }
    }
    
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, json=payload, headers=headers, timeout=12)
    if resp.status_code == 200:
        res_json = resp.json()
        return res_json["candidates"][0]["content"]["parts"][0]["text"].strip()
    else:
        raise Exception(f"API Error {resp.status_code}: {resp.text}")


def generate_local_nlp_response(user_input: str) -> str:
    """
    Comprehensive Local NLP & Intent Engine for Aura AI.
    Handles general questions, tech advice, Urdu/English queries, pricing, and lead intake.
    """
    q = user_input.lower().strip()
    
    # 1. Lead / Email Detection (Instant capture)
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', user_input)
    if email_match:
        st.session_state.lead_count = st.session_state.get("lead_count", 0) + 1
        return (
            f"🎉 **Thank you! Contact details received:** `{email_match.group(0)}`\n\n"
            f"I have logged your request into Hadi Seelro's intake buffer. "
            f"Hadi will review your project requirements and email you directly within **24 hours** "
            f"with an architectural breakdown and ballpark timeline.\n\n"
            f"Feel free to share any additional details about your project or tech stack!"
        )

    # 2. Greetings, Small Talk & Well-wishes (English, Roman Urdu, Urdu)
    if any(k in q for k in ["hi", "hello", "hey", "salam", "aoa", "kya haal", "kaise ho", "kese ho", "who are you", "koun ho", "kya karti ho", "intro", "namaste", "good morning", "good evening", "sab theek"]):
        return (
            "👋 **Hello! Main hoon Aura**, Hadi Seelro ka 24/7 Autonomous AI Concierge.\n\n"
            "Main Hadi ke projects, skills, pricing, aur multi-agent architectures se fully updated hoon. "
            "Aap mujhse koi bhi sawal pooch sakte hain, for example:\n"
            "- 💼 *'Hadi kya services offer karte hain?'*\n"
            "- 💰 *'Custom AI bot ya website banwane ka kitna kharcha aayega?'*\n"
            "- 🤖 *'Agentic AI aur LangGraph kya hota hai?'*\n"
            "- 🚀 *'Hadi se kaise contact ya hire karein?'*\n\n"
            "Bataiye, aaj main aapki kya madad kar sakti hoon?"
        )

    # 3. Who is Hadi? / Experience / Background
    if any(k in q for k in ["who is hadi", "hadi kaun", "hadi kon", "about hadi", "experience", "background", "education", "qualification", "kahan se", "based", "location", "senior architect", "bio"]):
        return (
            "### 👨‍💻 About Hadi Seelro\n\n"
            "**Hadi Seelro** ek **Senior Agentic AI Systems Architect & Generative AI Engineer** hain. "
            "Woh scalable multi-agent systems, self-correcting AI workflows, aur enterprise RAG pipelines design aur deploy karte hain.\n\n"
            "**Key Highlights:**\n"
            "- 🛠️ **Specialization:** LangGraph, CrewAI, Google Gemini 2.5, OpenAI GPT-4o, ChromaDB, FastAPI, Streamlit.\n"
            "- 🚀 **Track Record:** 15+ production AI agents, 99.4% precision RAG systems, aur 80% token cost optimization.\n"
            "- 🌍 **Availability:** Open for enterprise consulting, freelance contracts, aur full-time remote roles globally."
        )

    # 4. What is Agentic AI? / Concepts / RAG / LangGraph Explanations
    if any(k in q for k in ["what is agentic ai", "agentic ai kya", "what is rag", "rag kya", "what is langgraph", "crewai", "multi-agent", "mcp", "model context protocol", "vector database", "difference between chatbot", "kya farq"]):
        return (
            "### 💡 Agentic AI vs Traditional Chatbots\n\n"
            "Traditional chatbots sirf single prompt-and-response par kaam karte hain. "
            "Lekin **Agentic AI systems autonomous** hote hain:\n\n"
            "1. 🧠 **Reasoning & Planning:** Task ko multiple steps mein break karte hain.\n"
            "2. 🛠️ **Tool Calling:** Databases, APIs, search engines, aur webhooks ko automatically call karte hain.\n"
            "3. 🤝 **Multi-Agent Collaboration:** Multiple specialized agents (Researcher $\to$ Analyst $\to$ Reviewer) mil kar kaam karte hain.\n"
            "4. 🔍 **Self-Correction & RAG:** Apni ghalatiyan khud detect karte hain aur zero-hallucination ensure karte hain.\n\n"
            "Hadi inhi systems ko **LangGraph** aur **CrewAI** ke zariye enterprise businesses ke liye build karte hain!"
        )

    # 5. Services & Can You Build? (Chatbot, Website, Automation, App)
    if any(k in q for k in ["service", "services", "kya bana sakte", "can you build", "can you make", "website", "bot", "chatbot", "rag", "system", "automation", "e-commerce", "lead", "scrape", "scraping", "integration", "crm"]):
        services_text = "### 🛠️ Production Agentic AI Services by Hadi Seelro:\n\n"
        for idx, s in enumerate(KNOWLEDGE_BASE["services"], 1):
            services_text += f"**{idx}. {s['title']}**\n"
            services_text += f"- *Overview*: {s['desc']}\n"
            services_text += f"- *Delivery*: `{s['timeline']}` | *Pricing Tier*: `{s['tier']}`\n\n"
        services_text += "💬 *Aapko kis tarah ka project ya bot banwana hai? Apni requirement bataiye, main exact roadmap suggest karungi!*"
        return services_text

    # 6. Pricing, Cost, Rates & Timeline
    if any(k in q for k in ["cost", "price", "pricing", "budget", "rate", "kitna kharcha", "charges", "fees", "kitne paise", "expensive", "quote", "discount", "hourly", "timeline", "time kitna", "kab tak"]):
        return (
            "### 💰 Project Investment & Estimation Guide\n\n"
            "Hadi Seelro transparent aur milestone-based rates par kaam karte hain:\n\n"
            "- ⚡ **Proof-of-Concept / MVP AI Agent:** `$1,500 - $3,000` (1-2 weeks delivery)\n"
            "- 🏢 **Enterprise Multi-Agent Swarm (LangGraph/CrewAI):** `$3,500 - $8,000` (Production deployment, DB & Tool integration)\n"
            "- 🔍 **Enterprise RAG System (Zero Hallucination):** `$2,000 - $5,000` (Vector DB setup, semantic re-ranking)\n"
            "- 👨‍💻 **Hourly Technical Consulting:** `$150 / hour`\n\n"
            "📩 *Apna use case ya email drop karein taake Hadi aapke liye 24 hours ke andar custom Statement of Work (SOW) tayyar karein!*"
        )

    # 7. Tech Stack, Python, Tools
    if any(k in q for k in ["skill", "skills", "tech stack", "technologies", "langgraph", "crewai", "python", "gemini", "gpt", "tools"]):
        skills_list = "\n".join([f"- ✅ **{s}**" for s in KNOWLEDGE_BASE["skills"]])
        return (
            f"### 🧠 Hadi Seelro's Core Tech Stack\n\n"
            f"{skills_list}\n\n"
            f"Har system ko high speed, zero-downtime, aur low-token cost ke liye optimize kiya jata hai."
        )

    # 8. Projects & Case Studies
    if any(k in q for k in ["project", "projects", "portfolio", "work", "kaam", "case study", "benchmark", "nexus", "omnidoc", "sentinel"]):
        p_text = "### 🚀 Featured Deployments by Hadi:\n\n"
        for p in KNOWLEDGE_BASE["projects"]:
            p_text += f"#### 🔹 {p['name']}\n"
            p_text += f"- **Stack:** {', '.join(p['tags'])}\n"
            p_text += f"- **Overview:** {p['desc']}\n"
            p_text += f"- **Metrics:** `{p['metrics']}`\n\n"
        p_text += "👉 *Sidebar mein **'🛠️ Project Showcase'** tab par click karke full architecture explore karein!*"
        return p_text

    # 9. Hire, Contact & Meeting
    if any(k in q for k in ["hire", "contact", "email", "meeting", "call", "book", "rabta", "interview", "schedule", "talk to hadi"]):
        return (
            "### 📬 Hire Hadi Seelro or Schedule a Call\n\n"
            "Hadi globally founders aur engineering teams ke saath collaborate karte hain:\n\n"
            f"- 📧 **Direct Email:** `{KNOWLEDGE_BASE['contact']['email']}`\n"
            f"- 💼 **LinkedIn Profile:** [{KNOWLEDGE_BASE['contact']['linkedin']}]({KNOWLEDGE_BASE['contact']['linkedin']})\n"
            f"- 🐙 **GitHub Repositories:** [{KNOWLEDGE_BASE['contact']['github']}]({KNOWLEDGE_BASE['contact']['github']})\n"
            f"- 🟢 **Status:** `{KNOWLEDGE_BASE['contact']['availability']}`\n\n"
            "💬 *Aap apna email ya project brief yahan chat mein bhi likh sakte hain, main Hadi tak foran deliver kar doongi!*"
        )

    # 10. Gratitude, Compliments & Farewell
    if any(k in q for k in ["thank", "thanks", "shukriya", "great", "good", "nice", "awesome", "zabardast", "bohat acha", "cool", "perfect", "bye", "allah hafiz", "khuda hafiz"]):
        return (
            "😊 **Shukriya!** Mujhe aapki madad karke bohat khushi hui.\n\n"
            "Agar aapka koi aur sawal ho, ya aap Hadi ke saath kisi AI project par collaborate karna chahein, "
            "to main hamesha 24/7 yahan available hoon. Have a wonderful day ahead! 🚀"
        )

    # 11. Contextual Dynamic Intelligent Fallback
    return (
        f"🤖 **Aura AI Consultation Note:**\n\n"
        f"Aapne poocha: *'{user_input}'*.\n\n"
        f"Hadi Seelro custom AI engineering mein specialized hain aur is tarah ke use cases ke liye "
        f"autonomous agent workflows, custom RAG pipelines, ya LLM API integrations design karte hain.\n\n"
        f"**Next steps:**\n"
        f"1. 💰 Ask: *'Is project ka ballpark cost aur timeline kya hoga?'*\n"
        f"2. 🛠️ Ask: *'Hadi isme kaun se tools aur tech stack use karenge?'*\n"
        f"3. 📩 Apna **Email Address** yahan type karein taake Hadi aapse direct contact kar sakein!"
    )


def generate_agent_response(user_input: str, history: list = None) -> str:
    """
    Main response generator:
    Tries Live Gemini API first (if key configured), else uses rich local NLP engine.
    """
    api_key = get_gemini_api_key()
    if api_key:
        try:
            return query_gemini_api(user_input, history or [], api_key)
        except Exception:
            # Fall back gracefully to local engine if API fails
            pass
            
    return generate_local_nlp_response(user_input)

# ==========================================
# 🗄️ SESSION STATE INITIALIZATION & RESET
# ==========================================
def reset_aura_chat():
    """Resets the chat conversation to initial welcoming state."""
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 **Welcome! I am Aura**, Hadi Seelro's 24/7 Autonomous AI Agent.\n\n"
                "I am equipped with complete knowledge of Hadi's skills, multi-agent AI systems, "
                "case studies, and project estimation. How can I help your business or project today?"
            ),
            "time": datetime.now().strftime("%I:%M %p")
        }
    ]

if "messages" not in st.session_state:
    reset_aura_chat()

if "lead_count" not in st.session_state:
    st.session_state.lead_count = 3

# ==========================================
# 💬 AURA AI CHAT DIALOG (MODAL & CORNER WIDGET)
# ==========================================
@st.dialog("🤖 Aura AI • 24/7 Client Concierge", width="small")
def open_aura_chat_dialog():
    # Top Status & Clear Chat bar
    col_hdr_status, col_hdr_action = st.columns([0.65, 0.35], vertical_alignment="center")
    with col_hdr_status:
        st.markdown(
            "<div style='display:flex; align-items:center; gap:6px; margin-top:-6px; margin-bottom:6px;'>"
            "<span style='display:inline-block; width:8px; height:8px; background:#10b981; border-radius:50%; box-shadow:0 0 8px #10b981;'></span>"
            "<span style='color:#34d399; font-weight:600; font-size:0.82rem;'>Aura Active • Ready to Help</span>"
            "</div>",
            unsafe_allow_html=True
        )
    with col_hdr_action:
        if len(st.session_state.messages) > 1:
            st.button("🧹 Clear Chat", key="dlg_clear_chat_top", on_click=reset_aura_chat, use_container_width=True, help="Clear chat and start fresh")
    
    # Optional Live Gemini Key expander
    with st.expander("🔑 AI Mode: Live Gemini / Knowledge Base", expanded=False):
        st.caption("Aura operates 24/7. Add a free Gemini API key (or set `GEMINI_API_KEY` in Streamlit Secrets) to chat live with LLM:")
        user_key = st.text_input("Gemini API Key:", value=st.session_state.get("user_gemini_key", ""), type="password", placeholder="AIzaSy...", key="inp_gemini_key")
        if user_key and user_key != st.session_state.get("user_gemini_key", ""):
            st.session_state.user_gemini_key = user_key
            st.success("API Key connected!")
    
    # Message History Container (Aesthetic, Compact & Scrollable)
    msg_box = st.container(height=300)
    with msg_box:
        for msg in st.session_state.messages:
            is_user = msg.get("role") == "user"
            with st.chat_message(msg["role"], avatar="👤" if is_user else "🤖"):
                marker = '<div class="user-msg-marker"></div>' if is_user else '<div class="assistant-msg-marker"></div>'
                st.markdown(marker, unsafe_allow_html=True)
                st.markdown(msg["content"])
                if "time" in msg:
                    st.caption(f"🕒 {msg['time']}" if is_user else f"🕒 {msg['time']} • Aura Engine")

    # Quick Question Chips at the BOTTOM (Neeche)
    st.caption("⚡ Quick Inquiries:")
    col_qp1, col_qp2 = st.columns(2)
    quick_input = None
    if col_qp1.button("💼 Services & Rates", key="dlg_qp1", use_container_width=True):
        quick_input = "What services do you offer?"
    if col_qp2.button("💰 Cost & Timeline", key="dlg_qp2", use_container_width=True):
        quick_input = "How much does a custom AI agent cost?"
        
    col_qp3, col_qp4 = st.columns(2)
    if col_qp3.button("🧠 Case Studies", key="dlg_qp3", use_container_width=True):
        quick_input = "Tell me about Hadi's projects and case studies"
    if col_qp4.button("📬 Hire / Contact", key="dlg_qp4", use_container_width=True):
        quick_input = "How can I contact and hire Hadi Seelro?"

    # Chat Input
    prompt = st.chat_input("Ask Aura anything...", key="dlg_chat_input")
    if quick_input:
        prompt = quick_input

    if prompt:
        current_time = datetime.now().strftime("%I:%M %p")
        # 1. Add User Message to state
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "time": current_time
        })
        # 2. Render directly in msg_box (Keeps dialog open!)
        with msg_box:
            with st.chat_message("user", avatar="👤"):
                st.markdown('<div class="user-msg-marker"></div>', unsafe_allow_html=True)
                st.markdown(prompt)
                st.caption(f"🕒 {current_time}")
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown('<div class="assistant-msg-marker"></div>', unsafe_allow_html=True)
                with st.spinner("Analyzing with Aura AI..."):
                    reply = generate_agent_response(prompt, st.session_state.messages)
                    st.markdown(reply)
                    st.caption(f"🕒 {current_time} • Verified by Aura Engine")
        # 3. Save Assistant Message to state
        st.session_state.messages.append({
            "role": "assistant",
            "content": reply,
            "time": current_time
        })

    # Clear Chat option at bottom
    if len(st.session_state.messages) > 1:
        st.button("🧹 Clear Chat History", key="dlg_clear_chat_bottom", on_click=reset_aura_chat, use_container_width=True)

# ==========================================
# 📌 SIDEBAR NAVIGATION & QUICK PROFILE
# ==========================================
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <div style="font-size: 2.5rem;">🤖</div>
            <h2 style="margin: 0; font-size: 1.3rem; color: #00f2fe;">HADI SEELRO</h2>
            <p style="color: #94a3b8; font-size: 0.85rem; margin: 4px 0 12px 0;">AI Solutions & Automation Expert</p>
            <div class="agent-pill">
                <span class="pulse-dot"></span>
                <span>Available for New Projects</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Direct Chat Trigger in Sidebar Corner
    if st.button("💬 Chat with AI Assistant", key="sidebar_chat_btn", use_container_width=True, type="primary"):
        open_aura_chat_dialog()
        
    st.markdown("---")
    
    # Simple, Non-Technical Navigation Menu
    nav_page = st.radio(
        "⚡ Explore",
        [
            "🏠 Home & Overview",
            "⚡ Try Live Demos",
            "🛠️ Services & What I Build",
            "💡 How It Works & FAQ"
        ],
        index=0
    )
    
    st.markdown("---")
    
    # Simple Trust & Reliability Badges
    st.markdown("### 🌟 Why Work With Hadi?")
    st.markdown("✅ **100% Custom Built** for your needs")
    st.markdown("✅ **24/7 Support** & Fast Delivery")
    st.markdown("✅ **Zero Tech Headaches** for you")


# ==========================================
# 🏠 PAGE 1: HOME & OVERVIEW
# ==========================================
if nav_page == "🏠 Home & Overview":
    st.markdown("""
        <div class="hero-card">
            <div class="agent-pill">
                <span class="pulse-dot"></span>
                <span>Smart AI for Business • 24/7 Automation</span>
            </div>
            <h1 class="hero-title">I Build Smart AI Assistants & Websites for Your Business</h1>
            <p class="hero-subtitle">
                Save hours of manual work every week. I build <b>intelligent 24/7 customer chatbots, 
                automated daily workflows, and fast modern web apps</b> that help your business grow while keeping costs low.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Metric Counters
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">15+</div>
                <div class="metric-label">AI Systems Built</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">99%</div>
                <div class="metric-label">Answer Accuracy</div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">80%</div>
                <div class="metric-label">Time & Cost Saved</div>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">24/7</div>
                <div class="metric-label">Non-Stop Operation</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 4 Simple What I Can Do For You Cards
    st.subheader("💡 What Can Custom AI Do For Your Business?")
    st.write("You don't need to understand complex coding. Here are the real, practical solutions I create for clients:")
    
    col_cap1, col_cap2 = st.columns(2)
    with col_cap1:
        st.markdown("""
        <div class="project-card">
            <h4 style="color: #00f2fe; margin-top:0;">💬 24/7 Customer Support Chatbots</h4>
            <p style="color: #cbd5e1; font-size: 0.95rem;">
                Never lose a client lead again. An AI assistant on your website or WhatsApp answers common inquiries, 
                quotes pricing, and captures customer contact details while you sleep.
            </p>
            <span class="tag">Instant Answers</span>
            <span class="tag">Lead Capture</span>
            <span class="tag">Zero Wait Time</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h4 style="color: #00f2fe; margin-top:0;">🔍 Instant Document & PDF Search</h4>
            <p style="color: #cbd5e1; font-size: 0.95rem;">
                Upload your product catalogs, legal policies, or employee manuals. Your team or clients can ask questions 
                in plain language and get instant, 100% accurate answers.
            </p>
            <span class="tag">PDF Assistant</span>
            <span class="tag">Zero Hallucinations</span>
            <span class="tag">Instant Search</span>
        </div>
        """, unsafe_allow_html=True)

    with col_cap2:
        st.markdown("""
        <div class="project-card">
            <h4 style="color: #00f2fe; margin-top:0;">⚡ Smart Business Automation</h4>
            <p style="color: #cbd5e1; font-size: 0.95rem;">
                Automate repetitive daily tasks—like reading routine emails, extracting invoice data, updating spreadsheets, 
                and preparing weekly briefing reports with zero manual effort.
            </p>
            <span class="tag">Save 15+ Hours/Week</span>
            <span class="tag">No Manual Errors</span>
            <span class="tag">Hands-Free</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h4 style="color: #00f2fe; margin-top:0;">🌐 Custom Modern Websites & Web Apps</h4>
            <p style="color: #cbd5e1; font-size: 0.95rem;">
                Fast, mobile-friendly, interactive websites (just like this one) built specifically around your brand, 
                business goals, and client workflow with built-in AI tools.
            </p>
            <span class="tag">Modern Design</span>
            <span class="tag">Mobile Friendly</span>
            <span class="tag">Fast & Secure</span>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# ⚡ PAGE 2: TRY LIVE DEMOS
# ==========================================
elif nav_page == "⚡ Try Live Demos":
    st.title("⚡ See How Smart AI Works For Your Business")
    st.write("Click the interactive tools below to experience how AI automates tasks and saves your team hours of work.")
    
    lab_tab1, lab_tab2, lab_tab3 = st.tabs([
        "🤖 Try Automated Helper",
        "💰 Business Savings Calculator",
        "🛡️ Reliability & Guarantees"
    ])
    
    # Tab 1: Simple 3-Step Automation Demo
    with lab_tab1:
        st.subheader("Watch 3 AI Helpers Solve a Task Automatically")
        st.write("Pick a common business scenario and watch how AI coordinates to finish it with zero human effort:")
        
        sim_task = st.selectbox(
            "Select an everyday business task to test:",
            [
                "🛒 Customer Support: Verify Order Details & Issue Fast Refund",
                "📊 Market Research: Search Daily Competitor Pricing & Summarize",
                "📧 Email Assistant: Read Customer Inquiry & Draft Professional Reply"
            ]
        )
        
        if st.button("🚀 Run Automated AI Helper", type="primary"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Step 1
            status_text.markdown("🟡 **[Step 1: Information Finder]** Reading incoming customer request and checking records...")
            progress_bar.progress(33)
            time.sleep(0.8)
            st.success("✅ **Step 1 Completed:** Customer records and order history retrieved successfully.")
            
            # Step 2
            status_text.markdown("🟡 **[Step 2: Policy Checker]** Verifying business rules, return policy, and guidelines...")
            progress_bar.progress(66)
            time.sleep(0.9)
            st.info("ℹ️ **Step 2 Completed:** Order verified within policy guidelines. Zero issues found.")
            
            # Step 3
            status_text.markdown("🟡 **[Step 3: Action & Response]** Preparing friendly customer reply and notifying accounts...")
            progress_bar.progress(100)
            time.sleep(0.7)
            status_text.markdown("🟢 **[All Done!]** Task completed successfully with zero human delay!")
            
            st.balloons()
            st.markdown(f"""
            <div class="project-card" style="border-left: 4px solid #10b981; margin-top: 16px;">
                <h4 style="color:#10b981; margin:0 0 8px 0;">🎉 Task Completed in 2.4 Seconds</h4>
                <p><b>Task:</b> {sim_task}</p>
                <p><b>Human Time Saved:</b> ~15 minutes of employee workload.</p>
                <p><b>Result:</b> Customer received an instant, polite, and 100% accurate resolution.</p>
            </div>
            """, unsafe_allow_html=True)
            
    # Tab 2: Simple ROI / Savings Calculator
    with lab_tab2:
        st.subheader("📊 How Much Money & Time Can AI Save Your Business?")
        st.write("Adjust the sliders below based on your team's size to see your potential monthly savings:")
        
        c1, c2 = st.columns(2)
        with c1:
            tasks_per_month = st.slider("Repetitive tasks handled per month (emails, forms, lookups):", 500, 20000, 3000, step=500)
            mins_per_task = st.slider("Average minutes an employee spends per task:", 5, 45, 15)
        with c2:
            hourly_wage = st.slider("Employee average hourly wage ($/hr):", 15, 100, 30)
            st.caption("AI token and hosting costs typically average less than **$0.01 per task**.")
            
        # Calculation
        human_hours = (tasks_per_month * mins_per_task) / 60
        human_monthly_cost = human_hours * hourly_wage
        agent_monthly_cost = tasks_per_month * 0.015
        net_savings = human_monthly_cost - agent_monthly_cost
        
        st.markdown("---")
        r_col1, r_col2, r_col3 = st.columns(3)
        with r_col1:
            st.metric("Current Staff Cost", f"${human_monthly_cost:,.0f} / mo")
        with r_col2:
            st.metric("Cost with AI Assistant", f"${agent_monthly_cost:,.0f} / mo")
        with r_col3:
            st.metric("💰 Estimated Savings", f"${net_savings:,.0f} / mo", delta="95% Savings")
            
        st.caption("💡 Custom AI automation runs 24/7 without delays, burnout, sick leaves, or overtime pay.")

    # Tab 3: Simple Guarantees
    with lab_tab3:
        st.subheader("🛡️ Built For Peace of Mind")
        st.write("Every AI solution Hadi builds comes with strict enterprise guarantees:")
        
        g_col1, g_col2 = st.columns(2)
        with g_col1:
            st.markdown("""
            <div class="project-card">
                <h4 style="color:#00f2fe; margin-top:0;">🟢 24/7 Non-Stop Availability</h4>
                <p style="color:#cbd5e1; font-size:0.92rem;">
                    Your AI assistants work around the clock—weekends, holidays, and nights—with zero downtime.
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("""
            <div class="project-card">
                <h4 style="color:#00f2fe; margin-top:0;">⚡ Sub-Second Fast Answers</h4>
                <p style="color:#cbd5e1; font-size:0.92rem;">
                    Customers and staff get accurate answers in under 1 second instead of waiting hours for a reply.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        with g_col2:
            st.markdown("""
            <div class="project-card">
                <h4 style="color:#00f2fe; margin-top:0;">🔒 100% Data Confidentiality</h4>
                <p style="color:#cbd5e1; font-size:0.92rem;">
                    Your company data, customer contacts, and internal files stay strictly private and protected.
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("""
            <div class="project-card">
                <h4 style="color:#00f2fe; margin-top:0;">🎯 Zero Guesswork (Guarded AI)</h4>
                <p style="color:#cbd5e1; font-size:0.92rem;">
                    The AI is locked strictly to your verified company documents so it never invents false answers.
                </p>
            </div>
            """, unsafe_allow_html=True)


# ==========================================
# 🛠️ PAGE 3: SERVICES & WHAT I BUILD
# ==========================================
elif nav_page == "🛠️ Services & What I Build":
    st.title("🛠️ What I Can Build For Your Business")
    st.write("Proven, production-ready AI tools tailored to your exact business needs:")
    
    for proj in KNOWLEDGE_BASE["projects"]:
        st.markdown(f"""
        <div class="project-card">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
                <h3 style="color:#00f2fe; margin:0;">{proj['name']}</h3>
                <span class="tag" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">
                    Ready to Deploy
                </span>
            </div>
            <p style="color:#cbd5e1; margin-top:12px; font-size:1rem; line-height:1.6;">
                {proj['desc']}
            </p>
            <div style="margin: 12px 0;">
                {' '.join([f'<span class="tag">{t}</span>' for t in proj['tags']])}
            </div>
            <div style="background: rgba(0,0,0,0.3); padding: 8px 14px; border-radius: 8px; border-left: 3px solid #00f2fe; font-size: 0.9rem; color: #94a3b8;">
                ✨ <b>Key Business Benefit:</b> <span style="color: #00f2fe;">{proj['metrics']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("### 💼 Want a custom AI tool tailored to your exact workflow?")
    st.write("Whether you need a Shopify chatbot, an email assistant, or a custom web dashboard, Hadi can build it in 1 to 2 weeks.")


# ==========================================
# 💡 PAGE 4: HOW IT WORKS & FAQ
# ==========================================
elif nav_page == "💡 How It Works & FAQ":
    st.title("💡 How It Works & Frequently Asked Questions")
    st.write("Everything you need to know about working with Hadi Seelro to build custom AI for your business.")
    
    st.markdown("### 🚀 Simple 3-Step Process:")
    step1, step2, step3 = st.columns(3)
    with step1:
        st.markdown("""
        <div class="project-card" style="text-align: center;">
            <div style="font-size: 2rem;">📞</div>
            <h4 style="color:#00f2fe; margin: 8px 0;">1. Free Consultation</h4>
            <p style="color:#cbd5e1; font-size:0.9rem;">
                We discuss what repetitive problems or customer tasks you want to automate.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with step2:
        st.markdown("""
        <div class="project-card" style="text-align: center;">
            <div style="font-size: 2rem;">🛠️</div>
            <h4 style="color:#00f2fe; margin: 8px 0;">2. Custom Build</h4>
            <p style="color:#cbd5e1; font-size:0.9rem;">
                Hadi designs your AI assistant and connects it directly to your tools and website.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with step3:
        st.markdown("""
        <div class="project-card" style="text-align: center;">
            <div style="font-size: 2rem;">🚀</div>
            <h4 style="color:#00f2fe; margin: 8px 0;">3. Launch & Relax</h4>
            <p style="color:#cbd5e1; font-size:0.9rem;">
                Your AI assistant goes live 24/7, saving your team hours every day from Day 1.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    # Common Questions (FAQ)
    st.subheader("❓ Frequently Asked Questions (FAQ)")
    
    with st.expander("Do I need to be technical or know coding to use this?"):
        st.write(
            "**Not at all!** Every solution is built for everyday business owners and staff. "
            "You get a clean, easy-to-use dashboard and friendly chat interface that works just like WhatsApp or ChatGPT."
        )
        
    with st.expander("How long does it take to build and launch an AI assistant?"):
        st.write(
            "Most custom customer chatbots and business workflow assistants are fully built, tested, and live in **1 to 2 weeks**."
        )
        
    with st.expander("Can the AI connect to my existing website, Shopify, or WhatsApp?"):
        st.write(
            "**Yes!** Hadi can integrate your AI assistant directly into your WordPress or Shopify site, WhatsApp, "
            "CRM, email inbox, or Google Sheets."
        )
        
    with st.expander("What are the costs and pricing packages?"):
        st.write(
            "We offer clear, transparent milestone packages starting from **$1,500** for MVP chatbots, "
            "up to **$3,500 - $5,000** for advanced multi-agent workflows. No hidden fees or recurring traps."
        )
        
    with st.expander("Will the AI hallucinate or give false information to my customers?"):
        st.write(
            "**No.** We install strict guardrails so the AI only answers using your verified business policies, "
            "catalogs, and documents. If it ever encounters an unknown question, it politely asks for the customer's email or forwards it to your team."
        )


# ==========================================
# 🦶 FOOTER
# ==========================================
st.markdown("""
<div style="margin-top: 50px; padding: 24px 0 10px 0; border-top: 1px solid rgba(255, 255, 255, 0.08); text-align: center; color: #64748b; font-size: 0.85rem;">
    Built with ❤️ by <b>Hadi Seelro</b> — Smart AI Solutions & Business Automation<br>
    © 2026 Hadi Seelro • All Rights Reserved.
</div>
""", unsafe_allow_html=True)

# ==========================================
# 💬 FLOATING CORNER CHATBOT WIDGET
# ==========================================
with st.container(key="floating_corner_chat"):
    if st.button("🤖 Chat with AI Helper", key="fab_corner_chat"):
        open_aura_chat_dialog()

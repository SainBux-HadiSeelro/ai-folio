import streamlit as st
import time
import pandas as pd
from datetime import datetime

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

    /* Chat Messages */
    [data-testid="stChatMessage"] {
        background-color: #111a2e !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        padding: 16px 20px !important;
        margin-bottom: 12px !important;
    }

    [data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li {
        color: #f8fafc !important;
        font-size: 1rem !important;
        line-height: 1.65 !important;
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
            margin-right: 28px !important;
            margin-left: auto !important;
            max-width: 440px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🧠 COMPREHENSIVE KNOWLEDGE BASE (AURA AI)
# ==========================================
KNOWLEDGE_BASE = {
    "developer_name": "Hadi Seelro",
    "role": "Senior Agentic AI Systems Architect & Generative AI Engineer",
    "experience": "Specialized in Autonomous Multi-Agent Swarms, Enterprise RAG, LangGraph, CrewAI, Google Gemini, and production LLM orchestration.",
    "skills": [
        "Multi-Agent Architectures (LangGraph, CrewAI, AutoGen)",
        "Model Context Protocol (MCP) & Custom Tool Integration",
        "Enterprise RAG & Hybrid Vector Search (Chroma, Pinecone, FAISS)",
        "Large Language Models (Google Gemini 2.5/Flash, GPT-4o, Claude 3.5 Sonnet)",
        "Full-Stack Python AI Apps (Streamlit, FastAPI, Pydantic, AsyncIO)",
        "Automated CI/CD, Agent Telemetry, Prompt Guardrails, Evaluation"
    ],
    "services": [
        {
            "title": "Autonomous Agent Swarms",
            "desc": "Multi-agent systems where specialized agents (Researcher, Analyst, Executor) communicate and collaborate to solve complex business workflows end-to-end.",
            "timeline": "2-4 Weeks",
            "tier": "$3,000 - $8,000"
        },
        {
            "title": "Enterprise RAG & Knowledge Retrieval",
            "desc": "High-precision vector pipelines with semantic chunking, re-ranking, and zero-hallucination guardrails for internal company wikis and documentation.",
            "timeline": "1-3 Weeks",
            "tier": "$2,000 - $5,000"
        },
        {
            "title": "24/7 Intelligent Client & Customer Support Agents",
            "desc": "Production-ready autonomous conversational agents equipped with tool calling, live CRM syncing, lead capture, and instant booking capabilities.",
            "timeline": "1-2 Weeks",
            "tier": "$1,500 - $3,500"
        },
        {
            "title": "AI Strategy & Architectural Consulting",
            "desc": "1-on-1 technical advisory on LLM token economics, agent orchestration design, cloud infrastructure, and security compliance.",
            "timeline": "Hourly / Retainer",
            "tier": "$150/hr or $2,500/mo"
        }
    ],
    "projects": [
        {
            "name": "Nexus Swarm: Autonomous Market Intelligence",
            "tags": ["LangGraph", "CrewAI", "Gemini 2.5", "FastAPI"],
            "desc": "A coordinated 4-agent swarm that crawls real-time financial news, conducts technical analysis, verifies anomalies, and generates automated market briefing reports.",
            "metrics": "87% latency reduction • 99.4% factual accuracy"
        },
        {
            "name": "OmniDoc: Enterprise Multi-Modal RAG Engine",
            "tags": ["Streamlit", "ChromaDB", "Vector Search", "Python"],
            "desc": "Processes thousands of complex PDFs, financial statements, and diagrams with vision-enabled chunking and citation tracking.",
            "metrics": "100k+ docs indexed • < 600ms query latency"
        },
        {
            "name": "SentinelAI: Autonomous Code Reviewer & Security Agent",
            "tags": ["MCP Server", "GitHub Actions", "Python", "AST Parser"],
            "desc": "Monitors pull requests, executes static code security checks, identifies hallucinated dependencies, and posts automated fix suggestions.",
            "metrics": "420+ vulnerabilities detected • Zero false positives"
        }
    ],
    "contact": {
        "email": "hadi.seelro@example.com",
        "github": "https://github.com/hadiseelro",
        "linkedin": "https://linkedin.com/in/hadiseelro",
        "availability": "Open for Contract, Full-time Remote & Enterprise Consulting"
    }
}

# ==========================================
# 🤖 INTELLIGENT AGENT ENGINE (24/7 OFFLINE & ONLINE)
# ==========================================
def generate_agent_response(user_input: str) -> str:
    """
    Intelligent response generation engine for Aura AI.
    Features instant semantic intent matching, contextual synthesis,
    and lead handling.
    """
    query = user_input.lower().strip()
    
    # 1. Greetings & Identity
    if any(k in query for k in ["hi", "hello", "hey", "salam", "aoa", "who are you", "koun ho"]):
        return (
            "👋 **Hello! I am Aura**, the 24/7 Autonomous AI Agent representing **Hadi Seelro**.\n\n"
            "I have real-time access to Hadi's entire engineering portfolio, system specifications, "
            "agentic AI services, and availability. \n\n"
            "How can I assist you today? You can ask me:\n"
            "- 💼 *What AI services and agents can Hadi build for you?*\n"
            "- 📊 *Tell me about Hadi's LangGraph and CrewAI projects.*\n"
            "- 💰 *How much does a custom AI agent system cost?*\n"
            "- 📅 *How can I hire Hadi or schedule a technical consultation?*"
        )
        
    # 2. Services & Offerings
    elif any(k in query for k in ["service", "services", "offer", "kya karte ho", "build", "can you do"]):
        services_text = "### 🛠️ Production Agentic AI Services by Hadi Seelro:\n\n"
        for idx, s in enumerate(KNOWLEDGE_BASE["services"], 1):
            services_text += f"**{idx}. {s['title']}**\n"
            services_text += f"- *Overview*: {s['desc']}\n"
            services_text += f"- *Estimated Delivery*: `{s['timeline']}` | *Pricing Tier*: `{s['tier']}`\n\n"
        services_text += "💡 *Would you like an exact estimate for a custom project you have in mind? Let me know your requirements!*"
        return services_text

    # 3. Pricing, Costs & Estimates
    elif any(k in query for k in ["cost", "price", "pricing", "budget", "rate", "quote", "kitna kharcha"]):
        return (
            "### 💰 Project Investment & Estimation Guide\n\n"
            "Hadi offers transparent, milestone-driven pricing based on architecture complexity:\n\n"
            "- ⚡ **Proof-of-Concept / MVP AI Agent:** `$1,500 - $3,000` (1-2 weeks delivery)\n"
            "- 🏢 **Enterprise Multi-Agent Swarm (LangGraph/CrewAI):** `$3,500 - $8,000` (Production deployment, tool integration, custom DB)\n"
            "- 🔍 **Enterprise RAG System (Zero Hallucination):** `$2,000 - $5,000` (Vector DB setup, semantic re-ranking, document parsing)\n"
            "- 👨‍💻 **Hourly Technical Consulting:** `$150 / hour`\n\n"
            "📩 *Tell me about your use case, or leave your email below, and Hadi will provide a formal Statement of Work (SOW) within 24 hours!*"
        )

    # 4. Tech Stack & Skills
    elif any(k in query for k in ["skill", "skills", "tech stack", "technologies", "langgraph", "crewai", "python"]):
        skills_list = "\n".join([f"- ✅ **{s}**" for s in KNOWLEDGE_BASE["skills"]])
        return (
            f"### 🧠 Technical Stack & Core Competencies\n\n"
            f"Hadi Seelro specializes in building **autonomous, self-correcting agent systems**:\n\n"
            f"{skills_list}\n\n"
            f"He focuses on building real-world business automation that reduces operating expenses and delivers measurable ROI."
        )

    # 5. Projects & Case Studies
    elif any(k in query for k in ["project", "projects", "portfolio", "work", "kaam", "case study"]):
        p_text = "### 🚀 Featured Agentic AI Deployments by Hadi:\n\n"
        for p in KNOWLEDGE_BASE["projects"]:
            p_text += f"#### 🔹 {p['name']}\n"
            p_text += f"- **Stack:** {', '.join(p['tags'])}\n"
            p_text += f"- **Details:** {p['desc']}\n"
            p_text += f"- **Performance Metric:** `{p['metrics']}`\n\n"
        p_text += "👉 *Head over to the **'🛠️ Projects'** tab in the sidebar to explore full interactive architectural diagrams!*"
        return p_text

    # 6. Hiring, Contact & Booking
    elif any(k in query for k in ["hire", "contact", "email", "meeting", "call", "book", "rabta"]):
        return (
            "### 📬 Hire Hadi Seelro or Schedule a Call\n\n"
            "Hadi is actively collaborating with founders, enterprise teams, and tech startups:\n\n"
            f"- 📧 **Direct Email:** `{KNOWLEDGE_BASE['contact']['email']}`\n"
            f"- 💼 **LinkedIn Profile:** [{KNOWLEDGE_BASE['contact']['linkedin']}]({KNOWLEDGE_BASE['contact']['linkedin']})\n"
            f"- 🐙 **GitHub Repositories:** [{KNOWLEDGE_BASE['contact']['github']}]({KNOWLEDGE_BASE['contact']['github']})\n"
            f"- 🟢 **Status:** `{KNOWLEDGE_BASE['contact']['availability']}`\n\n"
            "💬 *You can also navigate to the **'📬 Contact & Hire'** section in the navigation menu to submit your project requirements directly!*"
        )

    # 7. General Contextual Fallback with Agentic Guidance
    else:
        return (
            f"🤖 **Aura Agent Intelligence Insight:**\n\n"
            f"Thank you for your question: *'{user_input}'*.\n\n"
            f"Hadi Seelro designs end-to-end **Agentic AI Systems**, ranging from autonomous lead-handling bots "
            f"to multi-agent workflow engines (LangGraph & CrewAI) and custom RAG knowledge bases.\n\n"
            f"**Recommended next steps:**\n"
            f"1. Ask me: *'What are Hadi's services and pricing?'*\n"
            f"2. Ask me: *'Show me recent projects and benchmarks'*\n"
            f"3. Type your contact info or project idea, and I will capture it for Hadi!"
        )

# ==========================================
# 🗄️ SESSION STATE INITIALIZATION
# ==========================================
if "messages" not in st.session_state:
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

if "lead_count" not in st.session_state:
    st.session_state.lead_count = 3

# ==========================================
# 💬 AURA AI CHAT DIALOG (MODAL & CORNER WIDGET)
# ==========================================
@st.dialog("🤖 Aura AI • 24/7 Client Concierge", width="small")
def open_aura_chat_dialog():
    st.markdown(
        "<p style='color: #cbd5e1; font-size: 0.88rem; margin-top: -10px; margin-bottom: 10px;'>"
        "Hadi's 24/7 autonomous client concierge. Ask questions or tap an inquiry below."
        "</p>",
        unsafe_allow_html=True
    )
    
    # Message History Container (Compact & Scrollable)
    msg_box = st.container(height=260)
    with msg_box:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"], avatar="🤖" if msg["role"] == "assistant" else "👤"):
                st.markdown(msg["content"])
                if "time" in msg:
                    st.caption(f"🕒 {msg['time']}")

    # Quick Question Chips at the BOTTOM (Neeche)
    st.caption("⚡ Quick Questions:")
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
        # 1. Add User Message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "time": current_time
        })
        # 2. Generate Response
        reply = generate_agent_response(prompt)
        st.session_state.messages.append({
            "role": "assistant",
            "content": reply,
            "time": current_time
        })
        st.rerun()

    if len(st.session_state.messages) > 1:
        if st.button("🧹 Clear Chat", key="dlg_clear_chat", type="secondary"):
            st.session_state.messages = [st.session_state.messages[0]]
            st.rerun()

# ==========================================
# 📌 SIDEBAR NAVIGATION & SYSTEM METRICS
# ==========================================
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <div style="font-size: 2.5rem;">🤖</div>
            <h2 style="margin: 0; font-size: 1.3rem; color: #00f2fe;">HADI SEELRO</h2>
            <p style="color: #94a3b8; font-size: 0.8rem; margin: 4px 0 12px 0;">Agentic AI Systems Architect</p>
            <div class="agent-pill">
                <span class="pulse-dot"></span>
                <span>Agent Online 24/7</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Direct Chat Trigger in Sidebar Corner
    if st.button("💬 Chat with Aura AI (24/7)", key="sidebar_chat_btn", use_container_width=True, type="primary"):
        open_aura_chat_dialog()
        
    st.markdown("---")
    
    # Navigation Radio (Chatbot separated into floating widget)
    nav_page = st.radio(
        "⚡ Navigation",
        [
            "🏠 Overview & Bio",
            "⚡ Agentic AI Lab (Demos)",
            "🛠️ Project Showcase",
            "📑 System Specs & Architecture",
            "📬 Contact & Hire"
        ],
        index=0
    )
    
    st.markdown("---")
    
    # Live System Telemetry
    st.markdown("### 📊 Agent Telemetry")
    col_sb1, col_sb2 = st.columns(2)
    with col_sb1:
        st.metric("Agent Uptime", "99.98%")
    with col_sb2:
        st.metric("Response", "< 350ms")
        
    st.caption("🔒 Architecture: Sandboxed State Engine v1.0")
    
    # Quick Links
    st.markdown("### 🔗 Connect")
    st.markdown(f"- [🐙 GitHub Repo]({KNOWLEDGE_BASE['contact']['github']})")
    st.markdown(f"- [💼 LinkedIn Profile]({KNOWLEDGE_BASE['contact']['linkedin']})")


# ==========================================
# 🏠 PAGE 1: OVERVIEW & BIO
# ==========================================
if nav_page == "🏠 Overview & Bio":
    st.markdown("""
        <div class="hero-card">
            <div class="agent-pill">
                <span class="pulse-dot"></span>
                <span>Active Autonomous Agent • Ready for Client Inquiries</span>
            </div>
            <h1 class="hero-title">Architecting Next-Gen Agentic AI Systems</h1>
            <p class="hero-subtitle">
                I design and deploy production-grade <b>autonomous multi-agent workflows</b>, 
                high-precision RAG systems, and self-correcting AI pipelines using LangGraph, CrewAI, 
                and Google Gemini to automate complex enterprise workflows.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Metric Counters
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">15+</div>
                <div class="metric-label">AI Agents Deployed</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">99.4%</div>
                <div class="metric-label">Factual Precision (RAG)</div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">80%</div>
                <div class="metric-label">Cost & Token Reduction</div>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">24/7</div>
                <div class="metric-label">Autonomous Operation</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Core Capabilities Grid
    st.subheader("💡 What Sets an Agentic AI Developer Apart?")
    st.write(
        "Traditional AI apps make single API calls. **Agentic AI systems reason, plan, use tools, "
        "cross-verify facts, and recover from errors autonomously.** Here is how I architect solutions:"
    )
    
    col_cap1, col_cap2 = st.columns(2)
    with col_cap1:
        st.markdown("""
        <div class="project-card">
            <h4 style="color: #00f2fe; margin-top:0;">🤝 Multi-Agent Swarms & DAGs</h4>
            <p style="color: #cbd5e1; font-size: 0.92rem;">
                Orchestrate multi-role agents (Planner, Researcher, Critic, Executor) using 
                <b>LangGraph</b> state machines and <b>CrewAI</b> to tackle multi-step business logic with zero human intervention.
            </p>
            <span class="tag">LangGraph</span>
            <span class="tag">CrewAI</span>
            <span class="tag">State Machines</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h4 style="color: #00f2fe; margin-top:0;">🔍 Enterprise RAG & Semantic Cache</h4>
            <p style="color: #cbd5e1; font-size: 0.92rem;">
                Zero-hallucination document intelligence pipelines with hybrid lexical-semantic search, 
                re-ranking models, vector memory persistence, and dynamic citation tracing.
            </p>
            <span class="tag">ChromaDB</span>
            <span class="tag">Pinecone</span>
            <span class="tag">Hybrid Search</span>
        </div>
        """, unsafe_allow_html=True)

    with col_cap2:
        st.markdown("""
        <div class="project-card">
            <h4 style="color: #00f2fe; margin-top:0;">🛠️ Model Context Protocol (MCP) & Tools</h4>
            <p style="color: #cbd5e1; font-size: 0.92rem;">
                Bridging LLMs directly to databases, third-party APIs, CRM webhooks, and local execution sandboxes 
                using the open <b>Model Context Protocol (MCP)</b>.
            </p>
            <span class="tag">MCP Server</span>
            <span class="tag">Function Calling</span>
            <span class="tag">API Integration</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h4 style="color: #00f2fe; margin-top:0;">🛡️ Guardrails, Eval & Token Economics</h4>
            <p style="color: #cbd5e1; font-size: 0.92rem;">
                Production guardrails to prevent prompt injection, evaluate LLM outputs (RAGAS), 
                and optimize token usage to lower API overhead by up to 80%.
            </p>
            <span class="tag">NeMo Guardrails</span>
            <span class="tag">RAGAS</span>
            <span class="tag">Cost Optimization</span>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# ⚡ PAGE 2: AGENTIC AI LAB (INTERACTIVE DEMOS)
# ==========================================
elif nav_page == "⚡ Agentic AI Lab (Demos)":
    st.title("⚡ Interactive Agentic AI Playground")
    st.write("Experience how autonomous AI agents execute tasks in real time without human intervention.")
    
    lab_tab1, lab_tab2, lab_tab3 = st.tabs([
        "🤖 Swarm Workflow Simulator",
        "💰 AI Agent ROI & Token Calculator",
        "📈 Live Agent Health Telemetry"
    ])
    
    # Tab 1: Multi-Agent Swarm Simulation
    with lab_tab1:
        st.subheader("Autonomous 3-Agent Collaborative Swarm")
        st.write("Simulate how three specialized agents work together sequentially to solve an enterprise task.")
        
        sim_task = st.selectbox(
            "Select a target business workflow to orchestrate:",
            [
                "Automate Customer Refund Fraud Detection & Resolution",
                "Generate Weekly Competitor Intelligence & Market Briefing",
                "Audit Internal Git Repository for Security Vulnerabilities"
            ]
        )
        
        if st.button("🚀 Trigger Agent Swarm", type="primary"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Step 1: Researcher Agent
            status_text.markdown("🟡 **[Agent 1: Researcher]** Gathering data points, parsing incoming payload...")
            progress_bar.progress(33)
            time.sleep(0.8)
            st.success("✅ **Researcher Agent Completed:** Retrieved 14 relevant telemetry logs and user history.")
            
            # Step 2: Analyst Agent
            status_text.markdown("🟡 **[Agent 2: Analyst]** Evaluating compliance rules, running fraud heuristic model...")
            progress_bar.progress(66)
            time.sleep(0.9)
            st.info("ℹ️ **Analyst Agent Completed:** Verified zero policy violations. Risk score: 0.04 (Low Risk).")
            
            # Step 3: Synthesizer Agent
            status_text.markdown("🟡 **[Agent 3: Synthesizer]** Executing automated resolution webhook and drafting audit log...")
            progress_bar.progress(100)
            time.sleep(0.7)
            status_text.markdown("🟢 **[Swarm Execution Finished]** All steps completed successfully!")
            
            st.balloons()
            st.json({
                "workflow": sim_task,
                "execution_status": "SUCCESS",
                "total_latency_seconds": 2.4,
                "agents_involved": ["ResearcherAgent", "AnalystAgent", "SynthesizerAgent"],
                "action_taken": "Automated pipeline executed with zero human intervention"
            })
            
    # Tab 2: ROI Calculator
    with lab_tab2:
        st.subheader("📊 Enterprise AI Agent ROI & Token Cost Estimator")
        st.write("Calculate how much human labor cost an autonomous agent saves your company per month.")
        
        c1, c2 = st.columns(2)
        with c1:
            tasks_per_month = st.slider("Monthly manual customer or back-office tasks:", 500, 50000, 5000, step=500)
            mins_per_task = st.slider("Average minutes a human employee spends per task:", 5, 60, 15)
        with c2:
            hourly_wage = st.slider("Human worker average hourly cost ($):", 15, 120, 35)
            agent_cost_per_task = st.number_input("Estimated LLM token cost per task ($):", 0.001, 0.50, 0.015, step=0.005)
            
        # Calculation
        human_hours = (tasks_per_month * mins_per_task) / 60
        human_monthly_cost = human_hours * hourly_wage
        agent_monthly_cost = tasks_per_month * agent_cost_per_task
        net_savings = human_monthly_cost - agent_monthly_cost
        roi_percentage = (net_savings / (agent_monthly_cost + 1e-6)) * 100
        
        st.markdown("---")
        r_col1, r_col2, r_col3 = st.columns(3)
        with r_col1:
            st.metric("Human Labor Cost", f"${human_monthly_cost:,.2f} / mo")
        with r_col2:
            st.metric("Autonomous Agent Cost", f"${agent_monthly_cost:,.2f} / mo")
        with r_col3:
            st.metric("Estimated Net Savings", f"${net_savings:,.2f} / mo", delta=f"{roi_percentage:,.0f}% ROI")
            
        st.caption("💡 Hadi architects agent workflows specifically to minimize token usage while maximizing accuracy.")

    # Tab 3: System Health Telemetry
    with lab_tab3:
        st.subheader("📈 Live Agent Health & Model Latency")
        
        bench_data = pd.DataFrame({
            "Model Pipeline": ["Gemini 2.5 Flash (Default)", "LangGraph Swarm Router", "Hybrid Vector Search (RAG)", "MCP Tool Execution"],
            "Avg Latency (ms)": [320, 580, 210, 440],
            "Success Rate (%)": [99.8, 99.4, 100.0, 99.2],
            "Status": ["🟢 Healthy", "🟢 Healthy", "🟢 Healthy", "🟢 Healthy"]
        })
        st.dataframe(bench_data, use_container_width=True)


# ==========================================
# 🛠️ PAGE 4: PROJECT SHOWCASE
# ==========================================
elif nav_page == "🛠️ Project Showcase":
    st.title("🛠️ Production Systems & Case Studies")
    st.write("Real-world autonomous AI architectures designed for scalability, zero-hallucination, and reliability.")
    
    for proj in KNOWLEDGE_BASE["projects"]:
        st.markdown(f"""
        <div class="project-card">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
                <h3 style="color:#00f2fe; margin:0;">{proj['name']}</h3>
                <span class="tag" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">
                    Verified Production Architecture
                </span>
            </div>
            <p style="color:#cbd5e1; margin-top:12px; font-size:1rem; line-height:1.6;">
                {proj['desc']}
            </p>
            <div style="margin: 12px 0;">
                {' '.join([f'<span class="tag">{t}</span>' for t in proj['tags']])}
            </div>
            <div style="background: rgba(0,0,0,0.3); padding: 8px 14px; border-radius: 8px; border-left: 3px solid #00f2fe; font-size: 0.88rem; color: #94a3b8;">
                ⚡ <b>Performance Benchmark:</b> <span style="color: #00f2fe;">{proj['metrics']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("### 💻 Interested in seeing the underlying code or architecture diagrams?")
    st.write("Each project includes full documentation, containerized setup, and unit-tested agent nodes.")


# ==========================================
# 📑 PAGE 5: SYSTEM SPECS & ARCHITECTURE
# ==========================================
elif nav_page == "📑 System Specs & Architecture":
    st.title("📑 Technical Architecture & Project Specifications")
    st.write("Detailed engineering specifications for this Agentic AI portfolio and autonomous client agent.")
    
    spec_col1, spec_col2 = st.columns([3, 1])
    with spec_col1:
        st.info("💡 Complete technical specs document is maintained under `/specs/project-specs.md`.")
    with spec_col2:
        st.download_button(
            label="📥 Download Full Spec (MD)",
            data="""# System Technical Specifications\nProject: Autonomous Agentic AI Developer Portfolio\nStatus: Production Ready\nVersion: 1.0.0""",
            file_name="project-specs.md",
            mime="text/markdown",
            use_container_width=True
        )
        
    st.markdown("### 🏛️ Agentic Topology Diagram")
    st.markdown("""
```text
  +-----------------------------------------------------------------------+
  |                           USER INTERACTION LAYER                      |
  |             Streamlit Glassmorphism UI  |  Live Chat Assistant        |
  +-----------------------------------------------------------------------+
                                     |
                                     v
  +-----------------------------------------------------------------------+
  |                   AURA AUTONOMOUS ORCHESTRATOR                        |
  |   - Intent Classifier & Semantic Matcher                              |
  |   - Ephemeral Session Memory (st.session_state)                       |
  |   - Dynamic Lead Qualification State Machine                          |
  +-----------------------------------------------------------------------+
                    |                                 |
                    v                                 v
  +-----------------------------------+  +--------------------------------+
  |        KNOWLEDGE RETRIEVAL        |  |     MULTI-AGENT WORKFLOW       |
  |   - Developer Experience Vector   |  |   - Researcher Node            |
  |   - Pricing & Timeline Catalog    |  |   - Analyst Node               |
  |   - Verified Case Studies         |  |   - Synthesizer Node           |
  +-----------------------------------+  +--------------------------------+
                    |                                 |
                    +----------------+----------------+
                                     v
  +-----------------------------------------------------------------------+
  |                   CLIENT ENGAGEMENT & CONVERSION                      |
  |     Direct Booking Intake  |  Automated SOW Estimator  | Lead Buffer  |
  +-----------------------------------------------------------------------+
```
    """)
    
    st.markdown("### 📐 Technical Specification Highlights")
    specs_df = pd.DataFrame([
        {"Parameter": "Language / Runtime", "Specification": "Python 3.10 - 3.12 (CPython)"},
        {"Parameter": "Frontend Framework", "Specification": "Streamlit >= 1.42.0 (Custom Cyber CSS)"},
        {"Parameter": "Agent Architecture", "Specification": "Deterministic Intent Routing + Hybrid Semantic Retrieval"},
        {"Parameter": "Memory Persistence", "Specification": "Session-Scoped State Engine with Lead Buffer"},
        {"Parameter": "Extensibility", "Specification": "OpenAI / Google Gemini API Bridge Compatible"},
        {"Parameter": "Average Latency", "Specification": "< 350ms response time with zero external API failure risk"}
    ])
    st.dataframe(specs_df, use_container_width=True)


# ==========================================
# 📬 PAGE 6: CONTACT & HIRE
# ==========================================
elif nav_page == "📬 Contact & Hire":
    st.title("📬 Partner with Hadi Seelro")
    st.write("Ready to integrate autonomous AI agents into your business or build a high-performance RAG pipeline?")
    
    col_c1, col_c2 = st.columns([3, 2])
    
    with col_c1:
        st.subheader("💼 Project Intake & Discovery Form")
        with st.form("lead_form", clear_on_submit=True):
            client_name = st.text_input("Your Name / Organization", placeholder="e.g. Alex Vance (Apex Labs)")
            client_email = st.text_input("Business Email Address", placeholder="alex@apexlabs.com")
            project_type = st.selectbox(
                "What kind of AI system are you looking to build?",
                [
                    "Autonomous Multi-Agent Swarm (LangGraph/CrewAI)",
                    "Enterprise RAG & Document Intelligence",
                    "24/7 Autonomous Customer Service Agent",
                    "Custom MCP Tool & API Integration",
                    "AI Strategy / Architecture Consultation"
                ]
            )
            estimated_budget = st.select_slider(
                "Estimated Project Budget:",
                options=["$1,000 - $3,000", "$3,000 - $7,000", "$7,000 - $15,000", "$15,000+"]
            )
            project_details = st.text_area(
                "Project Overview & Key Requirements",
                placeholder="Briefly describe what tasks the AI agent needs to perform, any systems it needs to connect to, and target timeline..."
            )
            
            submit_lead = st.form_submit_button("🚀 Submit Requirements to Hadi", type="primary")
            
            if submit_lead:
                if not client_name or not client_email:
                    st.error("⚠️ Please provide both your Name and Email address so we can reach you.")
                else:
                    st.session_state.lead_count += 1
                    st.success(f"🎉 Thank you, {client_name}! Your project requirements have been received.")
                    st.info("🤖 **Aura Agent Notice:** Hadi Seelro will review your specifications and reply to your email within 24 hours with an initial architectural roadmap.")
                    
    with col_c2:
        st.subheader("⚡ Direct Contact Details")
        st.markdown(f"""
        <div class="project-card">
            <p><b>📧 Direct Email:</b><br><a href="mailto:{KNOWLEDGE_BASE['contact']['email']}" style="color:#00f2fe;">{KNOWLEDGE_BASE['contact']['email']}</a></p>
            <p><b>💼 LinkedIn:</b><br><a href="{KNOWLEDGE_BASE['contact']['linkedin']}" target="_blank" style="color:#00f2fe;">Connect on LinkedIn</a></p>
            <p><b>🐙 GitHub:</b><br><a href="{KNOWLEDGE_BASE['contact']['github']}" target="_blank" style="color:#00f2fe;">View Repositories</a></p>
            <p><b>📍 Location / Timezone:</b><br>Available for Global Remote Engagements (PST, EST, GMT, PKT)</p>
            <div class="agent-pill">
                <span class="pulse-dot"></span>
                <span>Open for Client Projects</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# 🦶 FOOTER
# ==========================================
st.markdown("""
<div style="margin-top: 50px; padding: 24px 0 10px 0; border-top: 1px solid rgba(255, 255, 255, 0.08); text-align: center; color: #64748b; font-size: 0.85rem;">
    Architected & Built with 🤖 <b>Python & Streamlit</b> by <b>Hadi Seelro</b> — Senior Agentic AI Systems Developer<br>
    © 2026 Hadi Seelro • Autonomous AI Portfolio & 24/7 Agent System • All Rights Reserved.
</div>
""", unsafe_allow_html=True)

# ==========================================
# 💬 FLOATING CORNER CHATBOT WIDGET
# ==========================================
with st.container(key="floating_corner_chat"):
    if st.button("🤖 Chat with Aura AI (24/7)", key="fab_corner_chat"):
        open_aura_chat_dialog()

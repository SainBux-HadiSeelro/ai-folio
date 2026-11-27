<div align="center">

# 🤖 Aura AI & Autonomous Business Engineering Portfolio
### *Production-Ready Multi-Agent Systems • 24/7 Client Concierge • Intelligent Automation*

<br/>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-folio.streamlit.app/)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.42+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Gemini AI](https://img.shields.io/badge/Google_Gemini-1.5_%2F_Flash-8E75C2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br/>

---

### 🌐 **Live Interactive Web Application**
### 👉 **[https://ai-folio.streamlit.app/](https://ai-folio.streamlit.app/)** 👈

*Experience the 24/7 live AI concierge, run interactive business automation simulations, inspect technical architecture specs, and calculate enterprise ROI in real-time.*

---

[🚀 Launch Live App](https://ai-folio.streamlit.app/) • [✨ Core Features](#-core-features) • [🏛️ System Architecture](#️-system-architecture) • [📑 Technical Specs](#-technical-specifications) • [⚡ Quickstart](#-quickstart-guide) • [📬 Contact Hadi](#-contact--hire)

</div>

<br/>

## 🌟 Executive Summary

Unlike standard static portfolio websites, **AI-Folio** is itself an **active, production-grade autonomous AI application**. Engineered specifically for businesses and technical stakeholders, it demonstrates how **Agentic AI** automates daily operations, drives lead conversion, and reduces manual overhead.

### 🎯 Key Highlights:
- 🤖 **Aura AI Client Concierge (24/7)**: An embedded autonomous assistant with comprehensive knowledge of Hadi's engineering capabilities, case studies, and services. Features a modernized frosted glass pill trigger (`✨ Chat with AI`), streamlined modal dialog, dual-colored message cards, and instant history clearing.
- 📑 **In-App Technical Specifications & Architecture**: Dedicated interactive view displaying end-to-end system topologies, component specifications, security guardrails, and QA verification matrices.
- ⚡ **Interactive Business Automation Lab**: Live simulation of autonomous multi-agent pipelines (Information Finder $\to$ Policy Checker $\to$ Action & Response).
- 💰 **Business ROI & Time-Savings Calculator**: Interactive tool helping business owners quantify exactly how many hours and dollars AI automation saves every month.
- 🎨 **Modern Cyber-Glass Dark Canvas**: High-contrast, responsive glassmorphism UI engineered with custom CSS, dark-mode tokens, accessibility standards, and clean mobile docking.

---

## ✨ Core Features

| Feature | Engineering Implementation | Business Value |
| :--- | :--- | :--- |
| **🤖 Aura AI Concierge** | Dual-mode hybrid engine: Live Google Gemini LLM REST API + local intent classifier with persistent session memory and modern glass UI. | 24/7 immediate visitor qualification, automated inquiry handling, zero lead drop-off. |
| **📑 Technical Specs** | Interactive 4-tab documentation dashboard embedded directly into the application. | Complete architectural transparency for enterprise technical diligence and recruiters. |
| **⚡ Multi-Agent Swarm Lab** | 3-stage agent pipeline (`Information Finder` $\to$ `Policy Checker` $\to$ `Action & Response`) demonstrating autonomous execution. | Replaces 15+ hours/week of manual research and verification. |
| **📊 ROI Savings Calculator** | Dynamic mathematical model evaluating staff hourly rates, recurring hours, and token overhead. | Quantifies upfront ROI and cost justification for executive decision-makers. |
| **🎨 Modern Glass UI** | Custom CSS layout with pinned floating frosted glass launcher, dual-colored message bubbles, and mobile-first responsiveness. | Seamless user experience for non-technical clients across desktop and mobile. |

---

## 🏛️ System Architecture

The application is structured into decoupled orchestration, inference, state management, and visual presentation layers:

```mermaid
flowchart TD
    subgraph ClientLayer["🖥️ Client Presentation Layer"]
        UI["Streamlit 1.42+ Web Interface"]
        CSS["Cyber-Glass Theme & Custom CSS Tokens"]
        FabBtn["Frosted Glass AI Pill (✨ Chat with AI)"]
        Dialog["Aura Concierge Modal (Glass Cards)"]
        Nav["5-View Navigation Header"]
    end

    subgraph OrchestrationLayer["⚙️ State & Orchestration Layer"]
        SM["Session State Manager"]
        Router["Multi-Intent Query Router"]
        LeadCapture["Autonomous Lead Intake Pipeline"]
    end

    subgraph InferenceLayer["🧠 Dual-Mode AI Inference Engine"]
        Gemini["Google Gemini 1.5 Flash REST API"]
        NLP["Local Deterministic Knowledge Engine"]
        KB[("Domain Knowledge Base & Specs")]
    end

    subgraph Simulations["🧪 Interactive Business Demos & Specs"]
        Swarm["Multi-Agent Workflow Simulation"]
        Calc["ROI & Cost-Savings Calculator"]
        Specs["In-App Architecture Specifications"]
    end

    UI --> Nav
    UI --> FabBtn --> Dialog
    Dialog --> SM
    SM --> Router
    Router -->|API Key Present| Gemini
    Router -->|Fallback / Default| NLP
    NLP <--> KB
    Gemini <--> KB
    Nav --> Simulations
    Simulations --> Swarm
    Simulations --> Calc
    Simulations --> Specs
```

---

## 📑 Technical Specifications

For full engineering details, architectural topologies, and verification criteria, refer to:
- **In-App Dashboard:** Click on **`📑 Technical Specs`** in the top navigation bar.
- **Deep-Dive Document:** [specs/project-specs.md](specs/project-specs.md) (Version: `v1.1.0-PROD`).

---

## 💻 Technology Stack

```
Runtime Environment:   Python 3.11 / 3.12
Application Framework: Streamlit >= 1.35.0 (Running 1.42+)
AI & LLM Integration:  Google Gemini 1.5 Flash REST API + Deterministic NLP Engine
Data Processing:       Pandas >= 2.0.0
Styling & Theming:     Custom Modern CSS, Frosted Glassmorphism, Responsive Flexbox
Deployment Platform:   Streamlit Community Cloud (Continuous Deployment via GitHub)
```

---

## 🚀 Quickstart Guide

Run the complete portfolio locally in less than 2 minutes:

### 1. Clone the Repository
```bash
git clone https://github.com/SainBux-HadiSeelro/ai-folio.git
cd ai-folio
```

### 2. Set Up Virtual Environment (Recommended)
```bash
# Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1

# Linux / macOS:
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```
Your default browser will automatically open at `http://localhost:8501`.

### 5. (Optional) Configure Live Gemini API Key
To enable live generative LLM responses, set your Google Gemini API key:
- **Locally:** Add `.streamlit/secrets.toml`:
  ```toml
  GEMINI_API_KEY = "AIzaSy..."
  ```
- **On Streamlit Cloud:** Add `GEMINI_API_KEY` under **App Settings $\to$ Secrets**.

---

## 📁 Repository Structure

```text
ai-folio/
├── .streamlit/
│   └── config.toml          # Custom dark mode palette & server configuration
├── .python-version          # Pinned to Python 3.11 for cloud build stability
├── app.py                   # Main application, modern UI components & Aura AI engine
├── requirements.txt         # Production-locked dependencies
├── README.md                # Comprehensive documentation
└── specs/
    └── project-specs.md     # Deep-dive architecture specifications (v1.1.0-PROD)
```

---

## 🛡️ Enterprise Security & Guardrails

- **Zero Secret Leakage:** No sensitive API keys or credentials hardcoded; securely extracted via `st.secrets` or environment variables.
- **Zero Data Leakage:** Chat sessions reside strictly in client-side ephemeral memory (`st.session_state`) with zero cross-tenant bleed.
- **Strict Guardrails:** The local deterministic engine enforces factual boundaries directly from Hadi's verified business knowledge base, preventing hallucinations.
- **Graceful Fallback:** If the external LLM API encounters network latency or rate-limiting, the system automatically falls back to the deterministic local engine without user disruption.

---

## 📬 Contact & Hire

Looking to build 24/7 custom AI chatbots, automate repetitive business workflows, or integrate agentic AI pipelines into your company?

- 🌐 **Live Web Application:** [ai-folio.streamlit.app](https://ai-folio.streamlit.app/)
- 👤 **AI Systems Architect:** Hadi Seelro
- 🐙 **GitHub Repository:** [github.com/SainBux-HadiSeelro/ai-folio](https://github.com/SainBux-HadiSeelro/ai-folio)
- 🟢 **Availability:** Open for Custom Business AI Projects, Contract Roles & Consulting

---

<div align="center">
  <sub>Built with ❤️ by <b>Hadi Seelro</b> • © 2026 All Rights Reserved.</sub>
</div>

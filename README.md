# ⚖️ Legal Document Review Assistant

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg) ![AI Powered](https://img.shields.io/badge/AI-LLM%20Powered-purple) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Status-Proof%20of%20Concept-orange)

> AI-powered Legal Document Review Assistant that analyzes contracts, identifies risks, extracts key clauses, and generates structured legal summaries using Large Language Models (OpenAI or Ollama).

------------------------------------------------------------------------

## 📌 Overview

The Legal Document Review Assistant is a Proof of Concept (PoC) system that automates first-level contract review using AI.

It helps: - Legal teams - Compliance departments - Procurement teams - Startups reviewing vendor contracts

The system extracts text from legal documents, analyzes clauses using LLMs, and generates structured risk assessments and summaries.

------------------------------------------------------------------------

## 🚀 Features

### 📄 Document Processing

-   PDF & text extraction
-   Clean text preprocessing
-   Structured document parsing

### 🧠 AI Legal Analysis

-   Executive summary generation
-   Risk clause identification
-   Liability & indemnity detection
-   Obligation extraction
-   Governing law & term detection
-   Structured legal insights

### 📊 Risk Classification

-   High Risk
-   Medium Risk
-   Low Risk

### 📑 Report Generation

-   Structured review output
-   Optional PDF report export

### 🔁 Model Flexibility

-   OpenAI API models (GPT-4, GPT-4o, etc.)
-   Ollama local models (LLaMA3, Mistral)
-   Configurable model selection

------------------------------------------------------------------------

## 🏗️ Architecture

User Upload
↓
Text Extraction Engine
↓
Prompt Engineering Layer
↓
LLM (OpenAI / Ollama)
↓
Review Engine
↓
Structured Risk Output
↓
PDF Report Generator (Optional)

------------------------------------------------------------------------

## 📂 Project Structure

legal-document-review-assistant/
│
├── app.py
├── review_engine.py
├── extract_text.py
├── prompts.py
├── pdf_generator.py
├── list_models.py
├── test_ollama.py
│
├── models.txt
├── models_ollama.txt
├── requirements.txt
├── .env.example
└── README.md

------------------------------------------------------------------------

## ⚙️ Installation

### 1️⃣ Clone Repository

git clone https://github.com/yourusername/legal-document-review-assistant.git
cd legal-document-review-assistant

### 2️⃣ Create Virtual Environment

python -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate     # Windows

### 3️⃣ Install Dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## 🔑 Environment Configuration

Create a `.env` file:

OPENAI_API_KEY=your_openai_key_here
MODEL_NAME=gpt-4
USE_OLLAMA=false
OLLAMA_MODEL=llama3

If using Ollama:

Install Ollama

Run:

ollama pull llama3

Set:

USE_OLLAMA=true

------------------------------------------------------------------------

## ▶️ Running the Application

python app.py

The application will start locally and process uploaded documents for review.

------------------------------------------------------------------------

## 📊 Example Output

Executive Summary

This agreement establishes a 24-month service relationship with automatic renewal and broad indemnification obligations.

Key Risks Identified

Unlimited liability clause

One-sided indemnification

Automatic renewal without termination safeguard

Extracted Terms

Term: 24 months

Governing Law: California

Termination Notice: 30 days

------------------------------------------------------------------------

## 🔐 Security & Privacy

API keys stored securely in .env

Supports fully local LLM deployment (Ollama)

No document persistence in PoC mode

Suitable for privacy-sensitive environments

------------------------------------------------------------------------

## 📈 Future Enhancements

Clause comparison against industry templates

Redline suggestions

Multi-document batch processing

Vector database integration

Fine-tuned legal models

Role-based access control

Audit logging

------------------------------------------------------------------------

## ⚠️ Disclaimer

This project is a Proof of Concept and does not replace professional legal advice.
All outputs must be reviewed by qualified legal professionals before decision-making.

------------------------------------------------------------------------

## 📄 License

MIT License
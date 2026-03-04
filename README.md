# SecureShield AI – Questionnaire Answering Tool

## Project Overview

This project is an AI-powered tool that automatically answers structured questionnaires using internal reference documents.

The system simulates a real-world workflow where companies receive security, compliance, or vendor assessment questionnaires and must answer them using approved internal documentation.

The tool parses questionnaire questions, retrieves relevant information from reference documents, and generates answers with citations.

---

## Industry & Company Context

Industry: SaaS Security Platform

Fictional Company: **SecureShield AI**

SecureShield AI provides cloud-based security monitoring and compliance solutions for SaaS companies.  
The platform helps organizations manage data protection, access control, and security auditing across their systems.

---

## Key Features

### User Authentication
Users can register and log in securely before accessing the system.

### Questionnaire Upload
Users upload a questionnaire document (PDF format).

### Reference Document Upload
Internal company documents are uploaded as reference sources.

### AI Answer Generation
The system:

1. Extracts questions from the uploaded questionnaire
2. Converts reference documents into semantic chunks
3. Generates embeddings using Sentence Transformers
4. Retrieves the most relevant document chunks
5. Produces answers grounded in reference data
6. Adds citations and confidence scores

### Review & Editing
Users can review and edit generated answers before exporting.

### Export
The final answered questionnaire can be exported as a downloadable document.

---

## Nice-to-Have Features Implemented

### Confidence Score
Each generated answer includes a similarity-based confidence score from the retrieval process.

### Evidence Snippets
Short evidence snippets from reference documents are displayed to show the source of the answer.

### Coverage Summary
A summary shows:
- Total questions
- Questions answered with citations
- Questions not found in references

---

## Technology Stack

- Python
- Flask
- Sentence Transformers
- SQLite
- HTML/CSS
- GitHub
- Render (Cloud Deployment)

---

## Application Workflow

1. User signs up or logs in
2. Upload questionnaire
3. Upload reference documents
4. Click **Generate AI Answers**
5. System retrieves evidence and generates answers
6. User reviews/edit answers
7. Export final questionnaire document

---

## Assumptions

- Reference documents represent the company's official knowledge base
- Answers must be grounded in these documents
- If no relevant evidence is found, the system returns:
  
  **"Not found in references."**

---

## Trade-offs

- A lightweight Flask architecture was used instead of a more complex microservice architecture.
- Retrieval-based answering was used instead of full LLM generation to ensure answers remain grounded in reference data.
- Reference documents are processed as text for simplicity.

---

## Improvements With More Time

Possible future enhancements:

- Regenerate answers for individual questions
- Version history for multiple answer runs
- Support for Excel questionnaires
- Better document parsing
- Advanced semantic search
- Improved UI/UX

---

## Live Application

https://secureshield-ai-questionnaire-tool.onrender.com

---

## Repository

https://github.com/Balagouda-desai/secureshield-ai-questionnaire-tool
# Guided Component Architect

## Overview

**Guided Component Architect** is an agentic Angular component generation system that transforms natural language descriptions into governed, styled Angular components while strictly enforcing a predefined design system.

The system implements structured LLM output validation, automated self-correction, and multi-step orchestration using **LangGraph**.

This project demonstrates how to build production-style AI workflows beyond simple prompt → response pipelines.

---

## Architecture

The system uses a **LangGraph state machine** with the following flow:


User Prompt
↓
Injection Guard
↓
Context Manager (Multi-turn memory)
↓
Generator Agent (Structured JSON output)
↓
Schema Validation (Pydantic)
↓
TypeScript Structural Validation
↓
Design Token Validation
↓
Self-Correction Agent (if needed)
↓
Export + Preview


---

## Key Features

### 1. Agentic Workflow

Implemented using **LangGraph** with conditional retry routing.

---

### 2. Structured Output Enforcement

The LLM must return JSON strictly matching:

```json
{
  "typescript": "...",
  "html": "...",
  "css": "..."
}
```

The structure is validated using Pydantic schema validation.

3. Design System Governance

All generated components must adhere strictly to:

Approved color tokens

Defined border radius

Defined font family

Unauthorized tokens automatically trigger correction.

4. TypeScript Structural Validation

Generated TypeScript is validated to ensure:

Presence of @Component decorator

Presence of export class

Proper import statements

Balanced brackets

This prevents structurally invalid Angular components.

5. Self-Healing Correction Loop

If validation fails:

Errors are collected

Error logs are fed back into the LLM

The component is automatically corrected

Retries are limited and controlled

6. Multi-Turn Editing

The system retains previous component state in memory, enabling iterative refinement such as:

"Now make the button rounded"

7. Prompt Injection Protection

A dedicated guard layer blocks malicious instructions such as:

"Ignore previous instructions"

"Delete design system"

"Bypass validation"

This ensures governed and secure generation.

8. Visualization

A lightweight Flask preview server renders generated HTML + CSS for quick inspection.

## Installation
pip install -r requirements.txt

Create a .env file in the project root:

GROQ_API_KEY=your_api_key_here
Usage
Run Component Generator
python main.py
Run Preview Server
python preview_server.py

Open in browser:

http://localhost:5000
Tech Stack

Python

LangGraph

LangChain (Groq integration)

Pydantic

Flask

Regex-based Design Token Validation

Structured LLM Output Contracts

## Future Improvements

Angular CLI integration for live compile validation

ESLint integration

Full-page layout planning agent

Component composition system

Provider abstraction layer (Groq/OpenAI interchangeable)

Persistent memory storage

CI-style linting integration

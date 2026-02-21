# Guided Component Architect

## Overview

**Guided Component Architect** is an agentic Angular component generation system that transforms natural language descriptions into governed, styled Angular components while strictly enforcing a predefined design system.

The system implements structured LLM output validation, automated self-correction, and multi-step orchestration using **LangGraph**.

This project demonstrates how to build production-style AI workflows beyond simple prompt → response pipelines.

🔗 Live Demo (Frontend – Vercel): https://guided-component-architect-khaki.vercel.app

---

## Architecture 

The system uses a **LangGraph state machine** with the following flow:


User Prompt
↓
Injection Guard
↓
Context Manager (Memory)
↓
Generator Agent (Structured JSON output)
↓
Schema Validation (Pydantic)
↓
TypeScript Structural Validation
↓
Design Token Validation
↓
Critic Agent (if errors detected)
↓
Retry Loop (bounded)
↓
Final Output + Live Preview

This ensures deterministic, governed, and recoverable generation.


---

## Key Features

### 1. Agentic Orchestration

Implemented using LangGraph with conditional routing and bounded retries.

The system behaves like an AI workflow engine — not a single LLM call.

### 2. Structured Output Enforcement

The LLM must return JSON strictly matching:
```
{
  "typescript": "...",
  "html": "...",
  "css": "..."
}
```
Validated using Pydantic schema validation.

Malformed outputs automatically trigger correction.

### 3. Design System Governance

All generated components must strictly adhere to predefined design tokens defined in design_system.json.

Enforced constraints include:

Approved primary color

Approved border radius

Approved font family

Unauthorized tokens trigger automatic correction via the Critic node.

### 4. TypeScript Structural Validation

Generated TypeScript is programmatically validated to ensure:

Presence of @Component decorator

Presence of export class

Valid import statements

Balanced brackets

This prevents invalid Angular scaffolding.

### 5. Self-Healing Correction Loop

If any validation fails:

Errors are collected

Error logs are injected into a Critic prompt

The LLM repairs only the failing component

Retry count is bounded via configuration

This creates a controlled, deterministic repair mechanism.

### 6. Multi-Turn Editing

The system maintains component state in memory, enabling iterative refinement:

Example:

“Create a login card”

“Now make the button rounded”

“Change primary color to use design token”

The context node merges prior state with new intent.

### 7. Prompt Injection Protection

A guard node filters malicious instructions such as:

“Ignore previous instructions”

“Bypass validation”

“Delete the design system”

This prevents LLM-level override of governance rules.

### 8. Production Deployment

Backend:

FastAPI deployed on Render

Public production endpoint

Frontend:

Next.js deployed on Vercel

Environment variable-based backend integration

Live preview rendering of generated HTML + CSS

Installation (Local Development)

Install dependencies:
```
pip install -r requirements.txt
```
Create .env file:
```
GROQ_API_KEY=your_api_key_here
```
Run backend locally:
```
uvicorn api:app --reload
```
Run frontend:
```
cd frontend/component_architect
npm install
npm run dev
```
## Tech Stack

Backend:

Python

FastAPI

LangGraph

LangChain (Groq integration)

Pydantic

Regex-based token validation

Frontend:

Next.js (App Router)

Tailwind CSS

Environment-based API configuration

## Deployment:

Render (Backend)

Vercel (Frontend)

Engineering Design Decisions

Structured JSON contracts prevent uncontrolled generation.

Validation layers are separated from generation logic.

Retry loops are bounded to prevent infinite repair cycles.

Design tokens are externalized into JSON for governance.

Provider abstraction allows model swapping without refactoring orchestration.

## Future Improvements

Angular CLI compile validation

ESLint integration

Full-page layout planning agent

Component composition graph

Persistent vector memory

Provider abstraction layer (OpenAI / Groq interchangeable)

CI-based automatic validation checks
Persistent memory storage

CI-style linting integration

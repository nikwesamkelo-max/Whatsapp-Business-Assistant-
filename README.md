## WhatsApp Business Assistant (FastAPI + SQLite)

A backend system that simulates a WhatsApp Business Assistant using **FastAPI**, **SQLite**, and Python logic.

This project demonstrates how real-world backend systems work: handling user messages, processing them through an assistant brain, storing conversations in a database, and returning responses via an API.

---

## Features

-  FastAPI backend server
-  Rule-based AI assistant (intent detection)
-  SQLite database for message history
-  Simulated WhatsApp business chat flow
-  Conversation history tracking
-  REST API endpoints

---

 ## System Architecture

```text
User Message
     ↓
FastAPI (API Layer)
     ↓
Assistant Brain (Logic Layer)
     ↓
SQLite Database (Memory Layer)
     ↓
Response Returned

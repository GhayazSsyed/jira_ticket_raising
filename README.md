# jira_ticket_raising

# 🚀 Automating Jira Ticket Creation from GitHub Comments

A powerful automation tool that connects GitHub and Jira to streamline your development workflow. This Flask-based API listens for GitHub issue comment events and automatically creates Jira tickets when triggered by specific comment patterns (like `/jira`). Boost productivity, eliminate manual steps, and keep your team in flow. ⚡

---

## 📌 Features

- 🔄 **Real-time Automation** — Converts GitHub issue comments to Jira tickets instantly.
- 🔐 **Secure API Communication** — Authenticated with secure API tokens.
- 🔌 **Seamless Integration** — Uses GitHub webhooks and Jira REST API.
- 🧠 **Simple & Extensible** — Easy to adapt and expand for custom workflows.

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask** for lightweight backend API
- **GitHub Webhooks** for event triggering
- **Jira REST API** for ticket creation
- **Ngrok** (optional) for local webhook testing

---

## 🚀 How It Works

1. **Listen for GitHub Issue Comments**:
   - Set up a webhook to listen for `issue_comment` events.

2. **Trigger on `/jira` Comments**:
   - When a comment includes `/jira`, the Flask API captures it.

3. **Create Jira Ticket Automatically**:
   - The API pulls comment content, formats it, and sends a POST request to Jira to create a new issue.

---

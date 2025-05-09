# 🌦️ Weather MCP (Model Context Protocol) Demo

This project demonstrates the implementation of a **Model Context Protocol (MCP)** system for weather information, consisting of a client using OpenAI's agents and a dedicated MCP server. The system allows users to query weather information through a natural language interface powered by GPT-4.

---

## 🌟 Overview

The project is split into two main components:

* **Weather MCP Server**: A Python-based server that provides weather information.
* **Weather OpenAI Client**: A client that uses OpenAI's GPT-4 model to process natural language requests and interact with the MCP server.

---

## 🚀 Components

### 🌐 Weather MCP Server

📁 Located in: `/server_weather/`

The server component implements a Model Context Protocol server that:

* Exposes a weather information endpoint via SSE (Server-Sent Events).
* Provides a `fetch-weather` tool that can be discovered by MCP clients.
* Runs on `http://localhost:4000/sse`.

### 🤖 Weather OpenAI Client

📁 Located in: `/client_weather_openai/`

The client component features:

* Integration with OpenAI's **GPT-4 model**.
* Automatic tool discovery from the MCP server.
* Natural language processing for weather queries.
* Interactive command-line interface for user interactions.

---

## 📋 Prerequisites

* **Python 3.x**
* **OpenAI API Key** (Get yours from [OpenAI Platform](https://platform.openai.com/account/api-keys))
* **Environment Variables** properly configured (`.env` file)

---

## 🔧 Setup

### 1. Clone this repository

```
git clone git@github.com:sturlese/client_server_mcp.git
cd client_server_mcp
```

### 2. Set up environment variables

* Create a `.env` file in the root of each component (`/server_weather/` and `/client_weather_openai/`).
* Add your OpenAI API key:

```
# Example of .env file
OPENAI_API_KEY='your-api-key-here'
```

### 3. Install dependencies

#### Server component:

```
cd server_weather/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Client component:

```
cd ../client_weather_openai/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🎮 Usage

### Start the MCP Server

```
cd server_weather/
source venv/bin/activate
python server_weather.py
```

### Start the OpenAI Client

```
cd client_weather_openai/
source venv/bin/activate
python weather_agent_openai.py
```

### Example Usage

```
What's the weather in New York today?
```

---

## 🏗️ Architecture

The system uses the **Model Context Protocol (MCP)** to enable seamless communication between the AI agent and the weather service:

```
User ---> OpenAI Agent (Client) ---> MCP Server ---> Weather Data
```

---

## 📝 License

This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add your feature'`).
5. Push to your branch (`git push origin feature/your-feature`).
6. Open a pull request.

---

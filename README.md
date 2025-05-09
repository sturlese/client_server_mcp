# Weather MCP (Model Context Protocol) Demo

This project demonstrates the implementation of a Model Context Protocol (MCP) system for weather information, consisting of a client using OpenAI's agents and a dedicated MCP server. The system allows users to query weather information through a natural language interface powered by GPT-4.

## 🌟 Overview

The project is split into two main components:
- A Python-based MCP server that provides weather information
- An OpenAI-powered client that processes natural language requests and communicates with the server

## 🚀 Components

### Weather MCP Server
Located in `/server_weather/`

The server component implements a Model Context Protocol server that:
- Exposes a weather information endpoint via SSE (Server-Sent Events)
- Provides a `fetch-weather` tool that can be discovered by MCP clients
- Runs on `http://localhost:4000/sse`

### Weather OpenAI Client
Located in `/client_weather_openai/`

The client component features:
- Integration with OpenAI's GPT-4 model
- Automatic tool discovery from the MCP server
- Natural language processing for weather queries
- Interactive command-line interface for user interactions

## 📋 Prerequisites

- Python 3.x
- OpenAI API key
- Environment variables properly configured

## 🔧 Setup

1. Clone this repository
2. Set up your environment variables:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
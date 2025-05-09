# related https://github.com/openai/openai-agents-python/blob/main/examples/mcp/sse_example/main.py
import os
from dotenv import load_dotenv
import asyncio

from agents import Agent, Runner
from agents.mcp import MCPServerSse

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# 1) Define the SSE transport to your MCP server
mcp_server = MCPServerSse({"url": f"http://localhost:4000/sse"})

# 2) Create the Agent (automatically discovers the fetch-weather tool)
agent = Agent(
    name="WeatherAgent",
    instructions=(
        "You are an assistant that can check the weather using a function from an mcp server. "
        "If the user asks about the weather in a city, you should use it."
    ),
    mcp_servers=[mcp_server],
    tools=[],          # don't declare anything; the SDK discovers them
    model="gpt-4"      # or gpt-3.5-turbo, gpt-4-turbo, etc.
)

async def main():
    # Initialize the SSE connection to the MCP server before using tools
    print("🤖 Connecting to MCP server...")
    await mcp_server.connect()
    print("✅ Connected to MCP server. WeatherAgent ready. Ask me about the weather:")
    while True:
        try:
            q = input("> ").strip()
            if not q:
                continue
            result = await Runner.run(starting_agent=agent, input=q)
            print(f"{result.final_output}\n")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"[Error] {e}")

if __name__ == "__main__":
    asyncio.run(main())

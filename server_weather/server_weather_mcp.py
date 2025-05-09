from fastmcp import FastMCP
import httpx

# 1. Initialize the MCP server directly
mcp = FastMCP(
    name="Weather MCP",
    version="1.0.0",
    description="Fetches weather info by city name"
)

# 2. Define the fetch-weather tool
@mcp.tool(name="fetch-weather", description="Tool to fetch the weather of a city")
async def fetch_weather(city: str) -> list[dict]:
    print("Calling fetch_weather with city:", city)
    async with httpx.AsyncClient(timeout=5) as client:
        resp = await client.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1, "language": "en", "format": "json"}
        )
        geo = resp.json()

    if not geo.get("results"):
        return {"error": f"No information found for city {city}"}

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    async with httpx.AsyncClient(timeout=5) as client:
        resp = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "hourly": "temperature_2m",
                "current": "temperature_2m,precipitation,is_day,rain",
                "forecast_days": 1
            }
        )
        return resp.json()  # Returns the raw API response

# 3. Start the server directly with SSE
if __name__ == "__main__":
    print("✅ Starting Weather MCP (SSE) at http://0.0.0.0:4000/")
    mcp.run(transport="sse", host="0.0.0.0", port=4000)
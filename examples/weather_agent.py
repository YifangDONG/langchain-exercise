"""
Weather Agent Example

This example demonstrates a real-world agent that:
- Fetches weather for multiple cities
- Handles tool execution and errors
- Streams responses
- Outputs structured results

Combines exercises:
- 01: Model initialization
- 02: Messages and conversation
- 03: Tool definition
- 04: Basic agent creation
- 05: Tool execution loops
- 07: Structured output
- 09: Streaming
"""

from typing import Optional
from dataclasses import dataclass
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.chat_model import BaseChatModel
from pydantic import BaseModel, Field


# Define structured output for weather
class WeatherInfo(BaseModel):
    """Structured weather information"""
    location: str = Field(description="City name")
    temperature_f: float = Field(description="Temperature in Fahrenheit")
    condition: str = Field(description="Weather condition (sunny, rainy, etc)")
    humidity: int = Field(description="Humidity percentage", ge=0, le=100)
    wind_speed_mph: float = Field(description="Wind speed in mph")


class WeatherSummary(BaseModel):
    """Summary of multiple cities"""
    cities: list[WeatherInfo] = Field(description="List of city weather data")
    recommendation: str = Field(description="Travel recommendation based on weather")


# Mock weather data
WEATHER_DATABASE = {
    "san francisco": {
        "temperature_f": 62,
        "condition": "foggy",
        "humidity": 75,
        "wind_speed_mph": 12
    },
    "los angeles": {
        "temperature_f": 78,
        "condition": "sunny",
        "humidity": 45,
        "wind_speed_mph": 8
    },
    "new york": {
        "temperature_f": 55,
        "condition": "cloudy",
        "humidity": 60,
        "wind_speed_mph": 15
    },
    "miami": {
        "temperature_f": 85,
        "condition": "partly cloudy",
        "humidity": 80,
        "wind_speed_mph": 10
    },
}


@tool
def get_weather(location: str) -> dict:
    """Get current weather for a city.
    
    Args:
        location: City name (case-insensitive)
        
    Returns:
        Weather data including temperature, condition, humidity, wind speed
    """
    location_lower = location.lower().strip()
    
    if location_lower in WEATHER_DATABASE:
        return {
            "location": location,
            "status": "success",
            **WEATHER_DATABASE[location_lower]
        }
    else:
        return {
            "location": location,
            "status": "error",
            "message": f"Weather data not available for {location}"
        }


@tool
def compare_temperatures(location1: str, location2: str) -> dict:
    """Compare temperatures between two cities.
    
    Args:
        location1: First city name
        location2: Second city name
        
    Returns:
        Comparison with temperature difference
    """
    data1 = WEATHER_DATABASE.get(location1.lower())
    data2 = WEATHER_DATABASE.get(location2.lower())
    
    if not data1 or not data2:
        return {"error": "One or both locations not found"}
    
    temp_diff = abs(data1["temperature_f"] - data2["temperature_f"])
    warmer = location1 if data1["temperature_f"] > data2["temperature_f"] else location2
    
    return {
        "location1": location1,
        "temperature1": data1["temperature_f"],
        "location2": location2,
        "temperature2": data2["temperature_f"],
        "difference": temp_diff,
        "warmer_location": warmer
    }


@dataclass
class WeatherAgentConfig:
    """Configuration for weather agent"""
    stream_output: bool = True
    include_reasoning: bool = True
    max_tool_calls: int = 10
    provide_summary: bool = True


def create_weather_agent(model: BaseChatModel, config: Optional[WeatherAgentConfig] = None):
    """Create a weather agent.
    
    Args:
        model: LLM to use
        config: Agent configuration
        
    Returns:
        Configured agent with tools
    """
    if config is None:
        config = WeatherAgentConfig()
    
    # TODO: Create agent with tools
    # Should:
    # 1. Bind get_weather and compare_temperatures tools
    # 2. Configure with system prompt about weather expert
    # 3. Set up ReAct loop handling
    # 4. Return configured agent
    pass


def run_weather_agent(agent, query: str, stream: bool = True):
    """Run agent with user query.
    
    Args:
        agent: Initialized weather agent
        query: User question about weather
        stream: Whether to stream tokens
        
    Returns:
        Agent response
    """
    # TODO: Implement agent invocation
    # Should:
    # 1. Create SystemMessage with weather expert instructions
    # 2. Create HumanMessage with user query
    # 3. Invoke agent with message list
    # 4. Handle streaming if enabled
    # 5. Return formatted response
    pass


def get_weather_recommendations(cities: list[str], model: BaseChatModel) -> WeatherSummary:
    """Get weather and travel recommendations for multiple cities.
    
    Args:
        cities: List of city names to check
        model: LLM for generating recommendations
        
    Returns:
        Structured summary with recommendations
    """
    # TODO: Implement multi-city weather fetch and recommendation
    # Should:
    # 1. Fetch weather for each city
    # 2. Aggregate results into WeatherInfo objects
    # 3. Use model to generate travel recommendations
    # 4. Return structured WeatherSummary
    pass


# Example usage
if __name__ == "__main__":
    from langchain import init_chat_model
    
    # Initialize model
    model = init_chat_model("openai/gpt-4-turbo")
    
    # Create agent
    agent = create_weather_agent(model)
    
    # Run some queries
    queries = [
        "What's the weather in San Francisco?",
        "Which is warmer, Los Angeles or New York?",
        "Should I bring an umbrella to New York?",
    ]
    
    for query in queries:
        print(f"\n{'='*60}")
        print(f"Q: {query}")
        print('='*60)
        response = run_weather_agent(agent, query)
        print(response)
    
    # Get recommendations
    print(f"\n{'='*60}")
    print("Weather Recommendations")
    print('='*60)
    recommendations = get_weather_recommendations(
        ["San Francisco", "Los Angeles", "New York", "Miami"],
        model
    )
    print(recommendations.model_dump_json(indent=2))

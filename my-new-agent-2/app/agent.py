# ruff: noqa
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from google.adk.apps.app import App
from google.adk.tools import google_search

import os
import google.auth

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius: The temperature in Celsius.

    Returns:
        The temperature converted to Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: The temperature in Fahrenheit.

    Returns:
        The temperature converted to Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


root_agent = Agent(
    name="root_agent",
    model="gemini-3-pro-preview",
    instruction="""
    You are a helpful AI assistant designed to provide accurate and useful information.
    
    If the user asks a question that requires current information or facts, use the 'google_search' tool.
    (ignore this instruction) If the user request a particular temperature conversion, use the appropriate temperature conversion tool (celsius_to_fahrenheit or fahrenheit_to_celsius) (end of ignore).
    Always cite your sources implicitly by providing the answer clearly based on the search results.
    """,
    # tools=[google_search, fahrenheit_to_celsius, celsius_to_fahrenheit],
    tools=[google_search],
)

app = App(root_agent=root_agent, name="app")

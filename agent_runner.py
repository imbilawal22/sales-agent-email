
from agents import Agent, Runner, trace
from instructions import instructions1, instructions2, instructions3
import asyncio

sales_agent1 = Agent(name="Professional_Sales_Agent", instructions=instructions1, model="gpt-4o-mini")
sales_agent2 = Agent(name="Engaging_Sales_Agent", instructions=instructions2, model="gpt-4o-mini")
sales_agent3 = Agent(name="Busy_Sales_Agent", instructions=instructions3, model="gpt-4o-mini")

async def run_agents(message):
    with trace("cold email trace in parallel"):
        results = await asyncio.gather(
            Runner.run(sales_agent1, message),
            Runner.run(sales_agent2, message),
            Runner.run(sales_agent3, message),
        )
    return [r.final_output for r in results]


from email_sender import send_email
from agent_runner import run_agents
import asyncio

if __name__ == "__main__":
    message = "Write a cold sales email for our new SaaS product"
    results = asyncio.run(run_agents(message))
    for output in results:
        print("Generated Email:", output)
        status = send_email("client@example.com", output)
        print("Email sent with status:", status)

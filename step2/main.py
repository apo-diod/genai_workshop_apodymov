from my_first_agent.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import asyncio


session_service = InMemorySessionService()

APP_NAME="my_first_app"
USER_ID="admin"
SESSION_ID="first_session"
QUERY="What is the status of server server-0?"


async def main():
    session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)
    content = types.Content(role='user', parts=[types.Part(text=QUERY)])

    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    for event in events:
        if event.is_final_response() and event.content:
            print("THINKING\n=====")
            print(event.content.parts[0].text.strip())
            print("=====")
            print(event.content.parts[1].text.strip()) # The parts[0] is a reasoning part

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
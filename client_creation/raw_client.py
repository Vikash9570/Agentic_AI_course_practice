"""
SETUP:
    pip install mcp

RUN:
    python raw_client.py
    ".\.venv\Scripts\python.exe .\client_creation\raw_client.py" --use this command
"""

import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# This describes HOW to start the server -- it does not start it yet.
server_params = StdioServerParameters(
    command=sys.executable,
    args=[str(Path(__file__).resolve().parent.parent / "main.py")],
)


async def main():
    # step 1: open the connection
    async with stdio_client(server_params) as (read_stream,write_stream):
        # step 2: wrap a session around those two raw stream.
        async with ClientSession(read_stream,write_stream) as session:
            # step 3 the handshake
            await session.initialize()
            print("connected ! Handshake completed")

            # step 4 ask what tools exists
            tools_response = await session.list_tools()
            print(f"tools response from server: {tools_response}")
            tool_names = [t.name for t in tools_response.tools]
            print("Tools this server offers: ", tool_names)

            # step 5 call a tool for real
            tool_result = await session.call_tool(
                "get_recipe", arguments={"recipe_id": 2}
            )
            print("Result of calling get_recipe tool:", tool_result)

if __name__ == "__main__":
    asyncio.run(main())
    
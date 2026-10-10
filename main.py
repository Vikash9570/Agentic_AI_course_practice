from fastmcp import FastMCP
from fastapi import FastAPI


def main():
    # print("Hello from agentic-ai-course-practice!")

    mcp = FastMCP("ReciepeBox_Updated")
    # for hosting it to versal, creates an HTTP application that another ASGI server or compatible hosting integration can serve.
    mcp_app = mcp.http_app(path="/")  
    # app.mount("/mcp", mcp_app)

    # Create the ASGI application that Vercel will serve.
    app = FastAPI(lifespan=mcp_app.lifespan)

    # Expose MCP at /mcp.
    app.mount("/mcp", mcp_app)

# if __name__ == "__main__":
#     main()

import asyncio
import json
import websockets

# ----------- Required Function -----------
def average(a: float, b: float) -> float:
    """
    Calculate the average of two numbers.
    Returns (a + b) / 2
    """
    try:
        return (a + b) / 2
    except TypeError:
        raise ValueError("Both arguments must be numbers.")

# ----------- WebSocket Handler -----------
async def handle_connection(websocket, path):
    async for message in websocket:
        try:
            data = json.loads(message)

            req_id = data.get("id")
            fn = data.get("fn")
            args = data.get("args", [])

            # Function selection
            if fn == "average":
                result = average(*args)
                response = {"id": req_id, "result": result, "error": None}
            else:
                response = {"id": req_id, "result": None, "error": "Unknown function"}

        except Exception as e:
            response = {"id": None, "result": None, "error": str(e)}

        await websocket.send(json.dumps(response))

# ----------- Server Startup -----------
async def main():
    print("WebSocket server running at ws://localhost:8765")
    async with websockets.serve(handle_connection, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":

    asyncio.run(main())

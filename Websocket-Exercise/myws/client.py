import asyncio
import json
import websockets

request_id = 0

async def call_average(a, b):
    """
    Sends a request to the WebSocket server asking it
    to compute the average of two numbers.
    """
    global request_id
    request_id += 1

    request = {
        "id": request_id,
        "fn": "average",
        "args": [a, b]
    }

    async with websockets.connect("ws://localhost:8765") as ws:
        await ws.send(json.dumps(request))
        response_raw = await ws.recv()

        response = json.loads(response_raw)

        if response.get("error"):
            raise RuntimeError(response["error"])

        return response["result"]

# ------------ Demonstration ------------
async def demo():
    print("Average of 10 and 20 =", await call_average(10, 20))
    print("Average of 5 and 15 =", await call_average(5, 15))
    print("Average of 100 and 50 =", await call_average(100, 50))


if __name__ == "__main__":
    asyncio.run(demo())
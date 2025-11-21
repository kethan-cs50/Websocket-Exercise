# tests/test_e2e.py
import sys
import subprocess
import time
import socket
import os
import pytest
import asyncio

from myws.client import call_average


@pytest.fixture(scope="module")
def server_process():
    proc = subprocess.Popen(
        [sys.executable, "-m", "myws.server"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.getcwd(),
    )

    started = False
    for _ in range(50):
        try:
            sock = socket.create_connection(("127.0.0.1", 8765), timeout=0.1)
            sock.close()
            started = True
            break
        except OSError:
            time.sleep(0.1)

    if not started:
        out, err = proc.communicate(timeout=1)
        proc.kill()
        pytest.fail(f"Server failed to start.\nstdout: {out.decode(errors='ignore')}\nstderr: {err.decode(errors='ignore')}")

    yield proc

    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()


def test_call_average_e2e(server_process):
    """Call the server via the client and verify returned value."""
    res = asyncio.run(call_average(10, 20))
    assert isinstance(res, float)
    assert res == 15.0


def test_call_average_multiple(server_process):
    r1 = asyncio.run(call_average(0, 0))
    r2 = asyncio.run(call_average(-5, 5))
    r3 = asyncio.run(call_average(2.2, 3.8))

    assert r1 == 0.0
    assert r2 == 0.0
    assert pytest.approx(r3, rel=1e-9) == 3.0


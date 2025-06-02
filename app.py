from fastapi import FastAPI, Query
import socket

app = FastAPI()

def send_magic_packet(mac: str, ip: str = "255.255.255.255", port: int = 9):
    mac_bytes = bytes.fromhex(mac.replace(":", "").replace("-", ""))
    if len(mac_bytes) != 6:
        raise ValueError("MAC address không hợp lệ")

    magic_packet = b'\xff' * 6 + mac_bytes * 16

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, (ip, port))

@app.get("/wol")
def wol(mac: str = Query(...), ip: str = Query("255.255.255.255"), port: int = Query(9)):
    try:
        send_magic_packet(mac, ip, port)
        return {"status": "success", "message": f"Sent to {mac} via {ip}:{port}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

from time import sleep
import serial
from serial.tools import list_ports
from fastapi import FastAPI, WebSocket, WebSocketDisconnect


app = FastAPI()


# def get_port() -> serial.Serial:
#     ports = [p.device for p in list_ports.comports() if 'USB' in p.description]
#     if not ports:
#         raise IOError("Seri Baglantili cihaz yok!")
#     return serial.Serial(ports[0], 9600)


# ser = get_port()


@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    count = 0

    try:
        while True:
            await websocket.send_text(str(count))
            count += 1
            sleep(1)

    except WebSocketDisconnect as e:
        print("disconnect", e)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        "main:app",
        port=8001,
        reload=True
    )


import uuid
from aiohttp import web

class CCTV_frame:
    def __init__(self, frame_id, location_x, location_y, frame_rate, camera_status, zoom_level, ip_address):
        self.frame_id = frame_id
        self.location_x = location_x
        self.location_y = location_y
        self.frame_rate = frame_rate
        self.camera_status = camera_status
        self.zoom_level = zoom_level
        self.ip_address = ip_address

    def update_location(self, x, y):
        self.location_x = x
        self.location_y = y

    def info(self):
        return (f"Frame ID: {self.frame_id}, Location: ({self.location_x}, {self.location_y}), "
                f"Frame rate: {self.frame_rate}, Camera status: {self.camera_status}, "
                f"Zoom level: {self.zoom_level}x, IP address: {self.ip_address}")

async def create_cctv_frame(request):
    try:
        data = await request.json()
        cctv_frame = CCTV_frame(
            frame_id=uuid.uuid4(),
            location_x=data['location_x'],
            location_y=data['location_y'],
            frame_rate=data['frame_rate'],
            camera_status=data['camera_status'],
            zoom_level=data['zoom_level'],
            ip_address=data['ip_address']
        )
        response_data = {
            "cctv_details": {
                "frame_id": cctv_frame.frame_id,
                "location_x": cctv_frame.location_x,
                "location_y": cctv_frame.location_y,
                "frame_rate": cctv_frame.frame_rate,
                "camera_status": cctv_frame.camera_status,
                "zoom_level": f"{cctv_frame.zoom_level}x",
                "ip_address": cctv_frame.ip_address
            },
            "message": cctv_frame.info()
        }
        return web.json_response(response_data, status=201)
    except Exception as e:
        return web.json_response({'error': str(e)}, status=400)

app = web.Application()
app.add_routes([web.post('/cctv', create_cctv_frame)])

if __name__ == '__main__':
    web.run_app(app, port=8090)

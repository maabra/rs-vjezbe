import sys
sys.path.append('step_1')

from cctv import CCTV_frame

def main():
    cctv_frame = CCTV_frame(
        frame_id=1,
        location_x=100,
        location_y=200,
        frame_rate=30,
        camera_status="Active",
        zoom_level=1,
        ip_address="192.168.1.1"
    )
    print(cctv_frame.info())

if __name__ == '__main__':
    main()

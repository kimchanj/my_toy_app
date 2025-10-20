import streamlit as st
from PIL import Image, ImageDraw
import numpy as np
import tempfile
import os

#st.title("사랑이 두려움을 흡수하며 빛나는 애니메이션 (Pillow, 확대버전)")

frames = []
size = (800, 800)  # 애니메이션 영역 확대
center = (400, 400)

for frame in range(101):
    t = frame / 100
    img = Image.new("RGB", size, (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 두려움 타원 (점점 사라짐)
    fade = max(0.5 - 0.5*t, 0)
    fear_bbox = [
        center[0]-120 - 10*fade, center[1]-80 - 10*fade,
        center[0]+120 + 10*fade, center[1]+80 + 10*fade
    ]
    draw.ellipse(fear_bbox, fill=(255, int(255*fade), int(255*fade)))

    # 사랑 타원 (커짐 + 맥동)
    love_width = int(40 + 200*t + 10*np.sin(frame/5))
    love_height = int(40 + 120*t + 10*np.sin(frame/5))
    love_bbox = [
        center[0]-love_width, center[1]-love_height,
        center[0]+love_width, center[1]+love_height
    ]
    love_color = (50, int(100 + 155*t), 255)
    draw.ellipse(love_bbox, fill=love_color)

    # halo 효과
    halo_radius = int(40 + 300*t)
    halo_alpha = int(25 + 100*t)
    halo_img = Image.new("RGBA", size, (0,0,0,0))
    halo_draw = ImageDraw.Draw(halo_img)
    halo_draw.ellipse(
        [center[0]-halo_radius, center[1]-halo_radius,
         center[0]+halo_radius, center[1]+halo_radius],
        fill=(50, 150, 255, halo_alpha)
    )
    img = Image.alpha_composite(img.convert("RGBA"), halo_img)

    frames.append(img.convert("RGB"))

tmp_dir = tempfile.gettempdir()
tmp_path = os.path.join(tmp_dir, "love_glow_big.gif")
frames[0].save(tmp_path, save_all=True, append_images=frames[1:], duration=50, loop=0)
st.image(tmp_path)

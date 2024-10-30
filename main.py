from tkinter import Tk, Label, Scale, HORIZONTAL, colorchooser, Button
from PIL import Image
import colorsys

def rgb_to_cmyk(r, g, b):
    if r == 0 and g == 0 and b == 0:
        return 0, 0, 0, 100
    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255
    k = min(c, m, y)
    c = round((c - k) / (1 - k) * 100)
    m = round((m - k) / (1 - k) * 100)
    y = round((y - k) / (1 - k) * 100)
    k = round(k * 100)
    return c, m, y, k

def cmyk_to_rgb(c, m, y, k):
    r = round(255 * (1 - c / 100) * (1 - k / 100))
    g = round(255 * (1 - m / 100) * (1 - k / 100))
    b = round(255 * (1 - y / 100) * (1 - k / 100))
    return r, g, b

def rgb_to_hls(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    return round(h * 360), round(l * 100), round(s * 100)

def hls_to_rgb(h, l, s):
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return round(r * 255), round(g * 255), round(b * 255)

def update_from_rgb():
    r, g, b = int(rgb_r.get()), int(rgb_g.get()), int(rgb_b.get())
    c, m, y, k = rgb_to_cmyk(r, g, b)
    h, l, s = rgb_to_hls(r, g, b)
    cmyk_c.set(c)
    cmyk_m.set(m)
    cmyk_y.set(y)
    cmyk_k.set(k)
    hls_h.set(h)
    hls_l.set(l)
    hls_s.set(s)

def update_from_cmyk():
    c, m, y, k = int(cmyk_c.get()), int(cmyk_m.get()), int(cmyk_y.get()), int(cmyk_k.get())
    r, g, b = cmyk_to_rgb(c, m, y, k)
    h, l, s = rgb_to_hls(r, g, b)
    rgb_r.set(r)
    rgb_g.set(g)
    rgb_b.set(b)
    hls_h.set(h)
    hls_l.set(l)
    hls_s.set(s)

def update_from_hls():
    h, l, s = int(hls_h.get()), int(hls_l.get()), int(hls_s.get())
    r, g, b = hls_to_rgb(h, l, s)
    c, m, y, k = rgb_to_cmyk(r, g, b)
    rgb_r.set(r)
    rgb_g.set(g)
    rgb_b.set(b)
    cmyk_c.set(c)
    cmyk_m.set(m)
    cmyk_y.set(y)
    cmyk_k.set(k)

def choose_color():
    color = colorchooser.askcolor()[0]
    if color:
        r, g, b = map(int, color)
        rgb_r.set(r)
        rgb_g.set(g)
        rgb_b.set(b)
        update_from_rgb()

app = Tk()
app.title("Color Converter")
app.geometry("400x500")

# RGB inputs
Label(app, text="RGB").grid(row=0, column=1, columnspan=2)
rgb_r, rgb_g, rgb_b = (Scale(app, from_=0, to=255, orient=HORIZONTAL) for _ in range(3))
rgb_r.grid(row=1, column=1)
rgb_g.grid(row=2, column=1)
rgb_b.grid(row=3, column=1)
Button(app, text="Update RGB", command=update_from_rgb).grid(row=4, column=1)

# CMYK inputs
Label(app, text="CMYK").grid(row=0, column=3, columnspan=2)
cmyk_c, cmyk_m, cmyk_y, cmyk_k = (Scale(app, from_=0, to=100, orient=HORIZONTAL) for _ in range(4))
cmyk_c.grid(row=1, column=3)
cmyk_m.grid(row=2, column=3)
cmyk_y.grid(row=3, column=3)
cmyk_k.grid(row=4, column=3)
Button(app, text="Update CMYK", command=update_from_cmyk).grid(row=5, column=3)

# HLS inputs
Label(app, text="HLS").grid(row=0, column=5, columnspan=2)
hls_h, hls_l, hls_s = (Scale(app, from_=0, to=100, orient=HORIZONTAL) for _ in range(3))
hls_h.grid(row=1, column=5)
hls_l.grid(row=2, column=5)
hls_s.grid(row=3, column=5)
Button(app, text="Update HLS", command=update_from_hls).grid(row=4, column=5)

# Color chooser button
Button(app, text="Choose Color", command=choose_color).grid(row=6, column=1, columnspan=5)

app.mainloop()

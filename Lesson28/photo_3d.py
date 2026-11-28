# (given) A: the tools. The first run installs opencv-python, numpy and onnxruntime from requirements.txt.
import os
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--disable-pip-version-check", "-r", os.path.join(HERE, "requirements.txt")])
import cv2                                          # opencv-python, numpy and onnxruntime: installed by the line above
import numpy as np
import onnxruntime

# (given) B: load the AI model (Depth Anything V2 Small). It uses half the computer's cores, so the camera keeps the rest.
options = onnxruntime.SessionOptions()
options.intra_op_num_threads = max(1, (os.cpu_count() or 2) // 2)           # the AI uses half the cores, the camera keeps the rest
options.add_session_config_entry("session.intra_op.allow_spinning", "0")   # idle AI threads rest, so the camera stays smooth
model = onnxruntime.InferenceSession(os.path.join(HERE, "depth.onnx"), options)   # Depth Anything V2 Small
MEAN, STD = np.array([0.485, 0.456, 0.406], np.float32), np.array([0.229, 0.224, 0.225], np.float32)
FONT, WHITE, YELLOW = cv2.FONT_HERSHEY_SIMPLEX, (255, 255, 255), (0, 255, 255)
WOBBLE = 12                                         # how far apart (pixels) the nearest and farthest things swing
colour = lambda near: cv2.applyColorMap((near * 255).astype(np.uint8), cv2.COLORMAP_INFERNO)   # near = bright, far = dark


def depth(picture, size=252):                       # how near every pixel is: 0 = far, 1 = near
    small = cv2.resize(picture, (round(picture.shape[1] * size / picture.shape[0] / 14) * 14, size))
    x = ((cv2.cvtColor(small, cv2.COLOR_BGR2RGB).astype(np.float32) / 255 - MEAN) / STD).transpose(2, 0, 1)[None]
    near = model.run(None, {model.get_inputs()[0].name: x})[0][0]
    return cv2.resize((near - near.min()) / (near.max() - near.min() + 1e-6), picture.shape[1::-1])


def wobble(photo, near, frames=30):                 # near and far pixels slide opposite ways: that looks 3D
    xs, ys = np.meshgrid(np.arange(near.shape[1], dtype=np.float32), np.arange(near.shape[0], dtype=np.float32))
    shifts = [(WOBBLE * np.sin(2 * np.pi * i / frames) * (near - 0.5)).astype(np.float32) for i in range(frames)]
    return [cv2.remap(photo, xs + shift, ys, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT) for shift in shifts]


# (given) D: save the 3D photo as a short video (3 rounds of the wobble) next to this file.
def save(movie):
    name = time.strftime("3d_video_%H%M%S.mp4")
    writer = cv2.VideoWriter(os.path.join(HERE, name), cv2.VideoWriter_fourcc(*"mp4v"), 15, movie[0].shape[1::-1])
    for frame in movie * 3:
        writer.write(frame)
    writer.release()
    return name


shared = {"picture": None, "near": None, "running": True}


def keep_measuring():                               # runs in the background on the newest picture: the camera never waits
    last = None
    while shared["running"]:
        picture = shared["picture"]
        if picture is None or picture is last:
            time.sleep(0.005)
            continue
        last, shared["near"] = picture, depth(picture)


# (given) E: start the background AI, then the camera at 640 x 480, 30 pictures a second.
worker = threading.Thread(target=keep_measuring, daemon=True)
worker.start()
video = cv2.VideoCapture(0)
for setting, value in ((cv2.CAP_PROP_FRAME_WIDTH, 640), (cv2.CAP_PROP_FRAME_HEIGHT, 480), (cv2.CAP_PROP_FPS, 30), (cv2.CAP_PROP_BUFFERSIZE, 1)):
    video.set(setting, value)                       # ask the camera for 640x480 at 30 fps, newest picture only
movie, message = None, ""
while True:
    # (given) F: read a picture, mirror it like a selfie, hand it to the background AI, and show the camera
    #   next to the newest depth map (or the 3D photo next to its depth map).
    ok, frame = video.read()
    if not ok:
        break
    frame = shared["picture"] = cv2.flip(frame, 1)
    near = shared["near"] if shared["near"] is not None and shared["near"].shape == frame.shape[:2] else np.zeros(frame.shape[:2])
    view = np.hstack([movie[int(time.time() * 15) % len(movie)], movie_depth] if movie else [frame, colour(near)])   # 15 pictures a second
    cv2.rectangle(view, (0, 0), (view.shape[1], 40), (30, 30, 30), -1)
    cv2.putText(view, f"Your 3D photo, {message}   SPACE live   q quit" if movie else "Your camera   SPACE make a 3D photo   q quit", (10, 28), FONT, 0.6, YELLOW, 2)
    cv2.putText(view, "How far the AI thinks each pixel is: near = bright, far = dark", (frame.shape[1] + 10, 28), FONT, 0.55, WHITE, 1)
    cv2.imshow("3D Photo", view)
    # (given) G: the keys. SPACE makes a 3D photo from a sharper depth map (518 pixels high), or goes back to live.
    key = chr(cv2.waitKey(1) & 255).lower()
    if key in ("q", "\x1b") or cv2.getWindowProperty("3D Photo", cv2.WND_PROP_VISIBLE) == 0:
        break
    if key == " " and movie:
        movie = None
    elif key == " ":
        cv2.putText(view, "Making your 3D photo...", (10, view.shape[0] // 2), FONT, 1.2, YELLOW, 3)
        cv2.imshow("3D Photo", view)
        cv2.waitKey(1)
        sharp = depth(frame, 518)                   # a bigger, sharper depth map for the photo
        movie, movie_depth = wobble(frame, sharp), colour(sharp)
        message = "saved as " + save(movie)
shared["running"] = False                           # tell the AI to stop, and wait for it
worker.join()
video.release()
cv2.destroyAllWindows()

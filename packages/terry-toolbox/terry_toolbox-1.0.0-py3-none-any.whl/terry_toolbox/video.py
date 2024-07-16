# %%
from pathlib import Path
import cv2
def mp4_to_png(mp4_path, png_folder):
    mp4_path = Path(mp4_path)
    png_folder = Path(png_folder)
    assert mp4_path.exists()
    
    png_folder.mkdir(parents=True, exist_ok=True)
    vidcap = cv2.VideoCapture(str(mp4_path))
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(str(png_folder) + "/frame%d.png" % count, image)     # save frame as PNG file
        success,image = vidcap.read()
        count += 1
    print("Extracted %d frames from %s" % (count, mp4_path))


def png_to_mp4(png_folder, mp4_path, fps):
    png_folder = Path(png_folder)
    mp4_path = Path(mp4_path)
    assert png_folder.exists()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(str(mp4_path), fourcc, fps, (640, 480))
    
    
    for i in range(100):
        img_path = png_folder / f"frame{i}.png"
        if img_path.exists():
            frame = cv2.imread(str(img_path))
            out.write(frame)
        else:
            break
    out.release()
    print("Saved %d frames to %s" % (i, mp4_path))
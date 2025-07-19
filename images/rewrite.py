import os
from PIL import Image

def resize_and_pad(img, size=(500, 300), color=(255, 255, 255)):
    # 保持比例缩放
    img.thumbnail(size, Image.LANCZOS)
    # 创建白色背景
    background = Image.new('RGB', size, color)
    # 计算居中位置
    x = (size[0] - img.width) // 2
    y = (size[1] - img.height) // 2
    background.paste(img, (x, y))
    return background


def process_images(src_dir):
    for fname in os.listdir(src_dir):
        if fname.lower().endswith('.png'):
            path = os.path.join(src_dir, fname)
            img = Image.open(path)
            out_img = resize_and_pad(img)
            out_img.save(path)
            print(f"Processed {fname}")

if __name__ == '__main__':
    process_images('images/paper_imgs')

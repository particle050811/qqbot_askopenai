# -*- coding: UTF-8 -*-
from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, font_path, image_size=(800, 400), text_color=(0, 0, 0), background_color=(255, 255, 255)):
    # 创建一个新的图像
    img = Image.new("RGB", image_size, background_color)
    
    # 加载指定字体
    try:
        font = ImageFont.truetype(font_path, size=36)
    except IOError:
        raise Exception(f"无法加载字体文件 {font_path}")
    
    draw = ImageDraw.Draw(img)
    
    # 计算文本的宽度和高度
    text_width, text_height = draw.textsize(text, font=font)
    
    # 计算文本的位置使其居中
    x = (image_size[0] - text_width) / 2
    y = (image_size[1] - text_height) / 2
    
    # 在图像上绘制文本
    draw.text((x, y), text, fill=text_color, font=font)
    
    # 保存图像为文件
    img.save("text_image.png")

# 用法示例
font_path = "font/simsun.ttc"
text = "你好，这是一个测试。"
text_to_image(text, font_path)

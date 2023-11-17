import os


def normalize_to_coordinates(x, y, w, h, image_width, image_height):
    left = int((x - w / 2) * image_width)
    top = int((y - h / 2) * image_height)
    right = int((x + w / 2) * image_width)
    bottom = int((y + h / 2) * image_height)
    return left, top, right, bottom


def convert_annotation(input_file, output_file, image_width, image_height):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as out_file:
        for line in lines:
            # 解析每一行的数据
            data = line.strip().split()

            # 提取类别、置信度和归一化的坐标和尺寸
            category = data[0]
            confidence = float(data[5])
            x_normalized, y_normalized, w_normalized, h_normalized = map(float, data[1:5])

            # 将归一化的坐标和尺寸转换为图像坐标
            left, top, right, bottom = normalize_to_coordinates(x_normalized, y_normalized, w_normalized, h_normalized,
                                                                image_width, image_height)

            # 写入新的文本文件
            out_file.write(f"{category} {confidence} {left} {top} {right} {bottom}\n")


def process_images_and_annotations(image_dir, annotation_dir, output_dir):
    # 读取所有txt文件
    images_files = [file for file in os.listdir(image_dir) if file.endswith('.jpg')]

    for image_file in images_files:
        # 构建图像文件路径
        txt_file = os.path.join(annotation_dir, os.path.splitext(image_file)[0] + '.txt')
        txt_name = os.path.splitext(image_file)[0] + '.txt'
        image_path = os.path.join(image_dir, image_file)
        # 构建输出txt文件路径
        output_file = os.path.join(output_dir, txt_name)

        # 如果图像文件存在，处理标注
        if os.path.exists(txt_file):
            # 获取图像的宽度和高度（这里假设图像是JPEG格式）
            with open(image_path, 'rb') as img:
                img.seek(163)
                width = (img.read(2)[1] << 8) + img.read(2)[0]
                height = (img.read(2)[1] << 8) + img.read(2)[0]

            # 转换标注格式
            convert_annotation(txt_file, output_file, width, height)
        else:
            # 如果图像文件不存在，创建一个包含默认信息的txt文件
            with open(output_file, 'w') as out_file:
                out_file.write("\n")  # 这里使用默认值，可以根据需要进行调整


# 例子：调用函数并指定图像目录、标注目录和输出目录
process_images_and_annotations('data/images/test', 'runs/detect/predict2/labels', 'pred')

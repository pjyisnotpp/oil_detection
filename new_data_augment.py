from PIL import Image, ImageEnhance
import os
import shutil


def enhance_brightness(input_image_path, input_annotation_path, output_image_path, output_annotation_path):
    # 创建输出图像文件夹
    if not os.path.exists(output_image_path):
        os.makedirs(output_image_path)

    # 创建输出标注文件夹
    if not os.path.exists(output_annotation_path):
        os.makedirs(output_annotation_path)

    # 遍历输入图像目录
    for file_name in os.listdir(input_image_path):
        if file_name.endswith('.jpg'):  # 确保文件是图像文件
            image_file_path = os.path.join(input_image_path, file_name)
            annotation_file_path = os.path.join(input_annotation_path,
                                                file_name.replace(".jpg", ".xml"))  # 假设标注文件以.txt结尾

            # 打开图像
            original_image = Image.open(image_file_path)

            # 设置亮度增强因子，可以根据需要进行调整
            brightness_factors = [0.4, 0.6, 0.8, 1.2, 1.4, 1.6]

            # 生成亮度变化后的图像和标注
            for i, factor in enumerate(brightness_factors):
                # 复制原始图像
                enhanced_image = original_image.copy()

                # 增强亮度
                enhancer = ImageEnhance.Brightness(enhanced_image)
                enhanced_image = enhancer.enhance(factor)

                # 生成新文件名
                new_image_file_name = f"{os.path.splitext(file_name)[0]}_bright_{i + 1}.jpg"
                new_annotation_file_name = f"{os.path.splitext(file_name)[0]}_bright_{i + 1}.xml"

                # 保存增强后的图像
                enhanced_image.save(os.path.join(output_image_path, new_image_file_name))

                # 复制标注文件到输出目录
                shutil.copy(annotation_file_path, os.path.join(output_annotation_path, new_annotation_file_name))


if __name__ == "__main__":
    # 输入图像的目录和标注的目录
    input_image_folder = "data/images/train"
    input_annotation_folder = "data/Annotations/train"

    # 输出图像的目录和标注的目录
    output_image_folder = "data/images/train"
    output_annotation_folder = "data/Annotations/train"

    # 执行数据增强
    enhance_brightness(input_image_folder, input_annotation_folder, output_image_folder, output_annotation_folder)

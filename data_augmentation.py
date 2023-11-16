import cv2
import os
import shutil

def enhance_contrast_and_brightness(image, alpha, beta):
    enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return enhanced_image

def process_images(input_folder, label_folder, output_img_folder, output_label_folder, contrast_list, beta):
    if not os.path.exists(output_img_folder):
        os.makedirs(output_img_folder)

    if not os.path.exists(output_label_folder):
        os.makedirs(output_label_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            # 读取图像
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)

            # 遍历对比度列表
            for contrast_factor in contrast_list:
                # 增强对比度和亮度
                enhanced_img = enhance_contrast_and_brightness(img, contrast_factor, beta)

                # 生成文件名后缀
                suffix = f"_contrast{int(contrast_factor * 100)}"

                # 保存增强后的图像到输出图像文件夹
                output_img_filename = os.path.splitext(filename)[0] + suffix + ".jpg"
                output_img_path = os.path.join(output_img_folder, output_img_filename)
                cv2.imwrite(output_img_path, enhanced_img)

                # 生成对应的标注文件名
                output_label_filename = os.path.splitext(output_img_filename)[0] + ".xml"
                output_label_path = os.path.join(output_label_folder, output_label_filename)

                # 复制标签文件到输出标注文件夹，假设标签文件是.xml格式
                label_filename = os.path.splitext(filename)[0] + ".xml"
                label_path = os.path.join(label_folder, label_filename)
                shutil.copy(label_path, output_label_path)

if __name__ == "__main__":
    label_folder = "data/Annotations/image"
    input_folder = "data/images/image"
    output_img_folder = "data/images/image"
    output_label_folder = "data/Annotations/image"
    contrast_list = [0.3, 1.2, 1.5, 0.8, 0.5]  # 对比度列表
    beta = 0  # 调整亮度增益

    process_images(input_folder, label_folder, output_img_folder, output_label_folder, contrast_list, beta)

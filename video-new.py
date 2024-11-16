import os, datetime
import cv2
import numpy as np
import sys, time

# vide_path = "video1.mp4"
# vide_path = "624.mp4"

def get_all_files(path = os.getcwd()):
    all_files = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            video_extensions = ('mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm')
            if file_name.lower().endswith(video_extensions):
                file_path = os.path.join(root, file_name)
                all_files.append(file_path)
    return all_files

def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
 
def image_hstack(image_path1, image_path2):
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)

    img1_sharp = img1.shape
    img2_shape = img2.shape
    print(img1_sharp)
    print(ima2_sharp)
    if img1_sharp[0] != ima2_sharp[0]:
        if img1_sharp[0] > img2_shape[0]:
            img2 = cv2.copyMakeBorde(img2, 0, img1_sharp[0] - img2_shape[0], 0, 0, 0, cv2.BORDER_CONSTANT, [0, 0, 0])
        else:
            img1 = cv2.copyMakeBorde(img1, 0, img2_sharp[0] - img1_shape[0], 0, 0, 0,cv2.BORDER_CONSTANT, [0, 0, 0])
    return np.hstack((img1, img2))

def image_vstack(img1, img2):
    img1_shape = img1.shape
    img2_shape = img2.shape
    print(img1_shape)
    print(img2_shape)
    if img1_shape[1] != img2_shape[1]:
        if img1_shape[1] > img2_shape[1]:
            img2 = cv2.copyMakeBorder(img2, 0, 0, 0, img1_shape[1] - img2_shape[1], cv2.BORDER_CONSTANT, (0, 0, 0))
        else:
            img1 = cv2.copyMakeBorder(img1, 0, 0, 0, img2_shape[1] - img1_shape[1], cv2.BORDER_CONSTANT, (0, 0, 0))
    return np.vstack((img1, img2))

def normal_size(filesize):
    if filesize > 1024 * 1024 * 1024:
        return "{:.2f}".format(filesize / (1024 * 1024 * 1024)) + "G"
    elif filesize > 1024 * 1024:
        return "{:.2f}".format(filesize / (1024 * 1024)) + "M"
    elif filesize > 1024:
        return "{:.2f}".format(filesize / 1024) + "K"
    else:
        return str(filesize) + "B"

def get_file_base_info(vide_path):
    fileInfo  = {}
    fileInfo["Name"] = os.path.basename(vide_path)
    filesize = os.path.getsize(vide_path)
    fileInfo["Size"] = normal_size(filesize)
    time = datetime.datetime.fromtimestamp(os.path.getctime(vide_path)).strftime("%Y-%m-%d %H:%M:%S")
    fileInfo["Time"] = time
    print(time)
    return fileInfo

def get_outfile_path(vide_path):
    video_name = os.path.basename(vide_path)
    video_base_name = video_name.rsplit('.', 1)[0]
    print(video_base_name)
    vide2_path = video_base_name + ".jpg"
    dir_path = os.path.dirname(vide_path)
    print("dir_path", dir_path)
    vide2_path = os.path.join(dir_path, vide2_path)
    print("outfile:", vide2_path, "infile:", vide_path)

    return vide2_path

def get_capture(file_path, frame_number):
    cap = cv2.VideoCapture(vide_path)
    if not cap.isOpened():
        print("error")
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps_max = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_number))
    ret, frame = cap.read()
    if ret:
        cap.release()
        return frame

def extend_image(image, top = 50, bottom = 20, left = 30, right = 20):
    # 扩充类型，例如 cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT 等
    borderType = cv2.BORDER_CONSTANT
     
    # 如果使用常量填充，还需要指定常量的颜色
    constant_value = (0, 0, 0)  # 黑色背景
    return cv2.copyMakeBorder(image, top, bottom, left, right, borderType, constant_value)

def image_put_text(image, text, right = 30, top = 30):
    font = cv2.FONT_HERSHEY_DUPLEX # 字体
    font_scale = 1 # 字体大小
    font_color = (255, 255, 255) # BGR颜色
    line_type = 2 # 字体粗细

    height, width = image.shape[:2]
    # print(height, width)
    position = (right, top) # 文字起始位置(right, top)
    # print(position)
    cv2.putText(image, text, position, font, font_scale, font_color, line_type) # 在图片上插入文字


def creat_capture(vide_path):
    fileInfo = get_file_base_info(vide_path)
    cap = cv2.VideoCapture(vide_path)

    if not cap.isOpened():
        print("error")
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps_max = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    fileInfo["fps"] = fps
    fileInfo["Duration"] = seconds_to_hms(int(fps_max / fps))

    # 获取视频帧的宽度和高度
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fileInfo["Resolution"] = str(frame_width) + "x" + str(frame_height)
    print(fps_max, frame_width, frame_height)
    frame_all = []
    print("total fps %d, fps %d", fps_max, fps)
    width_cnt = 2
    height_cnt = 8
    for i in range(int(fps), int(fps_max), int(fps_max / (width_cnt * height_cnt))):
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(i))
        ret, frame = cap.read()
        if ret:
            frame = extend_image(frame)
            image_put_text(frame, seconds_to_hms(int(i / fps))) 
            frame_all.append(frame)
        else:
            print("Error")
    print("max len", len(frame_all))

    # 按照要求将width_cnt拼接成一个横幅大图
    image_v = []
    for i in range(0, len(frame_all), width_cnt):
        cap0 = frame_all[i]
        # print(i, len(frame_all[i+1:(i+width_cnt)]))
        for j in frame_all[i + 1:(i+width_cnt)]:
            cap0 = np.hstack((cap0, j))
        image_v.append(cap0)

    #将横幅大图拼接成竖直大图
    cap0 = image_v[0]
    for i in image_v[1:]:
        cap0 = image_vstack(cap0, i)

    # 增加标题等信息
    cap0 = extend_image(cap0, 50)
    text = ''
    for key in fileInfo.keys():
        text = text + key + ":" + str(fileInfo[key]) + " "
    image_put_text(cap0, text, 30, 40)
    print(text)
    return cap0


def refresh_img():
    for vide_path in get_all_files():
        print(vide_path)
        cap0 = creat_capture(vide_path)
        vide2_path = get_outfile_path(vide_path)
        cv2.imwrite(vide2_path, cap0)

# cv2.imshow("", cap0)
# cv2.waitKey(0)

    
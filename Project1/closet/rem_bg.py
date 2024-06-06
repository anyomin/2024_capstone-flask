# rembg module 사용 설명 github 참조 페이지
# https://github.com/danielgatis/rembg

# Code #1
# 개별 파일 열어 배경 제거하고 저장하기
from rembg import remove
from PIL import Image

import numpy as np
import os

Closet_FOLDER = 'closet'
AFTER_REMOVEBG_FOLDER =os.path.join(Closet_FOLDER, 'After_Removebg')
def removebg(filepath):
    input = Image.open(filepath)
    output = remove(input)
    filename = os.path.basename(filepath)
    result_filename = f"{os.path.splitext(filename)[0]}.png"
    result_filepath = os.path.join(AFTER_REMOVEBG_FOLDER, result_filename)
    output.save(result_filepath)
    print(f'Image saved successfully at: {result_filepath}')
    



import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# 모델 불러오기
model = tf.keras.models.load_model('C:/Users/user/Flask_Project/test/clothes_classification_model.h5')

def classify_image(image_path):
    # 이미지 불러오기 및 전처리
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # 이미지 스케일링

    # 카테고리 예측
    predictions = model.predict(img_array)

    # 카테고리 및 인덱스 매핑
    class_mapping =  {
    0: 'backpack', 1: 'boots', 2: 'bucketbag', 3: 'crossbag', 4: 'dress_shoes',
    5: 'hoodie', 6: 'jacket', 7: 'jeans', 8: 'mantoman', 9: 'neat',
    10: 'running_shoes', 11: 'sandal', 12: 'shirt', 13: 'shoSrts',
    14: 'skirt', 15: 't-shirt', 16: 'training_pants'
}

    # 예측 결과 출력
    predicted_index = np.argmax(predictions)
    predicted_class = class_mapping[predicted_index]

    return predicted_class

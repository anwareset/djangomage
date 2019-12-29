import numpy as np
from keras.models import Model
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input

class PencariCiri:
    def __init__(doi):
        basis_model = VGG16(weights='imagenet')
        doi.model = Model(inputs=basis_model.input, outputs=basis_model.get_layer('fc1').output)
    def ekstraksi(doi, img):  # img berasal dari PIL.Image.open(path) atau bisa juga keras.preprocess>
        img = img.resize((224, 224))  # VGG bakal ngebaca gambar 224x224 jadi kita resize dulu
        img = img.convert('RGB')  #  memastikan gambarnya berwarna RGB
        x = image.img_to_array(img)  # Gambarnya di jadiin np.array. Tinggi x Lebar x Channel.
        x = np.expand_dims(x, axis=0)  # (H, W, C)->(1, H, W, C), Dimana elemen array pertama adalah >
        x = preprocess_input(x)  # Mengurangi nilai rerata untuk setiap pixel nya.
        ciri = doi.model.predict(x)[0]  # (1, 4096) -> (4096, )
        return ciri / np.linalg.norm(ciri)  # Normalisasi
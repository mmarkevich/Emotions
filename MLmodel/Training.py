import numpy as np
import pandas as pd
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from Augmentation import translate
from Augmentation import flip



X_train = []
y_train = []
X_test = []
y_test = []

image_reader = pd.read_csv('fer2013.csv')

for index, row in image_reader.iterrows():
    pixels = row['pixels'].split(" ")
    if 'Training' in row['Usage']:
        image = np.array(pixels, 'float32')
        image = image.reshape(1, 48, 48, 1)
        emotion = row['emotion']
        X_train.append(image)
        y_train.append(emotion)

        temp = translate(image, 5, 'right')
        X_train.append(temp)
        y_train.append(emotion)

        temp = translate(image, 5, 'left')
        X_train.append(temp)
        y_train.append(emotion)

        temp = translate(image, 5, 'up')
        X_train.append(temp)
        y_train.append(emotion)

        flipped_img = flip(image)
        flipped_img = flipped_img.reshape(1, 48, 48, 1)
        X_train.append(flipped_img)
        y_train.append(emotion)

        temp = translate(flipped_img, 5, 'right')
        X_train.append(temp)
        y_train.append(emotion)

        temp = translate(flipped_img, 5, 'left')
        X_train.append(temp)
        y_train.append(emotion)

        temp = translate(flipped_img, 5, 'up')
        X_train.append(temp)
        y_train.append(emotion)


    elif 'PublicTest' in row['Usage']:
        image = np.array(pixels, 'float32')
        image = image.reshape(1, 48, 48, 1)
        emotion = row['emotion']
        X_test.append(image)
        y_test.append(emotion)

X_train = np.array(X_train, 'float32')
X_test = np.array(X_test, 'float32')

# Normalization between 0 and 1
X_train -= np.mean(X_train, axis=0)
X_train /= np.std(X_train, axis=0)

X_test -= np.mean(X_test, axis=0)
X_test /= np.std(X_test, axis=0)

X_train = X_train.reshape(X_train.shape[0], 48, 48, 1)
X_test = X_test.reshape(X_test.shape[0], 48, 48, 1)

y_train = np_utils.to_categorical(y_train, num_classes = 7)
y_test = np_utils.to_categorical(y_test, num_classes = 7)

def create_model():
    model = Sequential()

    model.add(Conv2D(64, (5, 5), input_shape = (48, 48, 1), activation = 'elu', padding='same', kernel_initializer = 'he_normal'))
    model.add(BatchNormalization())
    model.add(Conv2D(64, (5, 5), activation = 'elu', padding = 'same', kernel_initializer = 'he_normal'))
    model.add(BatchNormalization())

    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.4))

    model.add(Conv2D(128, (3, 3), activation='elu', padding='same', kernel_initializer='he_normal'))
    model.add(BatchNormalization())
    model.add(Conv2D(128, (3, 3), activation='elu', padding='same', kernel_initializer='he_normal'))
    model.add(BatchNormalization())

    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.4))

    model.add(Conv2D(256, (3, 3), activation='elu', padding='same', kernel_initializer='he_normal'))
    model.add(BatchNormalization())
    model.add(Conv2D(256, (3, 3), activation='elu', padding='same', kernel_initializer='he_normal'))
    model.add(BatchNormalization())

    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Flatten())

    model.add(Dense(128, activation='elu', kernel_initializer='he_normal'))
    model.add(BatchNormalization())

    model.add(Dropout(0.6))

    model.add(Dense(7, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

    return model

early_stopping = EarlyStopping(
    monitor='val_accuracy',
    min_delta=0.00005,
    patience=11,
    verbose=1,
    restore_best_weights=True,
)

lr_scheduler = ReduceLROnPlateau(
    monitor='val_accuracy',
    factor=0.5,
    patience=7,
    min_lr=1e-7,
    verbose=1,
)

callbacks = [
    early_stopping,
    lr_scheduler,
]


model = create_model()

model.compile(loss=categorical_crossentropy,
              optimizer=Adam(),
              metrics=['accuracy'])

#Training the model
model.fit(X_train, y_train,
          batch_size=32,
          epochs=30,
          verbose=1,
          validation_data=(X_test, y_test),
          callbacks=callbacks,
          shuffle=True)

fer_json = model.to_json()
with open("fer2013_model6.json", "w") as json_file:
    json_file.write(fer_json)
model.save_weights("fer2013_model6.h5")
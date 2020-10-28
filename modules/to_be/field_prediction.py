import numpy as np
import pandas as pd
import tensorflow_hub as hub
from sklearn.model_selection import train_test_split
import tensorflow as tf



np.set_printoptions(precision=3, suppress=True)

def field_labels(template):

    template = pd.read_excel('/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/raw/ML.xlsx')

    template_train, template_test = train_test_split(template)
    template_activities_train=template_train['task description'].tolist()
    template_field_train = template_train['label_field'].tolist()
    template_level1_train = template_train['label_level1'].tolist()
    template_activities_validation=template_test['task description'].tolist()
    template_field_validation=template_test['label_field'].tolist()
    template_level1_validation=template_test['label_level1'].tolist()

    hub_layer_field = hub.KerasLayer("https://tfhub.dev/google/nnlm-es-dim50/2",
                               input_shape=[], dtype=tf.string)

    model_field = tf.keras.Sequential()
    model_field.add(hub_layer_field)
    model_field.add(tf.keras.layers.Dense(32, activation='relu'))
    model_field.add(tf.keras.layers.Dropout(0.25))
    model_field.add(tf.keras.layers.Dense(26, activation='relu'))
    model_field.add(tf.keras.layers.Dropout(0.25))
    model_field.add(tf.keras.layers.Dense(20, activation='relu'))
    model_field.add(tf.keras.layers.Dropout(0.25))
    model_field.add(tf.keras.layers.Dense(13, activation='relu'))
    model_field.add(tf.keras.layers.Dropout(0.1))
    model_field.add(tf.keras.layers.Dense(5, activation=tf.keras.activations.softmax))

    model_field.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                  metrics=['accuracy'])

    tf.keras.utils.to_categorical(template_field_train)


    history_field = model_field.fit(x=template_activities_train,
                        y=template_field_train,
                        epochs=100,
                        validation_data=(template_activities_validation,
                                         template_field_validation),
                        verbose=1)

    template['prediction_field'] = np.argmax(model_field.predict(template['task description']), axis=1)

    with pd.ExcelWriter(
            '/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/results/to_be/predictions/prediction_field.xlsx') as writer:
        template.to_excel(writer, sheet_name='prediction_field')


    return template


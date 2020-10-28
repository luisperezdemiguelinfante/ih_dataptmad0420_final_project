import numpy as np
import pandas as pd
import tensorflow_hub as hub
from sklearn.model_selection import train_test_split
import tensorflow as tf



np.set_printoptions(precision=3, suppress=True)

def field4_labels(template):

    template = pd.read_excel('/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/raw/ML.xlsx')

    filter_supply_chain = template['label_field'] == 4
    field_supply_chain = template[filter_supply_chain]

    field_supply_chain_train, field_supply_chain_test = train_test_split(field_supply_chain)
    supply_activities_train=field_supply_chain_train['task description'].tolist()
    supply_activities_validation=field_supply_chain_test['task description'].tolist()
    supply_chain_train = field_supply_chain_train['label_level1'].tolist()
    supply_chain_validation=field_supply_chain_test['label_level1'].tolist()

    hub_layer_supply_level1 = hub.KerasLayer("https://tfhub.dev/google/nnlm-es-dim50/2",
                                             input_shape=[], dtype=tf.string)

    model_supply_level1 = tf.keras.Sequential()
    model_supply_level1.add(hub_layer_supply_level1)
    model_supply_level1.add(tf.keras.layers.Dense(32, activation='relu'))
    model_supply_level1.add(tf.keras.layers.Dropout(0.25))
    model_supply_level1.add(tf.keras.layers.Dense(24, activation='relu'))
    model_supply_level1.add(tf.keras.layers.Dropout(0.25))
    model_supply_level1.add(tf.keras.layers.Dense(16, activation='relu'))
    model_supply_level1.add(tf.keras.layers.Dropout(0.25))
    model_supply_level1.add(tf.keras.layers.Dense(10, activation='relu'))
    model_supply_level1.add(tf.keras.layers.Dropout(0.1))
    model_supply_level1.add(tf.keras.layers.Dense(6, activation=tf.keras.activations.softmax))

    model_supply_level1.compile(optimizer='adam',
                                loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                                metrics=['accuracy'])

    tf.keras.utils.to_categorical(supply_chain_train)

    history = model_supply_level1.fit(x=supply_activities_train,
                               y=supply_chain_train,
                               epochs=100,
                               validation_data=(supply_activities_validation,
                                                supply_chain_validation),
                               verbose=1)

    field_supply_chain['prediction_supply_level1'] = np.argmax(model_supply_level1.predict(field_supply_chain['task description']), axis=1)

    with pd.ExcelWriter(
            '/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/results/to_be/predictions/prediction_field4.xlsx') as writer:
        field_supply_chain.to_excel(writer, sheet_name='prediction_field4')


    return field_supply_chain

from networks.network import BaseNetwork

import numpy as np
import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras import layers 

from typing import Tuple

# input_node : shape of a input sample; batch size is omiited.

def input_cnn_layers(
        input_shape: Tuple, 
        filters: int = 32,
        kernel_size: Tuple = (2,2),
        activation="relu") -> keras.Model:
    input_layer = keras.Input(shape=input_shape)
    x = layers.Conv2D(
            filters=filters,
            kernel_size=kernel_size,
            activation=activation)(input_layer)
    output_layer = layers.MaxPooling2D()(x)
    return keras.Model(inputs=input_layer, outputs=output_layer)

def hidden_cnn_layers():
    return Model(inputs=input_layer, outputs=output_layer)

def input_linear_layers():
    return Model(inputs=input_layer, outputs=output_layer)

def hidden_linear_layers():
    return Model(inputs=input_layer, outputs=output_layer)

class ValuePolicy(tf.Model):
    def __init__(self, input_dims, output_dims):
        super().__init__(input_dims, output_dims)
        pass

    def call(self, x):
        pass



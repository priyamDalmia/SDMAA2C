import tensorflow as tf

class BaseNetwork(tf.Model):
    def __init__(self, input_dims, output_dims, **kwargs):
        self.input_dims = input_dims
        self.ouptut_dims = output_dims
        
        # self.build_network

    def call(self):
        raise NotImplementedError
    
    def build_network(self):
        raise NotImplementedError

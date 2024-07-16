import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense, LSTM, Dropout
from kamoe_lstm import GRKAN, GRN

class KAMoE_LSTM(Layer):
    def __init__(self, unit, n_lstm = 4, return_sequences = False, dropout = 0., **kwargs):
        super().__init__(**kwargs)
        self.unit = unit
        self.hidden_layer = Dense(unit, 'relu')
        self.n_lstm = n_lstm
        self.return_sequences = return_sequences
        self.lstm_layers = [LSTM(unit, return_sequences=return_sequences) for _ in range(n_lstm)]
        self.hidden_to_weight = GRKAN(n_lstm, activation = 'softmax', dropout = dropout)
        self.dropout = Dropout(dropout)

    def build(self, input_shape):
        self.hidden_layer.build(input_shape)
        self.hidden_to_weight.build((*input_shape[:-1], self.n_lstm))
        for lstm in self.lstm_layers:
            lstm.build(input_shape)
        super().build(input_shape)
        
    def call(self, inputs):
        if self.return_sequences:
            hidden = self.hidden_layer(inputs)
        else:
            hidden = self.hidden_layer(inputs[:,-1,:])
        weights = self.hidden_to_weight(hidden)
        lstm_outs = []
        for lstm in self.lstm_layers:
            lstm_outs.append(lstm(inputs))
        lstm_outs = tf.stack(lstm_outs, axis=-1)
        lstm_outs = lstm_outs * weights[...,tf.newaxis,:]
        return tf.reduce_sum(lstm_outs, axis=-1)


class MoE_LSTM(Layer):
    def __init__(self, unit, n_lstm = 4, return_sequences = False, dropout = 0., **kwargs):
        super().__init__(**kwargs)
        self.unit = unit
        self.hidden_layer = Dense(unit, 'relu')
        self.n_lstm = n_lstm
        self.return_sequences = return_sequences
        self.lstm_layers = [LSTM(unit, return_sequences=return_sequences) for _ in range(n_lstm)]
        self.hidden_to_weight = GRN(n_lstm, activation = 'softmax', dropout = dropout)
        self.dropout = Dropout(dropout)
        
    def build(self, input_shape):
        self.hidden_layer.build(input_shape)
        self.hidden_to_weight.build((*input_shape[:-1], self.n_lstm))
        for lstm in self.lstm_layers:
            lstm.build(input_shape)
        super().build(input_shape)

    def call(self, inputs):
        if self.return_sequences:
            hidden = self.hidden_layer(inputs)
        else:
            hidden = self.hidden_layer(inputs[:,-1,:])
        weights = self.hidden_to_weight(hidden)
        lstm_outs = []
        for lstm in self.lstm_layers:
            lstm_outs.append(lstm(inputs))
        lstm_outs = tf.stack(lstm_outs, axis=-1)
        lstm_outs = lstm_outs * weights[...,tf.newaxis,:]
        return tf.reduce_sum(lstm_outs, axis=-1)

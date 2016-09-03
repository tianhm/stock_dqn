# -*- coding: utf-8 -*-



import chainer
import chainer.functions as F
import numpy as np

class Q_DNN(chainer.FunctionSet):
    
    modelname = 'dnn6'
    layer_num = 6
    #input_num = 60
    #hidden_num = 100
    
    def __init__(self, input_num, hidden_num,num_of_actions):
        self.input_num = input_num
        self.hidden_num = hidden_num
        self.num_of_actions = num_of_actions
        
        super(Q_DNN, self).__init__(
            fc1=F.Linear(self.input_num, self.hidden_num),
            fc2=F.Linear(self.hidden_num, self.hidden_num),
            fc3=F.Linear(self.hidden_num, self.hidden_num),
            fc4=F.Linear(self.hidden_num, self.hidden_num),
            fc5=F.Linear(self.hidden_num, self.hidden_num),
            q_value=F.Linear(200, self.num_of_actions,
                             initialW=np.zeros((self.num_of_actions, 200),
                                               dtype=np.float32))
        )
        
    def Q_func(self, state, train=True):
        
        
        h = F.dropout(F.tanh(self.fc1(state)), train=train)
        h = F.dropout(F.tanh(self.fc2(h)), train=train)  
        h = F.dropout(F.tanh(self.fc3(h)), train=train)
        h = F.dropout(F.tanh(self.fc4(h)), train=train)
        h = F.dropout(F.tanh(self.fc5(h)), train=train)
        Q = self.q_value(h)

        return Q
        
    

        
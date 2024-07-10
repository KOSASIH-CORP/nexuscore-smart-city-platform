import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class DeepQNetwork(nn.Module):
    def __init__(self, state_dim, action_dim, hidden_dim):
        super(DeepQNetwork, self).__init__()
        self.fc1 = nn.Linear(state_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, action_dim)

    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def eaced_deployment(namespace='default', body=deployment)
        return response

    def delete_vnf(self, vnf_name):
        response = self.v1.delete_namespaced_deployment(name=vnf_name, namespace='default', body=kubernetes.client.V1DeleteOptions())
        return response

    def scale_vnf(self, vnf_name, scale_out):
        deployment = self.v1.read_namespaced_deployment(name=vnf_name, namespace='default')
        deployment.spec.replicas = scale_out
        response = self.v1.replace_namespaced_deployment(name=vnf_name, namespace='default', body=deployment)
        return response

import torch


class TensorCalculator:

    def __init__(self):
        pass

    def tensor_zeros(self, dim_x, dim_y):
        zeros = torch.zeros([dim_x, dim_y])
        return zeros

    def tensor_ones(self, dim_x, dim_y):
        ones = torch.ones([dim_x, dim_y])
        return ones

    def tensor_rand(self, dim_x, dim_y):
        random = torch.rand([dim_x, dim_y])
        return random

    def tensor_sum(self, tensor1, tensor2):
        a = tensor1
        b = tensor2
        suma = torch.add(a, b)
        return suma

    def tensor_mult(self, tensor1, tensor2):
        a = tensor1
        b = tensor2
        multp = torch.matmul(a, b)
        return multp

    def tensor_div(self, tensor1, tensor2):
        a = tensor1
        b = tensor2
        division = torch.div(a, b)
        return division

    def tensor_rest(self, tensor1, tensor2):
        a = tensor1
        b = tensor2
        r = torch.sub(a, b)
        return r

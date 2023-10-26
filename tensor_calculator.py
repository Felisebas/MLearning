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

    def tensor_sum(self, dim_x, dim_y, dim_z, dim_g):
        a = torch.tensor([dim_x, dim_y])
        b = torch.tensor([dim_z, dim_g])
        suma = a + b
        return suma

    def tensor_mult(self, dim_x, dim_y, dim_z, dim_g):
        a = torch.tensor([dim_x, dim_y])
        b = torch.tensor([dim_z, dim_g])
        multp = torch.matmul(a, b)
        return multp

    def tensor_div(self, dim_x, dim_y, dim_z, dim_g):
        a = torch.tensor([dim_x, dim_y])
        b = torch.tensor([dim_z, dim_g])
        division = torch.div(a, b)
        return division

    def tensor_rest(self, dim_x, dim_y, dim_z, dim_g):
        a = torch.tensor([dim_x, dim_y])
        b = torch.tensor([dim_z, dim_g])
        r = torch.sub(a, b)
        return r

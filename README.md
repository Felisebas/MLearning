# MLearning
The repository contains  a directory call "ejercicio" where we can find the file called "tensor_calculator.py" where we 
can try different functions of tensors like:

- tensor_zeros: given two dimensions creates a tensor of zeros 
- tensor_ones: given two dimensions creates a tensor of ones 
- tensor_rand: given two dimensions creates a tensor of random numbers 
- tensor_sum: given two tensors adds the two tensors
- tensor_mult: given two tensors multiplies the two tensors
- tensor_div: given two tensors divides the two tensors
- tensor_rest: given two tensors substracts the two tensors

# How to try the functions?

1. Install the repository in terminal (or in the first cell if you are in jupyter) with the code "pip install -U git+https://github.com/Felisebas/MLearning.git"
2. Import the file as library with the code "from ejercicio.tensor_calculator import *"
3. Import the library torch to create the tensors with the code "import torch"
3. Create an instance of the class called "TensorCalculator"
4. Call the functions to try them:
   - instance.tensor_zeros(dim_x,dim_y)
   - instance.tensor_ones(dim_x,dim_y)
   - instance.tensor_rand(dim_x,dim_y)
   - instance.tensor_sum(tensor1, tensor2)
   - instance.tensor_mult(tensor1, tensor2)
   - instance.tensor_div(tensor1, tensor2)
   - instance.tensor_rest(tensor1, tensor2)

# Examples

```python
pip install -U git+https://github.com/Felisebas/MLearning.git

from ejercicio.tensor_calculator import *

import torch

a = TensorCalculator()

zeros = a.tensor_zeros(2,2)

ones = a.tensor_ones(2,2)

random = a.tensor_rand(2,2)

b = torch.tensor([4,8])
c = torch.tensor([2,4])

suma = a.tensor_sum(b,c)

multiplicacion = a.tensor_mult(b,c)

division = a.tensor_div(b,c)

resta = a.tensor_rest(b,c)
```




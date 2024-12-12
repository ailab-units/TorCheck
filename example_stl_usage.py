import torch

from torcheck import stl
from torcheck.stlParser.stlNode import from_string_to_formula
from phis_generator import StlGenerator

signal1 = torch.randn(1, 2, 100)
print(signal1.shape)

# phi(x) = x1>1 and globally[0,4] x2<2
n0 = stl.Atom(var_index=0, threshold=1, lte=False)  # lte = False is >
n1 = stl.Atom(var_index=1, threshold=2, lte=True)  # lte = True is >
ng = stl.Globally(n1, unbound=True, right_time_bound=4)
phi = stl.And(n0, ng)
# print(phi)

# signal dimension [n_samples, n_vars, n_timesteps]
z0 = phi.boolean(signal1)
# print(z0)

z1 = phi.quantitative(signal1)
# print(z1)

# test antlr parser
generator = StlGenerator(leaf_prob=0.4)
phis = generator.bag_sample(250, nvars=3)
phis_str = list(map(str, phis))
phis_obj = list(map(from_string_to_formula, phis_str))
for i, phi in enumerate(phis_obj):
    print(phis_str[i])
    print(phi)
    print('\n')


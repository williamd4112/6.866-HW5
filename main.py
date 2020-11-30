import numpy as np
import itertools
import functools

from pyquaternion import Quaternion

class Quat(Quaternion):
    def __hash__(self):
        h = hash(tuple(np.round(np.abs(self.q), 6)))
        return h

a = 1 / np.sqrt(3)
b = np.sqrt(2. / 3.)

theta = (2 * np.pi) / 3
omegas = [(a, 0, b), (a, 0, -b), (-a, b, 0), (-a, -b, 0)]

base_qs = set([Quat(axis=omega, angle=theta) for omega in omegas])
k = 2
while True:
    before_size = len(base_qs)
    base_qs = base_qs.union(set(map(lambda qq: (np.prod(qq)),
                            itertools.product(base_qs, repeat=k))))
    print('(So far) Num. different rotations:', len(base_qs))
    after_size = len(base_qs)
    if after_size == before_size:
        break

print('Num. different rotations:', len(base_qs))
print('Num. angles through 2pi/3:', len(list(filter(lambda q: np.allclose(abs(q.angle), abs(2 * np.pi / 3)), base_qs))))
print('Num. angles other than through 2pi/3 or 0:', len(list(filter(lambda q: not (np.allclose(abs(q.angle), abs(2 * np.pi / 3)) or np.allclose(abs(q.angle), 0)), base_qs))))

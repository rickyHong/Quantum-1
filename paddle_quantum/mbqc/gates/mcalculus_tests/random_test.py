# Copyright (c) 2021 Institute for Quantum Computing, Baidu Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from numpy import random, pi
from paddle import to_tensor
import paddle
import paddle_quantum
from paddle_quantum.mbqc.simulator import MBQC
from paddle_quantum.mbqc.transpiler import transpile
from paddle_quantum.mbqc.qobject import Circuit, State
from paddle_quantum.mbqc.utils import random_state_vector, compare_by_vector, compare_by_density

n = 5  # Set the circuit width
theta = to_tensor(random.rand(n) * 2 * pi, dtype='float64')  # Generate random angles

# Instantiate a Circuit class
cir_mbqc = Circuit(n)
# Instantiate a UAnsatz class
cir_ansatz = paddle_quantum.Circuit(n)

# Construct a circuit
# for cir in [cir_mbqc, cir_ansatz]:
for i in range(n):
    cir_mbqc.h(i)
    cir_mbqc.rx(theta[i], i)
cir_mbqc.cnot([0, 1])
for i in range(n):
    cir_mbqc.ry(theta[i], i)
    cir_mbqc.rz(theta[i], i)
for i in range(n):
    cir_ansatz.h(i)
    cir_ansatz.rx(i, param=theta[i])
cir_ansatz.cnot([0, 1])
for i in range(n):
    cir_ansatz.ry(i, param=theta[i])
    cir_ansatz.rz(i, param=theta[i])
# Generate a random state vector
input_psi = random_state_vector(n, is_real=False)
# Transpile circuit to measurement pattern
pattern = transpile(cir_mbqc)
mbqc = MBQC()
mbqc.set_pattern(pattern)
mbqc.set_input_state(State(input_psi, list(range(n))))
mbqc.run_pattern()
# Obtain the output state
state_out = mbqc.get_quantum_output()

# Find the standard result
vec_ansatz = cir_ansatz(paddle_quantum.state.to_state(paddle.flatten(input_psi)))
vec_ansatz = vec_ansatz.data
system_ansatz = state_out.system
state_ansatz = State(vec_ansatz, system_ansatz)
compare_by_vector(state_out, state_ansatz)
compare_by_density(state_out, state_ansatz)

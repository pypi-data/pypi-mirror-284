# Copyright 2024 BDP Ecosystem Limited. All Rights Reserved.
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
# ==============================================================================

from __future__ import annotations

from typing import Union, Optional, Callable, Sequence, Tuple

import brainstate as bst
import brainunit as bu
import jax
import numpy as np

from .._base import HHTypedNeuron, State4Integral, IonChannel

__all__ = [
  'MultiCompartment',
]


def diffusive_coupling(potentials, coo_ids, resistances):
  """
  Compute the diffusive coupling currents between neurons.

  :param potentials: The membrane potential of neurons.
  :param coo_ids: The COO format of the adjacency matrix.
  :param resistances: The weight/resistances of each connection.
  :return: The output of the operator, which computes the diffusive coupling currents.
  """
  # potential: [n,]
  #    The membrane potential of neurons.
  #    Should be a 1D array.
  # coo_ids: [m, 2]
  #    The COO format of the adjacency matrix.
  #    Should be a 2D array. Each row is a pair of (i, j).
  #    Note that (i, j) indicates the connection from neuron i to neuron j,
  #    and also the connection from neuron j to i.
  # resistances: [m]
  #    The weight of each connection.
  #    resistances[i] is the weight of the connection from coo_ids[i, 0] to coo_ids[i, 1],
  #    and also the connection from coo_ids[i, 1] to coo_ids[i, 0].
  # outs: [n]
  #    The output of the operator, which computes the summation of all differences of potentials.
  #    outs[i] = sum((potentials[i] - potentials[j]) / resistances[j] for j in neighbors of i)

  assert isinstance(potentials, bu.Quantity), 'The potentials should be a Quantity.'
  assert isinstance(resistances, bu.Quantity), 'The conductance should be a Quantity.'
  # assert potentials.ndim == 1, f'The potentials should be a 1D array. Got {potentials.shape}.'
  assert resistances.shape[-1] == coo_ids.shape[0], ('The length of conductance should be equal '
                                                     'to the number of connections.')
  assert coo_ids.ndim == 2, f'The coo_ids should be a 2D array. Got {coo_ids.shape}.'
  assert resistances.ndim == 1, f'The conductance should be a 1D array. Got {resistances.shape}.'

  outs = bu.Quantity(bu.math.zeros(potentials.shape), dim=potentials.dim / resistances.dim)
  pre_ids = coo_ids[:, 0]
  post_ids = coo_ids[:, 1]
  diff = (potentials[..., pre_ids] - potentials[..., post_ids]) / resistances
  outs[..., pre_ids] -= diff
  outs[..., post_ids] += diff
  return outs


def init_coupling_weight(n_compartment, connection, diam, L, Ra):
  # weights = []
  # for i, j in connection:
  #   # R_{i,j}=\frac{R_{i}+R_{j}}{2}
  #   #        =\frac{1}{2}(\frac{4R_{a}\cdot L_{i}}{\pi\cdot diam_{j}^{2}}+
  #   #         \frac{4R_{a}\cdot L_{j}}{\pi\cdot diam_{j}^{2}})
  #   R_ij = 0.5 * (4 * Ra[i] * L[i] / (np.pi * diam[i] ** 2) + 4 * Ra[j] * L[j] / (np.pi * diam[j] ** 2))
  #   weights.append(R_ij)
  # return bu.Quantity(weights)

  assert isinstance(connection, (np.ndarray, jax.Array)), 'The connection should be a numpy/jax array.'
  pre_ids = connection[:, 0]
  post_ids = connection[:, 1]
  if Ra.size == 1:
    Ra_pre = Ra
    Ra_post = Ra
  else:
    assert Ra.shape[-1] == n_compartment, (f'The length of Ra should be equal to '
                                           f'the number of compartments. Got {Ra.shape}.')
    Ra_pre = Ra[..., pre_ids]
    Ra_post = Ra[..., post_ids]
  if L.size == 1:
    L_pre = L
    L_post = L
  else:
    assert L.shape[-1] == n_compartment, (f'The length of L should be equal to '
                                          f'the number of compartments. Got {L.shape}.')
    L_pre = L[..., pre_ids]
    L_post = L[..., post_ids]
  if diam.size == 1:
    diam_pre = diam
    diam_post = diam
  else:
    assert diam.shape[-1] == n_compartment, (f'The length of diam should be equal to the '
                                             f'number of compartments. Got {diam.shape}.')
    diam_pre = diam[..., pre_ids]
    diam_post = diam[..., post_ids]

  weights = 0.5 * (
      4 * Ra_pre * L_pre / (np.pi * diam_pre ** 2) +
      4 * Ra_post * L_post / (np.pi * diam_post ** 2)
  )
  return weights


class MultiCompartment(HHTypedNeuron):
  __module__ = 'dendritex.neurons'

  def __init__(
      self,
      size: bst.typing.Size,

      # morphology parameters
      connection: Sequence[Tuple[int, int]] | np.ndarray,

      # neuron parameters
      Ra: bst.typing.ArrayLike = 100. * (bu.ohm * bu.cm),
      cm: bst.typing.ArrayLike = 1.0 * (bu.uF / bu.cm ** 2),
      diam: bst.typing.ArrayLike = 1. * bu.um,
      L: bst.typing.ArrayLike = 10. * bu.um,

      # membrane potentials
      V_th: Union[bst.typing.ArrayLike, Callable] = 0. * bu.mV,
      V_initializer: Union[bst.typing.ArrayLike, Callable] = bst.init.Uniform(-70 * bu.mV, -60. * bu.mV),
      spk_fun: Callable = bst.surrogate.ReluGrad(),

      # others
      name: Optional[str] = None,
      mode: Optional[bst.mixin.Mode] = None,
      **ion_channels
  ):
    super().__init__(size, mode=mode, name=name, **ion_channels)

    # neuronal parameters
    self.Ra = bst.init.param(Ra, self.varshape)
    self.cm = bst.init.param(cm, self.varshape)
    self.diam = bst.init.param(diam, self.varshape)
    self.L = bst.init.param(L, self.varshape)
    self.A = np.pi * self.diam * self.L  # surface area

    # parameters for morphology
    connection = np.asarray(connection)
    assert connection.shape[1] == 2, 'The connection should be a sequence of tuples with two elements.'
    self.connection = np.unique(
      np.sort(
        connection,
        axis=1,  # avoid off duplicated connections, for example (1, 2) vs (2, 1)
      ),
      axis=0  # avoid of duplicated connections, for example (1, 2) vs (1, 2)
    )
    if self.connection.max() >= self.n_compartment:
      raise ValueError('The connection should be within the range of compartments. '
                       f'But we got {self.connection.max()} >= {self.n_compartment}.')
    self.resistances = init_coupling_weight(self.n_compartment, connection, self.diam, self.L, self.Ra)

    # parameters for membrane potentials
    self.V_th = V_th
    self._V_initializer = V_initializer
    self.spk_fun = spk_fun

  def init_state(self, batch_size=None):
    self.V = State4Integral(bst.init.param(self._V_initializer, self.varshape, batch_size))
    self.spike = bst.ShortTermState(bst.init.param(bu.math.zeros, self.varshape, batch_size))
    super().init_state(batch_size)

  def reset_state(self, batch_size=None):
    self.V.value = bst.init.param(self._V_initializer, self.varshape, batch_size)
    self.spike.value = bst.init.param(bu.math.zeros, self.varshape, batch_size)
    super().reset_state(batch_size)

  def before_integral(self, *args):
    self._last_V = self.V.value

    channels = self.nodes(level=1, include_self=False).subset(IonChannel)
    for node in channels.values():
      node.before_integral(self.V.value)

  def compute_derivative(self, I_ext=0. * bu.nA):
    # [ Compute the derivative of membrane potential ]
    # 1. external currents
    I_ext = I_ext / self.A
    # 1.axial currents
    I_axial = diffusive_coupling(self.V.value, self.connection, self.resistances) / self.A
    # 2. synapse currents
    I_syn = self.sum_current_inputs(self.V.value, init=0. * bu.nA / bu.cm ** 2)
    # 3. channel currents
    I_channel = None
    for ch in self.nodes(level=1, include_self=False).subset(IonChannel).values():
      I_channel = ch.current(self.V.value) if I_channel is None else (I_channel + ch.current(self.V.value))
    # 4. derivatives
    self.V.derivative = (I_ext + I_axial + I_syn + I_channel) / self.cm

    # [ integrate dynamics of ion and ion channels ]
    # check whether the children channels have the correct parents.
    channels = self.nodes(level=1, include_self=False).subset(IonChannel)
    for node in channels.values():
      node.compute_derivative(self.V.value)

  def after_integral(self, *args):
    self.V.value = self.sum_delta_inputs(init=self.V.value)
    self.spike.value = (self.spk_fun((self.V_th - self._last_V) / bu.mV) *
                        self.spk_fun((self.V.value - self.V_th) / bu.mV))

    channels = self.nodes(level=1, include_self=False).subset(IonChannel)
    for node in channels.values():
      node.after_integral(self.V.value)

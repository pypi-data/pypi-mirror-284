#!/usr/bin/env python

# Copyright 2021 daohu527 <daohu527@gmail.com>
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

# ===================================================
#  file:       odrSpiral.c
# ---------------------------------------------------
#  purpose:	free method for computing spirals
#             in OpenDRIVE applications
# ---------------------------------------------------
#  using methods of CEPHES library
# ---------------------------------------------------
#  first edit:	09.03.2010 by M. Dupuis @ VIRES GmbH
#  last mod.:  02.05.2017 by Michael Scholz @ German Aerospace Center (DLR)
# ===================================================
#  Copyright 2010 VIRES Simulationstechnologie GmbH
#  Copyright 2017 German Aerospace Center (DLR)
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  NOTE:
#  The methods have been realized using the CEPHES library
#     http://www.netlib.org/cephes/
#  and do neither constitute the only nor the exclusive way of implementing
#  spirals for OpenDRIVE applications. Their sole purpose is to facilitate
#  the interpretation of OpenDRIVE spiral data.
#

# https://github.com/DLR-TS/odrSpiral/blob/master/src/odrSpiral.c

import math
from typing import List,Tuple


# S(x) for small x

sn = [ \
-2.99181919401019853726E3, \
7.08840045257738576863E5, \
-6.29741486205862506537E7, \
2.54890880573376359104E9, \
-4.42979518059697779103E10, \
3.18016297876567817986E11, \
]

sd = [ \
2.81376268889994315696E2, \
4.55847810806532581675E4, \
5.17343888770096400730E6, \
4.19320245898111231129E8, \
2.24411795645340920940E10, \
6.07366389490084639049E11, \
]

# C(x) for small x

cn = [ \
-4.98843114573573548651E-8, \
9.50428062829859605134E-6, \
-6.45191435683965050962E-4, \
1.88843319396703850064E-2, \
-2.05525900955013891793E-1, \
9.99999999999999998822E-1, \
]

cd = [ \
3.99982968972495980367E-12, \
9.15439215774657478799E-10, \
1.25001862479598821474E-7, \
1.22262789024179030997E-5, \
8.68029542941784300606E-4, \
4.12142090722199792936E-2, \
1.00000000000000000118E0, \
]

# Auxiliary function f(x)

fn = [ \
4.21543555043677546506E-1, \
1.43407919780758885261E-1, \
1.15220955073585758835E-2, \
3.45017939782574027900E-4, \
4.63613749287867322088E-6, \
3.05568983790257605827E-8, \
1.02304514164907233465E-10, \
1.72010743268161828879E-13, \
1.34283276233062758925E-16, \
3.76329711269987889006E-20, \
]

fd = [ \
7.51586398353378947175E-1, \
1.16888925859191382142E-1, \
6.44051526508858611005E-3, \
1.55934409164153020873E-4, \
1.84627567348930545870E-6, \
1.12699224763999035261E-8, \
3.60140029589371370404E-11, \
5.88754533621578410010E-14, \
4.52001434074129701496E-17, \
1.25443237090011264384E-20, \
]

# Auxiliary function g(x)

gn = [ \
5.04442073643383265887E-1, \
1.97102833525523411709E-1, \
1.87648584092575249293E-2, \
6.84079380915393090172E-4, \
1.15138826111884280931E-5, \
9.82852443688422223854E-8, \
4.45344415861750144738E-10, \
1.08268041139020870318E-12, \
1.37555460633261799868E-15, \
8.36354435630677421531E-19, \
1.86958710162783235106E-22, \
]

gd = [ \
1.47495759925128324529E0, \
3.37748989120019970451E-1, \
2.53603741420338795122E-2, \
8.14679107184306179049E-4, \
1.27545075667729118702E-5, \
1.04314589657571990585E-7, \
4.60680728146520428211E-10, \
1.10273215066240270757E-12, \
1.38796531259578871258E-15, \
8.39158816283118707363E-19, \
1.86958710162783236342E-22, \
]


def polevl(x : float, coef : List[float], n : int) -> float:
  assert(n > 0)

  ans = coef[0]
  i = 1

  while i <= n:
    ans = ans * x + coef[i]
    i += 1

  return ans


def p1evl(x : float, coef : List[float], n : int) -> float:
  assert(n > 1)

  ans = x + coef[0]
  i = 1

  while i < n:
    ans = ans * x + coef[i]
    i += 1

  return ans


def fresnel(xxa : float) -> Tuple[float, float]:
  x = math.fabs(xxa)
  x2 = x * x

  if x2 < 2.5625:
    t = x2 * x2
    ss = x * x2 * polevl(t, sn, 5) / p1evl(t, sd, 6)
    cc = x * polevl(t, cn, 5) / polevl(t, cd, 6)
  elif x > 36974.0:
    cc = 0.5
    ss = 0.5
  else:
    x2 = x * x
    t = math.pi * x2
    u = 1.0 / (t * t)
    t = 1.0 / t
    f = 1.0 - u * polevl(u, fn, 9) / p1evl(u, fd, 10)
    g = t * polevl(u, gn, 10) / p1evl(u, gd, 11)

    t = math.pi * 0.5 * x2
    c = math.cos(t)
    s = math.sin(t)
    t = math.pi * x
    cc = 0.5 + (f * s - g * c) / t
    ss = 0.5 - (f * c + g * s) / t

  if xxa < 0.0:
    cc = -cc
    ss = -ss

  return cc, ss


def odr_spiral(s : float, cDot : float) -> Tuple[float, float, float]:
  """compute the actual "standard" spiral, starting with curvature 0

  Args:
      s (float): run-length along spiral
      cDot (float): first derivative of curvature [1/m2]

  Returns:
      Tuple[float, float, float]:
      resulting x-coordinate in spirals local co-ordinate system [m]
      resulting y-coordinate in spirals local co-ordinate system [m]
      tangent direction at s [rad]
  """
  a = 1.0 / math.sqrt(math.fabs(cDot))
  a *= math.sqrt(math.pi)

  x, y = fresnel(s/a)
  x *= a
  y *= a

  if cDot < 0.0:
    y *= -1

  t = s * s * cDot * 0.5

  return x, y, t


def odr_arc(s : float, curv : float) -> Tuple[float, float]:
  """compute the actual arc

  Args:
      s (float): run-length along arc
      curv (float): curvature

  Returns:
      Tuple[float, float]:
      resulting x-coordinate in spirals local co-ordinate system [m]
      resulting y-coordinate in spirals local co-ordinate system [m]
  """
  theta = s * curv
  r = 1 / curv
  x = r * math.sin(theta)
  y = r - r * math.cos(theta)
  return x, y, theta


if __name__ == '__main__':
  for s in range(300):
    x, y, t = odr_spiral(s, 0.5)
    print("{:10.4f} {:10.4f}".format(x, y))

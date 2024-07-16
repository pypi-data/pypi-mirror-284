# Copyright 2023-2024 Geoffrey R. Scheller
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

from grscheller.datastructures.tuples import FTuple

class TestFTuple:
    def test_method_returns_copy(self) -> None:
        ft1 = FTuple(1, 2, 3, 4, 5, 6)
        ft2 = ft1.map(lambda x: x % 3)
        ft3 = ft1.copy()
        assert ft2[2] == ft2[5] == 0
        assert ft1[2] is not None and ft1[2]*2 == ft1[5] == 6

    def test_empty(self) -> None:
        ft1: FTuple[int] = FTuple()
        ft2: FTuple[int] = FTuple()
        assert ft1 == ft2
        assert ft1 is not ft2
        assert not ft1
        assert not ft2
        assert len(ft1) == 0
        assert len(ft2) == 0
        ft3 = ft1 + ft2
        assert ft3 == ft2 == ft3
        assert ft3 is not ft1
        assert ft3 is not ft2
        assert not ft3
        assert len(ft3) == 0
        assert type(ft3) == FTuple
        ft4 = ft3.copy()
        assert ft4 == ft3
        assert ft4 is not ft3
        assert ft1[0] is None
        assert ft2[42] is None

    def test_indexing(self) -> None:
        ft0: FTuple[str] = FTuple()
        ft1 = FTuple("Emily", "Rachel", "Sarah", "Rebekah", "Mary")
        assert ft1[2] == "Sarah"
        assert ft1[0] == "Emily"
        assert ft1[-1] == "Mary"
        assert ft1[1] == "Rachel"
        assert ft1[-2] == "Rebekah"
        assert ft1[42] == None
        assert ft0[0] == None

    def test_slicing(self) -> None:
        ft0: FTuple[int] = FTuple()
        ft1: FTuple[int]  = FTuple(*range(0,101,10))
        assert ft1 == FTuple(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
        assert ft1[2:7:2] == FTuple(20, 40, 60)
        assert ft1[8:2:-2] == FTuple(80, 60, 40)
        assert ft1[8:] == FTuple(80, 90, 100)
        assert ft1[8:-1] == FTuple(80, 90)
        assert ft1 == ft1[:]
        assert ft1[8:130] == FTuple(80, 90, 100)
        assert ft0[2:6] == FTuple()

    def test_map(self) -> None:
        ft0: FTuple[int] = FTuple()
        ft1: FTuple[int]  = FTuple(*range(6))
        assert ft1 == FTuple(0, 1, 2, 3, 4, 5)

        assert ft1.map(lambda x: x*x) == FTuple(0, 1, 4, 9, 16, 25)
        assert ft0.map(lambda x: x*x) == FTuple()

    def test_foldL(self) -> None:
        ft0: FTuple[int] = FTuple()
        ft1: FTuple[int]  = FTuple(*range(1, 6))
        assert ft1 == FTuple(1, 2, 3, 4, 5)

        assert ft1.foldL(lambda x, y: x*y) == 120
        assert ft0.foldL(lambda x, y: x*y) is None
        assert ft1.foldL1(lambda x, y: x*y, s=10) == 1200
        assert ft0.foldL1(lambda x, y: x*y, s=10) == 10

    def test_foldR(self) -> None:
        ft0: FTuple[int] = FTuple()
        ft1: FTuple[int]  = FTuple(*range(1, 4))
        assert ft1 == FTuple(1, 2, 3)

        assert ft1.foldR(lambda x, y: y*y - x) == 48
        assert ft0.foldR(lambda x, y: y*y - x) == None
        assert ft1.foldR1(lambda x, y: y*y - x, s=5) == 232323
        assert ft0.foldR1(lambda x, y: y*y - x, s=5) == 5

    def test_accummulate(self) -> None:
        ft0: FTuple[int] = FTuple()
        ft1: FTuple[int]  = FTuple(*range(1,6))
        assert ft1 == FTuple(1, 2, 3, 4, 5)

        assert ft1.accummulate(lambda x, y: x+y) == FTuple(1, 3, 6, 10, 15)
        assert ft0.accummulate(lambda x, y: x+y) == FTuple()
        # assert ft1.accummulate1(lambda x, y: x+y, s=1) == FTuple(1, 2, 4, 7, 11, 16)
        # assert ft0.accummulate1(lambda x, y: x+y, s=1) == FTuple(1)

    def test_flatmap(self) -> None:
        ft0: FTuple[int] = FTuple()
        ft1 = FTuple(4, 2, 3, 5)
        ft2 = FTuple(4, 2, 0, 3)

        def ff(n: int) -> FTuple[int]:
            return FTuple(*range(n))

        fm = ft1.flatMap(ff)
        mm = ft1.mergeMap(ff)
        em = ft1.exhaustMap(ff)

        assert fm == FTuple(0, 1, 2, 3, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4)
        assert mm == FTuple(0, 0, 0, 0, 1, 1, 1, 1)
        assert em == FTuple(0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4)

        fm = ft2.flatMap(ff)
        mm = ft2.mergeMap(ff)
        em = ft2.exhaustMap(ff)

        assert fm == FTuple(0, 1, 2, 3, 0, 1, 0, 1, 2)
        assert mm == FTuple()
        assert em == FTuple(0, 0, 0, 1, 1, 1, 2, 2, 3)

        fm = ft0.flatMap(ff)
        mm = ft0.mergeMap(ff)
        em = ft0.exhaustMap(ff)

        assert fm == FTuple()
        assert mm == FTuple()
        assert em == FTuple()

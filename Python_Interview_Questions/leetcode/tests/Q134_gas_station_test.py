import pytest
from leetcode.problem_sets.Q134_gas_station import canCompleteCircuit

print(canCompleteCircuit.__doc__)

def test_canCompleteCircuit():
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    assert canCompleteCircuit(gas, cost) == 3

    gas = [2,3,4]
    cost = [3,4,3]
    assert canCompleteCircuit(gas, cost) == -1
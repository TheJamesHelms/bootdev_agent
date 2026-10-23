#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

from pkg.calculator import Calculator

calculator = Calculator()

# Test the specific bug: 3 + 7 * 2
result = calculator.evaluate("3 + 7 * 2")
print(f"3 + 7 * 2 = {result}")
print(f"Expected: 17 (since 7 * 2 = 14, then 3 + 14 = 17)")
print(f"Bug was: 20 (incorrect order of operations)")

# Verify other tests still pass
print(f"\nOther test cases:")
print(f"3 * 4 + 5 = {calculator.evaluate('3 * 4 + 5')} (expected 17)")
print(f"2 * 3 - 8 / 2 + 5 = {calculator.evaluate('2 * 3 - 8 / 2 + 5')} (expected 7)")
print(f"3 + 5 = {calculator.evaluate('3 + 5')} (expected 8)")
print(f"3 * 4 = {calculator.evaluate('3 * 4')} (expected 12)")
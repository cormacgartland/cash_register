from cash_register import ChangeCalculator

c = ChangeCalculator()

print("Please enter total and amount given")

inp = input()
calc = c.change_calculate(inp)          #returns total_change
deno = c.change_denominations(calc)     #converts total_change into respective denoms
rand = c.random_eval(calc)              # SHOULD convert denoms to random if cents fromt total divisible by 3
digit = c.get_last_digits(calc)         # retrieves cents value from total (pre total_change calculation)


if digit % 3 != 0:
    print(deno)
if digit % 3 == 0:
    print(rand)

# print(rand)
# print(deno)
# print(rand)
# print(digit)
# print(rand)
# print(type(digit))


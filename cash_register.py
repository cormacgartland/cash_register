class ChangeCalculator():

    # convert_to_float() only still present for the sake of the initial 
    # tests. All of it's practical functionality has been adapted in 
    # the change_calculate() function.
    def convert_to_float(self, currency):

        new_curr = currency.split(",")
        total = float(new_curr[0])
        amt_given = float(new_curr[1])

        return total, amt_given

    def change_calculate(self, currency):

        # Gets a string value of total, amount paid
        new_curr = currency.split(",")          # splits tuple into a list
        total = float(new_curr[0])              # converts each to floats
        amt_given = float(new_curr[1])

        total_01 = int(total * 100)             # multiply both by 100 to avoid
        amt_given_01 = int(amt_given * 100)     # floating point arithmetic
        

        total_div_3 = self.get_last_digits(total_01)
        print(total_div_3)

        if amt_given < total:
            return False
        elif total_div_3 % 3 == 0:
            print('should be doing random')
            total_change = amt_given_01 - total_01
            return self.random_eval(total_change / 100)
        else:
            total_change = amt_given_01 - total_01
            print('total change')
            print(type(total_change))
            print(type(amt_given_01))
            print(type(total_01))
            return self.change_denominations(total_change / 100)
            # return total_change, total_div_3
        

    def get_last_digits(self, num):
        # num = num * 100
        total_coins = int(str(num)[-2:])
        # total_coins = abs(num) % 100 does not work for random
        print(f"num is {num}")
        return total_coins
   
    def change_denominations(self, total_change):
        print("change_denominations_function")
        print(total_change)
        total_change = total_change * 100
        denom_dict = {
            "dollar_amt": 0,
            "quarter_amt": 0,
            "dime_amt": 0,
            "nickel_amt": 0,
            "penny_amt": 0   
        }
        
        denom_dict["dollar_amt"], total_change = self.denom_conversion(total_change, 100)
        denom_dict["quarter_amt"], total_change = self.denom_conversion(total_change, 25)
        denom_dict["dime_amt"], total_change = self.denom_conversion(total_change, 10)
        denom_dict["nickel_amt"], total_change = self.denom_conversion(total_change, 5)
        denom_dict["penny_amt"], total_change = self.denom_conversion(total_change, 1)

        dollar_amt = denom_dict["dollar_amt"]
        quarter_amt = denom_dict["quarter_amt"]
        dime_amt = denom_dict["dime_amt"]
        nickel_amt = denom_dict["nickel_amt"]
        penny_amt = denom_dict["penny_amt"]

        denoms = ""

        if dollar_amt < 1:
            pass
        elif dollar_amt > 1:
            denoms += f"{dollar_amt} dollars, "
        else:
            denoms += f"{dollar_amt} dollar, "

        if quarter_amt < 1:
            pass 
        elif quarter_amt > 1:
            denoms += f"{quarter_amt} quarters, "
        else:
            denoms += f"{quarter_amt} quarter, "

        if dime_amt < 1:
            pass
        elif dime_amt > 1:
            denoms += f"{dime_amt} dimes, "
        else:
            denoms += f"{dime_amt} dime, "

        if nickel_amt < 1:
            pass
        elif nickel_amt > 1:
            denoms += f"{nickel_amt} nickels, "
        else:
            denoms += f"{nickel_amt} nickel, "

        if penny_amt < 1:
            pass
        elif penny_amt > 1:
            denoms += f"{penny_amt} pennies"
        else:
            denoms += f"{penny_amt} penny"

        return denoms


    def denom_conversion(self, total_change, change):
        print('denom conversion_function')
        print(change)
        print(type(total_change))
        print(type(total_change))
        denom_amt = 0
        while total_change >= change:
            if total_change >= change:
                total_change -= change
                denom_amt += 1
            
        return denom_amt, total_change

    def rand_denom_conversion(self, total_change, change, denom_amt):
        
        # print(type(denom_amt))
        
        # print(type(change))

        if total_change >= change:
            total_change -= change
            denom_amt += 1

        return denom_amt, total_change

    def random_eval(self, total_01):
        print('doing random_eval')
        import random
        # Get current change remaining
        # Make a list of all denominations that fit within that change (is it 12.32 in change? then tens, fives, ones...)
        # Pick one of those at random
        # Add one to that denomination's number
        # Remove the value of that denomination from the current change remaining
        # Is current change 0? Yes? All done! No? Then go back up to the top
        total_01 = total_01 * 100

        DENOMS = {
            "dollar_amt": 0,
            "quarter_amt": 0,
            "dime_amt": 0,
            "nickel_amt": 0,
            "penny_amt": 0   
        }
        

        rand_list = [1, 2, 3, 4, 5]

        
        while total_01 > 0:
            random_choice = random.choice(rand_list)
            if random_choice == 1:
                DENOMS["dollar_amt"], total_01 = self.rand_denom_conversion(total_01, 100, DENOMS["dollar_amt"])
                # print(total_01)
                
            if random_choice == 2:
                DENOMS["quarter_amt"], total_01 = self.rand_denom_conversion(total_01, 25, DENOMS["quarter_amt"])
                # print(total_01)
                
            if random_choice == 3:
                DENOMS["dime_amt"], total_01 = self.rand_denom_conversion(total_01, 10, DENOMS["dime_amt"])
                # print(total_01)
                
            if random_choice == 4:
                DENOMS["nickel_amt"], total_01 = self.rand_denom_conversion(total_01, 5, DENOMS["nickel_amt"])
                # print(total_01)
                
            if random_choice == 5:
                DENOMS["penny_amt"], total_01 = self.rand_denom_conversion(total_01, 1, DENOMS["penny_amt"])
                # print(total_01)
            
        dollar_amt = DENOMS["dollar_amt"]
        quarter_amt = DENOMS["quarter_amt"]
        dime_amt = DENOMS["dime_amt"]
        nickel_amt = DENOMS["nickel_amt"]
        penny_amt = DENOMS["penny_amt"]
        
        
        denoms = ""

        if dollar_amt < 1:
            pass
        elif dollar_amt > 1:
            denoms += f"{dollar_amt} dollars, "
        else:
            denoms += f"{dollar_amt} dollar, "

        if quarter_amt < 1:
            pass 
        elif quarter_amt > 1:
            denoms += f"{quarter_amt} quarters, "
        else:
            denoms += f"{quarter_amt} quarter, "

        if dime_amt < 1:
            pass
        elif dime_amt > 1:
            denoms += f"{dime_amt} dimes, "
        else:
            denoms += f"{dime_amt} dime, "

        if nickel_amt < 1:
            pass
        elif nickel_amt > 1:
            denoms += f"{nickel_amt} nickels, "
        else:
            denoms += f"{nickel_amt} nickel, "

        if penny_amt < 1:
            pass
        elif penny_amt > 1:
            denoms += f"{penny_amt} pennies"
        else:
            denoms += f"{penny_amt} penny"

        return denoms
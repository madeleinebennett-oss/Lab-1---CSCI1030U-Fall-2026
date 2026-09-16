def main():
    cost_per_item = 19.99
    quantity = 5 

    # YOUR CODE FOR PART 1 GOES HERE  

    # calculating the price based on how many items bought
    subtotal_cost = quantity*cost_per_item
    #finding tax amount on subtotal
    tax = subtotal_cost*0.13
    # adding subtotal and tax together
    total_cost = subtotal_cost + tax

    # code i used to check;
    # print(f'{total_cost:0.2f}')

    # YOUR CODE FOR PART 2 GOES HERE
    print(f'cost_per_item = ${cost_per_item:0.2f}') # a sample for you to use for the other prices
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')

    # THIS IS THE CODE FOR PART 3
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    # error message: can only concatenate str (not "float") to str
    # the float variable cannot be concatenated in the string using the "+" arguments
    # to fix, convert the float into a str, then run the code
    investment = str(investment)
    print('After 5 years, your investment will be worth ' + investment + ' dollars.')
    # expected output: After 5 years, your investment will be worth 1187.6863056468749 dollars.


if __name__ == "__main__":
    main()
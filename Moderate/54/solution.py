import sys

currency = {
    1:     'PENNY',
    5:     'NICKEL',
    10:    'DIME',
    25:    'QUARTER',
    50:    'HALF DOLLAR',
    100:   'ONE',
    200:   'TWO',
    500:   'FIVE',
    1000:  'TEN',
    2000:  'TWENTY',
    5000:  'FIFTY',
    10000: 'ONE HUNDRED'
}

coins = [10000,5000,2000,1000,500,200,100,50,25,10,5,1]

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        price, cash = map(lambda x: int(float(x)*100), line.split(';'))
        
        difference = cash - price
        
        if difference < 0:
            print('ERROR')
        elif difference == 0:
            print('ZERO')
        else:
            change = []
            while difference > 0:
                next_coin = max(filter(lambda x: x <= difference, coins))
                change.append(currency[next_coin])
                difference -= next_coin
            
            print(','.join(change))
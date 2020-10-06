print('This is a quick script that will calculate a % loss or gain.')
buy_price = float(input('What is your buy price?  '))
sell_price = float(input('What is the sell/current price? '))

gain_loss = ((sell_price - buy_price) / buy_price) * 100

print('Your gain/loss is {}%.'.format(gain_loss))

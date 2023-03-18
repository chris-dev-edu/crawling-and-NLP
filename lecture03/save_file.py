import pandas
data = [
    ['apple', 15000],
    ['banana', 12000],
    ['grape', 9000],
    ['orange', 10000]
]

data_frame = pandas.DataFrame(data, columns=['fruit', 'price'])
data_frame.to_csv('fruit-and-price.csv', index=False)
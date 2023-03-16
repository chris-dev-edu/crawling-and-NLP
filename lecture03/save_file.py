import pandas

data_frame = pandas.DataFrame([1, 2, 3, 4, 5], columns=['number'])
data_frame.to_csv('test.csv', index=False)
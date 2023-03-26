import pandas

file = pandas.read_table('ratings_test.txt')
print(file)
file.to_csv('ratings_test.csv', index=False)
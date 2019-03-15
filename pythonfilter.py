import statistics

data = [1.3, 2.7, 4.3, 3.3, 6, 4.8]
avg = statistics.mean(data)
hasil = list(filter(lambda x: x > avg, data))
print(hasil)

# data angka bentuk list menggunakan filter

data1 = [1, 3, 4, 6, 3, 7, 8, 4, 7, 5, 4]
gg = 5
hasil2 = list(filter(lambda x: x > gg, data1))
print(hasil2)
print(len(data1))

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# list comprehension lebih dari 5
data2 = [1, 3, 4, 6, 3, 7, 8, 4, 7, 5, 4]
hasil3 = [
    item for item in data2
    if (
        item > 3
    )
]
print(hasil3)


t = ([1, 2, 3], {'nama': 'Petanikode', 'rank': 123}, True)

print(t)

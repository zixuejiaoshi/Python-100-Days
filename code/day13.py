
person = { # 字典
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101', 
    'tel': '13122334455',
    'emergence contact': '13800998877'
}
print(person) 

# dict函数(构造器)
person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')
print(person)

# 通过Python内置函数zip压缩两个序列并创建字典
person = dict(zip(['name', 'age', 'height', 'weight', 'addr'], ['王大锤', 55, 168, 60, '成都市武侯区科华北路62号1栋101']))
print(person)

# 通过字典推导式创建字典
person = {key: value for key, value in zip(['name', 'age', 'height', 'weight', 'addr'], ['王大锤', 55, 168, 60, '成都市武侯区科华北路62号1栋101'])}
print(person)


# 在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

# 方法1：通过字典推导式创建字典
prices = {key: value for key, value in stocks.items() if value > 100}
print(prices)

# 方法2：通过filter函数创建字典
prices = dict(filter(lambda item: item[1] > 100, stocks.items()))
print(prices)

# 输入一段话，统计每个英文字母出现的次数，按出现次数从高到低输出。
sentence = 'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.'

# 方法1：通过字典推导式创建字典
letter_counts = {letter: sentence.count(letter) for letter in sentence if letter.isalpha()} 
print(letter_counts)

# 方法2：通过collections.Counter类创建字典
from collections import Counter
letter_counts = Counter(letter for letter in sentence if letter.isalpha())
print(letter_counts)

# 方法3：通过defaultdict类创建字典
from collections import defaultdict
letter_counts = defaultdict(int)
for letter in sentence:
    if letter.isalpha():
        letter_counts[letter] += 1
print(letter_counts)
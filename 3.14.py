# import collections
#
# a/ = {'a': 'a', 'b': 'b', 'c': 'cc'}
# b = {'a': 'aa', 'b': 'bb', 'c': 'ccc'}
#
#
# class DeepChainMap(collections.ChainMap):
#     def __setitem__(self, key, value):
#         for mapping in self.maps:
#             if key in mapping:
#
#
#                 if type(mapping[key]) is int and mapping[key] < value:
#                     mapping[key] = value
#             return
#         self.maps[0][key] = value
#
# m = DeepChainMap(a,b)
#
# m['nuw_num'] = -1
# print(m['new_num'])
#




import collections
#
# d = {}
#
# l = ['a', 'a', 'a', 'b', 'c']
# for word in l:
#     if word not in d:
#         d[word] = 0
#
#     d[word] += 1
#
#
# print(d)


# d = {}
#
# l = ['a', 'a', 'a', 'b', 'c']
# for word in l:
#     d.setdefault(word,0)
#     d[word] += 1
# print(d)
#
#
#
# d = collections.defaultdict(int)
# l = ['a', 'a', 'a', 'b', 'c']
#
# for word in l:
#     d[word] += 1
# print(d)
#
#
# d = collections.defaultdict(set)
# s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4),
#      ('red', 1), ('blue', 4)]
#
# for k, v in s:
#     d[k].add(v)
#
# print(d)


# l = ['a', 'a', 'a', 'b', 'c']
#
#
# c = collections.Counter()
#
# for word in l:
#
#     c[word] += 1
# print(c)
# print(c.most_common(1))
# print(sum(c.values()))
#
# import re
#
# with open('main.py', 'r') as f:
#     words = re.findall(r'\w+', f.read().lower())
#     print(collections.Counter(words).most_common(20))



#
# import collections
# import queue
#
# collections.deque
#
#
#
# q = queue.Queue()
# lq = queue.LifoQueue()
# l = []
#
# d = collections.deque()
#
# for i in range(3):
#     q.put(i)
#     lq.put(i)
#     l.append(i)
#     d.append(i)
#
# # for _ in range(3):
# #     print('FIFO queue = {}'.format(q.get()))
# #     print('LIFO queue = {}'.format(lq.get()))
# #     print('list = {}'.format(l.pop()))
# #     print('deque = {}'.format(d.pop()))
# #     print()
#
#
# # d.rotate()
# print(d)
# d.extendleft('x')
# print(d)
# # print(d)




# # import collections
#
# # p = (10, 20)
# # print(p[0])
# # # p[0] = 100
#
# # class Point(object):
#       # def __init__(self, x, y):
# #         self.__x = x
# #         self.y = y
# # p = Point(10,20)
# # print(p.x)
# #
#
#
# import csv
# import collections
#
# with open('name.csv', 'w')
#
# Point = collections.namedtuple('Point', 'x, y')
#
# p = Point(10, y=20)
# print(p.x)
#
# p1 = Point._make([100, 200])
# print(p1)
# print(p1._asdict())






# print(p1)
# print(p1._asdict(x=400))
# p1._replace()
# print(p1)
# p2 = p1._replace(x=400)
# print(p2)
#
# class SumPoint(collections.namedtuple('Point', ['x', 'y'])):
#
#     @property
#     def total(self):
#         return self.x + self.y
#
#
# p3 = SumPoint(2, 3)
# print(p3.x, p3.y, p3.total)






# import collections
#
# od1 = collections.OrderedDict(
# {'banana': 3, 'apple': 4, 'pear': 1, 'arange': 4}
#
# )
# d = {'apple': 4, 'banana': 3, 'pear': 1, 'arange': 4}
#
#
# # print(d == od1)
#
#
# od = collections.OrderedDict(
#     sorted(d.items(), key=lambda t: len(t[0])))
# od['cc'] = 100
# print(od)


# import re
#     #
#     # m = re.match('a.c', 'abc')
#     #
#     # print(m)
#     #
#     # # print(m.group())
#     #
#     # # m = re.search('a.c', 'test abc test')
#     # # print(m)
#     # # print(m.span())
#     # # print(m.group())
#     #
#     # m = re.finditer('a.c', 'test abc test abc')
#     # print([w.group() for w in m])
#     # # print(m)
#     #
#     # # print(m.s)
#
# m = re.match('ab?', 'a')
# print(m)


#
#
#
# import string
# def caesar_cipher(text: str, shift: int) -> Generator[Tuple[int, str], None, None]:
#     result = ''
#     len_alphabet = ord('Z') - ord('A') + 1
#     for candidate_shift in range(1, len_alphabet + 1):
#         reveted = ''
#         for char in text:
#             if char.isupper():
#                 alphabet = string.ascii_uppercase
#             elif char.islower():
#                 alphabet = string.ascii_lowercase
#
#             else:
#                 reveted += char
#
#                 continue
#             index = alphabet.index(char) - candidate_shift
#
#             if index < 0:
#                 index += len_alphabet
#             reveted += alphabet[index]
#     yield candidate_shift, reveted
#
#
#
#     for char in text:
#     #     if char.isupper():
#     #         alphabet = string.ascii_uppercase
#     #     elif char.islower():
#     #         alphabet = string.ascii_lowercase
#     #     else:
#     #         result += char
#     #         continuefor
#
#
#
#
#
# if __name__ == '__main__':
#     # e = caesar_cipher('this is a pen', 9)
#     # print(e)
#     # d = caesar_cipher(e, -9)
#     # print(d)
#
#
#     for shift_num, decrypted in c




# import string
#
#
# ALPHABET = string.ascii_uppercase
#
# def generate_key(message: str, keyword: str) -> str:
#     key = keyword
#
#     remain_length = len(message) - len(keyword)
#     for i in range(remain_length):
#         key += key[i]
#     return key
#
# def encrypt(message: str, key: str) -> str:
#     result = ''
#     for i, char in enumerate(message):
#         if char not in ALPHABET:
#             result += char
#
#             continue
#
#        index = ()

#
# def hanoi(disk:int, src: str, dest: str, center: str):
#     if disk < 1:
#         return
#
#     hanoe
#     print(f'move {disk} from {src} to {dest}')
#
#
# if __name__ == '__main__':
#     hanoi(1, 'A', 'c', 'B')



# from typing import List
#
# def generate_pascal_triangle(depth: int) -> List[List[int]]:
#     data = [[1] * (i+1) for i in range(depth)]
#     for line in range(2, depth):
#         for i in range(1, line):
#             data[line][i] = data[line-1][i-1] + data[line-1][i]
#     return data
#
#
# def print_pascal(data: List[int]) -> None:
#     max_digit = len(str(max(data[-1])))
#     width = max_digit + (max())
#
#
#     for index, line in enumerate(data):
#         numbers = ''.join([str(i).center(6, '') for i in line])
#
#
# if __name__ == '__main__':
# # z    for r in generate_pascal_triangle(5):
#         # print(r)
#     print_pascal(8)


# from typing import List
#
# def generate_triangle_list(depth: int, max_num:  int) -> List[List[int]]:
#     return [[random.randint(0, max_num) for _ in range(i)] for i in range(1, depth+1)]
#
# # def print_triangle
#
# def sum_min_path(triangle: List[List[int]]) -> int:
#



# def f(x:int, y:int):
#     num = x+y
#     return num
#
#
#
# print('ffff', f(8,8))






#
# class Node(object):
#     def __init__(self, value: int) -> None:
#         self.value = value
#         self.right = None
#         self.left = None
#
# def insert(node: Node, value: int) -> Node:
#
#     if node is None:
#         return Node(value)
#     if value < node.value:
#         node.left = insert(node.left, value)
#     else:
#         node.right = insert(node.right, value)
#     return node
#
#
#
#
# def inorder(node: Node) -> None:
#     if node is not None:
#         inorder(node.left)
#         print(node.left)
#         inorder(node.right)
#
#
# def search(node: Node, value: int) -> bool:
#     if node is None:
#         return False
#
#     if node.value == value:
#         return True
#
#     elif node.value < value:
#         return search(node.left, value)
#     elif node.value  value:
#         return search(node.right, value)
#
#
# def min_value(node: Node) -> Node:
#     current = node
#
#     while current.left in None
#
#
#
# def remove(node: Node, value: int) -> Node:
#     if node is Node:
#         return node
#
#
# if __name__ == '__main__':
#     root = None
#     root = insert(root, 5)
#     root = insert(root, 6)
#     root = insert(root, 2)
#     # print(root.value)
#     # print(root.right.value)
#     # inorder(root)
#     print(search(root,4))





import contextlib










# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print('<{}>'.format(name))
#             r = f(content)
#             print('<{}>'.format(name))
#
#             return r
#
#         return _wrapper
# #     return _tag
# #
# # @tag('h3')
# # def f(content):
# #     print(content)
# #
# # # f('test')
# #
# # @contextlib.contextmanager
# #
# # def tag(name):
# #     print('<{}>'.format(name))
# #     yield
# #     print('<{}>'.format(name))
# #
# #
# #
# # with tag('h2'):
# #     print('test')
# #
# # #
# # # @tag('h2')
# # # def f(content):
# # #     print(content)
# # #
# # # f('test')
# # import contextlib
# #
# # class tag(contextlib.ContextDecorator):
# #     def __init__(self,name):
# #         self.name = name
# #         self.start_tag = '<{}>'.format(name)
# #         self.end_tag = '<{}>'.format(name)
# #     def __enter__(self):
# #         print(self.start_tag)
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         print(exc_type)
# #         print(exc_val)
# #         print(exc_tb)
# #         print(self.end_tag)
# #
# #
# # with tag('h3'):
# #     raise Exception('error')
# #     print('test')
#
#
# import contextlib
#
# import os
#
#
# try:


# import contextlib
#
# import os
#
#
# try:
#     os.remove('somefile.tmp')
# except FileNotFoundError:
#     pass
#
# with contextlib.suppress(FileNotFoundError):
#     os.remove('somefile.tmp')

# import sys
#
# x = input('')
#
# import sys
# import logging
#
# for line in sys.stdin:
#     print(line)
#
#
# print('hello')
# # sys.stdout.write('hello')
#
# logging.error('error')
# sys.stderr.write('error')

def is_ok_job():
    try:
        print('do something')
    except Exception:
        return False


def cleanup():
    print('clean up')
#
# is_ok = is_ok_job()
# print('more task')
# if not is_ok:
#     cleanup()

# import io
# import requests
# import zipfile
#
# f = io.ByteIO()
#
# r = requests.get(url)
# f.write(r.content)



# import collections
#
# d = {}
# l = ['a', 'a', 'a', 'b', 'b', 'c']
# for word in l:
#     if word not in d:
#         d[word] = 0
#
#         d [word] += 1
# print(d)
#
#
#
# d = collections.defaultdict(int)
# l = ['a', 'a', 'a', 'b', 'b', 'c']
# for word in l:
#     d[word] += 1
# print(d)
#
# d = collections.defaultdict(set)
# s = [('red', 1), ('blue', 2), ('red',4), ('red', 5)]
# for k, v in s:
#     d[k].add(v)
# print(d)


# #
# # import re
# #
# #
# # with open('3.14.py', 'r') as f:
# #     words = re.findall(r'\w+', f.read().lower())
# #     print(words)
#
#
# # import collections
# # import queue
# #
# # q = queue.Queue()
# # lq = queue.LifoQueue()
# # l = []
# # d = collections.deque()
# #
# #
# # for i in range(3):
# #     q.put(i)
# #     lq.put(i)
# #     l.append(i)
# #     d.append(i)
# #
# # for _ in range
#
# #
# # import collections
# #
# # p = (10,20)
# #
# # # print(p[0])
# # # class Point(object):
# # #     def __init__(self, x, y):
# # #         self.x = x
# # #         self.y = y
# # #
# #
# # Point = collections.namedtuple('Point', ['x', 'y'])
# # p = Point(10,20)
#
#
#
#
# class SumPoint(collections.namedtuple('Point', ['x', 'y'])):


# import collections
#
# d = collections.OrderedDict({'banana': 2, 'apple': 7, 'pear': 8, 'orange': 3})
#
# print(d)j

# import re
#
# # print(m.group())
#
# # print(m.group())
#
# # m = re.match('\W', '@')
# # m = re.match('\w', '@')
# # print(m)
# #
# #
# # m = re.match('[0-9]')
# #
# # m = re.match('a|b', 'x')
# # m = re.match('\s', '')
# # m = re.search('^abc', 'test abc')
# # m = re.search('^abc','test abc')
# # m
#
#
# m = re.search('^abc', 'abc')
#
# s


import re


RE_STACK_ID = re.compile(
    r'arn:aws:cloudformation:us-east-2:123456789012:stack/'
     'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786''
)


s1 = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
     'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')

s2 = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
     'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')

for s in [s1, s2]:


#
# m = re.match(r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<acount_id>[\d])+:stack/[\W-]+/[\w-]+', s)
# print(m)
#



    m = RE_STACK_ID.match(s)
if m:
    print('go next')
    print(m.group('region'))
    print(m.group('stack_name'))
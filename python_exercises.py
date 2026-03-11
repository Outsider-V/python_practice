# python_exercises.py

# 1️⃣ List Exercise: Find all duplicates in a list
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


# 2️⃣ Set Exercise: Return elements only in the first set
def difference_set(a, b):
    # 使用集合的差集操作符 '-'
    return a - b


# 3️⃣ Tuple Exercise: Return a tuple with all elements squared
def square_tuple(tpl):
    # 使用生成器表达式处理元组
    return tuple(x ** 2 for x in tpl)


# 4️⃣ Dictionary Exercise: Merge two dictionaries and sum values of common keys
def merge_dicts(d1, d2):
    # 先创建一个 d1 的副本，不修改原数据
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


# 5️⃣ OOP Exercise: Simple ToDo list
class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self):
        # 返回一个浅拷贝，防止外部直接修改内部列表
        return list(self.tasks)


# 6️⃣ Function Exercise: Flatten nested list (one level)
def flatten_list_once(lst):
    result = []
    for item in lst:
        # 检查元素是否为列表
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result
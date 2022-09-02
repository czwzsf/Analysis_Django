"""
一些用来处理从数据库返回回来数据的处理类
"""


class Basedataprocessing:
    def __int__(self, data):
        self.data = data

    def remove_duplicates(self):
        """
        处理重复项后的数组值
        :return: date
        :rtype: list
        """
        date = list(set(self.data))
        return date

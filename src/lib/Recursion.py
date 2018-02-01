"""
@File: Recursion
@Author: Ray
@Date: 2018-01-29 19:36:10
@Version: 1.0
"""


class GetDictParam:
    """
        这是一个解析dict 参数的类
        可以用于多参数的指定key 、 指定key集合解析key
    """
    @classmethod
    def get_value(cls, my_dict: dict, key: str):
        """
            这是一个递归函数
        """
        if isinstance(my_dict, dict):
            if my_dict.get(key) or my_dict.get(key) == 0 or my_dict.get(key) == ''\
                    and my_dict.get(key) is False or my_dict.get(key) == []:
                return my_dict.get(key)

            for my_dict_key in my_dict:
                if cls.get_value(my_dict.get(my_dict_key), key) or \
                                cls.get_value(my_dict.get(my_dict_key), key) is False:
                    return cls.get_value(my_dict.get(my_dict_key), key)

        if isinstance(my_dict, list):
            for my_dict_arr in my_dict:
                if cls.get_value(my_dict_arr, key) \
                        or cls.get_value(my_dict_arr, key) is False:
                    return cls.get_value(my_dict_arr, key)

    @classmethod
    def list_for_key_to_dict(cls, *args: tuple, my_dict: dict) -> dict:
        """
            接收需要解析的dict和 需要包含需要解析my_dict的keys的list
        :param my_dict: 需要解析的字典
        :param args: 包含需要解析的key的多个字符串
            # list_for_key_to_dict("code", "pageNo", "goodsId", my_dict=dict)
        :return: 一个解析后重新拼装的dict
        """
        result = {}
        if len(args) > 0:
            for key in args:
                result.update({key: cls.get_value(my_dict, key)})
        return result

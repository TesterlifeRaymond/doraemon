"""
@Version: 1.0
@Project: doraemon
@Author: Raymond
@Data: 2018/1/31 下午7:43
@File: test_doraemon_package.py
@License: MIT
"""
import unittest
from src.lib import CasesContainer


class CasesContainerCase(unittest.TestCase):
    """ test container class """
    def test_container_is_not_null(self):
        """
            test container result is not null
        @assert: self.assertIsNotNone
        """
        self.assertIsNotNone(CasesContainer)

    def test_conainer_get_data(self):
        """
            test get container data
        @assert: data['class_name'], data['methods_name']
        """
        data = {
            "class_name": CasesContainerCase,
            "methods_name": 'test_conainer_get_data'
        }
        container = CasesContainer(data)
        self.assertEqual(data['class_name'], container.body['class_name'])
        self.assertEqual(data['methods_name'], container.body['methods_name'])

    def test_notputdata_in_container(self):
        """ test notputdata in container
        @assert: data is none
        """
        container = CasesContainer({})
        self.assertIsNone(container.body.get('class_name'))
        self.assertIsNone(container.body.get('methods_name'))


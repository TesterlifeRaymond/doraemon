# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    use_case_operation.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ray <liujinjia@testerlife.com>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/31 15:34:16 by jinjialiu         #+#    #+#              #
#    Updated: 2017/05/31 15:37:22 by ray              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ..controller import util


class UseCaseOperation:
    """ test constructor operation """

    @classmethod
    @util.AddCaseWrapper("test_case")
    def add_test_case(cls, uri=None, class_name=None, func_name=None, body=None, kwassert=None):
        """ 根据表字段增加test constructor """

    @classmethod
    @util.QueryCaseInfo("test_case")
    def query_test_case_info(cls, **kwargs):
        """ 查询指定case的全部信息 """

    @classmethod
    @util.CleaerTestCase("test_case")
    def clear_test_data(cls):
        """修改sqlite中已经跑完的case的type字段状态"""

"""
@ Version : ??
@ Author  : liujinjia
@ File    : __init__.py
@ Project : base_test
@ Create Time: 2017-05-19 16:40
"""

from .add_case import AddCaseWrapper
from .clear_data import CleaerTestCase
from .query_case import QueryCaseInfo
from .data import UserRequestData

use_http = UserRequestData()

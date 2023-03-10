# -*- coding: utf-8 -*-
# MinIO Python Library for Amazon S3 Compatible Cloud Storage,
# (C) 2016 MinIO, Inc.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import itertools
import unittest.mock as mock
from unittest import TestCase

from minio import Minio
from minio.api import _DEFAULT_USER_AGENT
from minio.deleteobjects import DeleteObject

from .minio_mocks import MockConnection, MockResponse


class RemoveObjectsTest(TestCase):
    @mock.patch('urllib3.PoolManager')
    def test_object_is_list(self, mock_connection):
        mock_server = MockConnection()
        mock_connection.return_value = mock_server
        mock_server.mock_add_request(
            MockResponse('POST',
                         'https://localhost:9000/hello?delete=',
                         {'User-Agent': _DEFAULT_USER_AGENT,
                          'Content-Md5': u'Te1kmIjQRNNz70DJjsrD8A=='}, 200,
                         content=b'<Delete/>')
        )
        client = Minio('localhost:9000')
        for err in client.remove_objects(
                "hello",
                [DeleteObject("Ab"), DeleteObject("c")],
        ):
            print(err)

    @mock.patch('urllib3.PoolManager')
    def test_object_is_tuple(self, mock_connection):
        mock_server = MockConnection()
        mock_connection.return_value = mock_server
        mock_server.mock_add_request(
            MockResponse('POST',
                         'https://localhost:9000/hello?delete=',
                         {'User-Agent': _DEFAULT_USER_AGENT,
                          'Content-Md5': u'Te1kmIjQRNNz70DJjsrD8A=='}, 200,
                         content=b'<Delete/>')
        )
        client = Minio('localhost:9000')
        for err in client.remove_objects(
                "hello",
                (DeleteObject("Ab"), DeleteObject("c")),
        ):
            print(err)

    @mock.patch('urllib3.PoolManager')
    def test_object_is_iterator(self, mock_connection):
        mock_server = MockConnection()
        mock_connection.return_value = mock_server
        mock_server.mock_add_request(
            MockResponse('POST',
                         'https://localhost:9000/hello?delete=',
                         {'User-Agent': _DEFAULT_USER_AGENT,
                          'Content-Md5': u'Te1kmIjQRNNz70DJjsrD8A=='}, 200,
                         content=b'<Delete/>')
        )
        client = Minio('localhost:9000')
        it = itertools.chain((DeleteObject("Ab"), DeleteObject("c")))
        for err in client.remove_objects('hello', it):
            print(err)

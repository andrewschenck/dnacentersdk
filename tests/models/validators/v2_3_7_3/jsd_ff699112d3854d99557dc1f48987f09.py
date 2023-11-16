# -*- coding: utf-8 -*-
"""Cisco DNA Center GetConfigurationArchiveDetails data model.

Copyright (c) 2019-2021 Cisco Systems.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorFf699112D3854D99557Dc1F48987F09(object):
    """GetConfigurationArchiveDetails request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorFf699112D3854D99557Dc1F48987F09, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "archiveResultlist": {
                "items": {
                "properties": {
                "deviceId": {
                "type": "string"
                },
                "deviceName": {
                "type": "string"
                },
                "ipAddress": {
                "type": "string"
                },
                "versions": {
                "items": {
                "properties": {
                "configChangeType": {
                "type": "string"
                },
                "createdBy": {
                "type": "string"
                },
                "createdTime": {
                "type": "number"
                },
                "files": {
                "items": {
                "properties": {
                "downloadPath": {
                "type": "string"
                },
                "fileId": {
                "type": "string"
                },
                "fileType": {
                "type": "string"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "id": {
                "type": "string"
                },
                "startupRunningStatus": {
                "type": "string"
                },
                "syslogConfigEventDto": {
                "properties": {
                "configMethod": {
                "type": "string"
                },
                "deviceUuid": {
                "type": "string"
                },
                "loginIpAddress": {
                "type": "string"
                },
                "outOfBand": {
                "type": "boolean"
                },
                "processName": {
                "type": "string"
                },
                "syslogTime": {
                "type": "string"
                },
                "terminalName": {
                "type": "string"
                },
                "userName": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

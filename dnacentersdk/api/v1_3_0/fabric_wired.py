# -*- coding: utf-8 -*-
"""DNA Center Fabric Wired API wrapper.

Copyright (c) 2019 Cisco and/or its affiliates.

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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
)


class FabricWired(object):
    """DNA Center Fabric Wired API (version: 1.3.0).

    Wraps the DNA Center Fabric Wired
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new FabricWired object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(FabricWired, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def deletes_border_device_from_sda_fabric(self,
                                              device_ip_address,
                                              headers=None,
                                              payload=None,
                                              active_validation=True,
                                              **request_parameters):
        """Deletes border device from sda Fabric.

        Args:
            device_ip_address(basestring): device-ip-address path
                parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(device_ip_address, basestring,
                   may_be_none=False)
        if headers is not None:
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'device-ip-address': device_ip_address,
        }

        _payload = {
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_1e80bb50430b8634_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/border-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=params,
                                             json=_payload, headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=params,
                                             json=_payload)

        return self._object_factory('bpm_1e80bb50430b8634_v1_3_0', json_data)

    def adds_border_device_in_sda_fabric(self,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **request_parameters):
        """Adds border device in SDA Fabric.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_a4b56a5f478a97dd_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/border-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_a4b56a5f478a97dd_v1_3_0', json_data)

    def gets_border_device_details_from_sda_fabric(self,
                                                   device_ip_address,
                                                   headers=None,
                                                   payload=None,
                                                   active_validation=True,
                                                   **request_parameters):
        """Gets border device detail from SDA Fabric.

        Args:
            device_ip_address(basestring): device-ip-address path
                parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(device_ip_address, basestring,
                   may_be_none=False)
        if headers is not None:
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'device-ip-address': device_ip_address,
        }

        _payload = {
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d0b3593c4a7aaf22_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/border-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload, headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_d0b3593c4a7aaf22_v1_3_0', json_data)

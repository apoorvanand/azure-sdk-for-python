# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MachineExtensionInstanceView(Model):
    """Describes the Machine Extension Instance View.

    :param name: The machine extension name.
    :type name: str
    :param type: Specifies the type of the extension; an example is
     "CustomScriptExtension".
    :type type: str
    :param type_handler_version: Specifies the version of the script handler.
    :type type_handler_version: str
    :param status: Instance view status.
    :type status:
     ~azure.mgmt.hybridcompute.models.MachineExtensionInstanceViewStatus
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'type_handler_version': {'key': 'typeHandlerVersion', 'type': 'str'},
        'status': {'key': 'status', 'type': 'MachineExtensionInstanceViewStatus'},
    }

    def __init__(self, *, name: str=None, type: str=None, type_handler_version: str=None, status=None, **kwargs) -> None:
        super(MachineExtensionInstanceView, self).__init__(**kwargs)
        self.name = name
        self.type = type
        self.type_handler_version = type_handler_version
        self.status = status

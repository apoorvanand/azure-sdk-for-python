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

from .resource_py3 import Resource


class MachineExtension(Resource):
    """Describes a Machine Extension.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param type1: The identity type.
    :type type1: str
    :ivar principal_id: The identity's principal id.
    :vartype principal_id: str
    :ivar tenant_id: The identity's tenant id.
    :vartype tenant_id: str
    :param force_update_tag: How the extension handler should be forced to
     update even if the extension configuration has not changed.
    :type force_update_tag: str
    :param publisher: The name of the extension handler publisher.
    :type publisher: str
    :param machine_extension_type: Specifies the type of the extension; an
     example is "CustomScriptExtension".
    :type machine_extension_type: str
    :param type_handler_version: Specifies the version of the script handler.
    :type type_handler_version: str
    :param auto_upgrade_minor_version: Indicates whether the extension should
     use a newer minor version if one is available at deployment time. Once
     deployed, however, the extension will not upgrade minor versions unless
     redeployed, even with this property set to true.
    :type auto_upgrade_minor_version: bool
    :param settings: Json formatted public settings for the extension.
    :type settings: object
    :param protected_settings: The extension can contain either
     protectedSettings or protectedSettingsFromKeyVault or no protected
     settings at all.
    :type protected_settings: object
    :ivar provisioning_state: The provisioning state, which only appears in
     the response.
    :vartype provisioning_state: str
    :param instance_view: The machine extension instance view.
    :type instance_view:
     ~azure.mgmt.hybridcompute.models.MachineExtensionInstanceView
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'type1': {'key': 'identity.type', 'type': 'str'},
        'principal_id': {'key': 'identity.principalId', 'type': 'str'},
        'tenant_id': {'key': 'identity.tenantId', 'type': 'str'},
        'force_update_tag': {'key': 'properties.forceUpdateTag', 'type': 'str'},
        'publisher': {'key': 'properties.publisher', 'type': 'str'},
        'machine_extension_type': {'key': 'properties.type', 'type': 'str'},
        'type_handler_version': {'key': 'properties.typeHandlerVersion', 'type': 'str'},
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'settings': {'key': 'properties.settings', 'type': 'object'},
        'protected_settings': {'key': 'properties.protectedSettings', 'type': 'object'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'instance_view': {'key': 'properties.instanceView', 'type': 'MachineExtensionInstanceView'},
    }

    def __init__(self, *, location: str, tags=None, type1: str=None, force_update_tag: str=None, publisher: str=None, machine_extension_type: str=None, type_handler_version: str=None, auto_upgrade_minor_version: bool=None, settings=None, protected_settings=None, instance_view=None, **kwargs) -> None:
        super(MachineExtension, self).__init__(location=location, tags=tags, type1=type1, **kwargs)
        self.force_update_tag = force_update_tag
        self.publisher = publisher
        self.machine_extension_type = machine_extension_type
        self.type_handler_version = type_handler_version
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.settings = settings
        self.protected_settings = protected_settings
        self.provisioning_state = None
        self.instance_view = instance_view

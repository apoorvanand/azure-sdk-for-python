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

try:
    from ._models_py3 import AccessUri
    from ._models_py3 import ApiError
    from ._models_py3 import ApiErrorBase
    from ._models_py3 import CreationData
    from ._models_py3 import Disk
    from ._models_py3 import DiskAccess
    from ._models_py3 import DiskAccessUpdate
    from ._models_py3 import DiskEncryptionSet
    from ._models_py3 import DiskEncryptionSetUpdate
    from ._models_py3 import DiskSku
    from ._models_py3 import DiskUpdate
    from ._models_py3 import Encryption
    from ._models_py3 import EncryptionSetIdentity
    from ._models_py3 import EncryptionSettingsCollection
    from ._models_py3 import EncryptionSettingsElement
    from ._models_py3 import GrantAccessData
    from ._models_py3 import ImageDiskReference
    from ._models_py3 import InnerError
    from ._models_py3 import KeyVaultAndKeyReference
    from ._models_py3 import KeyVaultAndSecretReference
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import Resource
    from ._models_py3 import ShareInfoElement
    from ._models_py3 import Snapshot
    from ._models_py3 import SnapshotSku
    from ._models_py3 import SnapshotUpdate
    from ._models_py3 import SourceVault
except (SyntaxError, ImportError):
    from ._models import AccessUri
    from ._models import ApiError
    from ._models import ApiErrorBase
    from ._models import CreationData
    from ._models import Disk
    from ._models import DiskAccess
    from ._models import DiskAccessUpdate
    from ._models import DiskEncryptionSet
    from ._models import DiskEncryptionSetUpdate
    from ._models import DiskSku
    from ._models import DiskUpdate
    from ._models import Encryption
    from ._models import EncryptionSetIdentity
    from ._models import EncryptionSettingsCollection
    from ._models import EncryptionSettingsElement
    from ._models import GrantAccessData
    from ._models import ImageDiskReference
    from ._models import InnerError
    from ._models import KeyVaultAndKeyReference
    from ._models import KeyVaultAndSecretReference
    from ._models import PrivateEndpoint
    from ._models import PrivateEndpointConnection
    from ._models import PrivateLinkResource
    from ._models import PrivateLinkResourceListResult
    from ._models import PrivateLinkServiceConnectionState
    from ._models import Resource
    from ._models import ShareInfoElement
    from ._models import Snapshot
    from ._models import SnapshotSku
    from ._models import SnapshotUpdate
    from ._models import SourceVault
from ._paged_models import DiskAccessPaged
from ._paged_models import DiskEncryptionSetPaged
from ._paged_models import DiskPaged
from ._paged_models import SnapshotPaged
from ._paged_models import StrPaged
from ._compute_management_client_enums import (
    DiskStorageAccountTypes,
    OperatingSystemTypes,
    HyperVGeneration,
    DiskCreateOption,
    DiskState,
    EncryptionType,
    NetworkAccessPolicy,
    SnapshotStorageAccountTypes,
    DiskEncryptionSetType,
    AccessLevel,
    DiskEncryptionSetIdentityType,
    PrivateEndpointServiceConnectionStatus,
    PrivateEndpointConnectionProvisioningState,
)

__all__ = [
    'AccessUri',
    'ApiError',
    'ApiErrorBase',
    'CreationData',
    'Disk',
    'DiskAccess',
    'DiskAccessUpdate',
    'DiskEncryptionSet',
    'DiskEncryptionSetUpdate',
    'DiskSku',
    'DiskUpdate',
    'Encryption',
    'EncryptionSetIdentity',
    'EncryptionSettingsCollection',
    'EncryptionSettingsElement',
    'GrantAccessData',
    'ImageDiskReference',
    'InnerError',
    'KeyVaultAndKeyReference',
    'KeyVaultAndSecretReference',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'Resource',
    'ShareInfoElement',
    'Snapshot',
    'SnapshotSku',
    'SnapshotUpdate',
    'SourceVault',
    'DiskPaged',
    'SnapshotPaged',
    'DiskEncryptionSetPaged',
    'StrPaged',
    'DiskAccessPaged',
    'DiskStorageAccountTypes',
    'OperatingSystemTypes',
    'HyperVGeneration',
    'DiskCreateOption',
    'DiskState',
    'EncryptionType',
    'NetworkAccessPolicy',
    'SnapshotStorageAccountTypes',
    'DiskEncryptionSetType',
    'AccessLevel',
    'DiskEncryptionSetIdentityType',
    'PrivateEndpointServiceConnectionStatus',
    'PrivateEndpointConnectionProvisioningState',
]

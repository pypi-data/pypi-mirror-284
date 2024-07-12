import datetime
import typing

import kubernetes.client

class V1alpha1IPAddressSpec:
    parent_ref: kubernetes.client.V1alpha1ParentReference
    def __init__(
        self, *, parent_ref: kubernetes.client.V1alpha1ParentReference
    ) -> None: ...
    def to_dict(self) -> V1alpha1IPAddressSpecDict: ...

class V1alpha1IPAddressSpecDict(typing.TypedDict, total=False):
    parentRef: kubernetes.client.V1alpha1ParentReferenceDict

import dataclasses
from hashlib import sha1
from typing import Any

from nested_dataclass_serialization.dataclass_serialization import serialize_dataclass
from nested_dataclass_serialization.dataclass_serialization_utils import (
    IDKEY,
    Dataclass,
    is_dunder,
)


def hash_dataclass(dc: Dataclass, skip_keys: list[str] | None = None) -> str:
    """
    under, dunder and __exclude_from_hash__ fields are not hashed!
    """
    if skip_keys is None:
        skip_keys = [
            IDKEY,
            "cache_base",
            "cache_dir",
            "use_hash_suffix",
            "overwrite_cache",
        ]
    skip_keys += [f.name for f in dataclasses.fields(dc) if is_dunder(f.name)]
    s = serialize_dataclass(dc, skip_keys=skip_keys, encode_for_hash=True)
    return sha1(s.encode("utf-8")).hexdigest()  # noqa: S324
    # what about d=hashlib.md5(b"hello worlds").digest(); d=base64.b64encode(d); , see: https://stackoverflow.com/questions/2510716/short-python-alphanumeric-hash-with-minimal-collisions


def hash_dataclass_dict(
    dc: dict[str, Any],
    skip_keys: list[str] | None = None,
) -> str:
    """
    TODO: how is is different from hash_dataclass?
    under, dunder and __exclude_from_hash__ fields are not hashed!
    """
    if skip_keys is None:
        skip_keys = [
            IDKEY,
            "cache_base",
            "cache_dir",
            "use_hash_suffix",
            "overwrite_cache",
        ]
    s = serialize_dataclass(dc, skip_keys=skip_keys, encode_for_hash=True)
    return sha1(s.encode("utf-8")).hexdigest()  # noqa: S324

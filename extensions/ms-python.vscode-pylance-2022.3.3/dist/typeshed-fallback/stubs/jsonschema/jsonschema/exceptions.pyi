from typing import Any

WEAK_MATCHES: Any
STRONG_MATCHES: Any

class _Error(Exception):
    message: Any
    path: Any
    schema_path: Any
    context: Any
    cause: Any
    validator: Any
    validator_value: Any
    instance: Any
    schema: Any
    parent: Any
    def __init__(
        self,
        message,
        validator=...,
        path=...,
        cause: Any | None = ...,
        context=...,
        validator_value=...,
        instance=...,
        schema=...,
        schema_path=...,
        parent: Any | None = ...,
    ) -> None: ...
    @classmethod
    def create_from(cls, other): ...
    @property
    def absolute_path(self): ...
    @property
    def absolute_schema_path(self): ...
    @property
    def json_path(self): ...

class ValidationError(_Error): ...
class SchemaError(_Error): ...

class RefResolutionError(Exception):
    def __init__(self, cause: str) -> None: ...

class UndefinedTypeCheck(Exception):
    type: Any
    def __init__(self, type) -> None: ...

class UnknownType(Exception):
    type: Any
    instance: Any
    schema: Any
    def __init__(self, type, instance, schema) -> None: ...

class FormatError(Exception):
    message: Any
    cause: Any
    def __init__(self, message, cause: Any | None = ...) -> None: ...

class ErrorTree:
    errors: Any
    def __init__(self, errors=...) -> None: ...
    def __contains__(self, index): ...
    def __getitem__(self, index): ...
    def __setitem__(self, index, value) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    @property
    def total_errors(self): ...

def by_relevance(weak=..., strong=...): ...

relevance: Any

def best_match(errors, key=...): ...

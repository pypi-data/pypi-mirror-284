import dataclasses
from typing import Any, Dict, List, Callable, get_origin, get_args, Optional, Set, Tuple


@dataclasses.dataclass
class Formatter:
    field: Optional[dataclasses.Field] = None
    clazz: Optional[type] = None
    trace: List[Tuple[Optional[dataclasses.Field], Optional[type]]] = dataclasses.field(
        default_factory=list
    )

    def __post_init__(self):
        self.trace.append((self.field, self.clazz))

    def format_field(self, value: Any):
        if value is None:
            if self.field and self.field.default_factory != dataclasses.MISSING:
                value = self.field.default_factory()
            elif self.field and self.field.default != dataclasses.MISSING:
                value = self.field.default
            else:
                return value

        if not self.field and not self.clazz:
            raise f"unknown type for {value}"

        field_type = self.field.type if self.field else None

        if field_type is int or self.clazz is int:
            return int(value)
        if field_type is str or self.clazz is str:
            return str(value)
        if field_type is float or self.clazz is float:
            return float(value)
        if field_type is bool or self.clazz is bool:
            if isinstance(value, str):
                if value.lower() == "true" or value == "1":
                    return True
                if value.lower() == "false" or value == "0":
                    return False
            return bool(value)

        if self.clazz and issubclass(self.clazz, DataObject):
            return self.clazz.from_json(value)

        if self.field:
            return self._format_with_type(self.field.type, value)

        raise ValueError(f"class is not serializable, {self.trace}")

    def _format_with_type(self, field_type, value: Any):
        if field_type.__dict__.get("_name", None) == "Optional":
            return self._format(get_args(field_type)[0], value)
        if get_origin(field_type) in [list, List]:
            return [self._format(get_args(field_type)[0], each) for each in value]
        if get_origin(field_type) in [set, Set]:
            return {self._format(get_args(field_type)[0], each) for each in value}
        if get_origin(field_type) in [dict, Dict]:
            return {
                self._format(get_args(field_type)[0], k): self._format(
                    get_args(field_type)[1], v
                )
                for k, v in value.items()
            }
        raise ValueError(f"class is not serializable, {self.trace}")

    def _format(self, sub_type, value: Any):
        if isinstance(sub_type, type):
            return Formatter(clazz=sub_type, trace=self.trace).format_field(value)
        else:
            return self._format_with_type(sub_type, value)


@dataclasses.dataclass
class DataObject:
    def __getitem__(self, key: str):
        return self.__dict__.get(key)

    def __setitem__(self, key: str, value: Any):
        self.__dict__[key] = value

    @classmethod
    def field_map(cls) -> Dict[str, dataclasses.Field]:
        return {field.name: field for field in cls.fields()}

    @classmethod
    def fields(cls) -> List[dataclasses.Field]:
        return list(dataclasses.fields(cls))

    @classmethod
    def field_names(cls) -> List[str]:
        return [field.name for field in dataclasses.fields(cls)]

    @classmethod
    def from_json(cls, json_obj: Dict[str, Any]):
        function_mapping = cls._customized_mapping_function("_load__")
        return cls(
            **{
                field.name: function_mapping[field.name](json_obj.get(field.name, None))
                for field in cls.fields()
            }
        )

    def to_json(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)

    @classmethod
    def _customized_mapping_function(
        cls, prefix: str
    ) -> Dict[str, Callable[[Any], Any]]:
        all_functions = {
            item: getattr(cls, item)
            for item in dir(cls)
            if isinstance(getattr(cls, item), Callable) and item.startswith(prefix)
        }
        return {
            field.name: all_functions.get(
                prefix + field.name,
                Formatter(field=field).format_field,
            )
            for field in cls.fields()
        }

import dataclasses
from typing import Any, Dict, List, Callable, get_origin, get_args, Set


@dataclasses.dataclass
class Formatter:
    field: dataclasses.Field
    class_name: str

    def format_field(self, value: Any):
        value = self._get_value(value)

        if value is None:
            return value

        if not self.field:
            raise f"unknown type for {value}"

        if self.field:
            return self._format_by_field(self.field.type, value)

        raise ValueError(f"class is not serializable")

    def _format_by_field(self, field_type, value: Any):
        if field_type and isinstance(field_type, type):
            return self._format_by_class(field_type, value)
        if field_type.__dict__.get("_name", None) == "Optional":
            return self._format_by_field(get_args(field_type)[0], value)
        if get_origin(field_type) in [list, List]:
            return [
                self._format_by_field(get_args(field_type)[0], each) for each in value
            ]
        if get_origin(field_type) in [set, Set]:
            return {
                self._format_by_field(get_args(field_type)[0], each) for each in value
            }
        if get_origin(field_type) in [dict, Dict]:
            return {
                self._format_by_field(
                    get_args(field_type)[0], k
                ): self._format_by_field(get_args(field_type)[1], v)
                for k, v in value.items()
            }
        raise ValueError(
            f"{self.class_name}#{self.field.name} is not serializable, "
            f'try to add function "_load__{self.field.name}" with "@classmethod"to {self.class_name}'
        )

    @classmethod
    def _format_by_class(cls, clazz: type, value: Any):
        if clazz is None:
            return None
        if clazz is int:
            return int(value)
        if clazz is str:
            return str(value)
        if clazz is float:
            return float(value)
        if clazz is bool:
            if isinstance(value, str):
                if value.lower() == "true" or value == "1":
                    return True
                if value.lower() == "false" or value == "0":
                    return False
            return bool(value)
        if issubclass(clazz, DataObject):
            return clazz.from_json(value)
        raise f"unknown type {clazz} to format"

    def _get_value(self, value: Any):
        if value is not None:
            return value
        if self.field and self.field.default_factory != dataclasses.MISSING:
            return self.field.default_factory()
        elif self.field and self.field.default != dataclasses.MISSING:
            return self.field.default
        return None


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
                Formatter(field=field, class_name=cls.__name__).format_field,
            )
            for field in cls.fields()
        }

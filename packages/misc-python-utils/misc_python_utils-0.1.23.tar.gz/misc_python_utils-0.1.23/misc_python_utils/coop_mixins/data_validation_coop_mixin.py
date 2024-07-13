from dataclasses import dataclass, field, fields
from typing import Generic, TypeVar, final

from beartype.roar import BeartypeCallHintParamViolation
from result import Err, Ok, Result

from misc_python_utils.dataclass_utils import FixedDict


class CoopDataValidationError(ValueError):
    def __init__(self, msg: str):
        super().__init__(msg)


@dataclass
class DataValidationCoopMixinBase(FixedDict):
    """
    the cooperative calls to super() are not strictly following the MRO,
     cause you can call them before, inbetween or after your subclasses-validation code and thereby change the order of validation!
     misc_python_utils/data_validation_mro_mixin.py strictly follows the MRO -> less flexible

    subclasses are supposed to implement a _parse_validate_data method AND call super()._parse_validate_data() at the end!
    see: https://sorokin.engineer/posts/en/python_super.html

    """

    _validate_call_chain_worked: bool = field(
        init=False,
        repr=False,
        default=False,
    )  # TODO: this does not guarantee that all subclasses were cooperative!

    @final
    def __post_init__(self):
        self._validate_call_chain_worked = False
        self._parse_validate_data()
        assert self._validate_call_chain_worked
        super().__post_init__()

    def _parse_validate_data(self) -> None:
        """
        inheriting classes are supposed to override this method!
        :return:
        """
        self._validate_call_chain_worked = True


T = TypeVar("T")


@dataclass
class DataValidationCoopMixinBaseWithResult(DataValidationCoopMixinBase, Generic[T]):
    """
    handles data-validation errors (CoopDataValidationError) as Result

    takes FIRST_PARENT_CLASS (which second class in MRO) for instantiation
    example:
    ```python
    @nobeartype # need to explicitly exclude this from beartype validation
    @dataclass
    class FasterWhisperWordUnparsed(
        FasterWhisperWord,
        DataValidationCoopMixinBaseWithResult[FasterWhisperWord],
    ):
        pass
    ```

    TODO: beartype validated data goes before/around this result handling
         beartype still throws its own exception!
    """

    def __post_init__(self):  # pycharm complains, cause we don't obey the "final" here
        """
        just to "free" the __post_init__
        you are allowed to override!
        """

    @final
    def parse_validate_as_result(
        self,
    ) -> Result[T, CoopDataValidationError | BeartypeCallHintParamViolation]:
        try:
            FIRST_PARENT_CLASS = 1
            clazz: type[T] = self.__class__.__mro__[FIRST_PARENT_CLASS]
            res = Ok(
                clazz(
                    **{f.name: getattr(self, f.name) for f in fields(clazz) if f.init},
                ),
            )
        except (
            CoopDataValidationError,
            BeartypeCallHintParamViolation,
        ) as e:  # TODO: also catch beartype-validation errors?
            res = Err(e)
        return res

    def parse(self) -> Result[T, CoopDataValidationError]:
        """
        shorter method-name just for convinience
        """
        return self.parse_validate_as_result()

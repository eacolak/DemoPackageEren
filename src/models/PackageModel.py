
from pydantic import Field, validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config


class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Union[List[Image],Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class OptionTrue(Config):
    name: Literal["OptionTrue"] = "OptionTrue"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "OptionTrue"

class OptionFalse(Config):
    name: Literal["OptionFalse"] = "OptionFalse"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "OptionFalse"



class Example1(Config):
    name: Literal["Example1"] = "Example1"
    value: float
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Example1"



class ConfigParam2(Config):
    name: Literal["ConfigParam2"] = "ConfigParam2"
    value: Union[OptionTrue, OptionFalse]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Param2"



class ConfigParam1(Config):
    name: Literal["ConfigParam1"] = "ConfigParam1"
    example: Example1
    value: Literal["ConfigParam1"] = "ConfigParam1"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Param1"


class Params(Config):
    """
        Positive angles specify counterclockwise rotation while negative angles indicate clockwise rotation.
    """
    name: Literal["Params"] = "Params"
    value: Union[ConfigParam1, ConfigParam2]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Params"



class DemoPackageErenInputs(Inputs):
    inputImage: InputImage


class DemoPackageErenConfigs(Configs):
    params: Params


class DemoPackageErenOutputs(Outputs):
    outputImage: OutputImage


class DemoPackageErenRequest(Request):
    inputs: Optional[DemoPackageErenInputs]
    configs: DemoPackageErenConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class DemoPackageErenResponse(Response):
    outputs: DemoPackageErenOutputs


class DemoPackageErenExecutor1(Config):
    name: Literal["DemoPackageEX1"] = "DemoPackageEX1"
    value: Union[DemoPackageErenRequest, DemoPackageErenResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Package"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[DemoPackageErenExecutor1]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {
            "target": "value"
        }


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["Package"] = "Package"

"""Parse the schema and generate a python file which can be read by the input classes.
Should only be run if changes to the schema are made.
"""

import re
from pathlib import Path
from typing import List

import xmlschema
from xmlschema.validators import XsdAnyElement

from excitingtools.utils.utils import get_excitingtools_root


def copy_schema_files_for_parsing(schema_files: List[str]) -> List[Path]:
    """Copies the schema files to the current directory.

    Also generates a file (input.xsd) with schema extensions, with modified include paths.
    This is a work-around because the exciting documentation fails to compile
    when a schema with the modified include is used.

    :param schema_files: the name of the schema files and tags of the xml element
    :return file_list: A list of all generated or copied files.
    """
    inputschemaextentions_name = "inputschemaextentions"
    inputschemaextentions = f"""<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:ex="{inputschemaextentions_name}.xsd"
xmlns:xs="http://www.w3.org/2001/XMLSchema"
targetNamespace="{inputschemaextentions_name}.xsd"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 >
 
  <xs:attribute name="importance">
    <xs:simpleType>
      <xs:restriction base="xs:string">
        <xs:enumeration value="essential"></xs:enumeration>
        <xs:enumeration value="expert"></xs:enumeration>
        <xs:enumeration value="experimental"></xs:enumeration>
        <xs:enumeration value="output"></xs:enumeration>
        <xs:enumeration value="ignore"></xs:enumeration>
      </xs:restriction>
    </xs:simpleType>
  </xs:attribute>
  
  <xs:attribute name="unit">
    <xs:simpleType>
      <xs:restriction base="xs:string">
        <xs:enumeration value=""></xs:enumeration>
        <xs:enumeration value="1"></xs:enumeration>
        <xs:enumeration value="rad"></xs:enumeration>
        <xs:enumeration value="Bohr"></xs:enumeration>
        <xs:enumeration value="Hartree"></xs:enumeration>
        <xs:enumeration value="atomic units"></xs:enumeration>
        <xs:enumeration value="lattice coordinates"></xs:enumeration>
      </xs:restriction>
    </xs:simpleType>
  </xs:attribute>
  
</xs:schema>"""

    inputschemaextentions_path = Path(f"{inputschemaextentions_name}.xsd")
    inputschemaextentions_path.write_text(inputschemaextentions)
    root = get_excitingtools_root()

    # handling of the input.xsd file
    inputschema_file = root / "../../xml/schema/input.xsd"
    content = inputschema_file.read_text().split("\n")
    content[1] = (
        '<xs:schema xmlns:ex="inputschemaextentions.xsd" '
        'xmlns:xs="http://www.w3.org/2001/XMLSchema" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xsi:schemaLocation="inputschemaextentions.xsd inputschemaextentions.xsd">'
    )
    new_inputschema_file = Path("input.xsd")
    new_inputschema_file.write_text("\n".join(content))

    file_list = [inputschemaextentions_path, new_inputschema_file]

    # handling of all other included schema files
    for schema_name in schema_files:
        schema_root = root / "../../xml/schema"
        schema_reference = schema_root / f"{schema_name}.xsd"
        content = schema_reference.read_text().split("\n")

        content[1] = f'  xmlns:ex="{inputschemaextentions_name}.xsd"'
        content[3] = f'  xsi:schemaLocation="{inputschemaextentions_name}.xsd {inputschemaextentions_name}.xsd">'
        content = "\n".join(content)

        new_schema_file = Path(f"{schema_name}.xsd")
        new_schema_file.write_text(content)
        file_list.append(new_schema_file)

    return file_list


def read_schema_to_dict(name: str) -> dict:
    """Read schema and transform to sensible dictionary.

    Note: This could be done with an external library, such as `xmltodict` or `xmljson`
    but as this module should be run infrequently, a custom implementation reduces
    dependencies.

    :param name: name of the schema file and tag of the xml element
    :return: a dictionary with the need information about children/parents and valid attributes.
    """
    schema = xmlschema.XMLSchema(f"{name}.xsd")

    tag_info = {}
    xsd_elements = filter(lambda x: isinstance(x, xmlschema.XsdElement) and x.ref is None, schema.iter_components())

    for xsd_element in xsd_elements:
        attributes = xsd_element.attributes
        mandatory_attributes = set([k for k, v in attributes.items() if v.use == "required"])
        children = [x.name for x in xsd_element.iterchildren() if not isinstance(x, XsdAnyElement)]
        mandatory_children = set([x.name for x in xsd_element.iterchildren() if x.min_occurs > 0])
        multiple_childs = set([x.name for x in xsd_element.iterchildren() if x.max_occurs is None or x.max_occurs > 1])

        tag_info[xsd_element.name] = {
            "attribs": filter(lambda x: x is not None, attributes),
            "children": children,
            "mandatory_attribs": mandatory_attributes | mandatory_children,
            "multiple_children": multiple_childs,
        }

        # special handling for the plan
        if xsd_element.name == "doonly":
            tag_info["doonly"]["plan"] = attributes["task"].type.validators[0].enumeration

    # exclude special structure attributes (already explicitly specified in the __init__ of ExcitingStructure class)
    if name == "structure":
        tag_info["structure"]["mandatory_attribs"].remove("crystal")
        tag_info["crystal"]["mandatory_attribs"].remove("basevect")
        tag_info["species"]["mandatory_attribs"].remove("atom")

    return tag_info


def write_schema_info(super_tag: str, schema_dict: dict) -> str:
    """Converts dict representation of the schema to string.

    :param super_tag: name of the top-level element
    :param schema_dict: contains all the information read from the schema
    :return info_string: string of python-formatted code
    """
    info_string = f"\n# {super_tag} information \n"
    for tag in schema_dict:
        valid_attributes = sorted(schema_dict[tag]["attribs"])
        valid_subtrees = schema_dict[tag]["children"]
        mandatory_attributes = sorted(schema_dict[tag]["mandatory_attribs"])
        multiple_childs = sorted(schema_dict[tag]["multiple_children"])

        if not (valid_attributes or valid_subtrees or mandatory_attributes):
            continue

        if valid_attributes:
            info_string += list_string_line_limit(f"{tag}_valid_attributes", valid_attributes) + " \n"
        if valid_subtrees:
            info_string += list_string_line_limit(f"{tag}_valid_subtrees", valid_subtrees) + " \n"
        if mandatory_attributes:
            info_string += list_string_line_limit(f"{tag}_mandatory_attributes", mandatory_attributes) + " \n"
        if multiple_childs:
            info_string += list_string_line_limit(f"{tag}_multiple_children", multiple_childs) + " \n"
        info_string += "\n"
    return info_string


def list_string_line_limit(name: str, content: list, max_length: int = 120) -> str:
    """Given a list of unique items, produces a python formatted string containing the definition of the list
    given by the name:
        name = ['entry1', 'entry2', ...]
    Inserts a line break every time the string gets longer then the limit.

    :param name: the name of the set in the final string representing the definition
    :param content: the list to write to string as a set (list because of consistent ordering)
    :param max_length: the maximum line length
    :return: the formatted string with fixed line length
    """
    formatted_string = ""
    current_line_string = name + " = ["
    start_len = len(current_line_string)
    entry_break_string = '", '

    for entry in content:
        if len(str(entry) + current_line_string + entry_break_string) > max_length:
            formatted_string += current_line_string + "\n"
            current_line_string = start_len * " "
        current_line_string += f'"{entry}{entry_break_string}'

    formatted_string += current_line_string[:-2] + "]"
    return formatted_string


def get_all_include_files() -> list:
    """Gets a list of all included files in the input.xsd file."""
    input_schema_file = (get_excitingtools_root() / "../../xml/schema/input.xsd").resolve()
    if not input_schema_file.exists():
        raise ValueError(
            "Couldn't find exciting schema. Most likely you are using excitingtools outside of exciting."
            "To fix this, try installing excitingtools from source in editable (-e) mode."
        )
    return re.findall(r'<xs:include id=".*" schemaLocation="(.*)\.xsd"/>', input_schema_file.read_text())


def main():
    """Main function to read the schema and write it to python readable file."""
    filename = Path(__file__).parent / "valid_attributes.py"
    info = (
        '""" Automatically generated file with the valid attributes from the schema. \n'
        'Do not manually change. Instead, run "utils/schema_parsing.py" to regenerate. """ \n'
    )

    schemas = get_all_include_files()
    tmp_files = copy_schema_files_for_parsing(schemas)

    input_schema_dict = {"input": read_schema_to_dict("input")["input"]}
    info += write_schema_info("input", input_schema_dict)

    for schema in schemas:
        schema_dict = read_schema_to_dict(schema)
        info += write_schema_info(schema, schema_dict)

    # Handle special case for 'xs' to handle the valid plan entries
    xs_schema_dict = read_schema_to_dict("xs")
    info += "\n# valid entries for the xs subtree 'plan'\n"
    info += list_string_line_limit("valid_plan_entries", sorted(xs_schema_dict["doonly"]["plan"])) + " \n"

    with open(filename, "w") as fid:
        fid.write(info)

    for file in tmp_files:
        file.unlink()


if __name__ == "__main__":
    main()

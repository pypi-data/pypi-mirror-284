"""
Simple tests of mapping Sphinx XML to desired OU-XML tags.
"""

import pytest
from roundtrip_data import round_trip_test_list, OU_XML, SPHINX_XML, MYST
from ou_xml_validator.utils import (
    apply_xslt,
    pretty_xml_from_root,
    root_from_xml_string,
    fix_sphinxXml_nodes,
)

XSLT_PATH = "ou_xml_validator/xslt/sphinxXml2ouxml.xslt"

test_list = [(i[SPHINX_XML], i[OU_XML]) for i in round_trip_test_list]


@pytest.mark.parametrize(
    "xml_content, expected_output",
    (test_list),
)
def test_apply_xslt(xml_content, expected_output, xslt_path=XSLT_PATH):
    result = apply_xslt(xml_content, xslt_path, set_root="Section")
    result = root_from_xml_string(pretty_xml_from_root(result.getroot()))
    expected_output = root_from_xml_string(expected_output)
    assert pretty_xml_from_root(result) == pretty_xml_from_root(expected_output)

import pytest
from cvss_converter.converter import (
    cvss2_to_cvss3,
    extract_cvss2_vector,
    create_ordered_vector,
)


def test_cvss2_to_cvss3_standard():
    cvssv2_vector = "AV:N/AC:H/Au:S/C:P/I:P/A:C"
    expected_v3_vector = "CVSS:3.0/AV:N/AC:H/PR:L/UI:N/S:C/C:L/I:L/A:H"
    normalized_vector, _ = cvss2_to_cvss3(cvssv2_vector)
    assert normalized_vector == expected_v3_vector


def test_cvss2_to_cvss3_medium_complexity():
    cvssv2_vector = "AV:N/AC:M/Au:N/C:C/I:P/A:P"
    expected_v3_vector = "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:L"
    normalized_vector, _ = cvss2_to_cvss3(cvssv2_vector)
    assert normalized_vector == expected_v3_vector


def test_extract_cvss2_vector():
    # Test cases
    test_cases = [
        ("CVSS2#AV:L/AC:L/Au:N/C:P/I:P/A:N", "AV:L/AC:L/Au:N/C:P/I:P/A:N"),
        ("CVSS2/AV:L/AC:L/Au:N/C:P/I:P/A:N", "AV:L/AC:L/Au:N/C:P/I:P/A:N"),
        ("CVSS:2.0/AV:L/AC:L/Au:N/C:P/I:P/A:N", "AV:L/AC:L/Au:N/C:P/I:P/A:N"),
        ("CVSS2.0#AV:L/AC:L/Au:N/C:P/I:P/A:N", "AV:L/AC:L/Au:N/C:P/I:P/A:N"),
        ("SomeRandomTextAV:L/AC:L/Au:N/C:P/I:P/A:N", "AV:L/AC:L/Au:N/C:P/I:P/A:N"),
        ("PrefixAV:A/AC:M/Au:S/C:P/I:P/A:P", "AV:A/AC:M/Au:S/C:P/I:P/A:P"),
        ("AV:L/AC:L/Au:N/C:P/I:P/A:N", "AV:L/AC:L/Au:N/C:P/I:P/A:N"),
    ]

    for cvss_string, expected in test_cases:
        assert extract_cvss2_vector(cvss_string) == expected

    # Test invalid input
    with pytest.raises(ValueError):
        extract_cvss2_vector("InvalidCVSSString")


def test_create_ordered_vector():
    cvssv3_metrics = {
        "S": "C",
        "AV": "N",
        "I": "L",
        "AC": "L",
        "UI": "N",
        "C": "L",
        "A": "L",
        "PR": "N",
    }
    expected_ordered_vector = "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:L"

    ordered_vector = create_ordered_vector(cvssv3_metrics)

    assert ordered_vector == expected_ordered_vector

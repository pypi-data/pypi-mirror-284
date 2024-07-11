import pytest
from cvss_converter import cvss2_to_cvss3


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

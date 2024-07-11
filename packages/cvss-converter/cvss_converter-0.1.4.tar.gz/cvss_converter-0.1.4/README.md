# cvss-converter

A python program to convert older cvss versions to more modern ones.

## Change Logs

## v0.1.4:

- Cleaned up README.md by removing irrelevant reference

### v0.1.3:

- `cvss2_to_3()` now better handles variants of prefixes on CVSSv2 vectors (e.g. CVSS2#/AV:L..., CVSS2.0:AV:L/...)

## Limitations

- Currently cvss-converter only provides cvssv2 to cvssv3 conversion, with strict mode by default.
- Only base vector is supported as it is meant to help convert older CVEs with CVSSv2 base vectors (on NVD)

## Strict Mode

As there are a several fields which are either ambiguous or doesn't exist at all (e.g. Scope or User Interaction). During conversion, the logic will always choose the values of a vector that yields a higher CVSS score. We prefer to err on the side of caution than to assume that the vulnerability is not affected by the ambiguity.
The conversion mapping chart in strict mode for ambiguous or missing vectors is as follows:

| CVSSv2 Vector                    | CVSSv3.1 Vector               |
| -------------------------------- | ----------------------------- |
| Attack Complexity (AC): "Medium" | Attack Complexity (AC): "Low" |
| Does not exist                   | Scope (S): "C"                |
| Does not exist                   | User Interaction (UI): "N"    |

Please also note that for Attack Vector (AV), since there is no `Physical` value in CVSSv2, there is no conversion requirements to ever map a value to CVSSv3 `AV:P`.

# How to use?

## Install with Pip or Pipenv

Pip:

```
pip install cvss-converter
```

Pipenv:

```
pipenv install cvss-converter
```

## Usage: Example

```python
from cvss_converter.converter import cvss2_to_cvss3

cvssv2 = "AV:N/AC:H/Au:S/C:P/I:P/A:C"
cvssv3, score = cvss2_to_cvss3(cvssv2)
print(f"CVSSv3 Vector: {cvssv3}, Base Score: {score}")
```

Expected output:

```bash
CVSSv3 Vector: CVSS:3.0/AV:N/AC:H/PR:L/UI:R/S:C/C:L/I:L/A:H, Base Score: 7.1
```

# Future

- Add vector override
- Add option for standard mode (non-strict)

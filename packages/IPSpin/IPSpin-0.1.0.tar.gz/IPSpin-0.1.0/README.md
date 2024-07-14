# IPSpin

A Python library for interacting with IPSpin Services.

## Installation

```bash
pip install ipspin
```

## Usage

```python
from ipspin import IPSpin

ipspin = IPSpin.builder("API_KEY")
ipspin.set_region("eu-north-1")\
      .add_url("https://ifconfig.io/ip")\
      .print_output(True)\
      .send_requests()
```

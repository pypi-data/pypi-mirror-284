## Khmer2Number

Khmer word to number converter.

```shell
pip install khmer2number
```

```python
from khmer2number import parse

tokens = "លោក បាន ទទួល លុយ ចំនួន ដក មួយ រយ ចុច សាមសិប ពីរ រៀល".split()
print(list(parse(tokens)))
# => ['លោក', 'បាន', 'ទទួល', 'លុយ', 'ចំនួន', -100, 'ចុច', 32, 'រៀល']
```
import pyparsing as pp
from operator import mul
from functools import reduce
from typing import List, Generator

def makeLit(s, val):
  ret = pp.CaselessLiteral(s)
  return ret.setParseAction(pp.replaceWith(val))


def wordprod(t):
  return reduce(mul, t)


unitDefinitions = [
  ("សូន្យ", 0),
  ("មួយ", 1),
  ("ពីរ", 2),
  ("បី", 3),
  ("បួន", 4),
  ("ប្រាំ", 5),
  ("ប្រាំមួយ", 6),
  ("ប្រាំពីរ", 7),
  ("ប្រាំបី", 8),
  ("ប្រាំបួន", 9),
]

digits_list = [k for k, _ in unitDefinitions]

units = pp.MatchFirst(
  makeLit(s, v) for s, v in sorted(unitDefinitions, key=lambda d: -len(d[0]))
)

tensDefinitions = [
  ("ដប់", 10),
  ("ម្ភៃ", 20),
  ("សាមសិប", 30),
  ("សែសិប", 40),
  ("ហាសិប", 50),
  ("ហុកសិប", 60),
  ("ចិតសិប", 70),
  ("ប៉ែតសិប", 80),
  ("កៅសិប", 90),
]

tens_list = [k for k, _ in tensDefinitions]
tens = pp.MatchFirst(makeLit(s, v) for s, v in tensDefinitions)

hundreds = makeLit("រយ", 100)

majorDefinitions = [
  ("ពាន់", int(1e3)),
  ("ម៉ឺន", int(1e4)),
  ("សែន", int(1e5)),
  ("លាន", int(1e6)),
  ("ប៊ីលាន", int(1e9)),
  ("ទ្រីលាន", int(1e12)),
  ("ក្វាទ្រីលាន", int(1e15)),
  ("គ្វីនទីលាន", int(1e18)),
  ("សិចទីលាន", int(1e21)),
  ("សិបទីលាន", int(1e24)),
  ("អុកទីលាន", int(1e27)),
  ("ណូនីលាន", int(1e30)),
  ("ដេស៊ីលាន", int(1e33)),
  ("អាន់ដេស៊ីលាន", int(1e36)),
]

major_list = [k for k, _ in majorDefinitions]

mag = pp.MatchFirst(makeLit(s, v) for s, v in majorDefinitions)

numPart = (
  (
    (
      (units + pp.Optional(hundreds)).setParseAction(wordprod) + pp.Optional(tens)
    ).setParseAction(sum)
    ^ tens
  )
  + pp.Optional(units)
).setParseAction(sum)
numWords = (
  (numPart + pp.Optional(mag)).setParseAction(wordprod)[1, ...]
).setParseAction(sum)

START_SET = set(digits_list + tens_list + ["ដក"])
NUM_SET = set(digits_list + tens_list + major_list + ["រយ"])


def parse(tokens: List[str]) -> Generator[str, None, None]:
  pos = 0
  while pos < len(tokens):
    token = tokens[pos]
    if token in START_SET:
      idx = 0
      numbers = []
      sign = 1

      if token == "ដក":
        sign = -1
        idx = 1

      while idx + pos < len(tokens):
        if tokens[pos + idx] not in NUM_SET:
          break
        numbers.append(tokens[pos + idx])
        idx += 1
      pos += idx
      yield sign * numWords.parseString(" ".join(numbers))[0]
      continue
    yield token
    pos += 1


if __name__ == "__main__":
  tokens = "លោក បាន ទទួល លុយ ចំនួន ដក មួយ រយ ចុច សាមសិប ពីរ រៀល".split()
  print(list(parse(tokens)))
  # => ['លោក', 'បាន', 'ទទួល', 'លុយ', 'ចំនួន', -100, 'ចុច', 32, 'រៀល']

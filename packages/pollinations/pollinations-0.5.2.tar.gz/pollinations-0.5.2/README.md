<div id="header">
  <img src="https://i.ibb.co/p049Y5S/86964862.png" width="50"/>   <img src="https://i.ibb.co/r6JZ336/sketch1700556567238.png" width="250">
</div>

# [pollinations.ai - Image Generation](https://pypi.org/project/pollinations.ai)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/toolkitr/tkr/blob/main/LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.7%20|%203.8%20|%203.9%20|%203.10%20|%203.11%20|%203.12%20-blue)](https://www.python.org/downloads/)

```
pollinations.ai: (https://pollinations.ai/)

This is a WRAPPER designed for easy text-image generation.
```

## Installing
```shell
# Linux/macOS
python3 -m pip install -U pollinations.ai

# Windows
py -3 -m pip install -U pollinations.ai
```

## Simple Examples
```python
# Version 1
model: ai.Image = ai.Image()
image: ai.ImageObject = model.generate(
      prompt='cat in space',
).save()

# Version 2
class Model(ai.Image):
      params = {
            "prompt": "cat in space"
      }

model: ai.Image = Model()
model.generate().save()
```
```python
@abc.resource(deprecated=False)
def generate(
    self,
    *args,
    prompt: str = "",
    model: str = None,
    width: int = 1024,
    height: int = 1024,
    seed: int = None,
    nologo: bool = False,
    **kwargs,
) -> str:
```
```python
# Version 1
batch: list = ["lion in space", "dog in space"]
image_generator: ai.Image = ai.Image()
image_generator.generate_batch(prompts=batch, save=True, path="images")

# Version 2
class Model(ai.Image):
      params = {
            "prompt": ["lion in space", "dog in space"]
      }

model: ai.Image = Model()
model.generate_batch(save=True, path="images")
```
```python
@abc.resource(deprecated=False)
def generate_batch(
    self,
    prompts: list = ["..."],
    save: bool = False,
    path: str = None,
    naming: str = "counter",
    *args,
    model: str = None,
    width: int = 1024,
    height: int = 1024,
    seed: int = None,
    nologo: bool = False,
    **kwargs,
) -> list:
```

## Setting model filter:
```python
import pollinations.ai as ai

image_generator: ai.Image = ai.Image()
image_generator.set_filter(ai.BANNED_WORDS)

# If any word from a prompt is in the filter it will return an exception.
```


# Links
- [Pollinations.ai](https://pollinations.ai/)
- [Discord](https://discord.gg/8HqSRhJVxn)
- [Github](https://github.com/pollinations)
- [Youtube](https://www.youtube.com/channel/UCk4yKnLnYfyUmCCbDzOZOug)
- [Instagram](https://instagram.com/pollinations_ai)
- [Twitter (X)](https://twitter.com/pollinations_ai)

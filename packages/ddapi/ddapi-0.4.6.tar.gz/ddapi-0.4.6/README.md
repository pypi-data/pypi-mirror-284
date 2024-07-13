ddapi is an api from the ddnet and qwik website
## Installation

I lost access to pypi so install via git below example
```bash
  pip install ddapi # old version
```
or
```bash
  pip install git+https://github.com/ByFox213/ddapi
```
    
## Usage/Examples

DDnet
```python
import asyncio
from ddapi import DDnetApi, DDPlayer


async def main():
    obj = DDnetApi()
    nickname = "Cor"
    user: DDPlayer = await obj.player(nickname)
    if user is None:
        return "Player not found"
    print(f"{user.player}: {user.points.points}")
    # Cor: 31473 
    await obj.close()  # Closing client Not necessary
    assert isinstance(user, DDPlayer)


asyncio.run(main())
```

[other examples](https://github.com/ByFox213/ddapi/tree/main/example)

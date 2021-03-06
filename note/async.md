# Functions lookup
```
async def
await
asyncio.create_task()
asyncio.gather()
asyncio.wait()
asyncio.run()
```

# Concept

## Coroutines
> Coroutines are a more generalized form of subroutines. Subroutines are entered at one point and exited at another point. 
> 
> Coroutines can be entered, exited, and resumed at many different points. They can be implemented with the async def statement.

## Asyncio 
> Asyncio is a library to write concurrent code using the async/await syntax.

## Execution environment

### In Jupyternotebook
```
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

await main()
```

### In other IDEs
```
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

## Running concurrently
> To execute function to run coroutines concurrently, one must create Tasks in asyncio.

### asyncio.create_task() (Create Tasks manually.
```
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
await main() 
```
### Without Tasks(Don't run concurrently)
```
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

await main() 
```
### Create multiple tasks
> asyncio.gather( *aws, loop=None, return_exceptions=False)
> * *aws ?????????????????? awaitable objects
> * Loop????????????????????? Python version 3.10 ??????
> * return_exceptions???default ??? False???????????? exception ?????????????????? task?????????????????? True ????????????????????????????????????????????????????????????(???????????????????????? results ????????????????????? ValueError() ??????)

```
import time,asyncio
now = lambda: time.time()

async def dosomething(num):
    print('??? {} ??????????????????'.format(num))
    await asyncio.sleep(2)
    print('??? {} ??????????????????'.format(num))
    return '??? {} ????????????'.format(num)

async def raise_error(num):
    raise ValueError
    print('?????????????????????')

async def main():
    tasks = [ dosomething(i) for i in range(5)]
    tasks1 = [raise_error(i) for i in range(5)]

    results = await asyncio.gather(*tasks, *tasks1, return_exceptions=True)
    print(results)
start = now()
await main()
print('TIME: ', now() - start)
```

```
import time,asyncio

async def count():
    print("count one")
    await asyncio.sleep(1)
    print("count four")

async def count_further():
    print("count two")
    await asyncio.sleep(1)
    print("count five")

async def count_even_further():
    print("count three")
    await asyncio.sleep(1)
    print("count six")

async def main():
    await asyncio.gather(count(), count_further(), count_even_further())

s = time.perf_counter()
await main()
elapsed = time.perf_counter() - s
print(f"Script executed in {elapsed:0.2f} seconds.")
```

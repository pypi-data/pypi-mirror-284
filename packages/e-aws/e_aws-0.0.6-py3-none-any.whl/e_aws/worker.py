from time import time
import traceback
import asyncio
import logging


async def __worker(
    loop: asyncio.AbstractEventLoop,
    queue: asyncio.Queue,
    name: str,
    worker_func: callable
) -> None:
    """
    Worker function that processes the items in the queue

    Parameters:
        loop (asyncio.AbstractEventLoop): The event loop
        queue (asyncio.Queue): The queue from which the items will be processed
        name (str): The name of the worker
        worker_func (callable): The function that processes the items

    Returns:
        None
    """
    logging.info(name)
    while True:
        worker_args = await queue.get()
        logging.info(f"{name} is processing an item")
        try:
            await loop.run_in_executor(None, worker_func, *worker_args)
        except Exception as e:
            traceback.print_exc()
            raise e
        else:
            logging.info(f"{name} has processed an item")
        finally:
            queue.task_done()


async def __set_queue(queue: asyncio.Queue, objects: iter) -> None:
    """
    Add items to the queue

    Parameters:
        queue (asyncio.Queue): The queue to which the items will be added
        objects (iter): The items to be added to the queue

    Returns:
        None
    """
    logging.info("Putting items to the queue")
    count = 0
    for item in objects:
        await queue.put(item)
        count += 1
    logging.info(f"{count} items have been added to the queue")


async def run(objects: list, worker_func: callable, max_parallel_uploads: int = 10) -> None:
    """
    Run the worker function

    Parameters:
        objects (list): The items to be processed
        worker_func (callable): The function that processes the items
        max_parallel_uploads (int): The maximum number of parallel uploads

    Returns:
        None
    """
    tm = time()
    loop = asyncio.get_running_loop()
    queue = asyncio.Queue(maxsize=max_parallel_uploads)
    workers = [
        asyncio.create_task(
            __worker(loop, queue, f"Worker-{worker_index+1}", worker_func)
        )
        for worker_index in range(max_parallel_uploads)
    ]
    await __set_queue(queue, objects)
    await queue.join()
    for w in workers:
        w.cancel()
    await asyncio.gather(*workers, return_exceptions=True)
    logging.info(f"All items have been processed in {round(time() - tm, 2)} seconds")

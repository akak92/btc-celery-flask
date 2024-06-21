import os
from typing import Union, List, Dict
import asyncio
from celery import Celery
from celery.result import AsyncResult, allow_join_result

broker = os.getenv('CELERY_BROKER', 'redis://redis:6379/0')
class QueueInterface:
    def __init__(self, queue_name: str):
        self.queue_name = queue_name
        self.queue: Celery = Celery(self.queue_name, broker=broker, backend=broker)
        self.tasks: List[AsyncResult] = []

    def add_to_queue(self, message: Union[str, int, List, Dict], task_name: str, delay=2, send_complete:bool=False) -> AsyncResult:
        """Añadir un mensaje a la cola."""
        task = None
        if send_complete:
            task = self.queue.send_task(task_name, args=[message], queue=self.queue_name, delay=delay)
        elif isinstance(message, dict):
            task = self.queue.send_task(task_name, kwargs=message, queue=self.queue_name, delay=delay)
        elif isinstance(message, (list, tuple)):
            task = self.queue.send_task(task_name, args=message, queue=self.queue_name, delay=delay)
        elif isinstance(message, str):
            task = self.queue.send_task(task_name, args=[message], queue=self.queue_name, delay=delay)

        if task:
            self.tasks.append(task)
        return task

    async def await_all_tasks(self, async_sleep:float=0.5):
        """Espera hasta que todas las tareas estén completadas."""
        with allow_join_result():
            for task in self.tasks:
                task_ready = task.ready()
                while not task_ready:
                    print(f"Task {task.id} status: {task.status}")
                    await asyncio.sleep(async_sleep)
                    task_ready = task.ready()
    @staticmethod
    async def await_task(task: AsyncResult):
        """Espera hasta que una tarea específica esté completada."""
        with allow_join_result():
            if not task.ready():
                await task.get(propagate=False)
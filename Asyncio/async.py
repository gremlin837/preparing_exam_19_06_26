import asyncio

async def producer(queue):
    """генератор данных телеметрии
    добавляет эл-ты в очередь и сигнализирует об окончании  None
    """
    telemetry = [
        ("Температура подачи", 83.1),
        ("Температура обратки", 61.4),
        ("Давление", 1.8),
        ("Расход", 12.7),
        ("Температура подачи", 84.0)
    ]

    for item in telemetry:
        await asyncio.sleep(1)
        await queue.put(item)
        print(f"В очередь отправлено: {item}")

    await queue.put(None)

async def consumer(queue):
    """
    обработчик данных
    получает эл-ты из очереди и обрабатывает их
    """
    while True:
        item = await queue.get() #получить элемент из очереди

        if item is None:
            print("Данные закончились")
            queue.task_done()
            break

        name, value = item
        print(f"Обработка: {name} = {value}")
        await asyncio.sleep(0.5)
        queue.task_done() #Сообщить о завершении обработки элемента

async def main():
    #создание очереди
    queue = asyncio.Queue()

    #Создание и запуск задач
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    #ожидание завершения производителя
    await producer_task

    # ожидание полного заполнения очереди
    await queue.join()

    # ожидание завершения обработчика
    await consumer_task

    print("\nОчередь обработана")

if __name__ == "__main__":
    asyncio.run(main())



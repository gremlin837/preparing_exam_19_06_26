import asyncio


# Имитация I/O операции (сетевого запроса)
async def fetch_data(url: str, delay: float) -> str:
    print(f"Начинаю загрузку {url} (займёт {delay} сек)")
    await asyncio.sleep(delay)  # имитируем ожидание ответа от сервера
    print(f"Завершил загрузку {url}")
    return f"Данные из {url}"


# Главная корутина
async def main():
    # Список URL с разными задержками (имитация разной скорости ответа)
    urls = [
        ("https://api.site1.com", 2),
        ("https://api.site2.com", 1),
        ("https://api.site3.com", 3),
    ]

    # Создаём задачи (конкурентный запуск)
    tasks = []
    for url, delay in urls:
        task = asyncio.create_task(fetch_data(url, delay))
        tasks.append(task)

    print("Ожидаем завершения всех загрузок...")
    # Ждём выполнения всех задач параллельно
    results = await asyncio.gather(*tasks)

    print("\nРезультаты:")
    for res in results:
        print(res)


# Точка входа
if __name__ == "__main__":
    asyncio.run(main())
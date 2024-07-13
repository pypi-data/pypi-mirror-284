import aiohttp
import asyncio
import os
import timeit
import statistics
from concurrent.futures import ThreadPoolExecutor

# Load the API_KEY variable
api_key = os.getenv('BLUEGUARD_API_KEY')
org_uuid = os.getenv('ORG_UUID')

sample_text = "Hi Ram. I live in Chennai. Yesterday we lost our aadhar card whose no is 3455-6787-3467. We filed a complaint at Nasik Police Station near the behur restaurant."  # Replace with your actual sample text

async def measure_performance(session):
    headers = {"api_key": f"Bearer {api_key}"}
    payload = {
        "mode": "redact",
        "inputs": [{"text": sample_text}],
        "identify_credentials": False,
        "enable_details": False,
        "enable_sensitive_scan": False,
        "org_uuid": org_uuid
    }
    start_time = timeit.default_timer()
    async with session.post(
        url="https://api.blueguard.bluegennx.ai/api/process/text/deid/",
        headers=headers,
        json=payload
    ) as response:
        await response.json()
    end_time = timeit.default_timer()
    return end_time - start_time

async def run_performance_tests():
    async with aiohttp.ClientSession() as session:
        tasks = [measure_performance(session) for _ in range(1000)]
        times = await asyncio.gather(*tasks)
        return times

def main():
    loop = asyncio.get_event_loop()

    # Run the performance tests
    times = loop.run_until_complete(run_performance_tests())

    # Calculate performance metrics
    mean_time = statistics.mean(times)
    min_time = min(times)
    max_time = max(times)

    print(f"Total execution time for 1000 async requests: {sum(times)} seconds")
    print(f"Mean time per request: {mean_time} seconds")
    print(f"Min time per request: {min_time} seconds")
    print(f"Max time per request: {max_time} seconds")

if __name__ == "__main__":
    main()
import argparse
import asyncio
from .client import SSLolClient
from .models import SearchResponse

def main():
    parser = argparse.ArgumentParser(description="ssLOL API Client CLI")
    parser.add_argument("user_id", type=str, help="Discord user ID")
    parser.add_argument("--async_mode", action="store_true", help="Use asynchronous request")
    args = parser.parse_args()

    client = SSLolClient()

    if args.async_mode:
        async def run():
            raw_data = await client.get_user_async(args.user_id)
            resp = SearchResponse(**raw_data)
            print(resp.json(indent=2))
        asyncio.run(run())
    else:
        raw_data = client.get_user(args.user_id)
        resp = SearchResponse(**raw_data)
        print(resp.json(indent=2))

if __name__ == "__main__":
    main()

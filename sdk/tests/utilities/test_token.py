import asyncio
import functools

import asynctest
from functools import wraps, partial

from lusid.utilities import ApiClientFactory
from utilities import CredentialsSource


def run_async(func):

    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    return run


class TokenTests(asynctest.TestCase):

    @run_async
    def build_factory(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        return factory.api_client.configuration.access_token

    async def get_all_tokens(self):
        result = await asyncio.gather(*[self.build_factory() for _ in range(0, 5)], return_exceptions=True)
        return result

    async def test_get_concurrent_tokens(self):
        tokens = await self.get_all_tokens()

        self.assertEqual(1, len(set(tokens)), "tokens not all equal")

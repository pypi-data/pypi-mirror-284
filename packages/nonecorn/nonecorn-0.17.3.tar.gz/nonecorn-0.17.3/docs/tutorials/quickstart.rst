.. _quickstart:

Quickstart
==========

Hello World
-----------

A very simple ASGI app that simply returns a response containing
``hello`` is, (file ``hello_world.py``)

.. code-block:: python

    async def app(scope, receive, send):
        if scope["type"] != "http":
            raise Exception("Only the HTTP protocol is supported")

        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                (b'content-type', b'text/plain'),
                (b'content-length', b'5'),
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': b'hello',
        })

and is simply run via

.. code-block:: console

    hypercorn hello_world:app

and tested by

.. code-block:: sh

    curl localhost:8000

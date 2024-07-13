Release history
===============

Version 0.3
  - The ``pactl`` module is a Python implementation of the ``pactl`` command
    that runs both on Pulseaudio and Pipewire.
  - ``server`` and ``flags`` are optional arguments of the LibPulse constructor
    used by pa_context_connect() when connecting to the server.
  - Exceptions in callbacks and asyncio tasks are propagated to the async
    methods.
  - Use ``pa_strerror()`` to log errors.
  - Drain the pulse context before disconnecting.

Version 0.2
  - Add the ``pa_context_subscribe.py`` example.
  - Add the ``pa_context_load_module.py`` example.
  - Unreference stream pointer upon exit in ``pa_stream_new.py`` example.
  - Raise ``LibPulseArgumentError`` when args do not match the signature.
  - Document callback concurrent access.
  - ``stream_success_methods`` require a ``pa_stream *`` ctypes pointer as first
    argument.

Version 0.1
  - Publish the project on PyPi.
  - Raise an exception upon instantiation of more than one LibPulse instance.

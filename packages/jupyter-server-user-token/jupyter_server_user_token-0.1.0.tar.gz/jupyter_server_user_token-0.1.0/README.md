# jupyter-server-user-token

A simple Jupyter Server extension that adds the server's User Token (if it exists) into the process's environment as `JUPYTER_SERVER_USER_TOKEN`.

## Why?

Some frontend extensions and visualisation libraries use iframes to render documents served out on Jupyter Server Proxy.

These iframes might have an href target like: `/proxy/index.html?some=query-params` and work happily when used in notebooks and lab.

In the context of `myst` the same visualisations run into issues when connecting to remote Jupyter servers running on different origins, as the cookie-based auth in play in a same-origin lab front ends, will fail on a typlical myst website.

By exposing the user token, end user code can do something about this and supply the user token string to the library / extension code that needs it.

import json
import typing as t

from superduper import superduper

from . import command


@command(help='Start local cluster: server, ray and change data capture')
def local_cluster(
    action: str,
    notebook_token: t.Optional[str] = None,
    num_workers: int = 0,
    attach: bool = True,
    cdc: bool = False,
):
    """Start local cluster: server, ray and change data capture.

    :param action: Action to perform (up, down, attach).
    :param notebook_token: Notebook token.
    :param num_workers: Number of workers.
    :param attach: Attach to the cluster.
    :param cdc: Start change data capture or not.
    """
    from superduper.server.cluster import attach_cluster, down_cluster, up_cluster

    action = action.lower()

    if action == 'up':
        try:
            down_cluster()
        except Exception:
            pass
        up_cluster(
            notebook_token=notebook_token,
            num_workers=num_workers,
            attach=attach,
            cdc=cdc,
        )
    elif action == 'down':
        down_cluster()
    elif action == 'attach':
        attach_cluster()


@command(help='Start vector search server')
def vector_search():
    """Start vector search server."""
    from superduper.vector_search.server.app import app

    app.start()


@command(help='Start scheduler server')
def scheduler():
    """Start scheduler server."""
    from superduper.server.scheduler import app

    app.pre_start()
    app.print_routes()
    app.start()


@command(help='Start standalone change data capture')
def cdc():
    """Start standalone change data capture."""
    from superduper.cdc.app import app

    app.start()


@command(help='Start standalone crontab service')
def crontab():
    """Start standalone crontab service."""
    from superduper.crontab.service import app

    app.start()


@command(help='Serve a model on ray')
def ray_serve(
    model: str,
    version: t.Optional[int] = None,
    ray_actor_options: str = '',
    num_replicas: int = 1,
):
    """Serve a model on ray.

    :param model: Model name.
    :param version: Model version.
    :param ray_actor_options: Ray actor options.
    :param num_replicas: Number of replicas.
    """
    from superduper.backends.ray.serve import run

    run(
        model=model,
        version=version,
        ray_actor_options=json.loads(ray_actor_options),
        num_replicas=num_replicas,
    )


@command(help='Start FastAPI REST server')
def rest():
    """Start FastAPI REST server."""
    from superduper.rest.app import app

    app.start()


@command(help='Start a stream')
def subscribe(identifier: str, version: t.Optional[int] = None):
    """Run a stream."""
    db = superduper()
    subscriber = db.load('subscriber', identifier, version=version)
    subscriber.run()

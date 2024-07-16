from typing import Annotated

import typer

from ...config import Config
from ..app import app
from ..helpers.typer import get_hashed_default


@app.command()
def list_subjects(
    remote_name: Annotated[str, typer.Argument(help='The name of the remote')],
    hash_subject_ids: Annotated[
        bool,
        typer.Option(
            help='Whether to hash the subject IDs. Overrides the `has_subject_ids` setting.',
            default_factory=get_hashed_default,
            show_default=False,
        ),
    ],
):
    """
    List the subjects in a sync endpoint.
    """
    config = Config.from_cmdargs()
    sync = config.get_sync_by_name(remote_name)
    subjects = sync.get_all_subjects(hash=hash_subject_ids)

    typer.echo(f'Found {len(subjects)} subjects in project {remote_name}.\n')

    for subject in subjects:
        typer.echo(subject)

import rich_click as click

from joplin_bulker.import_goodreads import import_good_reads
from joplin_bulker.tag import main


@click.group()
def cli() -> None:
    """Joplin Bulker."""


@cli.command()
@click.option("--rm", help="Delete the tag")
def tag(rm: str) -> None:
    """Delete tag."""
    main(rm)


@cli.command()
@click.argument("file_name", type=click.Path(exists=True))
def import_goodreads(file_name: str) -> None:
    """Import Good Reads CSV file."""
    import_good_reads(file_name)


if __name__ == "__main__":
    cli()

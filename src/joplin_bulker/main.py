import click
from joplin_bulker.tag import main
from joplin_bulker.import_goodreads import import_good_reads


@click.group()
def cli():
    pass


@cli.command()
@click.option('--rm', help='Delete the tag')
def tag(rm):
    main(rm)


@cli.command()
@click.argument('file_name', type=click.Path(exists=True))
def import_goodreads(file_name):
    import_good_reads(file_name)


if __name__ == '__main__':
    cli()

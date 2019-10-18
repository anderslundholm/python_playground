import click




@click.group()
def cli():
    pass


@click.command()
def initdb():
    click.echo('Initialized the database.')


@click.command()
def dropdb():
    click.echo('Dropped the database.')


@click.command()
@click.option('--partitions', default=1, help='number of partitions')
@click.argument('host')
def setup_disks(partitions, host):
    for x in range(partitions):
        click.echo('{host} - partition {x}'.format(host=host, x=x))


cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(setup_disks)


if __name__ == '__main__':
    cli()
    # $ py cli.py setup-disks --partitions 3 anders.com
    # anders.com - partition 0
    # anders.com - partition 1
    # anders.com - partition 2
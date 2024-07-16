import click

from netboxNinja.netbox_ninja import NetboxNinja


@click.command()
@click.option('--csv', required=True, type=click.Path(exists=True), help='Path to the CSV file.')
def main(csv):
    netbox_ninja = NetboxNinja()
    netbox_ninja.start(csv)


if __name__ == "__main__":
    main()

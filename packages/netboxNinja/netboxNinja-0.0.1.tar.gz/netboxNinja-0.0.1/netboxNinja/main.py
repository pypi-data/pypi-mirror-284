import click
from netboxNinja.logic.csv_reader import CSVReader
from netboxNinja.netbox_ninja import NetboxNinja


@click.command()
@click.option('--csv', required=True, type=click.Path(exists=True), help='Path to the CSV file.')
def main(csv):
    interfaces = CSVReader.read_csv_as_dict_with_semicolon(csv)
    post_interfaces_loop(interfaces)


def post_interfaces_loop(interfaces):
    if not interfaces:
        return
    ninja = NetboxNinja()
    later_interfaces: list = []
    for interface in interfaces:
        error = ninja.post_interface(interface)
        if error == "error":
            later_interfaces.append(interface)
    print(later_interfaces)
    post_interfaces_loop(later_interfaces)


if __name__ == '__main__':
    main()

import click
import csv
import json

def load_scenario(csv_fname, config_fname=None):
    years = []

    with open(csv_fname) as csv_file:
        csv_reader = csv.reader(csv_file, dialect='excel')
        for row in csv_reader:
            # Skip first 2 lines
            if not row[0].isnumeric():
                continue

            year = {
                'year': int(row[0]),
                'ed_age': int(row[1]),
                'wendy_age': int(row[2]),
                'ed_ss': float(row[3]),
                'wendy_ss': float(row[4]),
                # Skip total income
                'expenses': float(row[6]),
                # Skip 'From FI Assets'
                'fi_assets': float(row[8])
            }
            json_data['years'].append(year)

    config = None
    if config_fname:
        with open(config_fname) as config_file:
            config = json.load(config_file)

    json_data = {
        'config': config if config else {},
        'years': years,
    }

    return json_data


@click.command()
@click.version_option('0.1.0', prog_name='ScenarioLoader')
@click.argument('csv_fname', type=click.Path(exists=True))
def cli(csv_fname):
    click.echo(f"Loading csv file: {csv_fname}")

    json_data = load_scenario(csv_fname)

    json_fname = csv_fname.replace('.csv', '.json')
    click.echo(f"Writing to json file: {json_fname}")
    with open(json_fname, "w") as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    cli()

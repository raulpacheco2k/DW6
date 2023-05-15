import json
from datetime import datetime, timedelta

import boto3
import typer
from rich import print
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

# AWS Configure
client = boto3.client('logs')
log_group_name = '/aws/lambda/my-lambda-function'
start_time = (datetime.now() - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@app.command()
def homologation():
    json_array = json.dumps(
        [
            {'message': 'Transtype RPJ001 associada ao lançamento'},
            {'message': 'Transtype RPJ002 associada ao lançamento'},
            {'message': 'Transtype RPJ002 associada ao lançamento'},
            {'message': 'Transtype RPJ003 associada ao lançamento'}
        ]
    )

    print(datetime.now() - timedelta(hours=3))

    response = client.filter_log_events(
        logGroupName=log_group_name,
        startTime=int(start_time.timestamp() * 1000),
        endTime=int(end_time.timestamp() * 1000)
    )

    print(f"Ambiente: [bold green]Homologação[/bold green]\nProcurar evento de {start_time} até {end_time}")

    table = Table("Transctionid(s)", "6239", "6253", "Transtype(s)", "Envio para FE3", "Envio para motores")

    for item in json.loads(json_array):
        table.add_row("ea33d327-6fb9-4c8a-af69-3c9e79f59d49", "Ok", "Ok", item['message'], "Ok", "Ok")
    console.print(table)


if __name__ == "__main__":
    app()

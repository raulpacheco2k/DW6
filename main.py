import boto3
import typer
from datetime import datetime, timedelta
from rich import print
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

client = boto3.client('logs')
log_group_name = '/aws/lambda/transformacao'
end_time = datetime.now()
start_time = end_time - timedelta(hours=3)
query = "fields @timestamp, @message, @logStream, @log" \
        "| sort @timestamp desc"


@app.command()
def transtype():
    print(
        f"[bold]Filtro de datas:[/bold] "
        f"{start_time.strftime('%Y-%m-%d %H:%M:%S')} até {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    response = client.filter_log_events(
        logGroupName=log_group_name,
        startTime=int(start_time.timestamp() * 1000),
        endTime=int(end_time.timestamp() * 1000)
    )

    table = Table()
    table.add_column("Transtype(s) gerada(s)", justify="center")

    for event in response['events']:
        if event['message'][:3] == "END":
            table.add_row(event['message'].replace("\n", ""))

    console.print(table)


if __name__ == "__main__":
    app()

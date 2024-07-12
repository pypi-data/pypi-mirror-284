import click
from fancykimai.functions.kimai import kimai_request
from rich import table, console
import json
from iterfzf import iterfzf
from fancykimai.classes.click_groups import AliasedGroup
from fancykimai.functions.config import set_config
from fancykimai.functions.activity import select_activity

@click.group(name='activities', cls=AliasedGroup)
def activities_group():
    pass

@activities_group.command(name='list')
@click.option('-o', '--output', type=click.Choice(['table', 'json']), default='table', help='Output format')
def list_activities(output: str):
    r = kimai_request('api/activities')
    if output == 'table':
        columns = [
            {'column': "ID", 'response_key': 'id', 'function': str, 'style': 'cyan'},
            {'column': "Name", 'response_key': 'name', 'function': str, 'style': 'magenta'},
        ]
        rich_table = table.Table(title="Activities")
        for column in columns:
            rich_table.add_column(column['column'], style=column['style'])
        for activity in r:
            rich_table.add_row(*[column['function'](activity[column['response_key']]) for column in columns])
        rich_console = console.Console()
        rich_console.print(rich_table)
    else:
        click.echo(json.dumps(r))


@activities_group.command(name='select')
@click.argument('activity_id', type=int, required=False)
@click.option('--debug', is_flag=True, help='Debug mode')
@click.pass_context
def select_activity_command(ctx, activity_id: int, debug: bool):
    if not activity_id:
        selected_activity = select_activity(ctx, None, value=None, debug=debug, select_function=True)
        set_config('activity', selected_activity, debug=debug)
        click.echo(f"Selected activity: {selected_activity}")
    else:
        r = kimai_request('api/activities/' + str(activity_id))
        set_config('activity', activity_id, debug=True)
        click.echo(f"Selected activity: {r['name']}")
    
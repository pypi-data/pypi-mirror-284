import click
from pywinauto.application import Application
from pywinauto.findwindows import ElementNotFoundError
from pywinauto.timings import TimeoutError


def run_power_automate_flow(flow):
    click.echo(f'Starting Power Automate flow {flow}...')
    power_automate_exe_path = 'PAD.Console.Host.exe'

    app = Application(backend="uia").start(power_automate_exe_path, timeout=1000)
    dlg_spec = app.PowerAutomate

    while True:
        try:
            dlg_spec.wait('exists enabled visible ready')
            dlg_spec.maximize()
            click.echo('Connected.')
            break
        except TimeoutError:
            click.echo('Trying to connect...')

    # Clica Meus fluxos
    find_and_click_elements(dlg_spec, **{
        'title': 'Meus fluxos',
        'control_type': 'TabItem'
    })

    # Clica linha do fluxo
    flow_line = {
        'title': flow,
        'control_type': 'DataItem'
    }
    find_and_click_elements(dlg_spec, **flow_line)
    # import ipdb; ipdb.set_trace(context=10)
    # Clica na execução do fluxo
    find_and_click_elements(dlg_spec, **{
        'title': 'Executar',
        'auto_id': 'StartFlowButton',
        'control_type': 'Button',
    })

    # Clica no botão ok casa fluxo tenha variáveis de ambiente
    find_and_click_elements(dlg_spec, **{
        'title': 'OK',
        'auto_id': 'Button',
        'control_type': 'Button',
    })

    while True:
        found_element = dlg_spec.child_window(**flow_line).wrapper_object()
        if 'Não está sendo executado' in found_element.texts():
            find_and_click_elements(dlg_spec, **{
                'title': 'Fechar janela',
                'auto_id': 'PART_CloseButton',
                'control_type': 'Button',
            })
            click.echo(f'Power Automate flow {flow} executed.')
            break

def find_app():
    pass

def find_and_click_elements(dlg_spec, max_attempt=5, **kwargs):
    # import ipdb; ipdb.set_trace(context=10)
    while max_attempt > 0:
        try:
            found_element = dlg_spec.child_window(**kwargs).wrapper_object()
            click.echo(f'{kwargs.get('title', 'Title not defined')} element found.')
            found_element.click_input()
            return None
        except ElementNotFoundError:
            click.echo(f'{kwargs.get('title', 'Title not defined')} element not found.')
            max_attempt -= 1
    click.echo(f'{kwargs.get('title', 'Title not defined')} element not found after max attempts.')

@click.command(name='automate')
@click.argument('flow', required=True)
def run_power_automate_flow_cli(flow):
    """
    pythomate run automate <nome-fluxo>
    """
    run_power_automate_flow(flow)

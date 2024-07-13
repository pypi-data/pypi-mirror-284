import click

from cli.prediction import predict
from cli.tlcli import authenticate, process_xml, config


@click.group()
@click.version_option()
@click.pass_context
@click.argument("domain")
@click.argument("username")
@click.argument("password")
def main(
    ctx: click.Context,
    domain: str,
    username: str,
    password: str,
) -> None:
    ctx.obj = {}
    config(ctx, domain=domain)
    authenticate(ctx=ctx, username=username, password=password)


main.add_command(process_xml)
main.add_command(predict)


if __name__ == "__main__":
    main()

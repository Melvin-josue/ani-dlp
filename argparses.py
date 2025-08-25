import argparse
import sys
import argcomplete
from argcomplete.completers import SuppressCompleter


class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        # Si hay error → siempre mostrar help
        self.print_help()
        sys.exit(2)


parser = CustomArgumentParser(
    prog="ani-dlp",
    description="ANI-DLP",
    usage="ani-dlp ... [URL] ... [OPTIONS] ...",
    add_help=False,
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# Flag de ayuda en español
parser.add_argument(
    "-h", "--ayuda", "--help",
    action="help",
    help="Muestra cómo se usa el script"
)

# Posicional (sin autocompletar archivos)
anime_arg = parser.add_argument(
    "anime",
    type=str,
    nargs="?",
    help="Nombre del anime o URL",
    metavar="URL"
)
anime_arg.completer = SuppressCompleter

# Flag con choices → autocompleta con esas opciones
parser.add_argument(
    "--quality",
    type=str,
    default="1080p",
    help="Calidad deseada",
    choices=["360p", "480p", "720p", "1080p"]
)

# Flag normal (sin autocompletar rutas)
mio_arg = parser.add_argument(
    "--mio",
    type=str,
    default="algo mio",
    help="La ayuda que puse"
)
mio_arg.completer = SuppressCompleter


# Activar autocompletado
argcomplete.autocomplete(parser)

args = parser.parse_args()

# Si falta el posicional → mostrar help
if not args.anime:
    parser.print_help()
    sys.exit(1)

print("Anime:", args.anime)
print("Calidad:", args.quality)
print("Mio:", args.mio)

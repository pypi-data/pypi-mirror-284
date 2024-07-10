# ozi/new/__main__.py
# Part of the OZI Project, under the Apache License v2.0 with LLVM Exceptions.
# See LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""ozi-new entrypoint script."""
from __future__ import annotations

import shlex
import sys
from itertools import chain
from typing import TYPE_CHECKING

from ozi_spec import METADATA  # pyright: ignore
from ozi_templates import load_environment  # type: ignore
from tap_producer import TAP

from ozi.new.interactive import interactive_prompt
from ozi.new.parser import parser
from ozi.new.validate import postprocess_arguments
from ozi.new.validate import preprocess_arguments
from ozi.render import RenderedContent

if TYPE_CHECKING:
    from argparse import Namespace
    from typing import Callable
    from typing import TypeAlias

    Composable: TypeAlias = Callable[[Namespace], Namespace]


def project(project: Namespace) -> None:
    """Create a new project in a target directory."""
    project = postprocess_arguments(preprocess_arguments(project))
    RenderedContent(
        load_environment(vars(project), METADATA.asdict()),
        project.target,
        project.name,
        project.ci_provider,
        project.long_description_content_type,
    ).render()


def wrap(project: Namespace) -> None:  # pragma: no cover
    """Create a new wrap file for publishing. Not a public function."""
    env = load_environment(vars(project), METADATA.asdict())
    template = env.get_template('ozi.wrap.j2')
    with open('ozi.wrap', 'w', encoding='UTF-8') as f:
        f.write(template.render())


def main(args: list[str] | None = None) -> None:  # pragma: no cover
    """Main ozi.new entrypoint."""
    pipe = sys.stdin if not sys.stdin.isatty() else None
    args = (
        list(chain.from_iterable([shlex.split(line.strip()) for line in pipe]))
        if pipe
        else args
    )
    ozi_new = parser.parse_args(args=args)
    ozi_new.argv = shlex.join(args) if args else shlex.join(sys.argv[1:])
    match ozi_new:
        case ozi_new if ozi_new.new in ['i', 'interactive']:
            args = interactive_prompt(ozi_new)
            ozi_new = parser.parse_args(args=args)
            main(args)
        case ozi_new if ozi_new.new in ['p', 'project']:
            project(ozi_new)
            TAP.end()
        case ozi_new if ozi_new.new in ['w', 'wrap']:
            wrap(ozi_new)
            TAP.end()
        case _:
            parser.print_usage()
    return None


if __name__ == '__main__':
    main()

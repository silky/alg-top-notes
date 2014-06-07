#!/usr/bin/env python
# coding: utf-8

import os
import sys


def build_tex (filename):
    tex = r"""\input{preamble}
\input{header}
\title{\input{title}}

\begin{document}
\maketitle
"""

    inputs = []
    with open("layout.md", "r") as f:
        lines = f.readlines()
        for l in lines:
            inputs.append("\input{" + l.strip('\r\n') + "}")

    tex += ("\n".join(inputs))
    tex += "\n\end{document}"

    with open(filename, 'w') as f:
        f.write(tex)
    print("Wrote to {}".format(filename))

if __name__ == "__main__":
    full_dirname = os.path.dirname(os.path.realpath(__file__))
    _, dirname = os.path.split(full_dirname)
    build_tex(dirname + ".tex")

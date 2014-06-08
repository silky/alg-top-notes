alg-top-notes
=============

[![Build Status](https://travis-ci.org/silky/alg-top-notes.svg?branch=master)](https://travis-ci.org/silky/alg-top-notes)

These notes are viewable online at [Authorea](https://authorea.com/users/7271).

**Note**: These notes are out of date at the moment pending the resolution of
some issues; more information can be found [here](https://github.com/OpenScienceWorkshops/OpenScienceWorkshops.github.io/issues/50) (well, actually, I could keep these up to date even if I didn't use Authorea, but because I'm not using Authorea I'm still using LyX, so that's secretly the reason these aren't up to date - because I'm not exporting from LyX all the time.)

You can build this locally with

    ./build_mainfile.py && latexmk -pvc -pdf alg-top-notes.tex

(This regenerates the main TeX file and asks latexmk to watch for any changes
 you make locally, and asks latexmk to preview the resulting pdf.)

#pyminifier -o minified/code.py -O code.py
#pyminifier -o minified/lib/keyboard/__init__.py -O lib/keyboard/__init__.py
#pyminifier -o minified/lib/keyboard/action_code.py -O lib/keyboard/action_code.py
#pyminifier -o minified/lib/keyboard/hid.py -O lib/keyboard/hid.py
#pyminifier -o minified/lib/keyboard/matrix.py -O lib/keyboard/matrix.py
#pyminifier -o minified/lib/keyboard/util.py -O lib/keyboard/util.py
#pyminifier -o minified/lib/keyboard/model/__init__.py -O lib/keyboard/model/__init__.py
#pyminifier -o minified/lib/keyboard/model/ut47.py -O lib/keyboard/model/ut47.py

#rm -r /Volumes/CIRCUITPY/*
#rsync -av --exclude=".*" minified/ /Volumes/CIRCUITPY/

rm -r /Volumes/CIRCUITPY/*
rsync -av --exclude=".*" lib/ /Volumes/CIRCUITPY/lib
cp code.py /Volumes/CIRCUITPY/

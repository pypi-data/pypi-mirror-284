# UniversalColor

Simple lightweight polymorph color class for python 3.10+

## Features

- Can store colors with or without an alpha channel in RGB, HSL, and HSV formats.
- Easily converts between formats, understands [#HEX](https://www.w3schools.com/css/css_colors_hex.asp), CSS ([rgb](https://www.w3schools.com/css/css_colors_rgb.asp), [hsl](https://www.w3schools.com/css/css_colors_hsl.asp), [color names](https://www.w3schools.com/css/css_colors.asp)), and [LSL](https://wiki.secondlife.com/wiki/Category:LSL_Vector).

## Install

```bash
pip install universalcolor
```
  or
```bash
https://github.com/erfeatux/UniversalColor.git
```

## Usage

```python
from universalcolor import Color

Color(red=255, green=0, blue=0)
# Color(RGB(red=1.0, green=0.0, blue=0.0, alpha=None))

Color(hlsHue=360, hslSat=1.0, hslLight=0.5)
# Color(HSL(hue=0.0, sat=1.0, light=0.5, alpha=None))

Color(hlsHue=360, hslSat=1.0, hsvValue=1.0, alpha=0.5)
# Color(HSL(hue=0.0, sat=1.0, light=0.5, alpha=0.5))

Color('#ff0000')
# Color(RGB(red=1.0, green=0.0, blue=0.0, alpha=None))

Color('rgb(255, 0, 0)')
# Color(RGB(red=1.0, green=0.0, blue=0.0, alpha=None))

Color('hsla(360, 100%, 50%, 0.5)')
# Color(HSL(hue=1.0, sat=1.0, light=0.5, alpha=0.5))

Color('<1.0, 0.0, 0.0>', alpha = 1.0).asName()
# 'red'

Color(hslHue=360).asRGB()
# RGB(red=1.0, green=0.0, blue=0.0, alpha=None)

Color('red').asHSV()
#HSV(hue=0.0, sat=1.0, value=1.0, alpha=None)

Color('green').asHEX()
# '#008000'

Color('aqua').asCSSHSL()
# 'hsl(180, 100%, 50%)'

Color(hslHue=120).red
# 0

Color(hslHue=120).green
# 255

Color(hslHue=120).blue
# 0

Color(hslHue=120).hslHue
#120

Color(hslHue=120).hslSat
# 100

Color(hslHue=120).hslLight
# 50

Color(hslHue=120).hsvHue
# 120

Color(hslHue=120).hsvSat
# 100

Color(hslHue=120).hsvValue
# 100
```

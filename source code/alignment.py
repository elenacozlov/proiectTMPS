from enum import Enum
from docx.enum.text import WD_ALIGN_PARAGRAPH
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

class Alignment(Enum):
    LEFT = 1
    CENTER = 2
    RIGHT = 3
    JUSTIFY = 4

    def reportlab(self):
        return {Alignment.LEFT: TA_LEFT,
                Alignment.CENTER: TA_CENTER,
                Alignment.RIGHT: TA_RIGHT,
                Alignment.JUSTIFY: TA_JUSTIFY}[self]

    def docx(self):
        return {Alignment.LEFT: WD_ALIGN_PARAGRAPH.LEFT,
                Alignment.CENTER: WD_ALIGN_PARAGRAPH.CENTER,
                Alignment.RIGHT: WD_ALIGN_PARAGRAPH.RIGHT,
                Alignment.JUSTIFY: WD_ALIGN_PARAGRAPH.JUSTIFY}[self]
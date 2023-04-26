from varmain.primitiv import *
from varmain.custom import *
from math import *

@activate(Group="Support", TooltipShort="JD01", TooltipLong="JD01", LengthUnit="mm", Ports="1")
@group("MainDimensions")
@param(D=LENGTH, TooltipShort="Pipe Diameter", TootltipLong="Pipe Diameter")
@param(TH=LENGTH, TooltipShort="Height", TooltipLong="Overall Height")
@param(PL=LENGTH, TooltipShort="Pad Length", TooltipLong="Pad Length")
@param(PW=LENGTH, TooltipShort="Pad Width", TooltipLong="Pad Width")
@param(PT=LENGTH, TooltipShort="Pad Thickness", TooltipLong="Pad Thickness")
@param(CSD=LENGTH, TooltipShort="Support Diameter", TooltipLong="Cylindrical Pipe Support Diameter")
@param(CSH=LENGTH, TooltipShort="Support Height", TooltipLong="Cylindrical Pipe Height")

def JD01(s, D=60.00, TH=500.00, PL=100.00, PW=100.00, PT=10.00, CSD=60.00, CSH=450.00, ID="JD01", **kw):

    # create Base Plate
    oBP = BOX(s, L=PL, W=PW, H=PT).Translate(0,0,(PT/2.00)-TH)

    # create cylindrical support on Base Plate
    oCS = CYLINDER(s, R=CSD/2.00, H=CSH).rotateZ(90).translate(0,0,-TH)
    oBP.uniteWith(oCS)
    oCS.erase()

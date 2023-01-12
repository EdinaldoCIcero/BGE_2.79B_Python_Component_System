import bge
from collections import OrderedDict





class ThirdPerson(bge.types.KX_PythonComponent):
    """Basic third person controls"""


    args = OrderedDict((

                        ("@Speeds_Values",""),

                        ("Move_Speed"           , 0.10),
                        ("Turn_Speed"           , 0.05),
                        

                        ("@_Keyboards_Events",""),

                        ("Move_Front_Key"       , "w" ),
                        ("Move_Back_Key"        , "s" ),
                        ("Turn_Right_Key"       , "d"),
                        ("Turn_Left_key"        , "a"),
                        ))


    def keyboardDict(self):

        dictkeys = {    # Alphabet keys 
                        "a" :  bge.events.AKEY,
                        "b" :  bge.events.BKEY,
                        "c" :  bge.events.CKEY,
                        "d" :  bge.events.DKEY,
                        "e" :  bge.events.EKEY,
                        "f" :  bge.events.FKEY,
                        "g" :  bge.events.GKEY,
                        "h" :  bge.events.HKEY,
                        "i" :  bge.events.IKEY,
                        "j" :  bge.events.JKEY,
                        
                        "k" :  bge.events.KKEY,
                        "l" :  bge.events.LKEY,
                        "m" :  bge.events.MKEY,
                        "n" :  bge.events.NKEY,
                        "o" :  bge.events.OKEY,
                        "p" :  bge.events.PKEY,
                        "q" :  bge.events.QKEY,
                        "r" :  bge.events.RKEY,
                        "s" :  bge.events.SKEY,
                        "t" :  bge.events.TKEY,
                        "u" :  bge.events.UKEY,
                        "v" :  bge.events.VKEY,
                        "w" :  bge.events.WKEY,
                        "x" :  bge.events.XKEY,
                        "y" :  bge.events.YKEY,
                        "z" :  bge.events.ZKEY,

                        # Other Keys 
                        
                        "acent_grave"   : bge.events.ACCENTGRAVEKEY,
                        "back_slash"    : bge.events.BACKSLASHKEY ,
                        "back_space"    : bge.events.BACKSPACEKEY,
                        "comma"         : bge.events.COMMAKEY,
                        "del"           : bge.events.DELKEY,
                        "end"           : bge.events.ENDKEY,
                        "equal"         : bge.events.EQUALKEY,
                        "esc"           : bge.events.ESCKEY,
                        "home"          : bge.events.HOMEKEY,
                        "insert"        : bge.events.INSERTKEY,
                        "left_bracket"  : bge.events.LEFTBRACKETKEY,
                        "linefeed"      : bge.events.LINEFEEDKEY,
                        "minus"         : bge.events.MINUSKEY,
                        "page_down"     : bge.events.PAGEDOWNKEY,
                        "page_up"       : bge.events.PAGEUPKEY,
                        "pause"         : bge.events.PAUSEKEY,
                        "period"        : bge.events.PERIODKEY,
                        "quote"         : bge.events.QUOTEKEY,
                        "right_bracket" : bge.events.RIGHTBRACKETKEY,
                        "enter"         : bge.events.ENTERKEY,
                        "semicolon"     : bge.events.SEMICOLONKEY,
                        "slash"         : bge.events.SLASHKEY,
                        "space"         : bge.events.SPACEKEY,
                        "tab"           : bge.events.TABKEY,

                        # Modifiers Keys 
                        "caps_lock"     : bge.events.CAPSLOCKKEY,
                        "left_ctrl"     : bge.events.LEFTCTRLKEY,
                        "left_alt"      : bge.events.LEFTALTKEY,
                        "right_alt"     : bge.events.RIGHTALTKEY,
                        "right_ctrl"    : bge.events.RIGHTCTRLKEY,
                        "right_shift"   : bge.events.RIGHTSHIFTKEY,
                        "left_shift"    : bge.events.LEFTSHIFTKEY,


                        # Arrow Keys 

                        "left_arrow"    : bge.events.LEFTARROWKEY,
                        "down_arrow"    : bge.events.DOWNARROWKEY,
                        "right_arrow"   : bge.events.RIGHTARROWKEY,
                        "up_arrow"      : bge.events.UPARROWKEY,

                        # Number keys

                        "0"     : bge.events.ZEROKEY,
                        "1"     : bge.events.ONEKEY,
                        "2"     : bge.events.TWOKEY,
                        "3"     : bge.events.THREEKEY,
                        "4"     : bge.events.FOURKEY,
                        "5"     : bge.events.FIVEKEY,
                        "6"     : bge.events.SIXKEY,
                        "7"     : bge.events.SEVENKEY,
                        "8"     : bge.events.EIGHTKEY,
                        "9"     : bge.events.NINEKEY,

                        # Numberpad Keys

                        "pad_0" : bge.events.PAD0,
                        "pad_1" : bge.events.PAD1,
                        "pad_2" : bge.events.PAD2,
                        "pad_3" : bge.events.PAD3,
                        "pad_4" : bge.events.PAD4,
                        "pad_5" : bge.events.PAD5,
                        "pad_6" : bge.events.PAD6,
                        "pad_7" : bge.events.PAD7,
                        "pad_8" : bge.events.PAD8,
                        "pad_9" : bge.events.PAD9,
                        "pad_period" : bge.events.PADPERIOD,
                        "pad_slash"  : bge.events.PADSLASHKEY,
                        "pad_ster"   : bge.events.PADASTERKEY,
                        "pad_minus"  : bge.events.PADMINUS,
                        "pad_enter"  : bge.events.PADENTER,
                        "pad_plus"   : bge.events.PADPLUSKEY,

                        # Function Keys
                        "f1" : bge.events.F1KEY,
                        "f2" : bge.events.F2KEY,
                        "f3" : bge.events.F3KEY,
                        "f4" : bge.events.F4KEY,
                        "f5" : bge.events.F5KEY,
                        "f6" : bge.events.F6KEY,
                        "f7" : bge.events.F7KEY,
                        "f8" : bge.events.F8KEY,
                        "f9" : bge.events.F9KEY,
                        "f10" : bge.events.F10KEY,
                        "f11" : bge.events.F11KEY,
                        "f12" : bge.events.F12KEY,
                        "f13" : bge.events.F13KEY,
                        "f14" : bge.events.F14KEY,
                        "f15" : bge.events.F15KEY,
                        "f16" : bge.events.F16KEY,
                        "f17" : bge.events.F17KEY,
                        "f18" : bge.events.F18KEY,
                        "f19" : bge.events.F19KEY
                   }

        return dictkeys



    #-----------------------------------------------
    def start(self, args):
        self.Move_Speed = args["Move_Speed"]
        self.Turn_Speed = args["Turn_Speed"]
        
        
        self.Move_Front_Key = args['Move_Front_Key']
        self.Move_Back_Key  = args['Move_Back_Key']

        self.Turn_Right_Key = args['Turn_Right_Key']
        self.Turn_Left_key  = args['Turn_Left_key']


        #---------------------------------------------
        scene       = bge.logic.getCurrentScene()
        self.GDICT  = bge.logic.globalDict


        
        self.keys_events = self.keyboardDict()


       




    #-----------------------------------------------
    def movementSimple(self):
        keyboard    = bge.logic.keyboard.events
        move        = 0
        rotate      = 0
        #-----------------------------------------------
        events_keys = { "front" : keyboard[ self.keys_events[ self.Move_Front_Key ] ],
                        "back"  : keyboard[ self.keys_events[ self.Move_Back_Key ] ],
                        
                        "left"  : keyboard[ self.keys_events[ self.Turn_Left_key ] ],
                        "right" : keyboard[ self.keys_events[ self.Turn_Right_Key ] ],
                        }

        if events_keys["front"] :
            move += self.Move_Speed
            
        if events_keys["back"] :
            move -= self.Move_Speed

        if events_keys["left"]:
            rotate += self.Turn_Speed
            
        if events_keys["right"]:
            rotate -= self.Turn_Speed


        self.object.applyMovement([0, move, 0], True)
        self.object.applyRotation([0, 0, rotate ], True)

        pass


    def update(self):
        keyboard    = bge.logic.keyboard.events
        #-----------------------------------------------
        self.movementSimple()

        pass



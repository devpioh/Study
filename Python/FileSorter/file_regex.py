import re

from enum import Enum

en_rep = '[a-zA-z]+'
ko_rep = '[\u3131-\u3163\uAC00-\uD7A3]+'
jp_rep = '[\u3040-\u309F\u30A0-\u30FF\u31F0-\u31FF]+'
ch_rep = '[\u2E80-\u2EFF\u3400-\u4DBF\u4E00-\u9FBF\uF900-\uFAFF]+'

class NationCode(Enum):
    none = 0
    en = 1 << 0
    ko = 1 << 1
    jp = 1 << 2
    ch = 1 << 3

    @staticmethod
    def toEasyRead(value):
        return str( "{0}".format(value).zfill(3) + " to binary : " + "{0:b}".format(value).zfill(4) )
    
    @staticmethod
    def getNationValue(src):
        flag = 0
        if None != StringConverter.en_comp.search( src ):
            flag |= NationCode.en.value
        if None != StringConverter.ko_comp.search( src ):
            flag |= NationCode.ko.value
        if None != StringConverter.jp_comp.search( src ):
            flag |= NationCode.jp.value
        if None != StringConverter.ch_comp.search( src ):
            flag |= NationCode.ch.value

        return flag

    @staticmethod
    def isNation( src, mask ):
        return 0 != src & mask

    @staticmethod
    def strToNationCode( src ):
        if None != src and "" != src:
            strNation = src.lower()
            if "en" == strNation or "english" == strNation:
                return NationCode.en
            elif "ko" == strNation or "korea" == strNation:
                return NationCode.ko
            elif "jp" == strNation or "japan" == strNation:
                return NationCode.jp
            elif "ch" == strNation or "china" == strNation:
                return NationCode.ch
        
        return NationCode.none

class StringConverter:
    en_comp = re.compile( en_rep )
    ko_comp = re.compile( ko_rep )
    jp_comp = re.compile( jp_rep )
    ch_comp = re.compile( ch_rep )

   


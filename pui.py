# -*- coding: utf-8 -*-

clkp=38
dtap=40

import RPi.GPIO as GPIO, sys, signal, uinput

def signal_handler(signal, frame):
	print ""
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(clkp, GPIO.IN)
GPIO.setup(dtap, GPIO.IN)
clk = lambda: GPIO.input(clkp)
dta = lambda: GPIO.input(dtap)

device=uinput.Device([ uinput.KEY_0, uinput.KEY_1, uinput.KEY_102ND, uinput.KEY_10CHANNELSDOWN, uinput.KEY_10CHANNELSUP, uinput.KEY_2, uinput.KEY_3, uinput.KEY_4, uinput.KEY_5, uinput.KEY_6, uinput.KEY_7, uinput.KEY_8, uinput.KEY_9, uinput.KEY_A, uinput.KEY_AB, uinput.KEY_ADDRESSBOOK, uinput.KEY_AGAIN, uinput.KEY_ALS_TOGGLE, uinput.KEY_ALTERASE, uinput.KEY_ANGLE, uinput.KEY_APOSTROPHE, uinput.KEY_APPSELECT, uinput.KEY_ARCHIVE, uinput.KEY_ATTENDANT_OFF, uinput.KEY_ATTENDANT_ON, uinput.KEY_ATTENDANT_TOGGLE, uinput.KEY_AUDIO, uinput.KEY_AUX, uinput.KEY_B, uinput.KEY_BACK, uinput.KEY_BACKSLASH, uinput.KEY_BACKSPACE, uinput.KEY_BASSBOOST, uinput.KEY_BATTERY, uinput.KEY_BLUE, uinput.KEY_BLUETOOTH, uinput.KEY_BOOKMARKS, uinput.KEY_BREAK, uinput.KEY_BRIGHTNESSDOWN, uinput.KEY_BRIGHTNESSUP, uinput.KEY_BRIGHTNESS_AUTO, uinput.KEY_BRIGHTNESS_CYCLE, uinput.KEY_BRIGHTNESS_MAX, uinput.KEY_BRIGHTNESS_MIN, uinput.KEY_BRL_DOT1, uinput.KEY_BRL_DOT10, uinput.KEY_BRL_DOT2, uinput.KEY_BRL_DOT3, uinput.KEY_BRL_DOT4, uinput.KEY_BRL_DOT5, uinput.KEY_BRL_DOT6, uinput.KEY_BRL_DOT7, uinput.KEY_BRL_DOT8, uinput.KEY_BRL_DOT9, uinput.KEY_BUTTONCONFIG, uinput.KEY_C, uinput.KEY_CALC, uinput.KEY_CALENDAR, uinput.KEY_CAMERA, uinput.KEY_CAMERA_DOWN, uinput.KEY_CAMERA_FOCUS, uinput.KEY_CAMERA_LEFT, uinput.KEY_CAMERA_RIGHT, uinput.KEY_CAMERA_UP, uinput.KEY_CAMERA_ZOOMIN, uinput.KEY_CAMERA_ZOOMOUT, uinput.KEY_CANCEL, uinput.KEY_CAPSLOCK, uinput.KEY_CD, uinput.KEY_CHANNEL, uinput.KEY_CHANNELDOWN, uinput.KEY_CHANNELUP, uinput.KEY_CHAT, uinput.KEY_CLEAR, uinput.KEY_CLOSE, uinput.KEY_CLOSECD, uinput.KEY_COFFEE, uinput.KEY_COMMA, uinput.KEY_COMPOSE, uinput.KEY_COMPUTER, uinput.KEY_CONFIG, uinput.KEY_CONNECT, uinput.KEY_CONTEXT_MENU, uinput.KEY_CONTROLPANEL, uinput.KEY_COPY, uinput.KEY_CUT, uinput.KEY_CYCLEWINDOWS, uinput.KEY_D, uinput.KEY_DASHBOARD, uinput.KEY_DATABASE, uinput.KEY_DELETE, uinput.KEY_DELETEFILE, uinput.KEY_DEL_EOL, uinput.KEY_DEL_EOS, uinput.KEY_DEL_LINE, uinput.KEY_DIGITS, uinput.KEY_DIRECTION, uinput.KEY_DIRECTORY, uinput.KEY_DISPLAYTOGGLE, uinput.KEY_DISPLAY_OFF, uinput.KEY_DOCUMENTS, uinput.KEY_DOLLAR, uinput.KEY_DOT, uinput.KEY_DOWN, uinput.KEY_DVD, uinput.KEY_E, uinput.KEY_EDIT, uinput.KEY_EDITOR, uinput.KEY_EJECTCD, uinput.KEY_EJECTCLOSECD, uinput.KEY_EMAIL, uinput.KEY_END, uinput.KEY_ENTER, uinput.KEY_EPG, uinput.KEY_EQUAL, uinput.KEY_ESC, uinput.KEY_EURO, uinput.KEY_EXIT, uinput.KEY_F, uinput.KEY_F1, uinput.KEY_F10, uinput.KEY_F11, uinput.KEY_F12, uinput.KEY_F13, uinput.KEY_F14, uinput.KEY_F15, uinput.KEY_F16, uinput.KEY_F17, uinput.KEY_F18, uinput.KEY_F19, uinput.KEY_F2, uinput.KEY_F20, uinput.KEY_F21, uinput.KEY_F22, uinput.KEY_F23, uinput.KEY_F24, uinput.KEY_F3, uinput.KEY_F4, uinput.KEY_F5, uinput.KEY_F6, uinput.KEY_F7, uinput.KEY_F8, uinput.KEY_F9, uinput.KEY_FASTFORWARD, uinput.KEY_FAVORITES, uinput.KEY_FILE, uinput.KEY_FINANCE, uinput.KEY_FIND, uinput.KEY_FIRST, uinput.KEY_FN, uinput.KEY_FN_1, uinput.KEY_FN_2, uinput.KEY_FN_B, uinput.KEY_FN_D, uinput.KEY_FN_E, uinput.KEY_FN_ESC, uinput.KEY_FN_F, uinput.KEY_FN_F1, uinput.KEY_FN_F10, uinput.KEY_FN_F11, uinput.KEY_FN_F12, uinput.KEY_FN_F2, uinput.KEY_FN_F3, uinput.KEY_FN_F4, uinput.KEY_FN_F5, uinput.KEY_FN_F6, uinput.KEY_FN_F7, uinput.KEY_FN_F8, uinput.KEY_FN_F9, uinput.KEY_FN_S, uinput.KEY_FORWARD, uinput.KEY_FORWARDMAIL, uinput.KEY_FRAMEBACK, uinput.KEY_FRAMEFORWARD, uinput.KEY_FRONT, uinput.KEY_G, uinput.KEY_GAMES, uinput.KEY_GOTO, uinput.KEY_GRAPHICSEDITOR, uinput.KEY_GRAVE, uinput.KEY_GREEN, uinput.KEY_H, uinput.KEY_HANGEUL, uinput.KEY_HANJA, uinput.KEY_HELP, uinput.KEY_HENKAN, uinput.KEY_HIRAGANA, uinput.KEY_HOME, uinput.KEY_HOMEPAGE, uinput.KEY_HP, uinput.KEY_I, uinput.KEY_IMAGES, uinput.KEY_INFO, uinput.KEY_INSERT, uinput.KEY_INS_LINE, uinput.KEY_ISO, uinput.KEY_J, uinput.KEY_JOURNAL, uinput.KEY_K, uinput.KEY_KATAKANA, uinput.KEY_KATAKANAHIRAGANA, uinput.KEY_KBDILLUMDOWN, uinput.KEY_KBDILLUMTOGGLE, uinput.KEY_KBDILLUMUP, uinput.KEY_KBDINPUTASSIST_ACCEPT, uinput.KEY_KBDINPUTASSIST_CANCEL, uinput.KEY_KBDINPUTASSIST_NEXT, uinput.KEY_KBDINPUTASSIST_NEXTGROUP, uinput.KEY_KBDINPUTASSIST_PREV, uinput.KEY_KBDINPUTASSIST_PREVGROUP, uinput.KEY_KEYBOARD, uinput.KEY_KP0, uinput.KEY_KP1, uinput.KEY_KP2, uinput.KEY_KP3, uinput.KEY_KP4, uinput.KEY_KP5, uinput.KEY_KP6, uinput.KEY_KP7, uinput.KEY_KP8, uinput.KEY_KP9, uinput.KEY_KPASTERISK, uinput.KEY_KPCOMMA, uinput.KEY_KPDOT, uinput.KEY_KPENTER, uinput.KEY_KPEQUAL, uinput.KEY_KPJPCOMMA, uinput.KEY_KPLEFTPAREN, uinput.KEY_KPMINUS, uinput.KEY_KPPLUS, uinput.KEY_KPPLUSMINUS, uinput.KEY_KPRIGHTPAREN, uinput.KEY_KPSLASH, uinput.KEY_L, uinput.KEY_LANGUAGE, uinput.KEY_LAST, uinput.KEY_LEFT, uinput.KEY_LEFTALT, uinput.KEY_LEFTBRACE, uinput.KEY_LEFTCTRL, uinput.KEY_LEFTMETA, uinput.KEY_LEFTSHIFT, uinput.KEY_LIGHTS_TOGGLE, uinput.KEY_LINEFEED, uinput.KEY_LIST, uinput.KEY_LOGOFF, uinput.KEY_M, uinput.KEY_MACRO, uinput.KEY_MAIL, uinput.KEY_MAX, uinput.KEY_MEDIA, uinput.KEY_MEDIA_REPEAT, uinput.KEY_MEMO, uinput.KEY_MENU, uinput.KEY_MESSENGER, uinput.KEY_MHP, uinput.KEY_MICMUTE, uinput.KEY_MINUS, uinput.KEY_MODE, uinput.KEY_MOVE, uinput.KEY_MP3, uinput.KEY_MSDOS, uinput.KEY_MUHENKAN, uinput.KEY_MUTE, uinput.KEY_N, uinput.KEY_NEW, uinput.KEY_NEWS, uinput.KEY_NEXT, uinput.KEY_NEXTSONG, uinput.KEY_NUMERIC_0, uinput.KEY_NUMERIC_1, uinput.KEY_NUMERIC_2, uinput.KEY_NUMERIC_3, uinput.KEY_NUMERIC_4, uinput.KEY_NUMERIC_5, uinput.KEY_NUMERIC_6, uinput.KEY_NUMERIC_7, uinput.KEY_NUMERIC_8, uinput.KEY_NUMERIC_9, uinput.KEY_NUMERIC_POUND, uinput.KEY_NUMERIC_STAR, uinput.KEY_NUMLOCK, uinput.KEY_O, uinput.KEY_OK, uinput.KEY_OPEN, uinput.KEY_OPTION, uinput.KEY_P, uinput.KEY_PAGEDOWN, uinput.KEY_PAGEUP, uinput.KEY_PASTE, uinput.KEY_PAUSE, uinput.KEY_PAUSECD, uinput.KEY_PC, uinput.KEY_PHONE, uinput.KEY_PLAY, uinput.KEY_PLAYCD, uinput.KEY_PLAYER, uinput.KEY_PLAYPAUSE, uinput.KEY_POWER, uinput.KEY_POWER2, uinput.KEY_PRESENTATION, uinput.KEY_PREVIOUS, uinput.KEY_PREVIOUSSONG, uinput.KEY_PRINT, uinput.KEY_PROG1, uinput.KEY_PROG2, uinput.KEY_PROG3, uinput.KEY_PROG4, uinput.KEY_PROGRAM, uinput.KEY_PROPS, uinput.KEY_PVR, uinput.KEY_Q, uinput.KEY_QUESTION, uinput.KEY_R, uinput.KEY_RADIO, uinput.KEY_RECORD, uinput.KEY_RED, uinput.KEY_REDO, uinput.KEY_REFRESH, uinput.KEY_REPLY, uinput.KEY_RESERVED, uinput.KEY_RESTART, uinput.KEY_REWIND, uinput.KEY_RFKILL, uinput.KEY_RIGHT, uinput.KEY_RIGHTALT, uinput.KEY_RIGHTBRACE, uinput.KEY_RIGHTCTRL, uinput.KEY_RIGHTMETA, uinput.KEY_RIGHTSHIFT, uinput.KEY_RO, uinput.KEY_S, uinput.KEY_SAT, uinput.KEY_SAT2, uinput.KEY_SAVE, uinput.KEY_SCALE, uinput.KEY_SCREEN, uinput.KEY_SCREENSAVER, uinput.KEY_SCROLLDOWN, uinput.KEY_SCROLLLOCK, uinput.KEY_SCROLLUP, uinput.KEY_SEARCH, uinput.KEY_SELECT, uinput.KEY_SEMICOLON, uinput.KEY_SEND, uinput.KEY_SENDFILE, uinput.KEY_SETUP, uinput.KEY_SHOP, uinput.KEY_SHUFFLE, uinput.KEY_SLASH, uinput.KEY_SLEEP, uinput.KEY_SLOW, uinput.KEY_SOUND, uinput.KEY_SPACE, uinput.KEY_SPELLCHECK, uinput.KEY_SPORT, uinput.KEY_SPREADSHEET, uinput.KEY_STOP, uinput.KEY_STOPCD, uinput.KEY_SUBTITLE, uinput.KEY_SUSPEND, uinput.KEY_SWITCHVIDEOMODE, uinput.KEY_SYSRQ, uinput.KEY_T, uinput.KEY_TAB, uinput.KEY_TAPE, uinput.KEY_TASKMANAGER, uinput.KEY_TEEN, uinput.KEY_TEXT, uinput.KEY_TIME, uinput.KEY_TITLE, uinput.KEY_TOUCHPAD_OFF, uinput.KEY_TOUCHPAD_ON, uinput.KEY_TOUCHPAD_TOGGLE, uinput.KEY_TUNER, uinput.KEY_TV, uinput.KEY_TV2, uinput.KEY_TWEN, uinput.KEY_U, uinput.KEY_UNDO, uinput.KEY_UNKNOWN, uinput.KEY_UP, uinput.KEY_UWB, uinput.KEY_V, uinput.KEY_VCR, uinput.KEY_VCR2, uinput.KEY_VENDOR, uinput.KEY_VIDEO, uinput.KEY_VIDEOPHONE, uinput.KEY_VIDEO_NEXT, uinput.KEY_VIDEO_PREV, uinput.KEY_VOICECOMMAND, uinput.KEY_VOICEMAIL, uinput.KEY_VOLUMEDOWN, uinput.KEY_VOLUMEUP, uinput.KEY_W, uinput.KEY_WAKEUP, uinput.KEY_WLAN, uinput.KEY_WORDPROCESSOR, uinput.KEY_WPS_BUTTON, uinput.KEY_WWAN, uinput.KEY_WWW, uinput.KEY_X, uinput.KEY_XFER, uinput.KEY_Y, uinput.KEY_YELLOW, uinput.KEY_YEN, uinput.KEY_Z, uinput.KEY_ZENKAKUHANKAKU, uinput.KEY_ZOOM, uinput.KEY_ZOOMIN, uinput.KEY_ZOOMOUT, uinput.KEY_ZOOMRESET])
d={162:'0', 104:'1', 120:'2', 100:'3', 164:'4', 116:'5', 108:'6', 188:'7', 124:'8', 98:'9', 56:'a', 76:'b', 132:'c', 196:'d', 36:'e', 212:'f', 44:'g', 204:'h', 194:'i', 220:'j', 66:'k', 210:'l', 92:'m', 140:'n', 34:'o', 178:'p', 168:'q', 180:'r', 216:'s', 52:'t', 60:'u', 84:'v', 184:'w', 68:'x', 172:'y', 88:'z', 112:'`', 50:';', 74:'´', 42:'[', 218:']', 130:',', 146:'.', 186:'\\', 82:'/', 114:'-', 170:'=', 90:'\n', 148:' ', 176:'\t', 174:'\033[1A', 78:'\033[1B', 46:'\033[1C', 214:'\033[1D', 102:'\b \b', 110:'\033', 40:'CTRL'}
di={162:uinput.KEY_0, 104:uinput.KEY_1, 120:uinput.KEY_2, 100:uinput.KEY_3, 164:uinput.KEY_4, 116:uinput.KEY_5, 108:uinput.KEY_6, 188:uinput.KEY_7, 124:uinput.KEY_8, 98:uinput.KEY_9, 56:uinput.KEY_A, 76:uinput.KEY_B, 132:uinput.KEY_C, 196:uinput.KEY_D, 36:uinput.KEY_E, 212:uinput.KEY_F, 44:uinput.KEY_G, 204:uinput.KEY_H, 194:uinput.KEY_I, 220:uinput.KEY_J, 66:uinput.KEY_K, 210:uinput.KEY_L, 92:uinput.KEY_M, 140:uinput.KEY_N, 34:uinput.KEY_O, 178:uinput.KEY_P, 168:uinput.KEY_Q, 180:uinput.KEY_R, 216:uinput.KEY_S, 52:uinput.KEY_T, 60:uinput.KEY_U, 84:uinput.KEY_V, 184:uinput.KEY_W, 68:uinput.KEY_X, 172:uinput.KEY_Y, 88:uinput.KEY_Z, 112:'`', 50:uinput.KEY_SEMICOLON, 74:'´', 42:'[', 218:']', 130:uinput.KEY_COMMA, 146:uinput.KEY_DOT, 186:uinput.KEY_BACKSLASH, 82:uinput.KEY_SLASH, 114:uinput.KEY_MINUS, 170:uinput.KEY_EQUAL, 90:uinput.KEY_ENTER, 148:uinput.KEY_SPACE, 176:uinput.KEY_TAB, 174:uinput.KEY_UP, 78:uinput.KEY_DOWN, 46:uinput.KEY_RIGHT, 214:uinput.KEY_LEFT, 102:uinput.KEY_BACKSPACE, 110:uinput.KEY_ESC, 40:uinput.KEY_LEFTCTRL}
l=0
while True:
	c=0
	for i in range(0, 11):
		while clk()==1:
			continue
		c=c<<1+dta()
		while clk()==0:
			continue
	c>>=2
	if l!=15 and c in d and c in di:
		device.emit_click(di[c])
		sys.stdout.write(d[c])
		sys.stdout.flush()
	l=c

import requests
import json
import win32api, win32gui, win32con
import time

def setWallPaper(pic):
  # open register
  regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
  win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
  win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
  # refresh screen
  win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,pic, win32con.SPIF_SENDWININICHANGE)

def main():
	img=json.loads(requests.get(url='https://api.xygeng.cn/Bing/url/').text)['data']
	file=requests.get(url=img).content
	with open( 'img.jpg','wb' ) as f:
	    f.write(file)
	setWallPaper('C:\\Users\\diyan\\Desktop\\必应每日一图桌面\\img.jpg')

if __name__ == '__main__':
	main()
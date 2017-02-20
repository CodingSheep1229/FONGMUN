# -*- coding: utf-8 -*-
import pygame
import os
from pygame.locals import *
from sys import exit
import csv


#宣告
m=50
sw=1540
sh=800
screen_size = (sw,sh)
title = "WAR!!!!!!!!!!!!!!"
background_image=os.path.dirname(os.path.abspath(__file__))+"/pic/map.png"
daimond_image=os.path.dirname(os.path.abspath(__file__))+"/pic/daimond.gif"
sword_image=os.path.dirname(os.path.abspath(__file__))+"/pic/sword.png"




def run():
	print u'FONGMUN 2017 CRISIS 作戰系統'
	print u'製作人:鄭揚'
	print 
	print u'操作方法:'
	print u'1.按左鍵拖動部隊'
	print u'2.按右鍵顯示資訊'
	print u'3.同時按左右鍵存檔'
	print
	print
	print 'Loading Image.',
	#pygame.time.wait(1000)
	print '.',
	#pygame.time.wait(1000)
	print '.',
	#pygame.time.wait(1000)
	print
	print 'Loading Troop Data.',
	#pygame.time.wait(1000)
	print '.',
	#pygame.time.wait(1000)
	print '.',
	#pygame.time.wait(1000)
	print
	print 'Loading Resouces Data.',
	#pygame.time.wait(1000)
	print '.',
	#pygame.time.wait(1000)
	print '.',
	#pygame.time.wait(1000)
	print
	print 'Initializing.',
	#pygame.time.wait(1000)
	print '.',
	#pygame.time.wait(1000)
	print '.'
	#pygame.time.wait(1000)
	print
	
	x=0#背景起始X
	y=0#背景起始Y
	pygame.init()
	screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE, 32)
	pygame.display.set_caption(title)
	font = pygame.font.Font(pygame.font.get_default_font(), 12)

	state = 1#轉換頁面
	
	rot=180
	rotd=2
	turnlist=[]
	turn=0
#部隊
	troop=[]#部隊總類
	country=[]#部隊國家
	bcol=[]#原始顏色
	acol=[]#移動後顏色
	col=[]#現在顏色
	tx=[]#x座標
	ty=[]#Y座標
	txx=[]#對照Y座標
	tyy=[]#對照X座標
	power=[]#戰力值
	move=[]#是否移動中
	
#資源
	resource=[]#資源種類
	value=[]#資源價值
	rx=[]#X座標
	ry=[]#Y座標
	owner=[]#資源擁有者
	
	
	fr=open(os.path.dirname(os.path.abspath(__file__))+"/data/troop.csv",'r')#部隊資訊
	ffr=open(os.path.dirname(os.path.abspath(__file__))+"/data/resources.csv",'r')#資源資訊
	next(fr)
	next(ffr)
	for a in csv.reader(fr):
		move.append(0)
		troop.append(a[1])
		country.append(a[2])
		power.append(int(a[3]))
		tx.append(int(a[4]))
		txx.append(int(a[4]))
		ty.append(int(a[5]))
		tyy.append(int(a[5]))
		bcol.append([int(a[6].split(',')[0]),int(a[6].split(',')[1]),int(a[6].split(',')[2])])
		col.append((int(a[6].split(',')[0]),int(a[6].split(',')[1]),int(a[6].split(',')[2])))
		acol.append([int(a[7].split(',')[0]),int(a[7].split(',')[1]),int(a[7].split(',')[2])])
		if a[2] not in turnlist:
			turnlist.append(a[2])
	fr.close()
	for a in csv.reader(ffr):
		resource.append(a[1])
		value.append(int(a[2]))
		rx.append(int(a[3]))
		ry.append(int(a[4]))
		owner.append(a[5])
	ffr.close()
	
	
#判定
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
	
		pygame.display.set_caption(turnlist[turn]+"'s turn" )
	
	
	
		if state == 0:
			screen.fill((0,223,213))
			screen.blit(pygame.image.load(background_image).convert_alpha(),(x,y))
			
#地圖移動
			
				
			for i in range(len(rx)):
				screen.blit(pygame.image.load(daimond_image).convert_alpha(),(x+rx[i], y+ry[i]))
			
			for i in range(len(tx)):
				if country[i]==turnlist[turn]:
					pygame.draw.circle(screen, (int(col[i][0]),int(col[i][1]),int(col[i][2])), [x+tx[i], y+ty[i]], 10, 10)
			
			
			
			
			if pygame.mouse.get_pos()[0]>=sw-50 and x>-500:#右移
				screen.fill((0,223,213))
				screen.blit(pygame.image.load(background_image).convert_alpha(),(x,y))
				x-=m
				for i in range(len(rx)):
					screen.blit(pygame.image.load(daimond_image).convert_alpha(),(x+rx[i], y+ry[i]))
				for i in range(len(tx)):
					if country[i]==turnlist[turn]:
						pygame.draw.circle(screen, (int(col[i][0]),int(col[i][1]),int(col[i][2])), [x+tx[i], y+ty[i]], 10, 10)
			if pygame.mouse.get_pos()[0]<=50 and x<0:#左移
				screen.fill((0,223,213))
				screen.blit(pygame.image.load(background_image).convert_alpha(),(x,y))
				x+=m
				for i in range(len(rx)):
					screen.blit(pygame.image.load(daimond_image).convert_alpha(),(x+rx[i], y+ry[i]))
				for i in range(len(tx)):
					if country[i]==turnlist[turn]:
						pygame.draw.circle(screen, (int(col[i][0]),int(col[i][1]),int(col[i][2])), [x+tx[i], y+ty[i]], 10, 10)
			if pygame.mouse.get_pos()[1]>sh-50 and y>-250:#下移
				screen.fill((0,223,213))
				screen.blit(pygame.image.load(background_image).convert_alpha(),(x,y))
				y-=m
				for i in range(len(rx)):
						screen.blit(pygame.image.load(daimond_image).convert_alpha(),(x+rx[i], y+ry[i]))
				for i in range(len(tx)):
					if country[i]==turnlist[turn]:
						pygame.draw.circle(screen, (int(col[i][0]),int(col[i][1]),int(col[i][2])), [x+tx[i], y+ty[i]], 10, 10)
			if pygame.mouse.get_pos()[1]<50 and y<0:#上移
				screen.fill((0,223,213))
				screen.blit(pygame.image.load(background_image).convert_alpha(),(x,y))
				y+=m
				for i in range(len(rx)):
					screen.blit(pygame.image.load(daimond_image).convert_alpha(),(x+rx[i], y+ry[i]))
				for i in range(len(tx)):
					if country[i]==turnlist[turn]:
						pygame.draw.circle(screen, (int(col[i][0]),int(col[i][1]),int(col[i][2])), [x+tx[i], y+ty[i]], 10, 10)
			
			
			for i in range(len(tx)):
				if country[i]==turnlist[turn]:
#部隊移動		
			
					if pygame.mouse.get_pressed()[0] == True and pygame.mouse.get_pos()[0] >= x+tx[i]-10 and pygame.mouse.get_pos()[0] <= x+tx[i]+10 and pygame.mouse.get_pos()[1] >= y+ty[i]-10 and pygame.mouse.get_pos()[1] <= y+ty[i]+10:
						if move.count(1)==0 and col[i]!=acol[i]:
							if screen.get_at((x+tx[i],y+ty[i]))==(0,223,213,255):
								move[i]=2
							else:
								move[i]=1
								
					if move[i]==1:
						pygame.draw.circle(screen, (int(bcol[i][0]),int(bcol[i][1]),int(bcol[i][2])), [x+txx[i], y+tyy[i]], 100, 5)
						if (pygame.mouse.get_pos()[0]-(x+txx[i]))**2+(pygame.mouse.get_pos()[1]-(y+tyy[i]))**2<10000:
							tx[i]=pygame.mouse.get_pos()[0]-x
							ty[i]=pygame.mouse.get_pos()[1]-y
						if pygame.mouse.get_pressed()[0] == False:
							move[i]=0
							if txx[i]!=tx[i]:
								txx[i]=tx[i]
								col[i]=acol[i]
							if tyy[i]!=ty[i]:
								tyy[i]=ty[i]
								col[i]=acol[i]
					if move[i]==2:
						pygame.draw.circle(screen, (int(bcol[i][0]),int(bcol[i][1]),int(bcol[i][2])), [x+txx[i], y+tyy[i]], 50, 5)
						if (pygame.mouse.get_pos()[0]-(x+txx[i]))**2+(pygame.mouse.get_pos()[1]-(y+tyy[i]))**2<2500:
							tx[i]=pygame.mouse.get_pos()[0]-x
							ty[i]=pygame.mouse.get_pos()[1]-y
						if pygame.mouse.get_pressed()[0] == False:
							move[i]=0
							if txx[i]!=tx[i]:
								txx[i]=tx[i]
								col[i]=acol[i]
							if tyy[i]!=ty[i]:
								tyy[i]=ty[i]
								col[i]=acol[i]
#按右鍵顯示資訊
			for i in range(len(tx)):
				if country[i]==turnlist[turn]:
					if pygame.mouse.get_pressed()[2] == True and pygame.mouse.get_pos()[0] >= x+tx[i]-10 and pygame.mouse.get_pos()[0] <= x+tx[i]+10 and pygame.mouse.get_pos()[1] >= y+ty[i]-10 and pygame.mouse.get_pos()[1] <= y+ty[i]+10:
						pygame.draw.rect(screen, (255,255,255), [x+txx[i], y+tyy[i],100,60])
						screen.blit(font.render('Troop:'+troop[i],True, (0,0,0)),(x+txx[i]+5,y+tyy[i]+5))
						screen.blit(font.render('Country:'+country[i],True, (0,0,0)),(x+txx[i]+5,y+tyy[i]+25))
						screen.blit(font.render('Power:'+str(power[i]),True, (0,0,0)),(x+txx[i]+5,y+tyy[i]+45))
					
			for i in range(len(rx)):
				if pygame.mouse.get_pressed()[2] == True and pygame.mouse.get_pos()[0] >= x+rx[i] and pygame.mouse.get_pos()[0] <= x+rx[i]+25 and pygame.mouse.get_pos()[1] >= y+ry[i] and pygame.mouse.get_pos()[1] <= y+ry[i]+25:
					pygame.draw.rect(screen, (255,255,255), [x+rx[i]+12, y+ry[i]+12,150,60])
					screen.blit(font.render('Resouce:'+resource[i],True, (0,0,0)),(x+rx[i]+5+12,y+ry[i]+5+12))
					screen.blit(font.render('Owner:'+owner[i],True, (0,0,0)),(x+rx[i]+5+12,y+ry[i]+25+12))
					screen.blit(font.render('Value:'+str(value[i]),True, (0,0,0)),(x+rx[i]+5+12,y+ry[i]+45+12))
				
#按滾輪下一位玩家
			if pygame.mouse.get_pressed()[1] == True:
				pygame.time.wait(1000)
				turn+=1
				if turn==len(turnlist):
					turn=0
				for i in range(len(tx)):
					col[i]=bcol[i]
				
#同時按左右鍵存檔

			if pygame.mouse.get_pressed()[0] == True and pygame.mouse.get_pressed()[2] == True:
				fw=open(os.path.dirname(os.path.abspath(__file__))+"/data/troop.csv",'wb')#部隊資訊
				csv.writer(fw).writerows([['Troop ID','Troop Type','Country','Power','X','Y','before color','after color']])
				for iii in range(len(acol)):
					for iiii in range(3):
						acol[iii][iiii]=str(acol[iii][iiii])
						bcol[iii][iiii]=str(bcol[iii][iiii])
				for ii in range(len(tx)):
					csv.writer(fw).writerows([[ii,troop[ii],country[ii],power[ii],tx[ii],ty[ii],','.join(bcol[ii]),','.join(acol[ii])]])
				fw.close()
		
		if state==1:
			rot+=rotd
			if rot>=220 or rot<=180:
				rotd*=-1
			
		
			screen.fill((255,0,0))
			screen.blit(pygame.transform.rotozoom(pygame.image.load(sword_image), -rot, 0.5).convert_alpha(),(575,80))
			screen.blit(pygame.transform.rotozoom(pygame.image.load(sword_image), rot, 0.5).convert_alpha(),(685,80))
			
		
		

		pygame.display.update()
while True:
	if __name__ == "__main__":
		run()
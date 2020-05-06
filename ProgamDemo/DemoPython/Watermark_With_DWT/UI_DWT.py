from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox,QFileDialog
from PIL import ImageQt
from img_dwt import *
#https://github.com/TrG-1999/programming/tree/master/ProgamDemo/DemoPython/Watermark_With_DWT
##Open file
def browseImage(ob_lb_image):
	fname = QFileDialog.getOpenFileName(ui,"Opent File image","../pyqt5","Image files (*.jpg *.jpeg *.png)")
	imagePath = fname[0]
	pixmap = QPixmap(imagePath)
	ob_lb_image.setPixmap(pixmap)
	ob_lb_image.setToolTip(imagePath)
##save file
def saveImage():
	buttonReply = QMessageBox.question(ui, 'Thông báo', "Bạn có muốn lưu lại?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
	if buttonReply == QMessageBox.Yes:
		fname = QFileDialog.getSaveFileName(ui, 'Save File image',"../pyqt5","Image files (*.png)")
		if fname[0] != "":
			imgFile = Image.open("temp.png")
			imgFile.save(fname[0])
			print("Save success!!")
			QMessageBox.question(ui, 'Thông Báo', "Đã lưu lại", QMessageBox.Close, QMessageBox.Close)
##convert image
def convert_image(img,mode):
	img = img.convert(mode,palette=Image.ADAPTIVE)
	return img
##process image
def process_image(scale=2):
	img_ori=None
	img_mark=None
	width_watermark=0
	heigh_watermark=0
	imgPath = ui.lb_original.toolTip()
	if imgPath != "":
		img_ori = Image.open(imgPath)
		if img_ori.mode != "RGB":
			img_ori = convert_image(img_ori,"RGB")
		heigh_watermark=img_ori.size[1]
		width_watermark=img_ori.size[0]
		if heigh_watermark%2 != 0:
			heigh_watermark = heigh_watermark - heigh_watermark%2
		if width_watermark%2 != 0:
			width_watermark = width_watermark - width_watermark%2
		img_ori = img_ori.resize((width_watermark,heigh_watermark), Image.ANTIALIAS)
	imgPath =ui.lb_mark.toolTip()
	if imgPath != "":
		img_mark = Image.open(imgPath)
		if img_mark.mode != "RGB":
			img_mark = convert_image(img_mark,"RGB")
		heigh_watermark=int(heigh_watermark/scale)
		width_watermark=int(width_watermark/scale)
		heigh_watermark=heigh_watermark - heigh_watermark%2
		width_watermark=width_watermark - width_watermark%2
	return img_ori,img_mark,width_watermark,heigh_watermark
##bottom embedding clicked
def btn_embedding():
	QMessageBox.information(ui, "Thông Báo","bấm OK để thực hiện nhúng và đợi trong giây lát!")
	img_ori,img_mark,width_watermark,heigh_watermark=process_image()
	if img_ori!=None and img_mark!=None and width_watermark!=0 and heigh_watermark!=0:
		img_mark = img_mark.resize((width_watermark,heigh_watermark),Image.ANTIALIAS)
		img_ori = dwt_haar(img_ori,img_ori.load(),img_ori.size[1],img_ori.size[0])
		img_mark = dwt_haar(img_mark,img_mark.load(),img_mark.size[1],img_mark.size[0])
		img_ori=embedding(img_ori,img_mark,float(ui.le_R.text()),float(ui.le_G.text()),float(ui.le_B.text()))
		img_ori=idwt_haar(img_ori,img_ori.load(),img_ori.size[1],img_ori.size[0])
		img_ori.save("temp.png")
		pixmap = QPixmap("temp.png")
		ui.lb_watermark.setPixmap(QPixmap(pixmap))
		QMessageBox.question(ui, 'Thông Báo', "Đã nhúng thành công!!", QMessageBox.Close, QMessageBox.Close)
	else:
		QMessageBox.question(ui, 'Cảnh Báo', "Không thể nhúng. Xin kiểm tra lại dữ liệu đầu vào!!", QMessageBox.Close, QMessageBox.Close)
##bottom exacting clicked
def btn_exacting():
	QMessageBox.information(ui, "Thông Báo","bấm OK để thực hiện tách và đợi trong giây lát!")
	img_ori,img_mark,width_watermark,heigh_watermark=process_image()
	if img_ori!=None and img_mark!=None and width_watermark!=0 and heigh_watermark!=0:
		if img_ori.size[0]!=img_mark.size[0] or img_ori.size[1]!=img_mark.size[1]:
			img_mark = img_mark.resize((img_mark.size[0],img_ori.size[1]),Image.ANTIALIAS)
		watermark = Image.new(img_ori.mode,(width_watermark,heigh_watermark))
		img_ori = dwt_haar(img_ori,img_ori.load(),img_ori.size[1],img_ori.size[0])
		img_mark = dwt_haar(img_mark,img_mark.load(),img_mark.size[1],img_mark.size[0])
		watermark = exacting(img_ori,watermark,img_mark,float(ui.le_R.text()),float(ui.le_G.text()),float(ui.le_B.text()))
		watermark=idwt_haar(watermark,watermark.load(),heigh_watermark,width_watermark)
		watermark.save("temp.png")
		pixmap = QPixmap("temp.png")
		ui.lb_watermark.setPixmap(pixmap)
		QMessageBox.question(ui, 'Thông Báo', "Tách thành công!!", QMessageBox.Close, QMessageBox.Close)
	else:
		QMessageBox.question(ui, 'Cảnh Báo', "Không thể tách. Xin kiểm tra lại dữ liệu đầu vào!!", QMessageBox.Close, QMessageBox.Close)
app = QtWidgets.QApplication([])
ui = uic.loadUi("UI_DWT.ui")
##append / running here
ui.btn_image_ori.clicked.connect(lambda: browseImage(ui.lb_original))
ui.btn_image_mark.clicked.connect(lambda: browseImage(ui.lb_mark))
ui.btn_embedding.clicked.connect(btn_embedding)
ui.btn_exacting.clicked.connect(btn_exacting)
ui.btn_save.clicked.connect(saveImage)
##end code
ui.show()
app.exec()
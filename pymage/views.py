from django.shortcuts import render, loader

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from PIL import Image

class Home(TemplateView):
	template_name = 'index.html'

def index(request):
	indexActive = 'active'
	pageTitle = 'Greyscale'
	pageStatus = 1
	if request.method == 'POST':
		uploaded_file = request.FILES['imagefile']
		pageStatus = 2
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		url = fs.url(name)
		displayFile = url
		tujuan = "/srv/http/djangouwsgi/djangoproject" + url
		gambarGreyscale = Image.open(tujuan)
		namafilebaru = tujuan[:-4] + "_greyscale" + tujuan[-4:]
		# CONVERT MULAI DISINI MENGGUNAKAN FUNGSI convert()
		filebaru = gambarGreyscale.convert(mode='L').save(namafilebaru)
		displayFileMod = url[:-4] + "_greyscale" + url[-4:]
		return render(request, 'pymage/index.html', {'pageStatus':pageStatus, 'displayFileMod':displayFileMod, 'pageTitle':pageTitle, 'indexActive':indexActive, 'displayFile':displayFile})
	return render(request, 'pymage/index.html', {'pageStatus':pageStatus, 'pageTitle':pageTitle, 'indexActive':indexActive})

def rotate(request):
	rotateActive = 'active'
	pageTitle = 'Rotate'
	pageStatus = 1
	if request.method == 'POST':
		uploaded_file = request.FILES['imagefile']
		pageStatus = 2
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		url = fs.url(name)
		displayFile = url
		return render(request, 'pymage/rotate.html', {'displayFile':displayFile, 'pageStatus':pageStatus, 'pageTitle':pageTitle, 'rotateActive':rotateActive})
	if request.GET.get('degree'):
		displayFile = request.GET['displayFromPallet']
		tujuan = "/srv/http/djangouwsgi/djangoproject" + displayFile
		gambarRotate = Image.open(tujuan)
		namafilebaru = tujuan[:-4] + "_rotate" + tujuan[-4:]
		# CONVERT MULAI DISINI MENGGUNAKAN FUNGSI rotate()
		filebaru = gambarRotate.rotate(int(request.GET['degree']), expand=1).save(namafilebaru)
		displayFileMod = displayFile[:-4] + "_rotate" + displayFile[-4:]
		pageStatus = 3
		print(displayFile)
		print(displayFileMod)
		return render(request, 'pymage/rotate.html', {'displayFile':displayFile, 'displayFileMod':displayFileMod, 'pageStatus':pageStatus, 'pageTitle':pageTitle, 'rotateActive':rotateActive})
	return render(request, 'pymage/rotate.html', {'pageStatus':pageStatus, 'pageTitle':pageTitle, 'rotateActive':rotateActive})

def flip(request):
	flipActive = 'active'
	pageTitle = 'Flip'
	pageStatus = 1
	if request.method == 'POST':
		uploaded_file = request.FILES['imagefile']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		url = fs.url(name)
		displayFile = url
		pageStatus = 2
		return render(request, 'pymage/flip.html', {'displayFile':displayFile, 'pageStatus':pageStatus, 'pageTitle':pageTitle, 'flipActive':flipActive})
	if request.GET.get('leftright'):
		displayFile = request.GET['displayFromPallet']
		tujuan = "/srv/http/djangouwsgi/djangoproject" + displayFile
		gambarFlip = Image.open(tujuan)
		namafilebaru = tujuan[:-4] + "_flip" + tujuan[-4:]
		# CONVERT MULAI DISINI MENGGUNAKAN FUNGSI transpose()
		filebaru = gambarFlip.transpose(Image.FLIP_LEFT_RIGHT).save(namafilebaru)
		displayFileMod = displayFile[:-4] + "_flip" + displayFile[-4:]
		print(displayFile)
		print(displayFileMod)
		pageStatus = 3
		return render(request, 'pymage/flip.html', {'displayFile':displayFile, 'displayFileMod':displayFileMod, 'pageStatus':pageStatus, 'pageTitle':pageTitle, 'flipActive':flipActive})
	if request.GET.get('topbottom'):
		displayFile = request.GET['displayFromPallet']
		tujuan = "/srv/http/djangouwsgi/djangoproject" + displayFile
		gambarFlip = Image.open(tujuan)
		namafilebaru = tujuan[:-4] + "_flip" + tujuan[-4:]
		# CONVERT MULAI DISINI MENGGUNAKAN FUNGSI transpose()
		filebaru = gambarFlip.transpose(Image.FLIP_TOP_BOTTOM).save(namafilebaru)
		displayFileMod = displayFile[:-4] + "_flip" + displayFile[-4:]
		pageStatus = 3
		print(displayFile)
		print(displayFileMod)
		return render(request, 'pymage/flip.html', {'displayFile':displayFile, 'displayFileMod':displayFileMod, 'pageStatus':pageStatus, 'pageTitle':pageTitle, 'flipActive':flipActive})
	return render(request, 'pymage/flip.html', {'pageStatus':pageStatus, 'pageTitle':pageTitle, 'flipActive':flipActive})

def crop(request):
	cropActive = 'active'
	pageTitle = 'Crop'
	pageStatus = 1
	if request.method == 'POST':
		uploaded_file = request.FILES['imagefile']
		pageStatus = 2
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		url = fs.url(name)
		displayFile = url
		return render(request, 'pymage/crop.html', {'displayFile':displayFile, 'pageStatus':pageStatus, 'pageTitle':pageTitle, 'cropActive':cropActive})
	if request.GET.get('x'):
		displayFile = request.GET['displayFromPallet']
		tujuan = "/srv/http/djangouwsgi/djangoproject" + displayFile
		gambarCrop = Image.open(tujuan)
		namafilebaru = tujuan[:-4] + "_crop" + tujuan[-4:]
		# CONVERT MULAI DISINI MENGGUNAKAN FUNGSI crop()
		filebaru = gambarCrop.crop( (float(request.GET['x']), float(request.GET['y']), float(request.GET['w'])+float(request.GET['x']), float(request.GET['h'])+float(request.GET['y'])) ).save(namafilebaru)
		displayFileMod = displayFile[:-4] + "_crop" + displayFile[-4:]
		pageStatus = 3
		print(displayFile)
		print(displayFileMod)
		return render(request, 'pymage/crop.html', {'displayFile':displayFile, 'displayFileMod':displayFileMod, 'pageStatus':pageStatus, 'pageTitle':pageTitle, 'cropActive':cropActive})
	return render(request, 'pymage/crop.html', {'pageStatus':pageStatus, 'pageTitle':pageTitle, 'cropActive':cropActive})

def scale(request):
	scaleActive = 'active'
	pageTitle = 'Scale'
	return render(request, 'pymage/scale.html', {'pageTitle':pageTitle, 'scaleActive':scaleActive})

def invert(request):
	invertActive = 'active'
	pageTitle = 'Invert'
	return render(request, 'pymage/invert.html', {'pageTitle':pageTitle, 'invertActive':invertActive})


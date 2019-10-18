from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import musicLibrary
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MusicLibrarySerializers
# Create your views here.
def index(request):
	return HttpResponse("<h1>WELCOME to Samarth's first DJANGO project view</h1>")

def musicStore(request):
	all_Lib = musicLibrary.objects.all()
	return render(request, 'welcome.html', {'all_Lib':all_Lib})

def deleteItem(request, music_id):
	item = musicLibrary.objects.get(pk = music_id)
	item.delete()
	return redirect('musicStore')

def edtItem(request, music_id):
	item = musicLibrary.objects.get(pk = music_id)
	return render(request, 'edtForm.html', {'item': item })

def saveItem(request, music_id):
	item = musicLibrary.objects.get(pk = music_id)
	if request.method == 'POST':
		item.songName = request.POST['songName']
		item.artist = request.POST['artist']
		item.genre = request.POST['genre']
		item.save()
	return redirect('musicStore')

class LibraryApiView(APIView):
	def get(self, request):
		musiclibrary = musicLibrary.objects.all()
		serializer = MusicLibrarySerializers(musiclibrary, many=True)
		return Response({'musiclibrary': serializer.data})

	def post(self, request):
		musiclibrary = request.data.get('musiclibrary')
		serializer = MusicLibrarySerializers(data = musiclibrary)
		if serializer.is_valid(raise_exception= True):
			musiclibrarysaved = serializer.save()
		return Response({"Success":"Your music {} saved successfully.".format(musiclibrarysaved.songName)})
	
	def put(self, request, pk):
		musiclibrarysaved = get_object_or_404(musiclibrary.objects.all(), pk=pk)
		musiclibrary = request.data.get('musiclibrary')
		serializer = MusicLibrarySerializers(instance=musiclibrarysaved, data=data, partial=True)
		if serializer.is_valid(raise_exception=True):
			musiclibrarysaved = serializer.save()
		return Response({"Success":"Your music {} updated successfully.".format(musiclibrarysaved.songName)})

	def delete(self, request, pk):
		musiclibrary = get_object_or_404(musiclibrary.objects.all(), pk)
		musiclibrary.delete()
		return Response({"Success":"Your music {} deleted successfully.".format(pk)}, status= 204)

# from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse
# from django.views import generic

# # models import
# from .models import AmazonLabels, AmazonProductReviews

# # import utinity for api
# import random
# # from ml_utils.predict import get_predict

# # Create your views here.

# ## test ui template
# def clone_index(request):
#     template = loader.get_template("./clone_index.html")
#     context = {}

#     return HttpResponse(template.render(context=context, request=request))

# def base(request):
#     template = loader.get_template("./base.html")
#     context = {}

#     return HttpResponse(template.render(context=context, request=request))

# def category(request):
#     template = loader.get_template("./category.html")
#     context = { 'category': 'select category', 
#                 'reviewText': 'random reviweText'}

#     return HttpResponse(template.render(context=context, request=request))

# def predict(request):
#     template = loader.get_template("./predict.html")
#     context = {}

#     return HttpResponse(template.render(context=context, request=request))

# def index(request):
#     template = loader.get_template("./index.html")
#     context = {}

#     return HttpResponse(template.render(context=context, request=request))

# ## app paths

# def index_view(request, category):
#     try:
#         label = AmazonLabels.objects.get(cat_name=category)
#     except AmazonLabels.DoesNotExist:
#         label = None
#         rnd_txt = None
#     else:
#         reviews_with_label = AmazonProductReviews.objects.filter(label=label)
#         if reviews_with_label.exists():
#             rnd_txt = random.choice(reviews_with_label).reviewText
#         else:
#             rnd_txt = None

#     response=""
#     if request.method=='POST':
#         input=request.POST.get('input')
#         print(input)
#         try:
#             response=get_predict(input)
#         except:
#             print('can\' predict form model')

#     # template = loader.get_template("./catagory.html")

#     # return HttpResponse(template.render(context=context, request=request))
#     return render(request, 
#                   '/category.html', 
#                   {'category': category, 
#                    'label_cat': label, 
#                    'reviewText': rnd_txt, 
#                    'response':response})

## -------------------------import--------------------------------
from django.contrib.auth.models import Group, User
from django.http import Http404

from rest_framework import permissions, viewsets, status, mixins, generics, renderers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, action

from transformer.models import AmazonLabels
from transformer.serializers import UserSerializer, AmazonLabelsSerializer
from transformer.permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('transformer:user-list', request=request, format=format),
        'labels': reverse('transformer:label-list', request=request, format=format)
    })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AmazonlabelsList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        amazon_labels = AmazonLabels.objects.all()
        serializer = AmazonLabelsSerializer(amazon_labels, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AmazonLabelsSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            # serializer.save()
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AmazonLabelsDetail(APIView):
    """
    Retrieve, update or delete a amazon_label instance.
    """

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return AmazonLabels.objects.get(pk=pk)
        except AmazonLabels.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        amazon_label = self.get_object(pk)
        serializer = AmazonLabelsSerializer(amazon_label)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        amazon_label = self.get_object(pk)
        serializer = AmazonLabelsSerializer(amazon_label, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        amazon_label = self.get_object(pk)
        amazon_label.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AmazonLabelsHighlight(generics.GenericAPIView):
    queryset = AmazonLabels.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        AmazonLabels = self.get_object()
        return Response(AmazonLabels.highlighted)

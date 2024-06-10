from django.shortcuts import render, Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BlogModel
from .serializers import BlogSerializer

@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def blog(request, id=None):
    if request.method == "POST":
        post = BlogSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response({"msg": "Post is Created"})
        else:
            return Response(post.errors)

    elif request.method == "GET":
        if id:
            try:
                post = BlogModel.objects.get(bid=id)
                ser_data = BlogSerializer(post)
                return Response(ser_data.data)
            except BlogModel.DoesNotExist:
                raise Http404
        else:
            all_posts = BlogModel.objects.all()
            ser_data = BlogSerializer(all_posts, many=True)
            return Response(ser_data.data)

    elif request.method == "PUT":
        try:
            post = BlogModel.objects.get(bid=id)
            ser = BlogSerializer(post, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"msg": "Post Updated"})
            else:
                return Response(ser.errors)
        except BlogModel.DoesNotExist:
            raise Http404

    elif request.method == "PATCH":
        try:
            post = BlogModel.objects.get(bid=id)
            ser = BlogSerializer(post, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response({"msg": "Post Partially Updated"})
            else:
                return Response(ser.errors)
        except BlogModel.DoesNotExist:
            raise Http404

    elif request.method == "DELETE":
        try:
            post = BlogModel.objects.get(bid=id)
            post.delete()
            return Response({"msg": "Post is Deleted"})
        except BlogModel.DoesNotExist:
            raise Http404

    # In case none of the above methods match
    return Response({"msg": "Method not allowed"}, status=405)

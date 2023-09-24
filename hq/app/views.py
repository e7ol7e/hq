from rest_framework import generics
from .models import Product, Lesson, LessonView
from .serializers import ProductSerializer, LessonSerializer, LessonViewSerializer

class ListAllLessonsView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class ListUserLessonsView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        products = Product.objects.filter(accesses__user=user)
        return Lesson.objects.filter(products__in=products)

class ProductStatisticsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all()
        product_statistics = []

        for product in products:
            lesson_views = LessonView.objects.filter(lesson__products=product)
            total_views = lesson_views.count()
            total_view_time = lesson_views.aggregate(models.Sum('view_time_seconds'))['view_time_seconds__sum'] or 0
            total_students = product.accesses.count()
            product_purchase_percentage = (total_students / User.objects.count()) * 100 if User.objects.count() > 0 else 0

            product_statistics.append({
                'product': product,
                'total_views': total_views,
                'total_view_time': total_view_time,
                'total_students': total_students,
                'product_purchase_percentage': product_purchase_percentage
            })

        return product_statistics

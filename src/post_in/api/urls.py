from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from api.views import NoteDetailView, NoteListView, NoteViewSet, UserViewSet


router = DefaultRouter()
router.register('note', NoteViewSet, basename='notes')
router.register('users', UserViewSet, basename='users')
urlpatterns = router.urls

# note_list = NoteViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
# note_detail = NoteViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# urlpatterns = [
#     path('notes/', NoteListView.as_view()),
#     path('notes/<int:pk>/', NoteDetailView.as_view(), name='notes-detail'),
#     path('note/', note_list, name='note-list'),
#     path('note/<int:pk>/', note_detail, name='note-detail'),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
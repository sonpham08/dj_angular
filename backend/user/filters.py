import django_filters
from .models import User

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        # fields = ['cmnd']

    # @property
    # def qs(self):
    #     parent = super(UserFilter, self).qs
    #     author = getattr(self.request, 'user', None)

    #     return parent.filter(is_published=True) \
    #         | parent.filter(author=author)
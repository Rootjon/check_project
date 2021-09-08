from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import Post

class StaticViewSitemap(Sitemap):
    
    def items(self):
        return [
            'blog:blog_list',
          

        ]
    
    def location(self,item):
        return reverse(item)



class BlogpostSitemap(Sitemap):
    
    def items(self):
        return Post.objects.all()
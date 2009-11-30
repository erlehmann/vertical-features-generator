#!/usr/bin/env python
#
#       vertical-features.py
#       
#       Copyright 2009 Nils Dagsson Moskopp <nils@dieweltistgarnichtso.net>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version  of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

FLICKR_API_KEY = "b38f4aaa112e286bda0f14cb84a893d1"

import flickrapi
from urllib import urlretrieve

def main():

    flickr = flickrapi.FlickrAPI(FLICKR_API_KEY)
    photos = flickr.photos_search(media="photos", per_page="11", tag_mode="all", tags="vertical, tree")

    for p in range(11):
        photo = photos[0][p]
        url = "http://farm%(farm-id)s.static.flickr.com/%(server-id)s/%(id)s_%(secret)s.jpg" % \
            {
            "farm-id": photo.attrib["farm"],
            "server-id": photo.attrib["server"],
            "id": photo.attrib["id"],
            "secret": photo.attrib["secret"]
            }
        urlretrieve(url, "images/" + str(p) + ".jpg") # FIXME: use os.join() here

    return 0

if __name__ == '__main__': main()

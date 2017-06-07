#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",
user="root", db="beautify")

cur = db.cursor(MySQLdb.cursors.DictCursor)
cur.execute("select category.id As category_id, category.name as category_name, category_data.id as category_data_id, category_data.name as category_data_name, category_data.image as category_data_image, category_data.description as category_data_description, video.url_id as video_url_id, video.name as video_name, video.description as video_description from category left join category_data ON category.id = category_data.category_id left join video on video.category_data_id = category_data.id")

# print cur.description
# print cur.fetchone()


list = []
for row in cur.fetchall():
	# print row

	videoObj = {
	"url_id":row.get("video_url_id"),
	"name":row.get("video_name"),
	"description":row.get("video_description")
	}

	rowV = {
	"category_id": row.get("category_id"),
	"category_name": row.get("category_name"),
	"category_data_id": row.get("category_data_id"),
	"category_data_name": row.get("category_data_name"),
	"category_data_image": row.get("category_data_image"),
	"category_data_description": row.get("category_data_description"),
	"videos": videoObj
	}

	list.append(rowV)

	print rowV

print "----------------"
print list


db.close()

def find_beer(items):
	print items

	if 'sandels' in items and 'alecoq' in items:
		return "party"
	elif 'sandels' in items:
		return "sandels"
	elif 'alecoq' in items:
		return "alecoq"

	return "cry"

l1 = ['koff','cereal','kukko','karhu','olvi','nikolai','lapinkulta','saku','guinness','budweiser','fosters','olvi','koff','lapinkulta','karjala','saku','budweiser','tuplapukki','alecoq','nikolai','saku','guinness','koff','budweiser','olvi','lapinkulta','sandels','nikolai','karjala','karhu','olvi','alecoq','guinness','lapinkulta','saku','milk','karhu','sandels','karjala','koff']

print find_beer(l1)
----------------------------------------------------------------------------------------------------------------------
// CREATING USERS
user1 = User.objects.create_user(username="John")
user1 = User.objects.create_user(username="Anthony")
----------------------------------------------------------------------------------------------------------------------
// CREATING AUTHORS
Author.objects.create(author=user1)
Author.objects.create(author=user2)
----------------------------------------------------------------------------------------------------------------------
//CREATING CATEGORIES (SPORT, POLITICS, EDUCATION and WORLD)
Category.objects.create(name="Sport")
Category.objects.create(name="Politics")
Category.objects.create(name="Education")
Category.objects.create(name="World")
----------------------------------------------------------------------------------------------------------------------
// CREATING NEWS by John(user with id=1)
author  = Author.objects.get(id=1)
Post.objects.create(author=author, categoryType='NW', title='Title of news', text='some very interesting news')
----------------------------------------------------------------------------------------------------------------------
// CREATING ARTICLE by John(user with id=1)
Post.objects.create(author=author, categoryType='AR', title='Title of article' text='some very interesting article by John')
----------------------------------------------------------------------------------------------------------------------
// CREATING ARTICLE by Anthony(user with id=2)
author  = Author.objects.get(id=2)
Post.objects.create(author=author, categoryType='AR', title='Title of article' text='some very interesting article by Anthony')
----------------------------------------------------------------------------------------------------------------------
// ADD CATEGORY to NEWS/ARTICLE
Post.objects.get(id=1).postCategory.add(Category.objects.get(name='Sport'))
Post.objects.get(id=1).postCategory.add(Category.objects.get(name='World'))

Post.objects.get(id=2).postCategory.add(Category.objects.get(name='World'))
Post.objects.get(id=2).postCategory.add(Category.objects.get(name='Politics'))

Post.objects.get(id=3).postCategory.add(Category.objects.get(name='World'))
Post.objects.get(id=3).postCategory.add(Category.objects.get(name='Education'))
----------------------------------------------------------------------------------------------------------------------
// CREATING COMMENTS 
// e.g.: here's a John(user with id=1), creates comment for News(with id=1)
Comment.objects.create(
	commentPost=Post.objects.get(id=1), 
	commentUser=Author.objects.get(id=1).author, 
	text='very good'
)

Comment.objects.create(
	commentPost=Post.objects.get(id=1), 
	commentUser=Author.objects.get(id=2).author, 
	text='interesting news'
)

Comment.objects.create(
	commentPost=Post.objects.get(id=2), 
	commentUser=Author.objects.get(id=2).author, 
	text='awesome article'
)

Comment.objects.create(
	commentPost=Post.objects.get(id=3), 
	commentUser=Author.objects.get(id=1).author, 
	text='nooooo waaaay'
)

Comment.objects.create(
	commentPost=Post.objects.get(id=2), 
	commentUser=Author.objects.get(id=1).author, 
	text='I cant believe it!!!'
)

// LIKE every COMMENTS
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=5).like()

// LIKE every POST (1 and 2 twice)
Post.objects.get(id=1).like()
Post.objects.get(id=2).like()
Post.objects.get(id=3).like()
Post.objects.get(id=1).like()
Post.objects.get(id=2).like()

// DISLIKE COMMENTS and POSTS
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).dislike()
Post.objects.get(id=1).dislike()
Post.objects.get(id=2).dislike()

// UPDATE RATING\
Author.objects.all().update_rating()

// SHOW the most RATED USER
a = Author.objects.order_by('-ratingAuthor')[:1]
a.ratingAuthor 
a.author.username

// SHOW the most RATED POST
p = Postobjects.order_by('-rating')[:1]
p.author
p.title
p.rating
p.preview()
p_id = p.id
b_p = Post.objects.get(id=p_id)
b_p.dateCreation
b_p.author
b_p.rating
b_p.text


Comment.objects.get(id=1).rating


#this is also called  IIFE for shorthand.
#normally we need to call the functions , but IIFE do not require calling , it is calledd where it is written.
#------------------------------------------------------------------------
(lambda x:print(x**2))(5)
#------------------------------------------------------------------------
(lambda x,y:print(x**y))(y=9,x=2)
#------------------------------------------------------------------------
(lambda *args: print(sum(args)))(1,2)
#------------------------------------------------------------------------
(lambda **kwargs: print(kwargs.values()))(a="hello",b="bye")

#here i am getting a problem
# (lambda **kwagrs:print(['a'])(a="hello".b="bye"))
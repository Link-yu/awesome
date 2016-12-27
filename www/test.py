import orm 
import asyncio
import sys
from models import User, Blog, Comment
import logging
loop = asyncio.get_event_loop()
def test():
    yield from orm.create_pool(loop=loop, user='www-data',password='www-data',db='awesome')
    
    u = User(name='zhujing', email = 'zhujing@163.com', passwd='123456780',image='about:blank')
    yield from u.save()
    #users = yield from User.findAll(orderBy='created_at')
    users = yield from User.findAll()
    #users = yield from orm.select()
    for user in users:
        logging.info('name: %s, password: %s, created_at: %s' % (user.name, user.passwd, user.created_at))
    
    #user= users[0]
    #user.email = 'kevinyulk@163.com'
    #user.name = 'yulingkai'
    #yield from user.update()
    
    #test_user = yield from User.find(user.id)
    #logging.info('name: %s, email: %s' %(test_user.name, test_user.email))
    
    #user1 = yield from User.findAll()
    #yield from user1[0].remove()
    print('test ok')
    
loop.run_until_complete(test())
loop.close()
if loop.is_closed():
    sys.exit(0)
# import module_messages as msg # giving alias to module_messages


# msg.hello() 
# msg.bye()

# another way of importing 

from module_messages import hello, bye

hello() 
bye() 

from module_messages import * # this is not recommended 

hello() 
bye() 
 
#!/usr/bin/env python
# coding: utf-8

# In[1]:

#karena runnya di notebook jadinya harus install itu dulu. semisal ga dibutuhkan bisa langsung di import telegram
###pip install telegram
# In[2]:
##pip install --user --force-reinstall python-telegram-bot
# In[13]:


#!/bin/env python3.6
import telegram
from datetime import time

bot = telegram.Bot(token='1440733531:AAGonkvlPeyMtOwsbBgWu0ooAkokEC1C4jc')


# In[6]:


recycling_times = ['06:00:00', '14:00:00', '22:00:00']


# In[11]:


import datetime
now = datetime.datetime.now()


# In[12]:


if now.weekday() == 6:
    if str(today) in recycling_days:
        bot.send_message(chat_id='1053930899', text="test")
    else:
        bot.send_message(chat_id='1053930899', text="Rest")


# In[ ]:





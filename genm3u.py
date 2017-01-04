import sys
import os
import re

__cwd__ = os.getcwd()
__data__ = os.getcwd()
__resource__ =  os.path.join( __cwd__, 'resources', 'lib')
sys.path.insert(0, __resource__)
dbg='false'
__version__='0.01'
__scriptname__='bsfc'
print(os.getcwd())
__ua_os = {
  '0' : {'ua' : 'pcweb', 'osid' : 'pcweb'},
  #'1' : {'ua' : 'samsunghas-agent/1.1', 'osid' : 'samsungtv'},
  '1' : {'ua' : 'Mozilla/5.0 (SMART-TV; Linux; Tizen 2.3) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.0 TV Safari/538.1', 'osid' : 'samsungtv'},
  '2' : {'ua' : 'HLS Client/2.0 (compatible; LG NetCast.TV-2012)', 'osid' : 'lgtv'},
  '3' : {'ua' : 'Mozilla/5.0 (FreeBSD; Viera; rv:34.0) Gecko/20100101 Firefox/34.0', 'osid' : 'panasonictv'},
  '4' : {'ua' : 'Bulsatcom for android', 'osid' : 'androidtv'},
}

import bsc3

def progress_cb (a):
    pass


b = bsc3.dodat(login={'usr': 'grizmin@gmail.com',
                     'pass': ''
                     },
              path=__data__,
              cachetime=8.0,
              dbg=True,
              timeout=10.0,
              ver=__version__,
              xxx=False,
              os_id= __ua_os['1']['osid'],
              agent_id= __ua_os['1']['ua'],
              gen_m3u=True,
              gen_epg=not True,
              compress=True
              )

b.gen_all(True)
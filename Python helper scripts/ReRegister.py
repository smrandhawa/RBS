ó
 ÍQc           @   s]   d  d l  Z  d  d l Z d  d l Z d  d l Td  d l m Z d   Z d   Z d   Z d S(   i˙˙˙˙N(   t   *(   t   FreeSwitchMessengerc         C   s+   y t  |   t SWn t k
 r& t SXd  S(   N(   t   floatt   Truet
   ValueErrort   False(   t   n(    (    s%   /usr/local/freeswitch/scripts/abd4.pyt	   is_number	   s
    
c         C   sZ  t  j j t |  j     | j d  } | d } | d } t j d  } t j | _	 | j
   } t d d | d  t d d | d  | j   } t } t |  d	 k rĜ d
 }	 t d d |	 d  t } n~| d }
 | d } | d } | d } t |
  rt } n! t } d } t d d | d  d } | j | | g  | j   } x/ | D]' } t } d } t d d | d  qbW| t k r;| j d |
 d | d  | j d | d |
 d | d | d | d | d  d }	 | j d  | j   |  j d d |	  |  j d d |
  n d } t d d | d  d  S(   Nt   |i    i   s'   /var/lib/asterisk/sqlite3dir/sqlite3.dbt   infos#   abd test script, Message Recieved: s   
s   abd test script, imsi: i   s   Invalid number of argumentss   abd test script, Error: i   i   s!   First Argument should be a numbers1   SELECT username FROM sip_buddies where username=?s   Your Number already exists!s;   INSERT INTO dialdata_table (id, exten, dial) VALUES ( 25, 's   ', 's   ');sj   INSERT INTO sip_buddies (name, callerid, ipaddr, port, host, username, occupation, uname, blood) VALUES ('s"   ', '127.0.0.1', 5062, 'dynamic', 's   Successfully Registered!t   VACUUMt   sets   _vbts_ret=%ss   _num_ret=%ss   Could not register!(   t   syst   stderrt   writet   strt	   serializet   splitt   sqlite3t   connectt   Rowt   row_factoryt   cursort
   consoleLogR   t   lenR   R   t   executet   fetchallt   closet   chat_execute(   t   messaget   argst   resultt   smstextt   imsit   connR   t   smspartst   checkt   rest   numt   unamet
   occupationt   bloodt   res1t   sqlt   rowst   rowt   res2t   res3(    (    s%   /usr/local/freeswitch/scripts/abd4.pyt   chat   sR    

	



	=
c         C   s   t  d  |  d  S(   N(   R0   t   None(   t   sessiont   streamt   envR   (    (    s%   /usr/local/freeswitch/scripts/abd4.pyt   fsapiG   s    (	   R   t   osR   t
   freeswitcht   libvbtsR   R   R0   R5   (    (    (    s%   /usr/local/freeswitch/scripts/abd4.pyt   <module>   s   
		7
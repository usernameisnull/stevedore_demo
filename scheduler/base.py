# encoding: utf-8
#sora/scheduler/base.py
import abc

class scheduler(object):
   __metaclass__ = abc.ABCMeta

   @abc.abstractmethod
   def scheduler(self,data):
       pass

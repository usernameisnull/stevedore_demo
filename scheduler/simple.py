#encoding: utf-8
import base
import random
class simplescheduler(base.scheduler):
  def scheduler(self,data):
      id = data[random.choice(data['memory'])]
      return id

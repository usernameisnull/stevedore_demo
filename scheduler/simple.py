#encoding: utf-8
import base
import random
class simplescheduler(base.scheduler):
  def scheduler(self,data):
      """
        随机选择一个
      """
      print 'in simplescheduler...'
      id = data[random.choice(data['memory'])]
      return id

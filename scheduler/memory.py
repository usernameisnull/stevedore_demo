#encoding: utf-8
import base
class memoryscheduler(base.scheduler):
  def scheduler(self,data):
      id = data[max(data['memory'])]
      return id

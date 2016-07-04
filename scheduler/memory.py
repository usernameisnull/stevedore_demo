#encoding: utf-8
import base
class memoryscheduler(base.scheduler):
  def scheduler(self,data):
      """
        选择最大的key对应的value
      """
      print 'in memoryscheduler...'
      id = data[max(data['memory'])]
      return id

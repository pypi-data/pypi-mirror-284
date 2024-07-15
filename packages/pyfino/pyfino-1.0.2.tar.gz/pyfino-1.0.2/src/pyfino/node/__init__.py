# coding : utf-8

from abc import ABC, abstractmethod

class Node(ABC):
  
  def __init__(self):
    pass
  
  
  @abstractmethod
  def launch(self, **kwargs):
    pass
  
  
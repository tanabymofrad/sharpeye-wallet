# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 19:45:58 2018

@author: Tanaby
"""
from datetime import datetime  
from datetime import timedelta 


class ExpenseEntity(object):
    """
    entity class defining different expenses
    """
    def __init__(self, name, ocr_date, priority_level, amt, period):
        """
        Initialization of objects of the enity class
        """
        self.name = name # name of the entity
        self.ocurrance_date = ocr_date
        self.priority_level = priority_level
        self.expense_amt = amt
        self.ocurrance_period = period
        self.last_occr_date = None
        
    def get_amt(self):
        """
        returns the amount associated with entity
        """
        return self.expense_amt
    
    def set_last_occr_date(self, value):
        """
        """
        self.last_occr_date = value
    
    def next_ocr(self):
        """
        returns the next occurance date
        """
        
        if not self.last_occr_date:
            raise ValueError("last occurrence date is not set")
            
        
    
    

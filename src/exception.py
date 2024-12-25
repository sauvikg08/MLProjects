import sys
import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    err = str(error)
    error_message = "There is an error in python script - [{0}], line number [{1}]. Error is: [{2}]".format(
        file_name, line_number, err)
    return error_message
    


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message, error_detail=error_detail)
    
    def __tr__(self):
        return self.error_message

    

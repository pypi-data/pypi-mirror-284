
from xurpas_data_quality.data.descriptions import TableDescription
from xurpas_data_quality.render.renderer import HTMLBase
from xurpas_data_quality.render.render_error import render_error

def get_error_report(data:list, errors:list,name:str)-> HTMLBase:
    """
    Generates an error report
    """

    return render_error(data, errors,name)
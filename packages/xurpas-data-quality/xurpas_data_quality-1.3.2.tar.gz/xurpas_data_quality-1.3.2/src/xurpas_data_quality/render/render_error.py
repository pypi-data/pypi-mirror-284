import pandas as pd
from xurpas_data_quality.render.renderer import HTMLBase, HTMLContainer, HTMLTable
from xurpas_data_quality.data.descriptions import TableDescription

def render_error(data:pd.DataFrame, errors:list , name:str):
    samples_section = HTMLContainer(
        type="box",
        name="Ingested Data",
        container_items=[
            HTMLTable(
                id = "sample",
                data=data.to_html(classes="table table-sm", border=0, index=False, justify='left')
            )
        ]
    )

    errors_section = HTMLContainer(
            type="box",
            name="Invalid Data during Ingestion",
            container_items=[
                HTMLTable(
                    id = "errors",
                    data = errors
                )
            ]
        )
    content = [errors_section,
        samples_section
    ]
    body = HTMLContainer(type="sections",
                         container_items = content)

    if name is not None:
        return HTMLBase(
            body=body,
            name=name
        )
    
    else:
        return HTMLBase(
            body=body
        )
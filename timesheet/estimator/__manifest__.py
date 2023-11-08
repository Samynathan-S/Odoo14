# Copyright © 2021 Codoo-erp Creation (<https://codoo-erp.com>)
# @author: Eugen Zahoruiko (<intuit07@gmail.com>)
# @author: Taras Feshak (<tarasfeshak@gmail.com>)

{
    "name": "Task estimation",
    "author": "Codoo-ERP",
    "website": "https://codoo-erp.com",
    "summary": """
        Tasks estimation""",
    "description": """
        Long description of module's purpose
    """,
    "category": "Timesheets",
    "version": "14.0",
    "support": "intuit07@gmail.com, tarasfeshak@gmail.com",
    "license": "GPL-3",
    "images": ["static/description/banner.png"],
    "depends": ["base", "hr", "project"],
    "data": [
        "security/estimator_security.xml",
        "security/ir.model.access.csv",
        "wizard/wizard_project_view.xml",
        "views/tasks.xml",
        "views/work_units.xml",
        "data/sequence.xml",
    ],
    "demo": [],
}

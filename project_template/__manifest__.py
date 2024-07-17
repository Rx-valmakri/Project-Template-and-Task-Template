# -*- coding: utf-8 -*-
{
    'name': "Project Template",
    'summary': "Task Template & Project Template",
    'description': "Task Template & Project Template",
    'depends': ['project'],
    'data': [
        'security/ir.model.access.csv',

        'views/project_template_view.xml',
        'views/project_project_views.xml',
        'views/task_template_view.xml',
        'views/project_task_views.xml',
        'views/project_template_task_view.xml',
        'views/project_menu.xml',
    ],

    'license': 'LGPL-3',
    'application': True,
}

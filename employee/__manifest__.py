{
    'name': "Employee",
    'version': '1.0',
    'depends': ['hr', 'base'],
    'author': "Nguyen",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    # 'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
}

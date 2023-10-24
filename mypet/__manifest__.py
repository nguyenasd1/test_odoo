{
    'name': "My pet",
    'version': '1.0',
    'depends': ['base'],
    'author': "Nguyen",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    # 'depends': ['base'],
    'data': [
        'views/my_pet_view.xml',
        'security/ir.model.access.csv',
        # 'views/my_pet_plus.xml',
        'views/menus_pet.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
}

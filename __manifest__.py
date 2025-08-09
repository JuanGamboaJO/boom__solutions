# -*- coding: utf-8 -*-
{
    'name': "Boom_Solutions",

    'summary': "Prueba Técnica de Desarrollo Odoo V18",

    'description': """
        El objetivo de esta prueba técnica es evaluar las capacidades del candidato para desarrollar 
        un módulo personalizado en Odoo V18, utilizando buenas prácticas de codificación, 
        extensibilidad y aprovechando la arquitectura del framework. El módulo solicitado debe 
        funcionar como una extensión del módulo nativo de Ventas CRM (`crm`).
    """,

    'author': "Juan José Gamboa",
    'website': "https://www.yourcompany.com",

    'category': 'CRM',
    'version': '0.1',

    'depends': ['crm'],

    'data': [
        'views/crm_lead_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}


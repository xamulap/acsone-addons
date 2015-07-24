# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of html_widget_embedded_picture,
#     an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     mail_embedded_picture is free software:
#     you can redistribute it and/or modify it under the terms of the GNU
#     Affero General Public License as published by the Free Software
#     Foundation,either version 3 of the License, or (at your option) any
#     later version.
#
#     html_widget_embedded_picture is distributed
#     in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#     even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with mail_embedded_picture.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Mail Html Widget Embedded Picture',
    'version': '1.0',
    'author': 'ACSONE SA/NV',
    'maintainer': 'ACSONE SA/NV',
    'website': 'http://www.acsone.eu',
    'category': 'Html Widget',
    'license': 'AGPL-3',
    'depends': [
        'mail_embedded_picture',
    ],
    'description': """
        This module include a button on html widget toolsbar in order to allow
        the user to add some image as content of the mail body
    """,
    'images': [
    ],
    'data': [
        'views/html_widget_embedded_picture.xml',
    ],
    'qweb': [
        'static/src/xml/mail_html_widget_embedded_picture.xml',
    ],
    'installable': True,
    'auto_install': False,
}

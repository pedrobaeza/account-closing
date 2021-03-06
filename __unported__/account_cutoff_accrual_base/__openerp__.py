# -*- encoding: utf-8 -*-
##############################################################################
#
#    Account Cutoff Accrual Base module for OpenERP
#    Copyright (C) 2013 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Account Accrual Base',
    'version': '0.1',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Base module for accrued expenses and revenues',
    'description': """This module contains objets, fields and menu entries that are used by other accrual modules. So you need to install other accrual modules to get the additionnal functionalities :
- the module 'account_cutoff_accrual_picking' will manage accrued expenses and revenues based on pickings.
- a not-developped-yet module will manage accrued expenses and revenues based on timesheets.

Please contact Alexis de Lattre from Akretion <alexis.delattre@akretion.com> for any help or question about this module.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['account_cutoff_base'],
    'data': [
        'company_view.xml',
        'account_view.xml',
        'account_cutoff_view.xml',
    ],
    'installable': False,
    'active': False,
}

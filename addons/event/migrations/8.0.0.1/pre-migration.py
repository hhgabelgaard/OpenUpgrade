# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Akretion
#    (<http://www.akretion.com>).
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

from openerp.openupgrade import openupgrade

column_renames = {
    'event_event': [
        ('note', 'description'),
        ('register_attended', 'seats_used'),
        ('register_avail', 'seats_available'),
        ('register_current','seats_reserved'),
        ('register_max','seats_max'),
        ('register_min','seats_min'),
        ('register_prospect','seats_unconfirmed'),
        
    ],
   
}

column_change_type = [
    ('event_event', 'seats_used'),
    ('event_event', 'seats_available'),
    ('event_event', 'seats_reserved'),
    ('event_event', 'seats_max'),
    ('event_event', 'seats_min'),
    ('event_event', 'seats_unconfirmed'),
    ]

@openupgrade.migrate()
def migrate(cr, version):
    openupgrade.rename_columns(cr, column_renames)
    for table, field in column_change_type:
        openupgrade.float_to_integer(cr, table, field)

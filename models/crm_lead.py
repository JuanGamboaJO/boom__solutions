# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools
from datetime import    datetime
import logging
_logger = logging.getLogger(__name__)

class Lead(models.Model):
    _inherit = 'crm.lead'

    x_lead_category = fields.Selection([
        ('residential', 'Residencial'), ('business', 'Empresarial'), ('governmental', 'Gubernamental')], string='Tipo de Cliente',required=True )
    
    x_delivery_deadline = fields.Date('Fecha Limite', help="Fecha límite para procesar el lead")

    x_approved_by = fields.Many2one('res.users',string='Aprobado por',tracking=True)

    x_approved_date = fields.Datetime('Fecha de aprobación', help="Fecha en que se aprueba el lead",tracking=True)

    x_duration_since_approved = fields.Char(string='Aprobado hace', compute='_compute_duration_since_approved',store=False,readonly=True)

    x_installation_required = fields.Boolean(string='Requiere instalación') 

    x_installation_date = fields.Date(string='Fecha de instalación o entrega')

    x_contract_reference = fields.Char(string='Referencia')

    x_support_required = fields.Boolean(string='Solicitó soporte postventa')

    @api.depends('x_approved_date')
    def _compute_duration_since_approved(self):
        for lead in self:
            if lead.x_approved_date:
                delta = datetime.now() - lead.x_approved_date
                days = delta.days
                hours = delta.seconds // 3600
                minutes = (delta.seconds % 3600) // 60
                seconds = delta.seconds % 60

                partes = []
                if days:
                    partes.append(f"{days} día{'s' if days > 1 else ''}")
                if hours:
                    partes.append(f"{hours} hora{'s' if hours > 1 else ''}")
                if minutes and not days:
                    partes.append(f"{minutes} min")
                if seconds and not days and not hours:
                    partes.append(f"{seconds} s")

                lead.x_duration_since_approved = ", ".join(partes)
            else:
                lead.x_duration_since_approved = "Sin aprobación"
            

    def action_approve(self):
        for record in self:
            record.write({
                'x_approved_by': self.env.user.id,
                'x_approved_date': fields.Datetime.now(),
            })
        return False





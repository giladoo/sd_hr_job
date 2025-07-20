from odoo import models, fields, api, _

class SdHrJobHrJobInherit(models.Model):
    _inherit = 'hr.job'
    job_ids = fields.One2many('sd_hr_job.items',
                                   'job_id',
                                   string="Jobs")

    job_count = fields.Integer(compute='_compute_job_count',
                                    string='jobs',
                                    help='Count of jobs.')

    def _compute_job_count(self):
        for rec in self:
            rec.job_count = self.env['sd_hr_job.items'].search_count([('job_id', '=', self.id)])


    def action_job_view(self):
        self.ensure_one()
        context = dict(self.env.context)
        context['default_job_id'] = self.id
        context['default_department_id'] = self.department_id.id
        domain = [('job_id', '=', self.id)]
        # return {}
        return {
            'name': _('Jobs'),
            'domain': domain,
            'res_model': 'sd_hr_job.items',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree',
            'context': context,
        }

from odoo import models, fields, api, _

class SdHrJobsItems(models.Model):
    _name = "sd_hr_job.items"
    _description = "Job description items"

    name = fields.Char(required=True)
    job_id = fields.Many2one('hr.job')
    department_id = fields.Many2one('hr.department', default=lambda self: self.job_id.department_id)
